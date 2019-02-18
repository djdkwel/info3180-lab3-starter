from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase123'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'e0d4d1e91de25a'
app.config['MAIL_PASSWORD'] = ' 7b2ee2b8cb6c17'

mail = Mail(app)
from app import views