import os
import subprocess

os.system("ls")

subprocess.run(["ls", "-la"])

# subprocess.run(["git", "log", "--oneline"])

command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
