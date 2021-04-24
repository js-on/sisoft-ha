#!/usr/bin/env python3
"""
Author: Jakob Schaffarczyk
Date: 24. April 2021
Contact: Jakob.Schaffarczyk@leibniz-fh.de
Description: wrong implementation of unparsed bash input
"""
from subprocess import Popen
from subprocess import PIPE
import os
import psutil

ip = input("IP: ")
cmd = f"ping -c1 {ip}"
p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()

proc = psutil.Process(os.getpid())
print("Memory used:", proc.memory_info().rss / 1048576, "MB")
print("Command:    ", cmd)
print("Output:     ", output.decode("utf-8"))
