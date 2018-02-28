#!/usr/bin/env python3

from Service import Service, ServiceTest
from threading import Thread
from binascii import b2a_hex
from time import sleep
import os

debug = True
round_time_in_seconds = 10
exit_file = 'exit_server.txt'
ip = '0.0.0.0'
file_directory = os.getcwd()

#ServiceClass, individual port, service name
service_list = [
    (ServiceTest, 1, "Service Test")#, (NewService, 1338, "New Service")]
]

#name, directory, auth_string, base_port
teams =  [
    ("R00t Reg", 'team1', 'teamPass1', 40000),
    ("Sh3ll Squad", 'team2', 'teamPass2', 41000),
    ("Pwn Plat00n", 'team3', 'teamPass3', 42000)
]

flags = []
flag_files = []

def add_flag(flag_file):
    with open(flag_file, 'wt') as f:
        flag = b2a_hex(os.urandom(16)).decode('utf-8')
        flags.append(flag)
        f.write(flag)

def create_flag(team_dir, service_name):
    flag_file = os.path.join(team_dir, service_name + '.flag')
    flag_files.append(flag_file)
    add_flag(flag_file)
    return flag_file

def update_flags():
    print("Updating Flags")
    for flag_file in flag_files:
        with open(flag_file, 'rt') as f:
            old_flag = f.read().strip()
        add_flag(flag_file)
        flags.remove(old_flag)


def launch_service(Service, ip, port, flag_location, name, debug, auth_string):
    new_service = Service(ip, port, flag_location, name, debug, auth_string)
    new_service.run_server()

if __name__ == "__main__":
    print("[*] Starting Services")
    with open(exit_file, 'wt') as f:
        f.write('\n')
    #create team directories if they do not exist
    for team_name, team_dir, auth_string, port_base in teams:
        real_team_dir = os.path.join(file_directory, team_dir)
        if not os.path.exists(real_team_dir):
            os.makedirs(real_team_dir)
            print("Making " + team_dir)
        #launch the threaded exploits
        for Service, port, name in service_list:
            flag_location=create_flag(real_team_dir, name)
            t = Thread(
                name="Port "+str(port),
                target=launch_service,
                args=(Service, ip, port_base + port, flag_location, name, debug, auth_string))
            t.start()
    while True:
        with open(exit_file, 'rt') as f:
            if f.read().strip() != "":
                os._exit(1)
        sleep(round_time_in_seconds)
        update_flags()
