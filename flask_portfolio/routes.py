from flask import render_template, url_for, flash, redirect
from flask_portfolio import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/examples")
def examples():
    return render_template('examples.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')
