import os
from flask import render_template, request, redirect
from testapp import app
from testapp import db
from testapp.models import Bukken

# トップページへリダイレクト
@app.route('/')
def redirect_top():
    return redirect('/static/index.html')

# 物件一覧(地図)表示ページ
@app.route('/hudousan')
def hudousan_map():
    # 環境変数からGoogle Maps APIキーを取得
    api_key = os.getenv('GOOGLE_MAPS_API_KEY_SYS_SOUSEI_2024')
    # hudousan.db bukkenテーブルから物件情報を取得
    bukken_list = Bukken.query.all()
    print(bukken_list)

    return render_template('testapp/hudousan_map.html', api_key=api_key, bukken_list=bukken_list)

# 物件詳細ページ
@app.route('/hudousan/bukken')
def hudousan_bukken():
    # URLパラメータ"id"を取得
    bukken_id = int(request.args.get('id'))
    # 取得したidで物件を検索
    bukken_detail = Bukken.query.get(bukken_id)
    return render_template('testapp/hudousan_bukken.html', bukken_detail=bukken_detail)

    