from flask import Flask

from helpers.cors import cors
from helpers.api import api, blueprint
from helpers.database import db, migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usr:pwd@localhost:5434/projeto20241"
db.init_app(app)
migrate.init_app(app, db)

api.init_app(app)
cors.init_app(app)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)
