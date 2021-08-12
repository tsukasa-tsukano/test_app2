from flask import Flask, render_template, session, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pandas as pd
import openpyxl

#インスタンスの作成
app = Flask(__name__)

#暗号鍵の作成
key = os.urandom(21)
app.secret_key = key

#メイン
@app.route("/")
def index():
    #表示させたいdataを渡す
    return render_template('index.html')

@app.route('/edit', methods=["POST"])
def edit():
    #取り出す
    hibetsu = request.files['hibetsu']

    day = request.form['day']
    print(day)
    list_day = day.split(", ")
    print(list_day)

    #今年の売上合計照会のCSVファイルを取得
    hibetsu_csv = pd.read_csv(hibetsu,encoding="shift-jis")

    for i in list_day:
        hibetsu_csv[hibetsu_csv["日付"] != i]
    
    print(hibetsu_csv)

    return redirect(url_for('index'))
#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)