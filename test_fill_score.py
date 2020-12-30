from unittest import TestCase
from unittest.mock import patch
from yahtzee import fill_score


class TestFillScore(TestCase):
    def testGetFiveSixesAndFillSixesRow(self):
        scorecard = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                     'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                     'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        score_row = 6
        hand = [6, 6, 6, 6, 6]
        actual = fill_score(scorecard, score_row, hand)
        expected = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: 30, 'upper_bonus': 0, 'three-of-a-kind': -1,
                    'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                    'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        self.assertEqual(expected, actual)

    def testGetZeroSixesAndFillSixesRow(self):
        scorecard = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                     'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                     'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        score_row = 6
        hand = [1, 2, 3, 4, 5]
        actual = fill_score(scorecard, score_row, hand)
        expected = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: 0, 'upper_bonus': 0, 'three-of-a-kind': -1,
                    'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                    'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        self.assertEqual(expected, actual)

    def testGetThreeOfAKindWithFourOnes(self):
        scorecard = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                     'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                     'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        score_row = "three-of-a-kind"
        hand = [1, 1, 1, 1, 5]
        actual = fill_score(scorecard, score_row, hand)
        expected = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': 9,
                    'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                    'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        self.assertEqual(expected, actual)

    def testGetFourOfAKindButOnlyThreeOnes(self):
        scorecard = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                     'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                     'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        score_row = "four-of-a-kind"
        hand = [1, 1, 1, 5, 5]
        actual = fill_score(scorecard, score_row, hand)
        expected = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                    'four-of-a-kind': 0, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                    'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        self.assertEqual(expected, actual)

    def testYahtzee(self):
        scorecard = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                     'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                     'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        score_row = "yahtzee"
        hand = [5, 5, 5, 5, 5]
        actual = fill_score(scorecard, score_row, hand)
        expected = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1,
                    'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': 50,
                    'chance': -1, 'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
        self.assertEqual(expected, actual)
