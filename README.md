### CONCEPT
This is a very simple threaded python3 (not python2) launcher for potential use in the upcoming attack and defend CTF.

A better although slightly more complicated launcher can be found here:
[Samurai's Shuriken](https://github.com/samuraictf/shuriken-framework)

### USAGE
`$ launcher.py` or `$ python3 launcher.py`

To use this launcher, you need a newline separated list of IP addresses that you want to attack. This list should go in ips.txt.

For each service, you need to create a new class that extends the Exploit() class. This class takes an IP address to run the script against. Inside this class, you need to write your own get_flag() function that returns the flag after exploiting the service, as well as a send_chaff() function that creates meaningless network traffic to throw off the defenders. 

Use ExploitShell.py as your starting point for new exploits. Set the PORT global variable to the port your exploit connects to, the super class will handle all socket setup and teardown. Once you have written your script, place it in the exploits/ directory. launcher.py will automatically scrape this directory and import and run any new exploits it finds. 

Finally, you need to write your own submit_flag() function in launcher.py. This function will be called after every exploit. 

### TODO
* Blacklist certain teams on certain ports
* Make a config file
* Logging and Daemonizing
