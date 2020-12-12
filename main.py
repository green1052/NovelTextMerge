import os
from natsort import natsorted


def file_write(content):
    file = open(f"output.txt", "a", encoding="utf-8")
    file.write(f"{content}\n")
    file.close()


for i in natsorted(os.listdir(os.getcwd())):
    if not i.endswith(".txt"):
        continue

    file = open(i, encoding="utf-8")
    file_write(file.read())
    file.close()
