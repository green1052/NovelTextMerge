import os
from datetime import datetime
from time import mktime

from natsort import natsorted
from win32_setctime import setctime


def change_file_time(file):
    setctime(file, 0)
    modTime = mktime(datetime(1970, 1, 1, 9).timetuple())
    os.utime(file, (modTime, modTime))


def file_write(content):
    file = open(f"output.txt", "a", encoding="utf-8")
    file.write(f"{content.replace('﻿', '', len(content))}\n")
    file.close()


for i in natsorted(os.listdir(os.getcwd())):
    if not i.endswith(".txt"):
        continue

    file = open(i, encoding="utf-8")
    file_write(file.read())
    file.close()

change_file_time("output.txt")
