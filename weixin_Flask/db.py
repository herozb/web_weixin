
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,func

import models
#创建连接池

engine = create_engine("mysql+pymysql://root:1qa2ws@127.0.0.1:3306/finance?charset=utf8", max_overflow=0, pool_size=5,)
Session = sessionmaker(bind=engine)


#从连接池中获取数据库链接
conn = Session()


# ############# 执行ORM操作 #############
#obj1 = models.userinfos(id="813",phone='111111111111',pwd='22222')
#conn.add(obj1)

#add1 = models.webuser(username="bing",password="123")
#conn.add(add1)

#obj2 = models.taxinfos(id="114",companyName="北京市朝阳区东四环中路财富国际金融中心",taxNumber="012345678987654321",address="北京市朝阳区中间财富中心22层",phone="010-88888888",bank="中国银行北京市分行",cardNo="564984416432")
#session.add(obj2)
'''
def select():
    #查询所有数据
#    data_list = conn.query(func.count(models.userinfos.id))
    data_list = conn.query(models.userinfos).all()
    print(data_list)
    #按照一定条件查询数据
    #data_list = conn.query(models.taxinfos).filter(models.taxinfos.id>= 114)
    #print(data_list)
    for row in data_list:
        ret = (row.id)
    #    print(row.id,row.phone,row.staffId,row.pwd)
        print(ret)
select()
'''
'''
a=conn.query(models.userinfos).order_by(models.userinfos.id.desc()).first()
b=(a.id)
print(b)
b+=1
print(b)
'''
#user = conn.query(models.webuser).filter(models.webuser.username == "refer").first()
#print(user.username)

#if user:
#    print("ok")
#for row in a:
#    print(row.username,row.password)
#删除
#session.query(models.taxinfos).filter(models.taxinfos.id>= 114).delete()

#修改
#session.query(models.taxinfos).filter(models.taxinfos.id== 116).update({"id":"112"})
# 提交事务
conn.commit()

#关闭数据库链接
conn.close()


