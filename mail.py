import smtplib
import requests

from email.mime.text import MIMEText


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'service@example.com'
    msg['To'] = 'costumer@example.com'

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as mail_server:
        mail_server.login('f915e1ec3a84f6', '5c36e6794ece0f')
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
