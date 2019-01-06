import subprocess

"""
# init ptable
cmd = ['pytho3','./tools/initCSV.py','random','QL']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))
cmd = ['python3','./tools/initCSV.py','zeros','MCM']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))

# do learning
cmd = ['python3','Learning.py','li.csv']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))

### --------- second learning --------- ###
# init ptable
cmd = ['python3','./tools/initCSV.py','zeros','QL']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))
cmd = ['python3','./tools/initCSV.py','random','MCM']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))

# do learning
cmd = ['python3','Learning.py','li.csv']
proc = subprocess.run(cmd,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
print(proc.stderr.decode("utf8"))
"""
subprocess.call('python3 ./tools/initCSV.py random QL')
subprocess.call('python3 ./tools/initCSV.py zeros MCM')
subprocess.call('python3 Learning.py li.csv')

subprocess.call('python3 ./tools/initCSV.py zeros QL')
subprocess.call('python3 ./tools/initCSV.py random MCM')
subprocess.call('python3 Learning.py li.csv')
