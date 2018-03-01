#!/usr/bin/env python3

from time import sleep
from os import _exit
from Exploit import Exploit, ExploitTest
from NewExploit import NewExploit
from threading import Thread
from random import shuffle

debug = True
round_time_in_seconds = 10
chaff_to_real_ratio = 20

#exploit list in format (ExploitClass, exploit_port, exploit_name)
exploit_list = [
    (ExploitTest, 1337, "Exploit Test"),
    (NewExploit, 1338, "New Exploit")
]

def submit_flag(flag):
    #write some code to connect to the flag server and summit your flags.
    print(flag)

def launch_exploit(Exploit, ip, port, name, debug):
    new_exploit = Exploit(ip, port, name, debug)
    chaff_array = [False]*chaff_to_real_ratio
    chaff_array.append(True)
    shuffle(chaff_array)
    #this is not threaded to prevent DOSing server, but also do not make
    #chaff_to_real_ratio so big it takes longer than a round
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
    #launch the threaded exploits
    while True:
        for ip in ips:
            for Exploit, port, name in exploit_list:
                t = Thread(
                    name=name+ " against " + ip,
                    target=launch_exploit,
                    args=(Exploit, ip, port, name, debug))
                t.start()
        sleep(round_time_in_seconds)
