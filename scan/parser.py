def parse_scan(nmap_output):
	ports = []

	for line in nmap_output.split("\n"):
		if "/tcp" in line and "open" in line:
			parts = line.split()
			port = parts[0]
			service = parts[2] if len(parts) > 2 else "unknown"
			ports.append((port, service))

	return ports
