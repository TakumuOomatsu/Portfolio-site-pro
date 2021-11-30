from flask import Flask, render_template
import os

# クラスの呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/')
def top():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/works')
def works():
  return render_template("works.html")

@app.route('/hello')
def hello():
  return render_template("sample.html")

if __name__=="__app__":
  port = int(os.getenv("PORT",5000))
  app.run(host="0.0.0.0",port=port)