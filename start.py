#!/usr/bin/python
from subprocess import Popen
import sys
import config

filename = config.file_name
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
