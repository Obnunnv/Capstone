def print_mini(analysis):
	print("\n=== MINI REPORT ===\n")

	for item in analysis:
		port = item["port"]
		service = item["service"]
		risk = item["risk"]

		print(f"{port}/tcp | {service} | {risk}")


def generate_report(analysis):
	print("\n=== FULL REPORT ===\n")

	for item in analysis:
		port = item["port"]
		service = item["service"]
		risk = item["risk"]

		print(f"Port: {port}")
		print(f"Service: {service}")
		print(f"Risk: {risk}")
		print("-" * 30)
