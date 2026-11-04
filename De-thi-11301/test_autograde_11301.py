"""Unit tests for the local grader of Python exam code 11301."""

import shutil
import tempfile
import unittest
from pathlib import Path

from autograde_11301 import (
    check_c1a, check_c1b, check_c1c,
    check_c2a, check_c2b, check_c2c,
    check_c3a, check_c3b, check_c3c,
    check_c4a, check_c4b, check_c5a, check_c5b,
    find_submission_dir,
)


class TestExam11301Grader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = find_submission_dir()
        if cls.folder is None:
            raise RuntimeError("Không tìm thấy thư mục chứa Cau1.py đến Cau5.py")

    def test_submission_directory_is_found(self):
        self.assertTrue(self.folder.is_dir())
        for number in range(1, 6):
            self.assertTrue((self.folder / f"Cau{number}.py").is_file())

    def test_all_rubric_checks_pass_for_reference_solution(self):
        checks = [
            check_c1a, check_c1b, check_c1c,
            check_c2a, check_c2b, check_c2c,
            check_c3a, check_c3b, check_c3c,
            check_c4a, check_c4b, check_c5a, check_c5b,
        ]
        results = [check(self.folder) for check in checks]
        failed = [f"{item.label}: {item.detail}" for item in results if not item.passed]
        self.assertEqual([], failed)
        self.assertAlmostEqual(10.0, sum(item.max_score for item in results))

    def test_wrong_answer_is_marked_as_fail(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            copied = Path(temp_dir) / "HOTEN_TEST"
            shutil.copytree(self.folder, copied)
            cau2 = copied / "Cau2.py"
            source = cau2.read_text(encoding="utf-8")
            source = source.replace("dem += 1", "dem += 2", 1)
            cau2.write_text(source, encoding="utf-8")
            check = check_c2a(copied)
            self.assertFalse(check.passed)
            self.assertEqual(0.75, check.max_score)


if __name__ == "__main__":
    unittest.main(verbosity=2)
