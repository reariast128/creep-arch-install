import socket


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

        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port))
            return True

        except socket.error as ex:
            print(f"Cannot connect to internet: {ex}")
            return False


if __name__ == '__main__':

    print(Preparation.get_cpu_manufacturer())
