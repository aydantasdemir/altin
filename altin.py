import urllib2
import json
import datetime
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "*****"
SMTP_PASSWORD = "*****"
EMAIL_TO = "******"
EMAIL_FROM = "bilgi@altinfiyat.com"
EMAIL_SUBJECT = "Gold price notifier"


def get_data(url, desc):
    request = urllib2.Request(url)
    result = urllib2.urlopen(request)
    content = "\n".join(result.readlines())
    data = json.loads(content)
    message = ""
    for x in range(0, 30):
        c = data[x]
        date = datetime.datetime.fromtimestamp(int(c['timestamp']))
        message += ("%s tarihinde %s %s\n" %
                (date.strftime('%Y-%m-%d'), desc, c['buy'][:-3]))
    return message


def send_email(message_to_be_send):
    msg = MIMEText(message_to_be_send)
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_TO
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()
url_ceyrek = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_CYR"
url_gram = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_GRM"
message = "---Ceyrek altin fiyatlari--- \n\n %s\n" % get_data(url_ceyrek,
                                                    "ceyrek altin fiyati")

message += "---Gram altin fiyatlari--- \n\n %s\n" % get_data(url_gram,
                                                    "gram altin fiyati")

send_email(message)
