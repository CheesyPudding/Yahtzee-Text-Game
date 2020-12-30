from unittest import TestCase
import io
from unittest.mock import patch
from yahtzee import round_end


class TestRoundEnd(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_one_wins_by_one_point(self, mock_output):
        card_win = {'ones': 1, 'twos': 4, 'threes': 9, 'fours': 12, 'fives': 15, 'sixes': 30,
                    'upperBonus': 35, 'x3': 17, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                    'yahtzee': 50, 'chance': 18, 'lowerBonus': 100, 'uTotal': 71, 'lTotal': 300, 'total': 371}
        card_lose = {'ones': 0, 'twos': 4, 'threes': 9, 'fours': 12, 'fives': 15, 'sixes': 30,
                     'upperBonus': 35, 'x3': 17, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                     'yahtzee': 50, 'chance': 18, 'lowerBonus': 100, 'uTotal': 70, 'lTotal': 300, 'total': 370}
        round_end(card_win, card_lose)
        printed_actual = mock_output.getvalue()
        expected = "Player 1 wins!"
        self.assertEqual(expected, printed_actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_two_wins(self, mock_output):
        card_lose = {'ones': 1, 'twos': 2, 'threes': 3, 'fours': 4, 'fives': 5, 'sixes': 6,
                     'upperBonus': 0, 'x3': 15, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                     'yahtzee': 50, 'chance': 9, 'lowerBonus': 0, 'uTotal': 21, 'lTotal': 189, 'total': 210}
        card_win = {'ones': 0, 'twos': 4, 'threes': 9, 'fours': 12, 'fives': 15, 'sixes': 30,
                    'upperBonus': 35, 'x3': 17, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                    'yahtzee': 50, 'chance': 18, 'lowerBonus': 100, 'uTotal': 70, 'lTotal': 300, 'total': 370}
        round_end(card_lose, card_win)
        printed_actual = mock_output.getvalue()
        expected = "Player 2 wins!"
        self.assertEqual(expected, printed_actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_tie(self, mock_output):
        card_one = {'ones': 1, 'twos': 2, 'threes': 3, 'fours': 4, 'fives': 5, 'sixes': 6,
                    'upperBonus': 0, 'x3': 15, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                    'yahtzee': 50, 'chance': 9, 'lowerBonus': 0, 'uTotal': 21, 'lTotal': 189, 'total': 210}
        card_two = {'ones': 1, 'twos': 2, 'threes': 3, 'fours': 4, 'fives': 5, 'sixes': 6,
                    'upperBonus': 0, 'x3': 15, 'x4': 20, 'fHouse': 25, 'sStraight': 30, 'lStraight': 40,
                    'yahtzee': 50, 'chance': 9, 'lowerBonus': 0, 'uTotal': 21, 'lTotal': 189, 'total': 210}
        round_end(card_one, card_two)
        printed_actual = mock_output.getvalue()
        expected = "Player 1 and player 2 tied!"
        self.assertEqual(expected, printed_actual)
