#!/usr/bin/python3
import os
import sys
import subprocess as sub
import time


message = str(sys.argv[1])
duration = float(sys.argv[2])
try:
    pid = os.fork()
    if pid > 0 :
      sys.exit(0)
except OSError:
    sys.stderr.write("fork 1 failed")
    sys.exit(1)

os.chdir("/")
os.setsid()
os.umask(0)

try:
    pid = os.fork()
    if pid > 0:
      sys.exit(0)
except OSError:
    sys.stderr.write("fork 2 failed")
    sys.exit(1)

time.sleep(duration)
sub.call(['notify-send',message])
