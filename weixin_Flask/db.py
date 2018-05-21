
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,func

import models
#创建连接池

engine = create_engine("mysql+pymysql://root:1qa2ws@127.0.0.1:3306/finance?charset=utf8", max_overflow=0, pool_size=5,)
Session = sessionmaker(bind=engine)


#从连接池中获取数据库链接
conn = Session()

# 提交事务
#conn.commit()

#关闭数据库链接
#conn.close()


