# Main program

import datetime
import json
from checks.system_info import get_system_info
from checks.check_privileges import check_privileges
import checks.check_firewalls as firewall_check
from checks.check_open_ports import check_open_ports, print_open_ports

print("""
Linux Security Auditor
======================
      """)


now = datetime.datetime.now()

print(f"Report generated on: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")


system_info = get_system_info()
privilege_info = check_privileges()
firewall_info = firewall_check.check_firewall()
open_ports_info = check_open_ports()

report = {
    "system": system_info,
    "privileges": privilege_info,
    "firewall": firewall_info,
    "open_ports": open_ports_info
}

print("""
System Information
------------------
      """)

for key, value in system_info.items():
    print(f"{key}: {value}")

print("""
Privilege Audit
---------------
""")


for key, value in privilege_info.items():
    print(f"{key}: {value}")

print("""
Firewall Audit
---------------
""")


for key, value in firewall_info.items():
    print(f"{key}: {value}")


print("""
Open Ports Audit
----------------
""")

print_open_ports(open_ports_info)

print("\nGenerating report...")

filename = f"report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.json"

with open(f"reports/{filename}", "w") as report_file:
    json.dump(report, report_file, indent=4)

print(f"Report saved to the reports directory as {filename}")