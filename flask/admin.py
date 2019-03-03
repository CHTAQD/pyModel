from flask import  Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
def login():
    return render_template('form.html')

@app.route('/logins',methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']

    if username=='haha'and password =='123':
        return render_template('user.html',username=username)
    else:
        return render_template('form.html',arr = '用户名或密码错误请从新输入' ,username=username)

if __name__ == '__main__':
    app.run('127.0.0.1','8888',debug=True)