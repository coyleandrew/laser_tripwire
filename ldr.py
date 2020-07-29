'''
This program is used in conjunction with a Raspberry Pi to create an intrusion
detection system
'''

from gpiozero import LightSensor, Buzzer
from time import sleep
import smtplib

'''
The Emailer class was created using the tutorial found at
https://www.bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/
'''
# Email variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'lasertripwire1@gmail.com'
GMAIL_PASSWORD = 'dQ6hvFD8CZkuMD2'
SEND_TO = 'coyleandrewi@gmail.com'
EMAIL_SUBJECT = 'Security Breach!'
EMAIL_CONTENT = 'The office door has been opened!'

class Emailer:
    def sendmail(self, recipient, subject, content):
        
        # Create Headers
        headers = ["From: " + GMAIL_USERNAME,
                   "Subject: " + subject,
                   "To: " + recipient]
        headers = "\r\n".join(headers)
        
        # Connect to gmail server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        
        # Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        # Send email and exit
        session.sendmail(GMAIL_USERNAME, recipient,
                         headers + "\r\n\r\n" +
                         content)

'''
The proceeding code was created with the help of the video:
https://www.youtube.com/watch?v=4oJiXlPs46o&list=LLKEK8OLeA8km6pzMdrogy4w&index=6&t=440s
'''
# Create necessary objects
sender = Emailer()
ldr = LightSensor(4)
buzzer = Buzzer(17)

while True:
    sleep(0.1)
    if ldr.value < 0.5:
        buzzer.on()
        sender.sendmail(SEND_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
    else:
        buzzer.off()

