def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Example
# print(check_even_odd(10))
# print(check_even_odd(7))


check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

# Example
print(check_even_odd(12))  # Even
print(check_even_odd(9))   # Odd