from flask import Flask


app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "BeatThemAll"
DB_USER = "postgres"
DB_PASS = "postgres"

from BeatThemAll2.routes import Index
app.register_blueprint(Index)