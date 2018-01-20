import time
import os
from datetime import datetime as dt


__win_host__ = r'C:\Windows\System32\drivers\etc\hosts'
__mac_linux_host__ = 'etc/hosts'
__temp_hosts__ = 'hosts.txt'

__redirect__ = '127.0.0.1'
__website_list__ = ['www.facebook.com', 'facebook.com', 'www.reddit.com', 'reddit.com']
__year__ = dt.now().year
__month__ = dt.now().month
__day__ = dt.now().day

while True:
    if dt(__year__, __month__, __day__, 8) <  dt.now() < dt(__year__, __month__, __day__, 16):
        print('Working hours')
        with open(__temp_hosts__, 'r+') as host_file:
            __content__ = host_file.read()
            for website in __website_list__:
                if website in __content__:
                    pass
                else:
                    host_file.write(__redirect__ + " " + website + "\n")
    else:
        with open(__temp_hosts__, 'r+') as host_file:
            __lines__ = host_file.readlines()
            host_file.seek(0)
            for line in __lines__:
                if not any(website in line for website in __website_list__):
                    host_file.write(line)
            host_file.truncate()
        print('Non-working hours')
    time.sleep(5)