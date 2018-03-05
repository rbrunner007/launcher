#!/usr/bin/env python3

from time import sleep
from os import listdir
from threading import Thread
from random import shuffle
from pydoc import locate
import socket

from Exploit import Exploit

DEBUG = True
VERBOSE = True
ROUND_TIME_IN_SECONDS = 10
# read as: 1 real exploit to XX chaff
CHAFF_TO_REAL_RATIO = 20 
VERIFICATION_SERVER = "127.0.0.1"
VERIFICATION_PORT = 1337

IP_FILE = 'ips.txt'
BLACKLIST_FILE = 'blacklist.txt'
EXPLOIT_DIR = 'exploits'

class Launcher:

    def submit_flag(self, flag):
        # write some code to connect to the flag server and summit your flags.
        print("[+] Submitting: " + flag)

        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #     s.connect((VERIFICATION_SERVER, VERIFICATION_PORT))
        #     s.send(flag.encode())
        #     print(s.recv(1024))
        if "" in response:
            # Success
            return None
        else:
            # Failure
            return None

    def launch_exploit(self, exploit, ip, DEBUG):
        new_exploit = exploit(ip, DEBUG)
        chaff_array = [False]*CHAFF_TO_REAL_RATIO
        chaff_array.append(True)
        shuffle(chaff_array)
        # this is not threaded to prevent DOSing server, but also do not make
        # CHAFF_TO_REAL_RATIO so big it takes longer than a round
        for value in chaff_array:
            if value:
                try:
                    flag = new_exploit.get_flag()
                    submit_flag(flag)
                except AttributeError as a:
                    print("[!] Failed to run exploit")
            else:
                new_exploit.send_chaff()


    def load_ips(self, ip_file):
        #get the list of ips
        with open(ip_file, 'rt') as f:
            ips = f.read().strip().split('\n')

        print("[*] " + str(len(ips)) + " IPs found...")
        if VERBOSE:
            for i in ips:
                print("   [I] " + i)

        return ips


    def load_blacklist(self, blacklist_file):
        with open(blacklist_file, 'rt') as b:
            blacklist = b.read().strip().split('\n')

        if blacklist[0] == '':
            blacklist = []
        else:
            print("[*] Blacklisting " + str(len(blacklist)) + " IPs: ")
            if VERBOSE:
                for i in blacklist:
                    print("   [B] " + str(i))

        return blacklist


    def load_exploits(self, exploit_dir):
        # create a list of all Exploits found in the exploit/ directory
        exploit_list = []
        for exploit in listdir("./" + exploit_dir):
            if exploit[-3:] == ".py" and exploit != "__init__.py":
                exploit_list.append(locate(exploit_dir + "." + exploit[:-3] + \
                                        "." + exploit[:-3]))

        print("[*] " + str(len(exploit_list)) + " exploits found...")
        if VERBOSE:
            for ex in exploit_list:
                print("   [E] " + ex.__name__)

        return exploit_list


    def start(self):
        print("[*] Starting Launcher")

        # launch the threaded exploits
        while True:
            ips = self.load_ips(IP_FILE)
            blacklist = self.load_blacklist(BLACKLIST_FILE)
            exploit_list = self.load_exploits(EXPLOIT_DIR)
            for ip in ips:
                if ip not in blacklist:
                    for exploit in exploit_list:
                        print("[+] Launching " + exploit.__name__ + " against " + ip)
                        try:
                            t = Thread(
                                    name=exploit.__name__ + " : " + str(ip),
                                    target=self.launch_exploit,
                                    args=(exploit, ip, DEBUG))
                            t.start()
                        except ConnectionRefusedError:
                            print("[!] Connection Refused by " + ip)
                            pass
                        except AttributeError:
                            print("[!] Cannot connect to " + ip)
                            pass
            sleep(ROUND_TIME_IN_SECONDS)
            print("[*] Round Complete. \n")


if __name__ == "__main__":
    l = Launcher()
    l.start()

