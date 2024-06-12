from partitions_operations import PartitionOperations as PartOps
from partitions_schemes import PartitionSchemes
from preparation import Preparation


def welcome() -> None:
    """Prints welcome message."""

    print("Welcome to Creep's Arch Install Script.")


if __name__ == "__main__":

    # Stage 0: Preparation

    welcome()
    cpu_manufacturer = Preparation.get_cpu_manufacturer()
    Preparation.check_internet_connection()
    Preparation.update_system_clock()

    # Stage 1: Preparing filesystem

    print("*"*30)
    print("\nNow, showing partitions.\n")
    PartOps.show_partitions()

    desired_partition_scheme = PartOps.choice_partition_scheme()
    partops = PartOps(desired_partition_scheme)
    partops.format_by_selected_partition_scheme()
