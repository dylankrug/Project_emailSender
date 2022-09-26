import os

import csv
import smtplib
from email.message import EmailMessage


email_sender = 'npc.dummy.mail@gmail.com'
email_password = os.environ.get("E_PASS")
subject = 'Python subscription'


with open('Email.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
        text = "Hello " + line[1] + " hope this email reached you well."
        # print(text)
        email_receiver = line[0]
        # print(email_receiver)
        msg = EmailMessage()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.set_content(text)
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

    smtp.quit()