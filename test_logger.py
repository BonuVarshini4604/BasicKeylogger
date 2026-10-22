
import tempfile
import unittest
from pathlib import Path

from logger_utils import (
    validate_sample,
    format_record,
    append_record,
    read_log,
    delete_log,
)


class TestInputValidation(unittest.TestCase):

    def test_valid_text(self):
        self.assertTrue(validate_sample("Hello Cybersecurity"))

    def test_empty_text(self):
        self.assertFalse(validate_sample(""))

    def test_whitespace_only(self):
        self.assertFalse(validate_sample("   \n\t"))

    def test_non_string_input(self):
        self.assertFalse(validate_sample(None))

    def test_empty_record_raises_error(self):
        with self.assertRaises(ValueError):
            format_record("   ")


class TestLogHandling(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_path = Path(self.temp_dir.name) / "test_log.txt"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_append_and_read_record(self):
        append_record(
            self.log_path,
            "Sample message",
            timestamp="2026-01-01 10:00:00",
        )

        content = read_log(self.log_path)
        self.assertIn("Sample message", content)
        self.assertIn("2026-01-01 10:00:00", content)

    def test_multiple_records(self):
        append_record(self.log_path, "First message")
        append_record(self.log_path, "Second message")

        content = read_log(self.log_path)
        self.assertIn("First message", content)
        self.assertIn("Second message", content)

    def test_missing_log_returns_empty_text(self):
        self.assertEqual(read_log(self.log_path), "")

    def test_delete_log(self):
        append_record(self.log_path, "Temporary test")
        delete_log(self.log_path)

        self.assertFalse(self.log_path.exists())
        self.assertEqual(read_log(self.log_path), "")

    def test_delete_missing_log(self):
        delete_log(self.log_path)
        self.assertFalse(self.log_path.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
