from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import Anuncio
import smtplib
import config

def notify(anuncio: Anuncio):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(config.email_user, config.email_password)
    # message
    msg = MIMEMultipart()
    msg['From'] = config.email_user
    msg['To'] = config.email_to_notify
    msg['Subject'] = anuncio.titulo
    server.quit()