from food_order import calculate_total

def test_order():
    assert calculate_total(10, 2) == 20

def test_total_30():
    assert calculate_total(10, 3) == 30

def test_total_100():
    assert calculate_total(20, 5) == 100

def test_total_10():
    assert calculate_total(5, 2) == 10

def test_invalid_price():
    assert calculate_total(-10, 2) == "Invalid price"

def test_invalid_quantity():
    assert calculate_total(10, -2) == "Invalid quantity"
