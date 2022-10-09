import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
from datetime import date
import time
todays_date = date.today()
mon="0"+str(todays_date.month)   
fromaddr = "ai.amams.bitdurg@gmail.com"
toaddr = ""
def send_csv(toaddr):   
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address  
    msg['From'] = fromaddr

    # storing the receivers email address 
    msg['To'] = toaddr

    # storing the subject 
    msg['Subject'] = "Attendance Sheet for the day is here!"

    # string to store the body of the mail
    body = "Greeting from AI-AMaMS: The Attendance Sheet for today is attached with this email.\nKindly Review\n\n\n Thank you!"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent 
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    filename = "Attendance_" + date + ".csv"
    path="Attendance\Attendance_" + date + ".csv"


    t="C:\\Users\\vaibh\\Downloads\\Attendance-System--main\\Attendance-System--main\\Project attendance\\Attendance\\Attendance_"+date+".csv"
    attachment = open(t, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "admin@BIT")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the
    s.quit()
tomail=""
def messmail(tomail):
  
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("ai.amams.bitdurg@gmail.com", "admin@BIT")

    # message to be sent
    message = "\n\n\n\n\n Greeting from AI-AMaMS:Your Attendance for today has been marked \n \n\n Thank you!"

    # sending the mail
    s.sendmail("ai.amams.bitdurg@gmail.com", tomail, message)

    # terminating the session
    s.quit()
def monthlyrpt(toaddre):
     # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address  
    msg['From'] = fromaddr

    # storing the receivers email address 
    msg['To'] = toaddre

    # storing the subject 
    msg['Subject'] = "Attendance Sheet for the day is here!"

    # string to store the body of the mail
    body = "Greeting from AI-AMaMS: The Monthly-Attendance Report Sheet is attached with this email.\nKindly Review\n\n\n Thank you!"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent 
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    filename = "MonthlyReport"+mon+".csv"
    


    t="C:\\Users\\vaibh\\Downloads\\Attendance-System--main\\Attendance-System--main\\Project attendance\\Attendance\\MonthlyReport"+mon+".csv"
    attachment = open(t, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "admin@BIT")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddre, text)

    # terminating the
    s.quit()
tomaile=""
def absentmark(tomaile):
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("ai.amams.bitdurg@gmail.com", "admin@BIT")

    # message to be sent
    message = "\n\n\n\n\n\nGreeting from AI-AMaMS:You have been marked absent for today  \n Kindly acknowledge to this. \n\n Thank you!"

    # sending the mail
    s.sendmail("ai.amams.bitdurg@gmail.com", tomaile, message)

    # terminating the session
    s.quit()


