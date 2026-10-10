import unittest

from task_state import format_task, parse_task


class FormatTaskTests(unittest.TestCase):
    def test_valid_and_normalized(self):
        self.assertEqual(format_task(" Doing ", " ship a demo "), "doing: ship a demo")

    def test_round_trip(self):
        record = format_task("TODO", "ship a demo")
        self.assertEqual(parse_task(record), ("todo", "ship a demo"))

    def test_colon_in_description(self):
        record = format_task("todo", "check A: B")
        self.assertEqual(record, "todo: check A: B")
        self.assertEqual(parse_task(record), ("todo", "check A: B"))

    def test_unknown_state(self):
        with self.assertRaises(ValueError):
            format_task("blocked", "ship a demo")

    def test_empty_description(self):
        with self.assertRaises(ValueError):
            format_task("done", "   ")

    def test_non_string_state(self):
        with self.assertRaises(TypeError):
            format_task(None, "ship a demo")

    def test_non_string_description(self):
        with self.assertRaises(TypeError):
            format_task("todo", None)


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
