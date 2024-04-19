# Rewrite the calculations for 'odd_numbers' and 'square_list' by using list comprehention.
# Have you used it before? Do you use it at all? What list was used in this example?

numbers = [1, 1, 2, 3, 5, 8, 13]

def is_odd(x):
    return bool(x % 2)

def square(x):
    return x*x

odd_numbers = list(filter(is_odd, numbers))
# odd_numbers = []
square_list = list(map(square, numbers))
# square_list = []

print(odd_numbers)
print(square_list)