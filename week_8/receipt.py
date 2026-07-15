def print_receipt(name, food, quantity, price, delivery_charges):

    subtotal = quantity * price
    service_charge = subtotal * 0.05
    grand_total = subtotal + service_charge + delivery_charges

    print("\n========== RECEIPT ==========")
    print("Customer :", name)
    print("Food     :", food)
    print("Quantity :", quantity)
    print("Price    : RM {:.2f}".format(price))
    print("------------------------------")
    print("Subtotal           : RM {:.2f}".format(subtotal))
    print("Service Charge (5%): RM {:.2f}".format(service_charge))
    print("Delivery Charge    : RM {:.2f}".format(delivery_charges))
    print("------------------------------")
    print("TOTAL              : RM {:.2f}".format(grand_total))
    print("==============================")