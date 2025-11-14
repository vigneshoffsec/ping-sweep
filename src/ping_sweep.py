import subprocess
import threading
import ipaddress
import queue
import time

THREADS = 50
TIMEOUT = 1  # seconds

results = []
lock = threading.Lock()


def is_host_up(ip):
    """
    Use system ping (ICMP) to check if host is alive.
    Works on Linux and Mac automatically.
    """
    try:
        output = subprocess.run(
            ["ping", "-c", "1", "-W", str(TIMEOUT), str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return output.returncode == 0
    except Exception:
        return False


def worker(q):
    while True:
        try:
            ip = q.get_nowait()
        except queue.Empty:
            return

        if is_host_up(ip):
            with lock:
                results.append(str(ip))
                print(f"[+] Host Up: {ip}")

        q.task_done()


def run_sweep(network):
    """
    Accepts a subnet like 192.168.1.0/24
    """
    net = ipaddress.ip_network(network, strict=False)

    q = queue.Queue()

    for ip in net.hosts():
        q.put(ip)

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)

    q.join()

    for t in threads:
        t.join()

    print("\n=== Alive Hosts ===")
    for host in results:
        print(host)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Threaded ICMP Ping Sweep Tool")
    parser.add_argument("network", help="Network in CIDR format, e.g., 192.168.1.0/24")

    args = parser.parse_args()
    run_sweep(args.network)
