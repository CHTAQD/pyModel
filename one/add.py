from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return '<h1>哈喽我是home</h1>'

@app.route('/login',methods=['GET'])
def login_from():
    return '<form action="/index" method="POST"><p><input name="username"</p><p><input name="password" type="password"></p><button type="submit">Sign In</button><p></p>'

@app.route('/index',methods=['POST'])
def logins():
    if request.form['username'] == 'haha' and request.form['password']=='123':
        return '<h3>hello word</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()
