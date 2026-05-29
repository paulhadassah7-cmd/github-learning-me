import os
import datetime

#print(os.system('df -h'))
#print(os.system('uptime'))
#print(os.system('systeminfo'))


def mylove(crush):
    return f"I love {crush}!"
print(mylove("python"))

def showdate():
    return datetime.datetime.now()

print(showdate())