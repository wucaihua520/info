from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config
from config import config

# 配置数据库
db = SQLAlchemy()
# 配置redis
redis_store = None


def create_app(config_name):
    app = Flask(__name__)

    # 配置
    # app.config.from_object('configmodule.DevelopmentConfig')
    # app.config.from_object(Config)
    app.config.from_object(config[config_name])

    # app.config.from_object(DevelopmentConfig)
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 设置CSRF防护
    CSRFProtect(app)
    # 设置session
    Session(app)
    return app
