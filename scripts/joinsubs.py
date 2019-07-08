#!/usr/bin/env python3
import sys

if len(sys.argv) != 4:
  print('Usage: ' + sys.argv[0] +' subdomains domains out-file')
  sys.exit(1)

subdomains = open(sys.argv[1]).read().split('\n')
domains = open(sys.argv[2]).read().split('\n')
outfile = sys.argv[3]

with open(outfile, 'w') as out_handler:
  for domain in domains:
    for sub in subdomains:
        sub = sub.strip()
        out_handler.write('{}.{}\n'.format(sub, domain))

