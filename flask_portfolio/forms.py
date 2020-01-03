from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class messageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message' validators=[DataRequired(), Length(min=2, max=10000)])
    submit = SubmitField('Send')

from flask_mail import Mail, Message


mail = Mail(app)
