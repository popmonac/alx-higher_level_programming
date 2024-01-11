#!/usr/bin/python3
import sys

if __name__ == "__main__":
   
    total = 0
    for i in range(len(sys.argv) - 1):
        i = i + 1
        total += int(sys.argv[i])
    print("{}".format(total))
