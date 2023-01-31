def calc_discount(x):
    discounted_price = x - (.4 * x)
    tax = .0775 * discounted_price
    return discounted_price + tax

x = 139.99
print(calc_discount(x))
print(calc_discount(99.99))