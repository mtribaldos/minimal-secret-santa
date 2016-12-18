#!/usr/bin/env python
# -*- coding: latin-1 -*-

""" minimal-secret-santa.py: Minimalistic 'Secret Santa' or secret gift assignation """

__author__ = u"Miguel Ángel Tribaldos"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "mtribaldos@gmail.com"

import smtplib
import random
from email.mime.text import MIMEText
import yaml
import sys
import os


def reshuffled_range(num_items):
    """
    Generate a reshuffled n-items range 
    """
    shuffled_range = range(num_items)
    random.shuffle(shuffled_range)
    return shuffled_range


def check_all_shuffled(sequence):
    """
    Check all elements in the sequence are out of its original position
    """
    return all([ index != value for (index, value) in enumerate(sequence) ])


def reshuffled_tested_range(num_items):
    """
    Shuffle a list of n items without any coincidence with its original position
    """
    while True:
        sequence = reshuffled_range(num_items)
        if check_all_shuffled(sequence):
            break    
    return sequence


def templatized_message(msg, involved_peers):
    """
    Prepare the message substituing some defined variables with its value
    """
    return msg.replace('%src_peer%', involved_peers['src']) \
              .replace('%dst_peer%', involved_peers['dst']) \
              .encode('utf-8')


def send_mail(mail_system, from_index, to_index):
    """
    Generate and send the Secret Santa message 
    """
    involved_peers = dict(src = peer_list.keys()[from_index],
                          dst = peer_list.keys()[to_index])
    message = MIMEText(templatized_message(config['message'], involved_peers), "html")
    mail_address = peer_list[involved_peers['src']]
    message['Subject'] = templatized_message(config['subject'], involved_peers)
    message['From'] = config['mail'].get('smtp_login') or os.environ['MAIL_SMTP_LOGIN']
    message['To'] = mail_address
    mail_system.sendmail("", [mail_address], message.as_string())


def init_mail_system():
    """
    Prepare the mail system
    """
    mail_system = smtplib.SMTP(config['mail']['smtp_server'], config['mail']['smtp_port'])
    mail_system.ehlo()
    mail_system.starttls()
    mail_system.ehlo()
    smtp_login = config['mail'].get('smtp_login') or os.environ['MAIL_SMTP_LOGIN']
    smtp_passwd = config['mail'].get('smtp_passwd') or os.environ['MAIL_SMTP_PASSWD']
    mail_system.login(smtp_login, smtp_passwd)
    return mail_system


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit("Usage:\n\t%s <config_file>\n" % sys.argv[0])
  
    with open(sys.argv[1], 'r') as stream:
        config = yaml.load(stream)

    peer_list = config['participants']
    dispatcher = init_mail_system()

    reshuffled_sequence = reshuffled_tested_range(len(peer_list.keys()))
    [ send_mail(dispatcher, src, dst) for (src, dst) in enumerate(reshuffled_sequence) ]

    dispatcher.close()

# vim: set expandtab ts=4 sw=4:
