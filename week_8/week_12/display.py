def display_status(computers, available):
    print("\n========= LAB STATUS =========")

    for number in range(len(computers)):
        print(
            f"Computer {number + 1}: {computers[number]}"
        )

    print("------------------------------")
    print(f"Available Computers: {available}")
    print("==============================")