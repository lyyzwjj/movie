# coding:utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# engine = create_engine('mysql+pymysql://root:%s@129.204.35.106:3306/movie' % parse.unquote_plus('Wzzst310@163.com'))
# app.config["SQALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Wzzst310@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Wzzst310@163.com@129.204.35.106:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "wzzst310"
app.debug = True
db = SQLAlchemy(app)

# system_url_prefix = "/movie"
system_url_prefix = ""
# app = Flask(__name__, static_folder='static', static_url_path=system_url_prefix + '/static')


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# app.register_blueprint(home_blueprint)
app.register_blueprint(home_blueprint, url_prefix=system_url_prefix)
app.register_blueprint(admin_blueprint, url_prefix=system_url_prefix + "/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
