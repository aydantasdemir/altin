import urllib2
import json
import datetime
import smtplib
import os.path
import ConfigParser
from email.mime.text import MIMEText

CONFIG_FILE = '~/.altin.conf'

DEFAULTS = {
    "SMTP_SERVER": "smtp.gmail.com",
    "SMTP_PORT": "587",
}


def get_config():

    if not os.path.exists(os.path.expanduser(CONFIG_FILE)):
        raise LookupError("no config file found. ({0})".format(CONFIG_FILE))

    config = ConfigParser.ConfigParser(DEFAULTS)
    config.read(os.path.expanduser('~/.altin.conf'))

    return config


def get_data(url, desc):

    result = urllib2.urlopen(urllib2.Request(url))
    content = "\n".join(result.readlines())
    data = json.loads(content)

    message = ""
    for x in range(0, 30):
        c = data[x]
        date = datetime.datetime.fromtimestamp(int(c['timestamp']))
        message += ("%s tarihinde %s %s\n" % (date.strftime('%Y-%m-%d'), desc, c['buy'][:-3]))

    return message


def send_email(message):

    config = get_config()

    msg = MIMEText(message)
    msg['Subject'] = "Gold price notifier"
    msg['Subject'] = "Gold price notifier"
    msg['To'] = config.get('UserInfo','EMAIL_TO')
    msg['From'] = "bilgi@altinfiyat.com"

    mail = smtplib.SMTP(config.get('UserInfo','SMTP_SERVER'), config.get('UserInfo','SMTP_PORT'))
    mail.starttls()
    mail.login(config.get('UserInfo','SMTP_USERNAME'), config.get('UserInfo','SMTP_PASSWORD'))
    mail.sendmail("noreply@altin.py", msg["To"], msg.as_string())
    mail.quit()


def main():

    url_ceyrek = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_CYR"
    url_gram = "http://api.piyasa.com/json/?kaynak=metal_arsiv_ay_alti_GRM"

    message = "---Ceyrek altin fiyatlari--- \n\n %s\n" % get_data(url_ceyrek, "ceyrek altin fiyati")
    message += "---Gram altin fiyatlari--- \n\n %s\n" % get_data(url_gram, "gram altin fiyati")
    send_email(message)
