from flask import render_template, url_for, flash, redirect
from flask_portfolio import app
from flask_portfolio.models import Example


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/examples")
def examples():
    examples = Example.query.all()
    return render_template('examples.html', examples=examples)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')
