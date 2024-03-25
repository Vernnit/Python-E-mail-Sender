import smtplib  # Simple Mail Transfer Protocol to send emails

# EmailMessage class from email module to write emails.
from email.message import EmailMessage


email_address = input('Enter your g-mail address: ')
# turn 2step verification ON and generate a app password and use that.
password = input('Enter Your password: ')

# Login to gmail using smtp server:
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

# Check if username or password is correct or incorrect.
log = False
while log == False:  # to loop until a correct password is acquired
    try:
        # attempt to log into smtp server
        smtpserver.login(email_address, password)
        log = True  # sets to true if log in is successful
        print('Login Successful !')
    except:
        print('Incorrect Username or Password:\n')
        # gets new username and password
        email_address = input('Enter new Username: ')
        password = input('Enter new Password: ')

#  write email:
email = EmailMessage()  # Instantiate a email object from EmailMessage class.

email['From'] = input('Write Your Name : ')

email['To'] = input(
    'Whom you want to send(separate by commas if multiple e-mail ids) : ')

email['Subject'] = 'I am a Ghost !'

email.set_content(
    'I hope this email finds you well. Ha ha ha !')

smtpserver.send_message(email)
