import re
import sys

if len(sys.argv) > 1 and sys.argv[1]:
    with open(sys.argv[1], "r") as file:
        data = file.read()
        data = re.sub(r'[^a-z]', "", data)
        with open(f'clean_{sys.argv[1]}', "w") as cleanFile:
            cleanFile.write(data)
else:
    print("file not defined")
    