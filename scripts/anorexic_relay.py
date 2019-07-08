#!/usr/bin/env python
## A simple passive-relay
## ^C to exit

from pwn import *

context.log_level = 'DEBUG'

client = listen(<LISTENING_PORT>).wait_for_connection()
server = remote('<IP_TO_MITM>', <PORTYBOI>)

while 1:
    print '\n[*] FROM CLIENT'
    msg_from_client = client.recv(timeout = 10)
    server.send(msg_from_client)

    print '\n[*] FROM SERVER'
    msg_from_server = server.recv(timeout = 10)
    client.send(msg_from_server)
