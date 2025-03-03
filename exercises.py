# Exercise 1: Calculate Area of a Triangle

# Define your function and call it below.
def calculate_area_triangle(base, height):
    area = (base * height) /2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest

def simple_interest(p, r, t):
    interest = (p * r * t) /100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount

def apply_discount(price, discount):
    new_price = price - (price * (discount/100))
    return new_price

print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature

def convert_temperature(temp, unit):
    if unit == 'C':
        temperature = (temp * 9/5) + 32
        return f"{temperature} F"
    elif unit == 'F':
        temperature = (temp - 32) * 5/9
        return f"{temperature} C"

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N

def sum_to(n):
    sum = 0
    integers = range(1, n + 1)
    for n in integers:
        sum += n
    return sum 

print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number

def largest(int1, int2, int3):
    # method using if else: 
    # if int1 > int2 and int1 > int3:
    #     return int1
    # elif int2 > int1 and int2 > int3:
    #     return int2
    # else: 
    #     return int3

    return max(int1, int2, int3)

print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip

def calculate_tip(price, tip_perc):
    tip_total = (price * tip_perc/100)
    return tip_total

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers

def product(*args):
    sum = 1
    for arg in args: 
        sum = sum * arg
    return sum 

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator


def basic_calculator(num, num2, op):

#  using if/else
    # if op == "subtract":
    #     sum = num - num2
    # elif op == "add":
    #     sum = num + num2
    # elif op == "multiply":
    #     sum = num * num2
    # elif op == "divide":
    #     sum = num / num2
    # return sum 

#  
    operations = {
        "subtract": num - num2,
        "add":  num + num2,
        "multiply": num * num2,
        "divide": num / num2
    }
    return operations.get(op)

print('Exercise 9 Result:', basic_calculator(10, 5, 'subtract'))



