import sys
import os
from datetime import datetime

args = sys.argv


def date() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")


if "-d" in args and "-f" not in args:
    path = os.path.join(*args[2:])
    os.makedirs(path, exist_ok=True)

elif "-f" in args and "-d" not in args:
    text = input("Enter content line: ")
    with open(args[2], "a") as file:
        if os.path.getsize(args[2]) != 0:
            file.write("\n")
        current_date = date()
        file.write(current_date)
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text}\n")
            text = input("Enter content line: ")

elif "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")
    path = os.path.join(*args[d_index + 1:f_index])
    os.makedirs(path, exist_ok=True)
    text = input("Enter content line: ")
    full_path = os.path.join(path, args[f_index + 1])
    with open(full_path, "a") as file:
        if os.path.getsize(full_path) != 0:
            file.write("\n")
        current_date = date()
        file.write(current_date)
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text}\n")
            text = input("Enter content line: ")
