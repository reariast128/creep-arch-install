from json import loads
import os
from typing import List, Dict

class PartitionOperations: 

    type lsblk_output = List[Dict[str, str | List[str | None]]]

    @staticmethod
    def get_partitions() -> lsblk_output:
        """Using `lsblk` to see the partitions and disks in the system. 
        Then, export the `lsblk` output to a JSON, and then parse in this function."""
    
        try:
            lsblk_partitions_deserialized = os.popen("lsblk --output=NAME,SIZE,TYPE,MOUNTPOINTS --tree --json").read()
            partitions = loads(lsblk_partitions_deserialized)
            return partitions['blockdevices']

        except os.error as e:
            print(f"An error has ocurred: {e}")
    
    @staticmethod
    def showing_partitions() -> None:
        """Outputs partitions to screen using lsblk."""

        print("Showing all partitions...")
        partitions = os.popen("lsblk")
        line: str = " "
        while line:
            line = partitions.read()
            print(line)