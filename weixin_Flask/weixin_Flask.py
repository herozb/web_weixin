from flask import Flask,render_template,request,redirect,session,send_file,flash
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

# 获取json串
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

#添加公司信息模块
@app.route("/change/添加公司信息",methods = ['GET', 'POST'])
def add_company():
    if request.method == "GET":
        return render_template('change/添加公司信息.html')
    else:
        companyName_input = request.form.get('companyname')
        taxNumber_input = request.form.get('taxnumber')
        address_input = request.form.get('address')
        phoneCompany_input = request.form.get('phoneCompany')
        bank_input = request.form.get('bank')
        carNumber_input = request.form.get('cardnumber')
        old_id = db.conn.query(models.taxinfos).order_by(models.taxinfos.id.desc()).first()
        new_id = (old_id.id)
        new_id += 1
        print(companyName_input, taxNumber_input, address_input, phoneCompany_input,bank_input,carNumber_input,new_id)
        add_sql = models.taxinfos(id=new_id, companyName=companyName_input, taxNumber=taxNumber_input, address=address_input,phone=phoneCompany_input,bank=bank_input,cardNo=carNumber_input)
        db.conn.add(add_sql)
        db.conn.commit()
        db.conn.close()
#        check_id=db.conn.query(models.taxinfos).order_by(models.taxinfos.id.desc()).first()
#        check_id_new=(check_id.id)
#        print(check_id_new)
#        if check_id_new == new_id:
 #       return render_template('change/添加公司成功.html')
        flash('You were successfully add')
        return redirect('change/添加公司成功.html')
#        else:
#            return render_template('change/添加公司失败.html')

#添加用户信息模块
@app.route("/change/添加用户信息",methods = ['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template('change/添加用户信息.html')
    else:
        phone_input = request.form.get('phone')
        oaid_input = request.form.get('oaid')
        pwd_input = request.form.get('pwd')
        old_id = db.conn.query(models.userinfos).order_by(models.userinfos.id.desc()).first()
        new_id = (old_id.id)
        new_id += 1
        print(phone_input,oaid_input,pwd_input,new_id)
        add_sql = models.userinfos(id=new_id,phone=phone_input,staffId=oaid_input,pwd=pwd_input)
#        add_sql = models.userinfos(id="814", phone="15648456654", staffId="78945", pwd="123456")
        db.conn.add(add_sql)
        db.conn.commit()
        return render_template('change/添加用户成功.html')
#    return render_template("change/添加用户信息.html")


"""
@app.route("/change/<string:str>",methods = ['GET', 'POST'])
def change(str):
    print(str)
#    return str
    str=
    return render_template('change/str.html',)
"""

#功能选择模块
@app.route("/index",methods = ['GET', 'POST'])
def index():
    return render_template('index.html',user_dict=function_list)

#登录模块
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