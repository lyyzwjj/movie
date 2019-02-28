# coding:utf8
from flask import Flask, render_template

# system_url_prefix = "/movie"
system_url_prefix = ""
# app = Flask(__name__, static_folder='static', static_url_path=system_url_prefix + '/static')
app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# app.register_blueprint(home_blueprint)
app.register_blueprint(home_blueprint, url_prefix=system_url_prefix)
app.register_blueprint(admin_blueprint, url_prefix=system_url_prefix + "/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
