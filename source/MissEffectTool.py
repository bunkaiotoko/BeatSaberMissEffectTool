import cv2
import numpy as np
import os
import sys
from PIL import Image
from obswebsocket import obsws, requests

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)
    
def load_settings(settings_file_path):
    settings = {}
    with open(settings_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue #空行やコメントはスキップ
            if '=' in line:
                key, value = line.split('=',1)
                settings[key.strip()] = value.strip()
    return settings

base_path = get_base_path()
settings_file_path = os.path.join(base_path, "Settings.txt")

#OBS Websocket接続情報
settings = load_settings(settings_file_path)
host = settings.get("host")
port = int(settings.get("port"))
password = settings.get("password")

try:
    ws = obsws(host, port, password)
    ws.connect()
    print("WebSocket 接続に成功しました。")
except Exception as e:
    print("WebSocket 接続に失敗しました。\nSettings.txtのWebSocket接続設定が正しいか確認してください。")
    print('')
    input("終了するにはEnterキーを押してください...")
    sys.exit(1)

scene_name_misseffect = settings.get("SceneName")
source_name_misseffect = "miss_effect"
items_left = ws.call(requests.GetSceneItemList(sceneName=scene_name_misseffect)).getSceneItems()
scene_item_id = next((item['sceneItemId'] for item in items_left if item['sourceName'] == source_name_misseffect), None)

miss_templates = {str(i): cv2.imread(os.path.join(base_path,f'misscount_{i}.png'), 0) for i in range(10)}

#OBSの仮想カメラ出力から映像取り込み
VideoID = int(settings.get("VideoID"))
cap = cv2.VideoCapture(VideoID) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#ミスカウントの座標指定
roi_miss = (1365,27,1391,63)

#変数の初期値設定
i_temp_left = 0
 
while True:

    ret, cap_raw = cap.read()
    copy_cap = cap_raw.copy()
    
    #範囲設定
    cap_roi_miss_left = cap_raw[roi_miss[1]: roi_miss[3], roi_miss[0]: roi_miss[2]]

    #範囲内をグレースケール化
    cap_gray_miss_left = cv2.cvtColor(cap_roi_miss_left, cv2.COLOR_BGR2GRAY)

    for i, template in miss_templates.items():
        result = cv2.matchTemplate(cap_gray_miss_left, template, cv2.TM_SQDIFF_NORMED)
        min_val_left, _, min_loc, _ = cv2.minMaxLoc(result)

        if min_val_left < 0.10:
            misscount_left = i
            if i != i_temp_left:
                i_temp_left = i
                #print(f"ミスカウント読み取り数値：{i}")
                print("ミス発生")
                ws.call(requests.SetSceneItemEnabled(
                sceneName = settings.get("SceneName"),
                sceneItemId = scene_item_id,
                sceneItemEnabled = True
                ))
                ws.call(requests.SetSceneItemEnabled(
                sceneName = settings.get("SceneName"),
                sceneItemId = scene_item_id,
                sceneItemEnabled = False
                ))

cap.release()
cv2.destroyAllWindows()