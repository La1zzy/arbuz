from flask import Flask
import os
from models import db
from routes import routes
from config import Config

def create_app():
    app = Flask(__name__)
    
    try:
        app.config.from_object(Config)
        print(f"Database URL configured: {app.config['SQLALCHEMY_DATABASE_URI'][:20]}...")
        
        db.init_app(app)
        app.register_blueprint(routes)
        
        print("Application successfully configured")
    except Exception as e:
        print(f"Error during app initialization: {str(e)}")
        print(f"Environment variables: {dict(os.environ)}")
        raise

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
