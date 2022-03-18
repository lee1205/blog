from wtforms import Form, StringField, TextAreaField, PasswordField, validators, widgets
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm
from wtforms.fields import html5, simple
from utils import MysqlUtil

#登录用户类
# Login Form Class
class LoginForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(message='请输入用户名'),
            Length(min=2, max=25, message='长度在4-25个字符之间')
        ]
    )
    password = PasswordField(
        '密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6, max=20, message='长度在6-20个字符之间'),
        ]
    )

    def validate_username(self, field):
        sql = "SELECT * FROM users  WHERE username = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if not result:
            raise ValidationError("用户名不存在")

#注册类
#Register Form Class
class RegisterForm(FlaskForm):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default=' '
    )

    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    def validate_username(self, field):
        sql = "SELECT * FROM users  WHERE username = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if result:
            raise ValidationError("用户名已经存在")

    def validate_password(self, field):
        if field.data != self.data('password'):
            raise ValidationError("密码不一致")

#文章类
# Article Form Class
class ArticleForm(Form):
    title = StringField(
        '标题',
        validators=[
            DataRequired(message='长度在2-30个字符'),
            Length(min=2, max=30)
        ]
    )
    content = TextAreaField(
        '内容',
        validators=[
            DataRequired(message='长度不少于5个字符'),
            Length(min=5)
        ]
    )