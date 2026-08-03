import subprocess

result = subprocess.run(["ss", "-tuln"], capture_output=True, text=True)

lines = result.stdout.splitlines()

def check_exposure(address):
    if address.startswith("0.0.0.0:") or address.startswith(":::") or address.startswith("[::]:"):
        return True
    return False

def check_open_ports():
    output_data = []
    for line in lines[1:]:
        if line.strip():
            col = line.split()
            output_data.append({
                "protocol": col[0],
                "state": col[1],
                "exposure": check_exposure(col[4]),
                "address": col[4],
                "port": col[4].rsplit(":", 1)[1]
            })
    return output_data


def print_open_ports(ports):
    for port in ports:
        print(
            f"{port['protocol'].upper()} {port['port']} - "
            f"{'Network accessible' if port['exposure'] else 'Local only'}"
        )
