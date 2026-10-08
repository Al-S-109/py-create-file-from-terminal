import sys
import os
from datetime import datetime

args = sys.argv

if "-d" in args and "-f" not in args:
    path = "/".join(args[2:])
    os.makedirs(path)

elif "-f" in args and "-d" not in args:
    text = input("Enter content line: ")
    with open(args[2], "a") as file:
        if os.path.getsize(args[2]) != 0:
            file.write("\n")
        current_date = datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))  # data
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text}\n")
            text = input("Enter content line: ")

elif "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")
    path = "/".join(args[d_index + 1:f_index])
    os.makedirs(path)
    text = input("Enter content line: ")
    with open(args[f_index + 1], "a") as file:
        if os.path.getsize(args[f_index + 1]) != 0:
            file.write("\n")
        current_date = datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))  # data
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text}\n")
            text = input("Enter content line: ")

print(args)
