### CONCEPT
This is a very simple threaded python3 (not python2) set server primarily to test the student's ability to use a launcher in an Attack and Defend CTF. You can use it to run multiple different services, or you can simply run the same service on multiple ports.

### USAGE
The main file is the server.py file that utilizes the Service.py Class file. The server.py file is responsible for making multiple, threaded instances of each of the included Services (one per team). The server.py file is also responsible for generating and then updating the flag files over a periodic basis (as set by round_time_in_seconds).

The Service Class files are responsible for replicating the functionality of an individual service included the ability to handle incoming threaded connections.

To run, you need to update the server.py file. In particular, you need to update the teams array with a tuple for each team that includes the team's name (string), directory (string that will be created if it does not exist), auth_string (password to access services if required), base_port (int). The base_port is generally a 100 port range per team). You also need to update the service_list array with a tuple that is the ServiceClass, individual port (int), and service name for each service.

### TODO
