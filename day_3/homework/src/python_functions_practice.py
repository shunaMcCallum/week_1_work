def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / 2

def subtract(num1, num2):
    return num1 - num2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(month3):
    return months [month3 - 1]

def number_to_full_month_name(month1):
    return months [month1 - 1]

def number_to_short_month_name(month4):
    month = months[month4 - 1]
    return month[:3]

def number_to_short_month_name(month1):
    month = months[month1 - 1]
    return month[:3]

def number_to_short_month_name(month10):
    month = months[month10 - 1]
    return month[:3]

def volume_of_cube(num1, num2, num3):
    return num1 * num2 * num3

def reverse_string(string):
    return string[::-1]

def farenheit_to_celsius(x):
    celsius = (x - 32) * (5 / 9)
    return round(celsius, 2)
