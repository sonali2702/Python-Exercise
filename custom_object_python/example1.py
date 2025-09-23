'''
A custom object (created from a class) allows you to bundle this 
related data and behavior into a single, 
clean, and reusable blueprint. Instead of passing around 
loose dictionaries or lists, 
you work with meaningful objects like Server or LogEntry, 
making your code easier to read, maintain, and debug.
'''

# The Core Custom Object: Server

class Server:
    """A custom object to represent a server with its key attributes."""
    def __init__(self, hostname: str, ip_address: str, status: str, cpu_usage: float, memory_usage: float):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage

    def __repr__(self):
        """Provides a developer-friendly string representation of the object."""
        return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")
    
    def to_dict(self):
        """Converts the object's attributes to a dictionary."""
        return self.__dict__
    
    
# s=Server("sonali","11234","True",12.34,23.4)
# print(s.__repr__())
# print(s.to_dict())

# 1. List Operations on Custom Objects
# Exercise 1: Filtering and Sorting a Server List

# Create a list of Server objects
servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
    Server("cache-01", "192.168.1.13", "online", 5.2, 22.8),
    Server("db-02", "192.168.1.14", "offline", 0.0, 10.0),
]


'''
Scenario: You are given a list of servers and need to identify all servers that are offline 
for a maintenance report. You also need to find the server with the highest CPU usage.
'''


# --- Filtering ---
# Use a list comprehension to find all offline servers
offline_servers=[s for s in servers if s.status == "offline" ]
print(offline_servers)
print("--- Offline Servers Report ---")
for server in offline_servers:
    print(server)
    
    
# --- Sorting ---
# Use the sorted() function with a lambda key to sort by CPU usage in descending order

servers_sorted_by_cpu = sorted(servers, key=lambda s: s.cpu_usage, reverse=True)

print("\n--- Servers Sorted by CPU Usage (High to Low) ---")

for server in servers_sorted_by_cpu:
    print(server)
    
    
print(f"\nServer with highest CPU usage: {servers_sorted_by_cpu[0].hostname}")

# Exercise 2: Transforming Object Data

'''
Scenario: You need to generate a list of strings,
where each string contains the hostname and IP address of a server, for a network inventory.
'''


# Use a list comprehension to transform the data
inventory_report = [f"{s.hostname} ({s.ip_address})" for s in servers]
print(inventory_report)

print("--- Network Inventory ---")
for entry in inventory_report:
    print(entry)
    
 
#  Exercise 3: Aggregating Data from a List of Objects   
    
'''
Scenario: You need to calculate the average CPU usage for 
all servers that are currently online.
'''

# First, get only the online servers
online_servers = [s for s in servers if s.status == "online"]
print(online_servers)

if online_servers:
    # Get a list of just the CPU usage values
    cpu_usages = [s.cpu_usage for s in online_servers]
    print(cpu_usages)
    
    # Calculate the average
    average_cpu = sum(cpu_usages) / len(cpu_usages)
    print(average_cpu)
    
    print(f"--- Health Summary for {len(online_servers)} Online Servers ---")
    print(f"Average CPU Usage: {average_cpu:.2f}%")

else:
    print("No online servers found.")

# Exercise 4: Building and Accessing a Server Dictionary    
'''
Scenario: Convert your list of servers into a dictionary where 
the hostname is the key. Then, quickly retrieve the details for server app-01.
'''

# Use a dictionary comprehension to build the dictionary
# Key: server's hostname, Value: the Server object itself
for s in servers:
    print(s)
    print(s.hostname)
servers_dict = {s.hostname: s for s in servers}
print("--- Server Dictionary ---")
print(servers_dict)

# --- Fast Lookup ---
target_hostname = "app-01"
if target_hostname in servers_dict:
    app_server = servers_dict[target_hostname]
    print(f"\n--- Details for {target_hostname} ---")
    print(f"Status: {app_server.status}, CPU: {app_server.cpu_usage}%")
else:
    print(f"\nServer '{target_hostname}' not found.")
    
    
# Exercise 5: Updating Objects Within a Dictionary

'''
Scenario: A monitoring script has detected a change in web-01's status. 
Update the server's object in your dictionary to reflect that it is now 
offline and its CPU usage is 0.0.
'''

print(f"Status of web-01 before update: {servers_dict['web-01'].status}")

# --- Update the object's state ---
target_server = servers_dict.get("web-01")
print(target_server)
if target_server:
    target_server.status = "offline"
    target_server.cpu_usage = 0.0
    print("Updated web-01 status.")
    
print(f"Status of web-01 after update: {servers_dict['web-01'].status}")

print(f"Full object after update: {servers_dict['web-01']}")