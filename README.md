### CONCEPT
This is a very simple threaded python3 (not python2) launcher for potential use in the upcoming attack and defend CTF.

A better although slightly more complicated launcher can be found here:
[Samurai's Shuriken](https://github.com/samuraictf/shuriken-framework)

### USAGE
To use this launcher, you need a newline separated list of IP addresses that you want to attack. This list should go in ips.txt.

For each service, you need to create a new class that extends the Exploit() class. Inside this class, you need to write your own get_flag() function that returns the flag after exploiting the service.

These new classes can either be inside the Exploit.py file or new stand alone classes in their own file like the NewExploit.py example. Once you create your own exploit class, you need to include (import) it in launcher.py. You also need to append it to the exploits_list in launcher.py in the tuple format (ExploitClass, port (int), exploit_name (string)).

Finally, you need to write your own submit_flag() function in launcher.py. This function will be called after every exploit. If necessary, you can include arguments to this function if the submission engine requires additional service specific information.

### TODO
* Blacklist certain teams on certain ports
* Enable ability to add an exploit without restarting the launcher
* Error handling for bad connections
