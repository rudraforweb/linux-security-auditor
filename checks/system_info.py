import socket
import platform
import distro


def get_system_info():
      info = platform.uname()
      return {
            "hostname": socket.gethostname(),
            "os": distro.name(pretty=True),
            "kernel": f"{info.system} {info.release}"
      }



