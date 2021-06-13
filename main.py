import os
from datetime import datetime
from time import mktime

from natsort import natsorted
from win32_setctime import setctime


def change_file_time(file):
    setctime(file, 0)
    mod_time = mktime(datetime(2000, 1, 1, 9).timetuple())
    os.utime(file, (mod_time, mod_time))


def file_write(content):
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(f"{content}\n")

    change_file_time("output.txt")


for i in natsorted(os.listdir(os.getcwd())):
    if not i.endswith(".txt"):
        continue

    with open(i, encoding="utf-8") as file:
        file_write(file.read())
