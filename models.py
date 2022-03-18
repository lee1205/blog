import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Articles(db.Model):
    __tablename__ = "articles"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}


    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.VARCHAR(255), default=' ', comment='标题')
    content = db.Column(db.TEXT, default=' ', comment='内容')
    aythor = db.Column(db.VARCHAR(255), default=' ', comment='作者')
    create_date = db.Column(db.DateTime, default=' ', comment='创建日期')

    def __repr__(self):
        return "Articles:%s" % self.title


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.VARCHAR(255), default=' ', comment='账号')
    email = db.Column(db.VARCHAR(255), default=' ', comment='邮箱')
    password = db.Column(db.VARCHAR(255), default=' ', comment='密码')

    def __repr__(self):
        return "Users:%s" % self.username
