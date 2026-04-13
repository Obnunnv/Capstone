from scanner import run_scan
from parser import parse_scan
from analyzer import analyze_results
from report import generate_report, print_mini
import shutil
import time
import subprocess
import os

os.system("clear")

def check_tool(tool):
	return shutil.which(tool) is not None

def get_distro():
	try:
		with open("/etc/os-release") as f:
			data = f.read().lower()
			if "ubuntu" in data or "debian" in data:
				return "debian"
			elif "fedora" in data or "rhel" in data or "centos" in data:
				return "redhat"
			elif "arch" in data:
				return "arch"
	except:
		pass
	return "unknown"

def suggest_install(tool, distro):
	commands = {
		"debian": f"sudo apt update && sudo apt install {tool}",
		"redhat": f"sudo dnf install {tool}",
		"arch": f"sudo pacman -S {tool}"
	}

	if distro in commands:
		print(f"[ ] Install {tool} using: {commands[distro]}")

def install(tool, distro):
	if distro == "debian":
		subprocess.run(f"sudo apt install {tool} -y", shell=True)
	elif distro == "arch":
		if tool == "wireshark":
			tool = "wireshark-qt"
		subprocess.run(f"sudo pacman -S {tool} --noconfirm", shell=True)
	elif distro == "redhat":
		subprocess.run(f"sudo dnf install {tool} -y", shell=True)

def manual(tools, distro):
	print("How would you like to install missing tools?")
	print("1. Manually")
	print("2. Automatically")

	choice = input("> ")

	os.system("clear")  

	if choice == "1":
		for tool in tools:
			suggest_install(tool, distro)

	elif choice == "2":
		print("Which tool would you like to install?\n1. Nmap\n2. Wireshark\n3. Both")
		tchoice = input("> ")

		os.system("clear")  

		if tchoice == "1":
			install("nmap", distro)
		elif tchoice == "2":
			install("wireshark", distro)
		elif tchoice == "3":
			install("nmap", distro)
			install("wireshark", distro)

print("Checking required tools...\n")

distro = get_distro()
tools = ["nmap", "wireshark"]

missing_tools = []

for tool in tools:
	if check_tool(tool):
		print(f"[✓] {tool} is installed")
	else:
		print(f"[✗] {tool} is NOT installed")
		missing_tools.append(tool)

if missing_tools:
	manual(missing_tools, distro)
else:
	print("\nAll tools are installed!")
time.sleep(3)
os.system("clear")





def main():
	print("1. Mini Scan")
	print("2. Full Report")

	choice = input("> ")
	target = "127.0.0.1"

	raw_output = run_scan(target)
	parsed = parse_scan(raw_output)
	analysis = analyze_results(parsed)

	if choice == "1":
		print_mini(analysis)
	elif choice == "2":
		generate_report(analysis)

if __name__ == "__main__":
	main()
