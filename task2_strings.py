"""Task 2: Strings, escape sequences, f-strings, string methods  (lessons 1.3 to 1.6)

Complete each function. Keep the function names and parameters.
Run the checks with:  python -m unittest tests.test_tasks.Task2Strings -v
"""


def greet(name):
    """Return 'Hello, <name>!' using an f-string.  greet('Ana') -> 'Hello, Ana!'"""
    return f"Hello, {name}"


def clean(text):
    """Remove spaces at both ends and make it Title Case.
    clean('  juan dela cruz ') -> 'Juan Dela Cruz'"""
    return text.strip().title()


def shout(text):
    """Return the text in UPPER CASE followed by '!'.  shout('hey') -> 'HEY!'"""
    return text.upper() + "!!"


def dialogue(speaker, line):
    """Return: <speaker> says: "<line>"  (the line wrapped in double quotes).
    dialogue('Maria', 'Hi') -> 'Maria says: "Hi"'
    Use an escape sequence or different quote types."""
    return f'{speaker} says: "{line}"'


def receipt():
    """Return a two line string using escape sequences:
    line 1 is  Item<TAB>Price   line 2 is  Pen<TAB>10
    The result must be exactly 'Item\\tPrice\\nPen\\t10'."""
    return "Item\tPrice\nPen\t10"


def initials(full_name):
    """Return the capital first letters of each word.
    initials('juan dela cruz') -> 'JDC'  (hint: split, then a loop or join)"""
    return ''.join(word[0].upper() for word in  full_name.split())


if __name__ == "__main__":
    print(greet("Ana"))
    print(clean("  juan dela cruz "))
    print(shout("hey"))
    print(dialogue("Maria", "Hi"))
    print(receipt())
    print(initials("juan dela cruz"))
