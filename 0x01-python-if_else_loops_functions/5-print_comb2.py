#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print("0{:d}".format(i), end=", ")
        continue
    else:
        print("{:d}".format(i), end=", " if i < 99 else "\n")
