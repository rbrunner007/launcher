#!/usr/bin/env python3

from time import sleep
from os import _exit
from Exploit import Exploit, ExploitTest
from NewExploit import NewExploit
from threading import Thread

debug = True
round_time_in_seconds = 10

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
    flag = new_exploit.get_flag()
    submit_flag(flag)

if __name__ == "__main__":
    print("[*] Starting Launcher")
    #get the list of ips
    with open('ips.txt', 'rt') as f:
        ips = f.read().strip().split('\n')
    #launch the threaded exploits
    while True:
        exit_test()
        for ip in ips:
            for Exploit, port, name in exploit_list:
                t = Thread(
                    name=name+ " against " + ip,
                    target=launch_exploit,
                    args=(Exploit, ip, port, name, debug))
                t.start()
        sleep(round_time_in_seconds)
