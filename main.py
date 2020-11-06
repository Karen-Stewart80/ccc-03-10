from flask import Flask
app = Flask(__name__)

from books import books
app.register_blueprint(books)