
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models
#创建连接池

engine = create_engine("mysql+pymysql://root:1qa2ws@127.0.0.1:3306/finance?charset=utf8", max_overflow=0, pool_size=5,)
Session = sessionmaker(bind=engine)


#从连接池中获取数据库链接
session = Session()


# ############# 执行ORM操作 #############
#obj1 = models.userinfos(id="998",phone='111111111111',pwd='22222')
#session.add(obj1)

obj2 = models.taxinfos(id="114",companyName="北京市朝阳区东四环中路财富国际金融中心",taxNumber="012345678987654321",address="北京市朝阳区中间财富中心22层",phone="010-88888888",bank="中国银行北京市分行",cardNo="564984416432")
session.add(obj2)
# 提交事务
session.commit()

#关闭数据库链接
session.close()


