#! /usr/bin/env python

with open('google_domains.txt') as f:
    domains = f.readlines()

for domain in domains:
    domain = domain.strip()
    if not domain:
        continue
    print "address=/%s/127.0.0.1" % domain
    print "address=/.%s/127.0.0.1" % domain
