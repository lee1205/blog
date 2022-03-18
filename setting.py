class MySQLConfig(object):

    DEBUGE = True
    SECRET_KEY = "dokea.com"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{ipaddress}:{port}/{database}".format(
        username="root", password="root", ipaddress="127.0.0.1", port="3306", database="blog")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #动态修改配置
    SQLALCHEMY_ECHO = True