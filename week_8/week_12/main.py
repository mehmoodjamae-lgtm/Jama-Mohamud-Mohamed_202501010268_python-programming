from computer import check_computers
from counter import count_available
from display import display_status


def main():
    while True:
        computers = check_computers()
        available = count_available(computers)
        display_status(computers, available)

        again = input("\nPerform another monitoring cycle? (Y/N): ").upper()
        if again != "Y":
            print("Monitoring stopped.")
            break


main()