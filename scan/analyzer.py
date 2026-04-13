from knowledge_base import SERVICE_INFO

def analyze_results(ports):
	results = []

	for port, service in ports:
		service = service.lower()

		info = SERVICE_INFO.get(service)

		if info:
			results.append({
				"port": port,
				"service": service,
				"risk": info["risk"],
				"description": info["description"],
				"danger": info["danger"],
				"fix": info["fix"]
			})
		else:
			results.append({
				"port": port,
				"service": service,
				"risk": "UNKNOWN",
				"description": "No known data for this service.",
				"danger": "Risk cannot be determined.",
				"fix": "Manually investigate or disable service if unnecessary."
			})

	return results

