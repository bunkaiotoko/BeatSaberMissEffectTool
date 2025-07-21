import cv2

from pygrabber.dshow_graph import FilterGraph

def list_cameras_with_names():
    graph = FilterGraph()
    devices = graph.get_input_devices()
    
    print("利用可能なカメラデバイス:")
    for idx, name in enumerate(devices):
        print(f"ID {idx}: {name}")

if __name__ == "__main__":
    list_cameras_with_names()
    
print('')
print('デバイス名が"OBS Virtual Camera"のIDをSettings.txtのVideoIDに入れてください。')
print('')
input("終了するにはEnterキーを押してください...")