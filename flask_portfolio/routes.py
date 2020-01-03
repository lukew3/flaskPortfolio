from flask import render_template, url_for, flash, redirect
from flask_portfolio import app, db, mail
from flask_portfolio.models import Example
from flask_mail import Message
from flask_portfolio.forms import MessageForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/examples")
def examples():
    examples = Example.query.all()
    return render_template('examples.html', title='Examples', examples=examples)

def send_email():
    msg = Message('Contact from portfolio', sender='lukew25073@gmail.com', recipients='lukew25073@gmail.com')
    msg.body = "Message content - {{ messageForm.email }}"


@app.route("/contact")
def contact():
    form = MessageForm()
    return render_template('contact.html', title='Contact', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
