#!/usr/bin/env python3

from time import sleep
from os import _exit
from os import listdir
from threading import Thread
from random import shuffle
from Exploit import Exploit
from pydoc import locate

DEBUG = True
ROUND_TIME_IN_SECONDS = 10
CHAFF_TO_REAL_RATIO = 20

def submit_flag(flag):
    # write some code to connect to the flag server and summit your flags.
    print("[+] Submitting: " + flag)

def launch_exploit(exploit, ip, DEBUG):
    new_exploit = exploit(ip, DEBUG)
    chaff_array = [False]*CHAFF_TO_REAL_RATIO
    chaff_array.append(True)
    shuffle(chaff_array)
    # this is not threaded to prevent DOSing server, but also do not make
    # CHAFF_TO_REAL_RATIO so big it takes longer than a round
    for value in chaff_array:
        if value:
            flag = new_exploit.get_flag()
            submit_flag(flag)
        else:
            new_exploit.send_chaff()


if __name__ == "__main__":
    print("[*] Starting Launcher")
    #get the list of ips
    with open('ips.txt', 'rt') as f:
        ips = f.read().strip().split('\n')
    print("[*] " + str(len(ips)) + " IPs found...")

        
    # launch the threaded exploits
    while True:
        # create a (empty) list of all Exploits found in the exploit/ directory
        exploit_list = []
        for exploit in listdir("./exploits"):
            if exploit[-3:] == ".py" and exploit != "__init__.py":
                exploit_list.append(locate("exploits." + exploit[:-3] + \
                                        "." + exploit[:-3]))
        print("[*] " + str(len(exploit_list)) + " exploits found...")

        for ip in ips:
            for exploit in exploit_list:
                try:
                    print("[+] Launching " + exploit.__name__ + " against " + ip)
                    t = Thread(
                            name=exploit.__name__ + ":" + str(ip),
                            target=launch_exploit,
                            args=(exploit, ip, DEBUG))
                    t.start()
                except AttributeError:
                    pass
        sleep(ROUND_TIME_IN_SECONDS)
        print("[*] Round Complete. \n")
