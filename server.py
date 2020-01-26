import smtplib

sender = 'testing123@gmail.com'
receivers = ['testing@hotmail.com']

message = """From: From Manav <testing123@gmail.com>
To: To Manav <testing@hotmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

gmail_user = "testing123@gmail.com"
gmail_app_password = "sslkhjzhsdfgg"
sent_from = "testing123@gmail.com"
sent_to = "testing@hotmail.com"
email_text = message

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
