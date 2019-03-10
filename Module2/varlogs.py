#!/usr/bin/env python
import re
import sys

if len(sys.argv) !=2:
    print "Wrong number of args. varlogs.py string"
    sys.exit(1)

word = sys.argv[1]

with open("/var/log/messages", "r") as f:	
	for line in f:
		if line.find(word) !=-1 :
                    print line.strip()

