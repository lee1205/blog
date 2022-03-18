import time
from passlib.hash import sha256_crypt
from mysql_util import *

#hash加密
def hash(password):
    return sha256_crypt.hash(password)

#hash解密
def hashc(password_candidate, password):
    # 调用verify方法验证，如果为真，验证通过
    if sha256_crypt.verify(password_candidate, password):
        return True
    else:
        return False

#时间
def getDatatime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#时间戳
def getTimeStamp():
    return time.localtime()

#判断账号密码是否为空
def is_mull(username, password, confirm):
    if username == '':

        return '用户名不能为空'
    elif (password == '' or confirm == ''):
        return '密码或确认密码为空'
    else:
        return True

#检测账号是否已存在
def checkusername(username):
    db = MysqlUtil()
    sql = "select * from users where username = '%s'" % (username)
    result = db.fetchone(sql)
    if result == None:
        return True
    else:
        return False



#添加账户
def addacount(username, password, email):
    db = MysqlUtil()
    sql = "INSERT INTO users(username,email, password)  VALUES ('%s', '%s', '%s')" % (username, email, password)
    result = db.insert(sql)
    return result

