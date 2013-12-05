altin
=====

Monthly gold price notifier

Get Started
===========

You should define this variables before execute

```python
 SMTP_USERNAME = "Must be a gmail account"
 SMTP_PASSWORD = "Password for gmail account which is reference in SMTP_USERNAME"
 EMAIL_TO = "Mail address to send gold prices"
```
 
Usage
=====
 
   If you want to get an e-mail from this script everyday example at 8:00 a.m edit your crontab file with this line
   

```python
0 8 * * * /usr/bin/python /path/to/altin.py
```
