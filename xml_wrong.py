#!/usr/bin/env python3
"""
Author: Jakob Schaffarczyk
Date: 24. April 2021
Contact: Jakob.Schaffarczyk@leibniz-fh.de
Description: wrong implementation of XML parsing
"""
from time import time
import os
import xml.etree.ElementTree as ET
import psutil

start = time()
tree = ET.parse("bomb.xml")
root = tree.getroot()
end = time()

proc = psutil.Process(os.getpid())
print("Memory used:", proc.memory_info().rss / 1048576, "MB")
print(f"Time needed: {end-start}s")
print("Output:", root.tag)
