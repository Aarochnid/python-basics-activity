import unittest
import keyword

import task1_variables as t1
import task2_strings as t2
import task3_numbers as t3


class Task1Variables(unittest.TestCase):
    def test_my_details(self):
        self.assertIsInstance(t1.student_name, str)
        self.assertTrue(t1.student_name.strip())
        self.assertIs(type(t1.age), int)
        self.assertIs(type(t1.gpa), float)
        self.assertIs(type(t1.is_enrolled), bool)

    def test_swap(self):
        self.assertEqual((t1.a, t1.b), (7, 3))

    def test_valid_names(self):
        expected = [c for c in t1.candidates if c.isidentifier() and not keyword.iskeyword(c)]
        self.assertEqual(t1.valid_names, expected)

    def test_multiple_assignment(self):
        self.assertEqual((getattr(t1, "x", None), getattr(t1, "y", None), getattr(t1, "z", None)), (0, 0, 0))


class Task2Strings(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(t2.greet("Ana"), "Hello, Ana!")
        self.assertEqual(t2.greet("Jo"), "Hello, Jo!")

    def test_clean(self):
        self.assertEqual(t2.clean("  juan dela cruz "), "Juan Dela Cruz")

    def test_shout(self):
        self.assertEqual(t2.shout("hey"), "HEY!")

    def test_dialogue(self):
        self.assertEqual(t2.dialogue("Maria", "Hi"), 'Maria says: "Hi"')

    def test_receipt(self):
        self.assertEqual(t2.receipt(), "Item\tPrice\nPen\t10")

    def test_initials(self):
        self.assertEqual(t2.initials("juan dela cruz"), "JDC")
        self.assertEqual(t2.initials("ana lim"), "AL")


class Task3Numbers(unittest.TestCase):
    def test_average(self):
        self.assertEqual(t3.average(80, 85, 90), 85.0)
        self.assertEqual(t3.average(1, 2, 2), 1.67)

    def test_hours_minutes(self):
        self.assertEqual(t3.to_hours_minutes(135), (2, 15))
        self.assertEqual(t3.to_hours_minutes(59), (0, 59))

    def test_celsius(self):
        self.assertEqual(t3.celsius_to_f(100), 212.0)
        self.assertEqual(t3.celsius_to_f(0), 32.0)

    def test_add_strings(self):
        r = t3.add_strings("12", "30")
        self.assertIs(type(r), int)
        self.assertEqual(r, 42)

    def test_even(self):
        self.assertIs(t3.is_even(4), True)
        self.assertIs(t3.is_even(7), False)

    def test_circle(self):
        self.assertEqual(t3.circle_area(2), 12.57)
        self.assertEqual(t3.circle_area(1), 3.14)


if __name__ == "__main__":
    unittest.main()
