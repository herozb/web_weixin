from flask import Flask,render_template,request,redirect,session,send_file
import db
import os,json,datetime
import models,pymysql

app = Flask(__name__)
app.secret_key = "123456"

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


from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

date_all = db.conn.query(models.taxinfos).all()
data = json.dumps(date_all, cls=AlchemyEncoder)
json2python = json.loads(data)
print(json2python)
for i in json2python:
    print(type(i))
#data=json.dumps(date_all, cls=AlchemyEncoder)
#date_all = db.conn.query(models.taxinfos).all()
#for row in date_all:
#    ret = (row.id, row.companyName, row.taxNumber, row.address, row.phone, row.bank, row.cardNo)
#    data = json.dumps(ret, cls=AlchemyEncoder)
#    json2python = json.loads(data)
@app.route("/change/查看用户信息",methods = ['GET', 'POST'])
def change():

    return render_template("change/查看用户信息.html", data=json2python)




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
        user_input = request.form.get('user')
        pwd_input = request.form.get('pwd')
        user = db.conn.query(models.webuser).filter(models.webuser.username == user_input).first()
        if user:
            passwd = db.conn.query(models.webuser).filter(models.webuser.password == pwd_input).first()
            if passwd:
                session['user'] = user_input
#                session.permanent = True
                return render_template("index.html",user_dict=function_list)
            else:
                return "用户名或密码错误"
        else:
            return "登陆失败  %s用户不存在!" %(user_input)



if __name__ == '__main__':
    app.run(debug=True)