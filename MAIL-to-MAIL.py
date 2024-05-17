import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 

RECIPIENT_EMAIL = "rabotaem@radevich-hair.ru"

def send_email(subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = os.getenv("EMAIL_USER")
    smtp_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body,"plain"))


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user,RECIPIENT_EMAIL,msg.as_string())
        server.quit()
        print(f"Email sent to {RECIPIENT_EMAIL} with subject: {subject}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


def send_message_via_email(message_text, link):
    
    send_email(subject='New Message', body=message_text)
    send_email(subject='New Link', body=link)

