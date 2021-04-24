#!/usr/bin/env python3
"""
Author: Jakob Schaffarczyk
Date: 24. April 2021
Contact: Jakob.Schaffarczyk@leibniz-fh.de
Description: correct implementation of XML parsing
"""
import os
import sys
from time import time
import psutil
from defusedxml.ElementTree import parse
from defusedxml.ElementTree import EntitiesForbidden

start = time()
try:
    et = parse("bomb.xml")
    root = et.getroot()
    print("Output:     ", root.tag)
except EntitiesForbidden as error:
    end = time()
    proc = psutil.Process(os.getpid())
    print("Memory used:", proc.memory_info().rss / 1048576, "MB")
    print(f"Time needed: {end-start}s")
    print("Error:      ", error)
    sys.exit(1)
except Exception as error:
    print("error:", error)
    sys.exit(1)
