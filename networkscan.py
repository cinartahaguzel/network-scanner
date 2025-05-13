import subprocess
import ipaddress
import platform

def ping(ip):
    """
    Belirtilen IP adresine ping atar.
    Aktifse True, değilse False döner.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]

    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_network(network, max_ips=20):
    """
    Verilen IP aralığında belirtilen sayıda cihazı ping ile tarar.
    """
    print(f"\n[+] Scanning network: {network}")
    net = ipaddress.ip_network(network, strict=False)

    count = 0
    try:
        for ip in net.hosts():
            if count >= max_ips:
                break
            if ping(ip):
                print(f"[✓] {ip} is active")
            else:
                print(f"[x] {ip} is not responding")
            count += 1
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting...")

if __name__ == "__main__":
    print("🔍 Basit Ağ Tarayıcı")
    network_input = input("Enter IP range (e.g., 192.168.1.0/24): ")
    max_hosts = input("How many IPs do you want to scan? (default=20): ")

    if not max_hosts.strip():
        max_hosts = 20
    else:
        max_hosts = int(max_hosts)

    scan_network(network_input, max_hosts)
