import sys
import os
import subprocess

#execute command in shell (cmd)
subprocess = subprocess.Popen("curl hack.rootkit.education:2870", shell=True, stdout=subprocess.PIPE)

#read and print shell output
subprocess_return = subprocess.stdout.readlines()
print(subprocess_return)

#take the numbers from the shell output and calculate
result = int(str(subprocess_return).split()[11]) + int(str(subprocess_return).split()[13])

#input the result to shell
stream = os.popen(str(result))

#print out shell respond
output = stream.read()
print(output)

