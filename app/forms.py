from app import app, mail
from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField 
from wtforms.validators import DataRequired,Email 
from flask_mail import Message

class ContactForm(FlaskForm):
    Name = StringField('Name',validators=[DataRequired()])
    
    email = StringField('email',validators=[DataRequired(),Email()])
    
    Subject = StringField('Subject',validators=[DataRequired()])
    
    Message = StringField('Message',validators=[DataRequired()])
    
    
    