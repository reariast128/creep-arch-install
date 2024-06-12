from partitions_operations import PartitionOperations as PartOps
from partitions_schemes import PartitionSchemes
from preparation import Preparation


def welcome() -> None:
    """Prints welcome message."""

    print("Welcome to Creep's Arch Install Script.")


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


def user_input_partition(partitions: PartOps.lsblk_output) -> str:
    # TODO: Implement this.

    try:
        desired_partition = input("Select an option -> ")

    except Exception as e:
        print("An error has ocurred:", e)


if __name__ == "__main__":

    # Stage 0: Preparation

    welcome()
    cpu_manufacturer = Preparation.get_cpu_manufacturer()
    Preparation.check_internet_connection()
    Preparation.update_system_clock()

    # Stage 1: Preparing filesystem
    print("*"*30)
    print("\nNow, showing partitions.\n")
    PartOps.showing_partitions()

    desired_partition_scheme = choice_partition_scheme()
