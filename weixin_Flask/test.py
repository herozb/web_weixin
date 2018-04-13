from flask import Flask,render_template,request,redirect,session,url_for
import db
import models

app = Flask(__name__)
app.secret_key = "tttttrrrrr"

@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user_input = request.form.get('user')
        pwd_input = request.form.get('pwd')
        user = db.conn.query(models.webuser).filter(models.webuser.username == user_input).first()
        if user:
            passwd = db.conn.query(models.webuser).filter(models.webuser.password == pwd_input).first()
            if passwd:
                session['user'] = user_input
#                session.permanent = True
                return "123"
            else:
                return "用户名或密码错误"
        else:
            return "<h1>login Failure 用户不存在!</h1>"

if __name__ == '__main__':
    app.run()