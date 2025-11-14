# 🖧 Live Host Discovery (Ping Sweep)

A fast, threaded **ICMP + TCP SYN host discovery tool** designed to identify live systems across large subnets while minimizing noisy traffic patterns that trigger basic IDS alerts.

This tool produces **Nmap-ready host lists**, clean reports, and supports large `/16` or `/24` range sweeps with high-speed concurrency.

---

# 📂 Project Structure

```
ping-sweep/
│── src/
│   └── ping_sweep.py
│── wordlists/
│   └── .gitkeep
│── reports/
│   └── .gitkeep
│── README.md
│── LICENSE
```

---

# 🚀 Features

### ✔ ICMP Ping + TCP SYN Fallback

* ICMP ping for standard host discovery
* TCP SYN (default port 80) for hosts that block ICMP
* Works even in restricted or filtered environments

### ✔ High-Speed Threaded Scanning

* Default **100 threads**
* Handles large subnets quickly
* Optimized for recon and OSCP-style labs

### ✔ Randomized IP Order (Basic IDS Evasion)

Prevents linear scanning patterns often detected by IDS.

### ✔ Real-Time Progress Bar

Track sweep progress with live percentage updates.

### ✔ Nmap-Ready Export

Automatically generates:

```
reports/nmap-list-<timestamp>.txt
```

Use directly:

```bash
nmap -sV -Pn -iL reports/nmap-list-*.txt
```

### ✔ Multi-Format Reporting

All results stored in `reports/`:

* `.txt` — simple host list
* `.json` — structured host inventory
* `.txt` (Nmap list) — for immediate vulnerability scanning

---

# 🧪 Usage

### Basic Scan

```bash
python3 src/ping_sweep.py 192.168.1.0/24
```

### Example Output

```
Progress: 57.20%
[+] Host Up: 192.168.1.10
[+] Host Up: 192.168.1.25

=== Scan Completed ===
Reports saved in /reports folder
```

### Example Report Files

```
reports/hosts-20251114-141200.txt
reports/hosts-20251114-141200.json
reports/nmap-list-20251114-141200.txt
```

---

# 🛠 How It Works

### 1. ICMP Probe

A lightweight ICMP echo request:

```
ping -c 1 -W 1 <IP>
```

Quiet, fast, and reliable.

### 2. TCP SYN Probe

If ICMP fails, the script opens a TCP connection:

```python
sock.connect((ip, 80))
```

Many networks allow TCP even when ping is blocked.

### 3. Randomized Target Order

The list of IPs is shuffled to avoid sequential scanning patterns.

### 4. Thread Pool Model

100 worker threads pull IPs from a queue for rapid enumeration.

### 5. Reporting Engine

Results are saved into **TXT, JSON, and Nmap formats** automatically.

---

# 📈 Benchmarks (Local Lab Test)

Subnet: `10.0.0.0/24` (254 hosts)
Threads: 100

| Probe Type          | Avg Time     |
| ------------------- | ------------ |
| ICMP only           | ~3.8 seconds |
| ICMP + TCP fallback | ~5.1 seconds |

Speed varies by network latency and firewall behavior.

---

# 📌 Roadmap / Future Enhancements

* ARP sweep mode (local network)
* Masscan integration
* Custom TCP port selection
* Passive sniffing mode
* OS fingerprint hints via TTL analysis

---

# 🧑‍⚖️ Ethical Disclaimer

This tool is intended for **authorized penetration testing and educational use only**.
Scanning networks that you do not own or have explicit permission to test is **illegal**.

---

# 👨‍💻 Author

**Vignesh Mani**
Offensive Security Researcher
GitHub: [https://github.com/vigneshoffsec](https://github.com/vigneshoffsec)
LinkedIn: [https://linkedin.com/in/vignesh-m17](https://linkedin.com/in/vignesh-m17)
