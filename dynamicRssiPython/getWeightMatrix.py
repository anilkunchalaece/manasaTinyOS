#!/usr/bin/python

import subprocess
import time
import re

cmd = 'java RssiDemo -comm serial@/dev/ttyUSB0:telos'
#cmd = 'python ./output.py'

proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

output = ''
while True:
    result = proc.poll()
    delta = proc.stdout.readline()
    print re.findall('\d+',delta)
    if len(re.findall('-',delta)) > 0:
        print "received -ve" 
    #print re.findall(r"^-?\d+(\.\d+)?$",delta)
    print delta
    #print re.findall(r'^-?[0-9]\d*(\.\d+)?$',delta)
