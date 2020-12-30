from unittest import TestCase
import io
from unittest.mock import patch
from yahtzee import roll_dice


class TestRollDice(TestCase):
    @patch('builtins.input', side_effect=['4'])
    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    def testRollOneOfEachNumberNoSwap(self, mock_input, mock_randint):
        hand = []
        actual = roll_dice(hand, 3)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    @patch('random.randint', side_effect=[6, 6, 6, 6, 6])
    def testRollFiveSixes(self, mock_input, mock_randint):
        hand = []
        actual = roll_dice(hand, 3)
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    @patch('random.randint', side_effect=[6, 6])
    def testRollTwoSixesWithThreeInHandAlready(self, mock_input, mock_randint):
        hand = [6, 6, 6]
        actual = roll_dice(hand, 3)
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3', '4'])
    @patch('random.randint', side_effect=[3, 2, 1, 4, 5, 6, 6, 6, 6, 6])
    def testReRollOnceAndGetSixYahtzee(self, mock_input, mock_randint):
        hand = []
        actual = roll_dice(hand, 3)
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3', '3', '4'])
    @patch('random.randint', side_effect=[3, 2, 1, 4, 5, 3, 2, 1, 4, 5, 6, 6, 6, 6, 6])
    def testReRollTwiceAndGetSixYahtzee(self, mock_input, mock_randint):
        hand = []
        actual = roll_dice(hand, 3)
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '1', '4'])
    @patch('random.randint', side_effect=[3, 2, 1, 4, 5, 6, 6, 6, 6])
    def addOneDiceToHandAndReRollGetOneThreeAndRestSixes(self, mock_input, mock_randint):
        hand = []
        actual = roll_dice(hand, 3)
        expected = [3, 6, 6, 6, 6]
        self.assertEqual(expected, actual)
