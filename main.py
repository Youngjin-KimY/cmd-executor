
import subprocess

cmd = ["sshfs","{account}@ip:remotepath", "localapth","-p1230"]

result = subprocess.run(cmd, capture_output=True, text=True)

# Retrieve the output or the error message
output = result.stdout if result.returncode == 0 else result.stderr
print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
