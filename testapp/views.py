import os
from flask import render_template, request
from testapp import app

# 物件一覧(地図)表示ページ
@app.route('/hudousan')
def hudousan_map():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY_SYS_SOUSEI_2024')
    return render_template('testapp/hudousan_map.html', api_key=api_key)

# 物件詳細ページ
@app.route('/hudousan/bukken')
def hudousan_bukken():
    # URLパラメータ"id"を取得し、物件詳細ページに渡す
    bukken_id = request.args.get('id')
    return render_template('testapp/hudousan_bukken.html', bukken_id=bukken_id)

    