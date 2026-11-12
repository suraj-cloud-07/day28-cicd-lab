import unittest
from app import calculate_average, get_result


class TestStudentResult(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 75, 90]), 81.66666666666667)

    def test_pass_result(self):
        self.assertEqual(get_result(80), "PASS")

    def test_fail_result(self):
        self.assertEqual(get_result(30), "FAIL")

    def test_empty_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == "__main__":
    unittest.main()
