import subprocess

def run_scan(target):
	cmd = ["nmap", "-sV", target]
	result = subprocess.run(cmd, capture_output=True, text=True)
	return result.stdout
