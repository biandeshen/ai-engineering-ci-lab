import unittest

from task_state import parse_task


class ParseTaskTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(parse_task(" Doing : ship a demo "), ("doing", "ship a demo"))

    def test_colon_in_description(self):
        self.assertEqual(parse_task("todo: check A: B"), ("todo", "check A: B"))

    def test_missing_separator(self):
        with self.assertRaises(ValueError):
            parse_task("todo ship a demo")

    def test_unknown_state(self):
        with self.assertRaises(ValueError):
            parse_task("blocked: ship a demo")

    def test_empty_description(self):
        with self.assertRaises(ValueError):
            parse_task("done:   ")

    def test_non_string(self):
        with self.assertRaises(TypeError):
            parse_task(None)


if __name__ == "__main__":
    unittest.main()
