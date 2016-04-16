#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Zabbix SMTP Alert script for ele mail.
"""

import sys
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

import logging
LOG_FILE = "/var/log/zabbix/smtp.log" 

# Mail Account
MAIL_ACCOUNT = ''
MAIL_PASSWORD = ''

# Sender Name
SENDER_NAME = u'Zabbix_Email_Alerm'

# Mail Server
SMTP_SERVER = ''
SMTP_PORT = 25
# TLS
SMTP_TLS = False

def log(log):
	logging.basicConfig(filename=LOG_FILE, format='%(asctime)s %(message)s', level=logging.DEBUG)
	logging.warning(log)

def send_mail(recipient, subject, body, encoding='utf-8'):
	session = None
	msg = MIMEText(body, 'plain', encoding)
	msg['Subject'] = Header(subject, encoding)
	msg['From'] = Header(SENDER_NAME, encoding)
	msg['To'] = recipient
	msg['Date'] = formatdate()
	try:
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		if SMTP_TLS:
			session.ehlo()
			session.starttls()
			session.ehlo()
		session.login(MAIL_ACCOUNT, MAIL_PASSWORD)
		session.sendmail(MAIL_ACCOUNT, recipient, msg.as_string())
		return 0
	except Exception as e:
		log("Send Unsucess!{0}".format(e))
		return 1
	finally:
		# close session
		if session:
			session.quit()

if __name__ == '__main__':
	"""
	recipient = sys.argv[1]
	subject = sys.argv[2]
	body = sys.argv[3]
	"""
	if len(sys.argv) == 4:
		send_mail(
		recipient=sys.argv[1],
		subject=sys.argv[2],
		body=sys.argv[3])
	else:
		print u"""requires 3 parameters (recipient, subject, body)
\t$ zabbix-alert-smtp.py recipient subject body
"""
