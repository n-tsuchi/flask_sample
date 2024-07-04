# サンプル不動産

## 起動方法(Windowsの場合)
- 環境変数(GOOGLE_MAPS_API_KEY_SYS_SOUSEI_2024)にGoogle Maps API Keyを設定
- Windowsを再起動
- 下記コマンドを順に実行
    ```
    git clone https://github.com/n-tsuchi/flask_sample.git
    cd flask_sample
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python .\server.py
    ```

## 起動方法(Dockerの場合)
- 環境変数(GOOGLE_MAPS_API_KEY_SYS_SOUSEI_2024)にGoogle Maps API Keyを設定
- 下記コマンドを順に実行
    ```
    git clone https://github.com/n-tsuchi/flask_sample.git
    cd flask_sample
    docker compose up -d
    ```

## サーバ起動後
- http://localhost:5000/ にアクセス


