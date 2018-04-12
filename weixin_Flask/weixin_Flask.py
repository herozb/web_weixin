from flask import Flask,render_template,request
import s1
app = Flask(__name__)


#@app.route("/")
#def index():
#    return render_template("login.html")

function_list = {
    1:{'action':'查看用户信息'},
    2:{'action':'查看公司信息'},
    3:{'action':'添加用户信息'},
    4:{'action':'修改用户信息'},
    5:{'action':'添加公司信息'},
    6:{'action':'修改公司信息'}

}

@app.route("/change/查看用户信息",methods = ['GET', 'POST'])
def change():
    print (s1.select())
    return render_template('change/查看用户信息.html')

"""
@app.route("/change/<string:str>",methods = ['GET', 'POST'])
def change(str):
    print(str)
#    return str
    str=
    return render_template('change/str.html',)
"""

@app.route("/index",methods = ['GET', 'POST'])
def index():
    return render_template('index.html',user_dict=function_list)

@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user=="zhangbing" and pwd=="123":
            return render_template('index.html')
        else:
            return "<h1>login Failure !</h1>"



if __name__ == '__main__':
    app.run(debug=True)