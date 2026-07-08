from food_order import calculate_total

def main():
    price = float(input("Price (RM): "))
    quantity = int(input("Quantity: "))

    total = calculate_total(price, quantity)

    print(f"Total Payment = RM {total:.2f}" if isinstance(total, (int, float)) else total)

if __name__ == "__main__":
    main()