from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)  # 先にappを定義
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # そのあとに設定
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///reservations.db' #SQLiteで保存
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #警告防止
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    
    db.init_app(app) #DB初期化

    from .routes import main
    app.register_blueprint(main)

    return app
