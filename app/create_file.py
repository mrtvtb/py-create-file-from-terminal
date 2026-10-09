import os
import sys
from datetime import datetime


if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        if d_index < f_index:
            directory_names = sys.argv[d_index + 1:f_index]
            file_name = sys.argv[f_index + 1]
        else:
            directory_names = sys.argv[d_index + 1:]
            file_name = sys.argv[f_index + 1]
        path = os.path.join(*directory_names)
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, file_name)
    else:
        directory_names = sys.argv[d_index + 1:]
        path = os.path.join(*directory_names)
        os.makedirs(path, exist_ok=True)
elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    full_path = file_name


if "-f" in sys.argv:
    if os.path.exists(full_path):
        needs_blank_line = True
    else:
        needs_blank_line = False

    with open(full_path, "a") as f:
        lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            lines.append(user_input)
        if needs_blank_line:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")
