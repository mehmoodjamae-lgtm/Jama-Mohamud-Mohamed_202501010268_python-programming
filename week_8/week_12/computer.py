def check_computers():
    computers = []  # initial value

    # iterate & check for 5 computer
    for i in range(1, 6):
        # prompt the user to classify each computer to either
        # A - Available, U - Used, M - Maintenance
        status = input(f"Computer {i} Status (A/U/M): ").upper()
        computers.append(status)

    return computers