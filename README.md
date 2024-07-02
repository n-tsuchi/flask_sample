# サンプル不動産

## セットアップ
- 下記コマンドを順に実行
    ```
    git clone https://github.com/n-tsuchi/flask_sample.git
    cd flask_sample
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```
- 上記コマンド実行後、環境変数(GOOGLE_MAPS_API_KEY_SYS_SOUSEI_2024)にGoogle Maps API Keyを設定

## サーバ起動
```
python .\server.py
```
### サーバ起動後以下にアクセス
http://localhost:5000/static/index.html
