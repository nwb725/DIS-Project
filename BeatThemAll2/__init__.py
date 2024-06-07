from flask import Flask


app = Flask(__name__)

from BeatThemAll2.routes import Index
app.register_blueprint(Index)