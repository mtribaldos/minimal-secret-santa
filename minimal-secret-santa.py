#!/usr/bin/env python
# -*- coding: latin-1 -*-

import smtplib
import random
from email.mime.text import MIMEText
import yaml
import sys

config = yaml.load(open(sys.argv[1], 'r'))
peerlist = config['participants']
template_msg = config['message']

sequence = range(len(peerlist.keys()))
randsequence = sequence[:]

eqcount = 1
while eqcount > 0:
        eqcount = 0;
        random.shuffle(randsequence)
        for x in sequence:
                if x == randsequence[x]:
                        eqcount = eqcount + 1

s = smtplib.SMTP(config['mail_smtp_server'], config['mail_smtp_port'])
s.ehlo()
s.starttls()
s.ehlo()
s.login(config['mail_smtp_login'], config['mail_smtp_passwd'])


for x in sequence:
        msgpeer = peerlist.keys()[x]
        dstpeer = peerlist.keys()[randsequence[x]]
        msg = MIMEText(template_msg.replace('%msgpeer%', msgpeer).replace('%dstpeer%', dstpeer).encode('utf-8'), "html")
        you = peerlist[msgpeer]
        msg['Subject'] = config['subject'].replace('%msgpeer%', msgpeer).replace('%dstpeer%', dstpeer).encode('utf-8')

        msg['From'] = config['mail_from']
        msg['To'] = you
        s.sendmail("", [you], msg.as_string())
        print you, msg.as_string()
