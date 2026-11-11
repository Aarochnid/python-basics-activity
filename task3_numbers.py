"""Task 3: Numbers, working with numbers, type conversion  (lessons 1.7 to 1.9)

Complete each function. Keep the function names and parameters.
Run the checks with:  python -m unittest tests.test_tasks.Task3Numbers -v
"""
import math


def average(a, b, c):
    """Return the average of three numbers rounded to 2 decimal places.
    average(80, 85, 90) -> 85.0"""
    return round((a + b + c) / 3, 2)


def to_hours_minutes(total_minutes):
    """Return a tuple (hours, minutes). Use // and %.
    to_hours_minutes(135) -> (2, 15)"""
    return (total_minutes // 60, total_minutes % 60)


def celsius_to_f(c):
    """Return the Fahrenheit value: c * 9 / 5 + 32.  celsius_to_f(100) -> 212.0"""
    return c * 9 / 5 + 32


def add_strings(x, y):
    """x and y are numbers typed as text. Return their sum as an int.
    add_strings('12', '30') -> 42   (type conversion!)"""
    return int(x) + int(y)


def is_even(n):
    """Return True if n is even, else False. Use the % operator."""
    return n % 2 == 0


def circle_area(r):
    """Return pi * r squared, rounded to 2 decimals. Use math.pi.
    circle_area(2) -> 12.57"""
    return round(math.pi * r ** 2, 2)


if __name__ == "__main__":
    print(average(80, 85, 90))
    print(to_hours_minutes(135))
    print(celsius_to_f(100))
    print(add_strings("12", "30"))
    print(is_even(7))
    print(circle_area(2))
