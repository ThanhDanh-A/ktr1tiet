"""Kiem tra logic cua bo cham: tranh tinh PASS sai khi thieu output."""

import unittest

from autograde_de1_v2 import matches_expected


class TestExpectedMatching(unittest.TestCase):
    def test_string_expected_must_match_whole_phrase(self):
        self.assertTrue(
            matches_expected(
                ["Nhap ten: Nhap tuoi: Xin chào An, bạn 20 tuổi."],
                "Xin chào An, bạn 20 tuổi.",
            )
        )
        self.assertFalse(matches_expected(["Xin chào Binh"], "Xin chào An"))

    def test_list_expected_requires_every_output_line(self):
        expected = ["apple", "cherry", "coc"]
        self.assertTrue(matches_expected(["apple", "cherry", "coc"], expected))
        self.assertFalse(matches_expected(["apple"], expected))
        self.assertFalse(matches_expected(["apple", "cherry"], expected))

    def test_repeated_expected_values_need_distinct_output_lines(self):
        self.assertFalse(matches_expected(["same"], ["same", "same"]))
        self.assertTrue(matches_expected(["same", "same"], ["same", "same"]))

    def test_dict_expected_is_parsed_and_compared(self):
        expected = {"a": 2, "b": 1}
        self.assertTrue(matches_expected(["{'a': 2, 'b': 1}"], expected))
        self.assertFalse(matches_expected(["{'a': 2, 'b': 2}"], expected))


if __name__ == "__main__":
    unittest.main(verbosity=2)
