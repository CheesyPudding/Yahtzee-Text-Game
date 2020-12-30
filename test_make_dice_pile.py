from unittest import TestCase
from unittest.mock import patch
from yahtzee import make_dice_pile


class TestMakeDicePile(TestCase):
    @patch('random.randint', side_effect=[1, 1, 1, 1, 1])
    def testRollAllOnesPile(self, mock_randint):
        rolled_dice = 5
        actual = make_dice_pile(rolled_dice)
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 2, 3])
    def testRollOneTwoThree(self, mock_randint):
        rolled_dice = 3
        actual = make_dice_pile(rolled_dice)
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def testRollOneDiceOnlyOne(self, mock_randint):
        rolled_dice = 1
        actual = make_dice_pile(rolled_dice)
        expected = [1]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 2, 1, 4])
    def testRollStraight(self, mock_randint):
        rolled_dice = 4
        actual = make_dice_pile(rolled_dice)
        expected = [3, 2, 1, 4]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 2, 3, 4, 2])
    def testRollFiveRandomDice(self, mock_randint):
        rolled_dice = 5
        actual = make_dice_pile(rolled_dice)
        expected = [1, 2, 3, 4, 2]
        self.assertEqual(expected, actual)
