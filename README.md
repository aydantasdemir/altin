[![PyPi version](https://pypip.in/v/altin/badge.png)](https://crate.io/packages/altin/)
[![PyPi downloads](https://pypip.in/d/altin/badge.png)](https://crate.io/packages/altin/)

altin
=====

Monthly gold price notifier


Installation
============
```bash
$ (sudo) pip install altin
```

Usage
=====

Create a config file named as *.altin.conf* in your user's home folder. Example:

```bash
$ cat ~/.altin.conf

[UserInfo]
SMTP_USERNAME=yourmailusername
SMTP_PASSWORD=yourmailpassword
EMAIL_TO=mail@mail.com

```

Just run **altin** to get e-mail notifications.

```bash
$ altin
```

**example crontab entry -- run everyday at 08:00 pm.** 
```bash
0 8 * * * /usr/local/bin/altin
```

**Note**: By default, altin should be located at ```/usr/local/bin/altin```. If that's not the case, you can check the altin executable with ```pip show -f altin```)


