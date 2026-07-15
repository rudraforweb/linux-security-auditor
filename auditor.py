import socket
import platform
import distro



print("""
Linux Security Auditor
======================
      """)

def get_system_info():
      info = platform.uname()
      return {
            "hostname": socket.gethostname(),
            "os": distro.name(pretty=True),
            "kernel": f"{info.system} {info.release}"
      }

def print_system_info(system_info):
    for key, value in system_info.items():
        print(f"{key}: {value}")

print_system_info()
