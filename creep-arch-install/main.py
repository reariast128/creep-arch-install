import os

if __name__ == "__main__":
    print("Welcome to Creep's Arch Install Script.")
    print("Showing all partitions...")
    partitions = os.popen("lsblk")
    line: str = " "
    while line:
        line = partitions.read()
        print(line)