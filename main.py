from src.early_algo import EarlyAlgo
from src.grammar import Grammar

document = input('Please, enter filename (Example: test_src.txt):\t')


words_to_check = list()
early = EarlyAlgo(Grammar(document, words_to_check))

for i in range(1, int(words_to_check[0]) + 1):
    print('Yes' if early.predict(words_to_check[i]) else 'No')


