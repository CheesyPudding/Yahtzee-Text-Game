from unittest import TestCase
import io
from unittest.mock import patch
from yahtzee import print_scorecard


class TestPrintScorecard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_score(self, mock_output):
        empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                      'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                      'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        print_scorecard("1", empty_card)
        printed_actual = mock_output.getvalue()
        expected = "|***YAHTZEE PLAYER 1***|\n"\
                   "|**   UPPER SECTION  **|\n"\
                   "|ONES                ()|\n"\
                   "|TWOS                ()|\n"\
                   "|THREES              ()|\n"\
                   "|FOURS               ()|\n"\
                   "|FIVES               ()|\n"\
                   "|SIXES               ()|\n"\
                   "|*>62 BONUS          (0)|\n"\
                   "|**   LOWER SECTION  **|\n"\
                   "|3 OF A KIND         ()|\n"\
                   "|4 OF A KIND         ()|\n" \
                   "|FULL HOUSE          ()|\n" \
                   "|SMALL STRAIGHT      ()|\n"\
                   "|LARGE STRAIGHT      ()|\n"\
                   "|YAHTZEE             ()|\n"\
                   "|CHANCE              ()|\n"\
                   "|*YAHTZEE BONUS      (0)|\n"\
                   "|*UPPER TOTAL        (0)|\n"\
                   "|*LOWER TOTAL        (0)|\n"\
                   "|*TOTAL              (0)|\n\n"
        self.assertEqual(expected, printed_actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_partially_filled_score(self, mock_output):
        card = {1: 1, 2: 2, 3: 3, 4: -1, 5: 5, 6: 6, 'upper_bonus': 0, 'three-of-a-kind': -1,
                'four-of-a-kind': -1, 'full-house': 25, 'small straight': 30, 'large straight': -1, 'yahtzee': -1,
                'chance': -1, 'lower_bonus': 0, 'u_total': 18, 'l_total': 55, 'total': 73}
        print_scorecard("1", card)
        printed_actual = mock_output.getvalue()
        expected = "|***YAHTZEE PLAYER 1***|\n" \
                   "|**   UPPER SECTION  **|\n" \
                   "|ONES                (1)|\n" \
                   "|TWOS                (2)|\n" \
                   "|THREES              (3)|\n" \
                   "|FOURS               ()|\n" \
                   "|FIVES               (5)|\n" \
                   "|SIXES               (6)|\n" \
                   "|*>62 BONUS          (0)|\n" \
                   "|**   LOWER SECTION  **|\n" \
                   "|3 OF A KIND         ()|\n" \
                   "|4 OF A KIND         ()|\n" \
                   "|FULL HOUSE          (25)|\n" \
                   "|SMALL STRAIGHT      (30)|\n" \
                   "|LARGE STRAIGHT      ()|\n" \
                   "|YAHTZEE             ()|\n" \
                   "|CHANCE              ()|\n" \
                   "|*YAHTZEE BONUS      (0)|\n" \
                   "|*UPPER TOTAL        (18)|\n" \
                   "|*LOWER TOTAL        (55)|\n" \
                   "|*TOTAL              (73)|\n\n"
        self.assertEqual(expected, printed_actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_filled_score(self, mock_output):
        card = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 'upper_bonus': 63, 'three-of-a-kind': 20,
                'four-of-a-kind': 25, 'full-house': 25, 'small straight': 30, 'large straight': 40, 'yahtzee': 50,
                'chance': 35, 'lower_bonus': 100, 'u_total': 18, 'l_total': 55, 'total': 73}
        print_scorecard("1", card)
        printed_actual = mock_output.getvalue()
        expected = "|***YAHTZEE PLAYER 1***|\n" \
                   "|**   UPPER SECTION  **|\n" \
                   "|ONES                (1)|\n" \
                   "|TWOS                (2)|\n" \
                   "|THREES              (3)|\n" \
                   "|FOURS               (4)|\n" \
                   "|FIVES               (5)|\n" \
                   "|SIXES               (6)|\n" \
                   "|*>62 BONUS          (63)|\n" \
                   "|**   LOWER SECTION  **|\n" \
                   "|3 OF A KIND         (20)|\n" \
                   "|4 OF A KIND         (25)|\n" \
                   "|FULL HOUSE          (25)|\n" \
                   "|SMALL STRAIGHT      (30)|\n" \
                   "|LARGE STRAIGHT      (40)|\n" \
                   "|YAHTZEE             (50)|\n" \
                   "|CHANCE              (35)|\n" \
                   "|*YAHTZEE BONUS      (100)|\n" \
                   "|*UPPER TOTAL        (18)|\n" \
                   "|*LOWER TOTAL        (55)|\n" \
                   "|*TOTAL              (73)|\n\n"
        self.assertEqual(expected, printed_actual)
