import smtplib
sender = "email@gmail.com"  #Enter the email
password = "password"       #Enter the apppasword
reciever = ('receiver@gmail.com')
body = 'test email using python'
subject = 'Testing..'
print(reciever)
message = f"""From:{sender}
To:{reciever}
Subject:{subject}\n
{body}

"""
print("Connecting...")
HOST = "smtp.gmail.com"
PORT = 587
smtp = smtplib.SMTP(HOST, PORT)
smtp.starttls()
smtp.login(sender,password)
print("logged in...")
smtp.sendmail(sender,reciever,message)
print("email has been sent successfully")
