# BeatSaberMissEffectTool
リュナンさん制作のtournament_overlayと組み合わせて使用する、  
BeatSaber配信でバッドカット、ミスカットをしたときに配信画面上にエフェクトを出すツールです。  

# OBS、Settings.txtの設定
miss_effect.pngをOBSのソースに追加。  
ソースの名前をmiss_effectに設定してください。  
miss_effectのソースを右クリック→表示トランジション/非表示トランジションをフェードに、  
フェード時間を150ms~250msぐらいに設定(フェード時間はお好みで)  
  
<img width="469" height="466" alt="misseffect" src="https://github.com/user-attachments/assets/b2c20387-db9f-4eb3-a44a-fbceb8be96ae" />  
  
__WebSocket接続設定__  
ツール→WebSocketサーバー設定をクリックしてサーバー設定画面を開く。  
プラグイン設定のWebSocketサーバーを有効にするにチェックを入れる。  
サーバー設定の認証を有効にするにチェックを入れて右下の適用を押してからパスワード生成をクリックする。  
生成したパスワードは接続情報を表示をクリックすると開くウィンドウでコピーできます。  
  
__Settings.txt__  
上記のWebSocketサーバー設定の情報をSettings.txtに入れていきます。  
hostは基本的にはlocalhostのままで大丈夫です。  
portはWebSocketサーバー設定のサーバーポートの値を入れます。  
passwordは生成したサーバーパスワードを入れます。  
  
シーン名にmiss_effectを入れたシーンの名前を入れます。  
※日本語が含まれていると文字化けして正常に動きません。  
  
VideoIDにOBSの仮想カメラのカメラIDを入れます。  
同梱のCameraID_CheckTool.exeを実行するとカメラデバイス一覧が表示されます。  
デバイス名が"OBS Virtual Camera"のIDを入れてください。  
<img width="737" height="481" alt="CameraID" src="https://github.com/user-attachments/assets/419f9d6c-a075-4a64-93f9-04327e6974dc" />  


以上で設定は完了です。  

# 使い方

MissEffectTool.exeをダブルクリックして起動するだけ。  
  
起動するとコンソールが立ち上がります。  
WebSocket 接続に成功しました。とメッセージが出ていればWebSocketの設定は正しくされています。  
OSBを起動していなかったり、設定が正しくないとエラーが出ます。  
  
正常に起動していて、リュナンさんのオーバーレイの数値が正しく読み取れていればミスエフェクトが表示されます。
