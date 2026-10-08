import os
import sys
from datetime import datetime


if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        directories = sys.argv[d_index+1:f_index]
        file_name = sys.argv[f_index+1:]
    else:
        directories = sys.argv[d_index+1:]
    
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

lines = []
while True:
    user_input = input("Enter content line: ")
    if user_input == "stop":
        break
    lines.append(user_input)

with open(file_name, "a") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")