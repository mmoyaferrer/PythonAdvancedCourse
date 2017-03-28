import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

sender = 'madrilillo94@gmail.com'
receivers ='madrilillo94@gmail.com'


sender_pwd = '4k8gtanM'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender, sender_pwd)

header = 'To:' + receivers + '\n' + 'From: ' + sender + '\n' + 'Subject:testing \n'
print header

#############################
msg = MIMEMultipart()
 
msg['From'] = sender
msg['To'] = receivers
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "registro.txt"
attachment = open('C:\\Users\\Moya\\Documents\\windowsys.txt', "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
################################

message=msg.as_string()

smtpserver.sendmail(sender, receivers, message)         
print "Successfully sent email"

smtpserver.close()