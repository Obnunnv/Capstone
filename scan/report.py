def print_mini(analysis):
	print("\n=== MINI REPORT ===\n")

	for port, service, risk in analysis:
		print(f"{port} | {service} | {risk}")


def generate_report(results):
	print("\n=== FULL SECURITY REPORT ===\n")

	for item in results:
		print(f"Port: {item['port']}")
		print(f"Service: {item['service']}")
		print(f"Risk: {item['risk']}\n")

		print("Description:")
		print(item["description"])

		print("\nWhy this is risky:")
		print(item["danger"])

		print("\nHow to fix it:")
		print(item["fix"])

		print("\n" + "-" * 40 + "\n")
