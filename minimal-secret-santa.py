#!/usr/bin/env python
# -*- coding: latin-1 -*-

import smtplib
import random
from email.mime.text import MIMEText
import yaml
import sys


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


def templatized_message(msg):
    """
    Prepare the message substituing some defined variables with its value
    """
    return msg.replace('%src_peer%', msg_peer).replace('%dst_peer%', dst_peer).encode('utf-8')


def send_mail(from_index, to_index):
    """
    Generate and send the Secret Santa message 
    """
    src_peer = peer_list.keys()[from_index]
    dst_peer = peer_list.keys()[to_index]
    message = MIMEText(templatized_msg(config['message']), "html")
    mail_address = peer_list[src_peer]
    msg['Subject'] = templatized_msg(config['subject'])
    msg['From'] = config['mail_from']
    msg['To'] = mail_address
    s.sendmail("", [mail_address], message.as_string())


def init_mail_system():
    """
    Prepare the mail system
    """
    s = smtplib.SMTP(config['mail_smtp_server'], config['mail_smtp_port'])
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config['mail_smtp_login'], config['mail_smtp_passwd'])



if __name__ == '__main__':

    config = yaml.load(open(sys.argv[1], 'r'))
    peer_list = config['participants']
    init_mail_system()

    reshuffled_sequence = reshuffled_tested_range(len(peer_list.keys()))
    [ send_mail(src, dst) for (src, dst) in enumerate(reshuffled_sequence) ]

# vim: set expandtab ts=4 sw=4:
