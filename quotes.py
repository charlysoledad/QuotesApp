import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vagtzlssjukvjy:57090a0d3416593843483c33c7c079b28a26f4515cafe274f8267033701e4575@ec2-3-211-37-117.compute-1.amazonaws.com:5432/dfmcjmvk4fq119'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class FavQuotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = FavQuotes.query.all()
    return render_template('index.html', result=result)
    #return render_template('index.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = FavQuotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))