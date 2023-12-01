from test_src.test_results import result
from src.early_algo import EarlyAlgo
from src.grammar import Grammar
from unittest import TestCase


class AlgoTests(TestCase):

    def get_early(self, number, words_to_check):
        filename = 'test_src/test_' + str(number) + '.txt'
        return EarlyAlgo(Grammar(filename, words_to_check))

    def pre_t_num(self, number: int):
        words_to_check = list()
        early = self.get_early(number, words_to_check)
        for i in range(int(words_to_check[0])):
            self.assertEqual(result[number][i], early.has_word(words_to_check[i + 1]))

    def test(self):
        for j in range(10):
            self.pre_t_num(j)

