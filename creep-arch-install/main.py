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

    partition_choice = input("\nPlease, select between an option -> ")
    while partition_choice not in ("1", "2"):
        print("\nYou entered an invalid option.")
        partition_choice = input("Please, select between an option -> ")

    match int(partition_choice):
        case 1:
            return PartitionSchemes.CLASSIC_SCHEME
        case 2:
            return PartitionSchemes.SEPARATED_HOME_SCHEME


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
    Preparation.verify_internet_connection()
    Preparation.update_system_clock()
