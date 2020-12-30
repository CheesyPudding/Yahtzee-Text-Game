from unittest import TestCase
import io
from unittest.mock import patch
from yahtzee import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_to_add_dice_to_hand(self, mock_input):
        actual = get_user_choice()
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_to_return_dice_from_hand_to_pile(self, mock_input):
        actual = get_user_choice()
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_choose_to_re_roll_pile(self, mock_input):
        actual = get_user_choice()
        expected = 2
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_choose_keep_hand(self, mock_input):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0', '4'])
    def test_clumsy_out_of_range_choose_keep_hand(self, mock_input):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5', '4'])
    def test_clumsy_out_of_range_max_choose_keep_hand(self, mock_input):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdas', "sad", "Add dice pile to hand (confirm hand)", '4'])
    def test_clumsy_strings_choose_keep_hand(self, mock_input):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)