import smtplib  # Simple Mail Transfer Protocol to send emails

# EmailMessage class from email module to write emails.
from email.message import EmailMessage

email = EmailMessage()  # Instantiate a email object from EmailMessage class.


email['From'] = input('Write Your Name : ')

email['To'] = input(
    'Whom you want to send(separate by commas if multiple e-mail ids) : ')

email['Subject'] = 'I am a Ghost !'

email.set_content(
    'I hope this email finds you well. Ha ha ha !')


# Login to gmail using smtp server
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

smtpserver.login('andreihoward603@gmail.com', 'rwov kzvk zxge xize')

smtpserver.send_message(email)
