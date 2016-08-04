from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask('app')
app.config.update(DEBUG = True, SQLALCHEMY_DATABASE_URI="sqlite:///../database.db")
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'blog is here'
