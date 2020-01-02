from flask import Flask, session, g, render_template
app = Flask(__name__)

from flask_portfolio import routes
