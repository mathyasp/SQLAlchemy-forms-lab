from books_app.extensions import app, db
from books_app.routes import main
from flask_migrate import Migrate

app.register_blueprint(main)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
