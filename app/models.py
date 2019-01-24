# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SAQALCHEMY_DATABASE_URI"] = "mysql://root:Wzzst310@163.com@129.204.35.106:3306/movie"
app.config["SAQAlCHEMY_TRACK_MODIFICATIONS"] = "true"
db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship('userlog', backref='user')  # 会员日志外键关系关联

    def __repr__(self):
        return "<User %r" % self.name


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<User %r" % self.id
