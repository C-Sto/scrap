#!/usr/bin/env python
# This sends emails with payloads in subject and body
# Used to test for command injection server-side mail processors/parsers 

import smtplib
import sys

# errcheck
if len(sys.argv) < 2:
    'Usage: ' + sys.argv[0] + ' payloads.txt'
    sys.exit(1)

# fill these things out properly
smtp_username = ''
smtp_password = ''
smtp_server = ''

# these things too
smtp_port = 1337
to_address = ''
from_address = ''
    
# setup SMTP connection
smtpObj = smtplib.SMTP(smtp_server, smtp_port)
smtpObj.starttls()
smtpObj.login(smtp_username, smtp_password)

payloads = []

# read payloads from file
filename = sys.argv[1]
with open(filename, 'r') as in_file:
    for line in in_file:
        payloads.append(line.rstrip())

# send an email with each payload in the subject and body
# add in from_address if using a relay that doesn't validatet from address
for payload in payloads:
    subject = 'Subject: ' + payload + '\n'
    body = payload
    message = subject + body

    print '\n\nSending ' + message
    
    smtpObj.sendmail(from_address, to_address, message)

smtpObj.quit()
