from flask import Flask
from .extensions import mongo
from .main.routes import main
import certifi
certifi.where()

def create_app():
    app=Flask(__name__)
    app.config['MONGO_URI'] ='mongodb+srv://newuser1:<Password>@cluster0.c0zk9.mongodb.net/<Database_name>?ssl=true&ssl_cert_reqs=CERT_NONE' 
    # retryWrites=true&w=majority'

    mongo.init_app(app)
    app.register_blueprint(main)
    return app
