from flask import Flask
from models import db
from routes import routes
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Проверяем конфигурацию перед инициализацией
    try:
        app.config.from_object(Config)
        db.init_app(app)
        app.register_blueprint(routes)
    except Exception as e:
        print(f"Error during app initialization: {str(e)}")
        raise

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
