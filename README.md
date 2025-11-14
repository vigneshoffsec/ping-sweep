# Live Host Discovery (Ping Sweep)

A threaded ICMP host discovery tool that identifies live hosts across large subnets and outputs results rapidly.

## Usage

```bash```
python3 src/ping_sweep.py 192.168.1.0/24
Example Output
yaml
Copy code
[+] Host Up: 192.168.1.10
[+] Host Up: 192.168.1.50

=== Alive Hosts ===
192.168.1.10
192.168.1.50
