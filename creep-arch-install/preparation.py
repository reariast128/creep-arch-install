import socket
import subprocess


class Preparation:
    """This class provides methods to prepare the install environment."""

    @staticmethod
    def get_cpu_manufacturer() -> str:
        """Retrieves CPU vendor."""

        manufacturer = "Unknown"

        try:
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "vendor_id" in line:
                        manufacturer = line.strip().split(":")[1].strip()
                        break

        except FileNotFoundError:
            print("Error: /proc/cpuinfo not found.")

        except Exception as e:
            print(f"Error while reading `/proc/cpuinfo`: {e}")

        return manufacturer

    @staticmethod
    def check_internet_connection(host: str = "9.9.9.9", port: int = 53, timeout: int = 3) -> bool:
        """Checks internet connection trying to connect to a DNS server."""

        print(f"Trying to connect to {host}")

        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port))
            return True

        except socket.error as ex:
            print(f"Cannot connect to internet: {ex}")
            return False

    @staticmethod
    def update_system_clock() -> None:
        try:
            subprocess.run(["timedatectl"])

        except OSError as e:
            print(f"Error while executing timedatectl: {e}")


if __name__ == '__main__':

    print(Preparation.get_cpu_manufacturer())
    Preparation.check_internet_connection()
