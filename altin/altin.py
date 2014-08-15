import urllib2
import json
import datetime
import smtplib
import os.path
import ConfigParser
from email.mime.text import MIMEText

config= ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.altin.conf'))

SMTP_SERVER = "smtp.gmail.com" #SMTP server for gmail
SMTP_PORT = 587 #SMTP port for gmail
SMTP_USERNAME = config.get('UserInfo','SMTP_USERNAME')
SMTP_PASSWORD = config.get('UserInfo','SMTP_PASSWORD')
EMAIL_TO = config.get('UserInfo','EMAIL_TO')
EMAIL_FROM = "bilgi@altinfiyat.com" #You may change this mail address
EMAIL_SUBJECT = "Gold price notifier" #You may change this subject


def get_data(url, desc):
    """Get data from api, parse it and return as message"""
    request = urllib2.Request(url)
    result = urllib2.urlopen(request)
    content = "\n".join(result.readlines())
    data = json.loads(content)
    message = ""
    for x in range(0, 30):#Get all data in a month
        c = data[x]
        date = datetime.datetime.fromtimestamp(int(c['timestamp']))
        message += ("%s tarihinde %s %s\n" %
                (date.strftime('%Y-%m-%d'), desc, c['buy'][:-3]))
    return message


def send_email(message_to_be_send):
    """Send mail using SMTP"""
    msg = MIMEText(message_to_be_send)
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_TO
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

def main():
    url_ceyrek = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_CYR" #API for ceyrek
    url_gram = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_GRM" #API for gram
    message = "---Ceyrek altin fiyatlari--- \n\n %s\n" % get_data(url_ceyrek,
                                                    "ceyrek altin fiyati")

    message += "---Gram altin fiyatlari--- \n\n %s\n" % get_data(url_gram,
                                                    "gram altin fiyati")
    send_email(message)
