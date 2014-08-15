altin
=====

Monthly gold price notifier

Get Started
===========

You should define .altin.conf file in your home directory in this format

```
$ vi ~/.altin.conf

[UserInfo]
SMTP_USERNAME=yourmailusername
SMTP_PASSWORD=yourmailpassword
EMAIL_TO=mail@mail.com

```
 
Usage
=====
 
   If you want to get an e-mail from this script everyday example at 8:00 a.m edit your crontab file with this line
   

```python
0 8 * * * /usr/bin/python /path/to/altin.py
```
