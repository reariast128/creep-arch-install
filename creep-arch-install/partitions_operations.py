from json import loads
import os
from typing import List, Dict
from partitions_schemes import PartitionSchemes


class PartitionOperations:

    type lsblk_output = List[Dict[str, str | List[str | None]]]

    @staticmethod
    def choice_partition_scheme() -> PartitionSchemes:
        """Asks to the user which partitions scheme desires and return a `PartitionScheme`."""

        print("These are the supported partition schemes:")
        print("\t( 1 ) Classic scheme: You will have a `/` ext4 partition, and a `/boot` fat32 partition.")
        print("\t( 2 ) Separated home scheme: You will have a `/` ext4 partition, a `/home` partition, and a `/boot` partition.")
        print("\t( 3 ) Classic scheme w/ swap partition: Same as classic scheme, with a swap partition.")
        print("\t( 4 ) Separated home scheme w/ swap partition: Same as separated home scheme, with a swap partition.")

        partition_choice = input("\nPlease, select between an option -> ")

        while partition_choice not in ("1", "2", "3", "4"):
            print("\nYou entered an invalid option.")
            partition_choice = input("Please, select between an option -> ")

        match int(partition_choice):
            case 1:
                return PartitionSchemes.CLASSIC_SCHEME
            case 2:
                return PartitionSchemes.SEPARATED_HOME_SCHEME
            case 3:
                return PartitionSchemes.SWAP_CLASSIC_SCHEME
            case 4:
                return PartitionSchemes.SWAP_SEPARATED_HOME_SCHEME

    @staticmethod
    def get_partitions() -> lsblk_output:
        """Using `lsblk` to see the partitions and disks in the system. 
        Then, export the `lsblk` output to a JSON, and then parse in this function.
        
        The returned JSON is in this format:

        [
            "name": ...,
            "size": ...,
            "type": ...,
            "mountpoints": [
                ...
            ],
            "children": [
                "name": ...,
                "size": ...,
                "type": ...,
                "mountpoints": [
                    ...
                ]
            ]
            ...
        ]
        """

        try:
            lsblk_partitions_deserialized = os.popen(
                "lsblk --output=NAME,SIZE,TYPE,MOUNTPOINTS --tree --json").read()
            partitions = loads(lsblk_partitions_deserialized)
            return partitions['blockdevices']

        except os.error as e:
            print(f"An error has ocurred: {e}")

    @staticmethod
    def showing_partitions() -> None:
        """Outputs partitions to screen using lsblk."""

        partitions = os.popen("lsblk")
        line: str = " "
        while line:
            line = partitions.read()
            print(line)
