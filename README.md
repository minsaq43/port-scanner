# Port Scanner - Mini Nmap

A simple Python Port Scanner I built to understand how Nmap works behind the scenes.

## What does it do?

- Takes a target IP from the user
- Scans ports 1 to 1024
- Shows which ports are OPEN
- Uses Python `socket` library

## How to use it?

1. Run the file:
   python port_scanner.py

2. Enter target IP when it asks:
   Example: 127.0.0.1

3. It will print:
   Port 80 is Open
   Port 443 is Open

## What did I learn?

- How TCP connections work
- What `socket`, `connect_ex`, `settimeout`, and `close` do
- Why Nmap needs timeout to be fast
- How to debug: factory vs car, pair (IP, Port), indentation

## Disclaimer

For learning and authorized testing only. Only scan systems you own or have permission to test.
