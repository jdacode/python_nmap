import nmap3


class Nmap:
    def __init__(self, ip):
        self.ip = ip

    def run_nmap(self):
        print(self.ip)
        nmap = nmap3.Nmap()
        os_results = nmap.scan_top_ports("127.0.0.1")
        return os_results






