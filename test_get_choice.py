from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_choice


class TestGetChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_select_ones_row_in_empty_scorecard(self, mock_input):
        empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                      'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        actual = get_choice(empty_card)
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_select_sixes_row_in_empty_scorecard(self, mock_input):
        empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                      'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        actual = get_choice(empty_card)
        expected = 6
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_select_full_house_in_empty_scorecard(self, mock_input):
        empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                      'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        actual = get_choice(empty_card)
        expected = "full-house"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['12'])
    def test_select_yahtzee_in_empty_scorecard(self, mock_input):
        empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                      'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        actual = get_choice(empty_card)
        expected = "yahtzee"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_chance_to_completely_fill_scorecard(self, mock_input):
        empty_card = {1: 1, 2: 2, 3: 3, 4: 0, 5: 0, 6: 0, 'upper_bonus': 0, 'three-of-a-kind': 0,
                      'four-of-a-kind': 0, 'full-house': 0, 'small straight': 0, 'large straight': 0, 'yahtzee': 0,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        actual = get_choice(empty_card)
        expected = "chance"
        self.assertEqual(expected, actual)
