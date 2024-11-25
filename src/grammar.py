ALLOWED_TERMINALS = set("abcdefghijklmnopqrstuvwxyz0123456789()[]{}+-*/=")
ALLOWED_NON_TERMINALS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class CustomError(Exception):
    pass


class Rule:
    _left_part = str()
    _right_part = str()

    def __init__(self, pre_rule: str):
        try:
            self._left_part, self._right_part = pre_rule.split('->', 1)
            self._left_part = self._left_part.strip()
            self._right_part = self._right_part.strip()
        except ValueError as e:
            print(f"Ошибка при разделении строки: {e}")
            raise
        except Exception as e:
            print(f"Другая ошибка: {e}")
            raise
        self.str = f"{self.left_part}->{self._right_part}"

    def __eq__(self, other):
        return self._right_part == other.right_part and self._left_part == other.left_part

    @property
    def left_part(self):
        return self._left_part

    @property
    def right_part(self):
        return self._right_part

    def print_rule(self):
        print(self.str)


class Grammar:
    def is_terminal(self, c: str) -> bool:
        return c in self._terminals

    def is_non_terminal(self, c: str) -> bool:
        return c in self._non_terms

    def is_valid_rule(self, rule: Rule) -> bool:
        valid = self.is_non_terminal(rule.left_part)
        for symbol in rule.right_part:
            valid &= (self.is_terminal(symbol) or self.is_non_terminal(symbol))

        return valid

    @property
    def rules(self):
        return self._rules

    def add_rule(self, rule: str) -> bool:
        rule_c = Rule(rule)
        if self.is_valid_rule(rule_c):
            self._rules.append(rule_c)
            return True
        return False

    def __init__(self, filename: str, list_of_words: list):
        self._non_terms_amount = int()
        self._terminals_amount = int()
        self._rules_amount = int()

        self._non_terms = set()
        self._terminals = set()
        self._rules = list()
        self._start_non_term = str()

        file = open(filename, 'r')
        line = file.readline()

        if not line:
            raise CustomError("Неправильный формат входных данных: количество строк")

        amounts = line.split()

        for index, attr_name in enumerate(['non_terms_amount', 'terminals_amount', 'rules_amount']):
            try:
                value = int(amounts[index])
            except ValueError as ve:
                raise CustomError(f"Неправильный формат входных данных: {ve}")
            except Exception as e:
                raise CustomError(f"Произошла неожиданная ошибка: {e}")

            setattr(self, f"_{attr_name}", value)

        line = file.readline()
        if not line:
            raise CustomError("Неправильный формат входных данных: количество строк")

        for c in line.strip():
            if c not in ALLOWED_NON_TERMINALS:
                raise CustomError("Неправильное значение нетерминального символа")

            self._non_terms = set(line.strip())

        line = file.readline()
        if not line:
            raise CustomError("Неправильный формат входных данных: количество строк")

        for c in line.strip():
            if c not in ALLOWED_TERMINALS:
                raise CustomError("Неправильное значение терминального символа")

            self._terminals = set(line.strip())

        # self._rules = list()
        for i in range(self._rules_amount):
            line = file.readline()
            if not self.add_rule(line):
                raise CustomError("Неправильный формат правила")

        line = file.readline()
        if not line:
            raise CustomError("Неправильный формат входных данных: количество строк")

        line = line.strip()
        if line not in self._non_terms:
            raise CustomError("Неправильный формат входных данных: стартовый символ")
        self._start_non_term = line

        self._rules.sort(key=self.custom_compare)

        lines = file.readlines()
        is_last_void = False
        for line in lines:
            is_last_void = line.endswith('\n')
            list_of_words.append(line.strip('\n'))
        if is_last_void:
            list_of_words.append('')

        if len(self._non_terms) != self._non_terms_amount:
            raise CustomError(
                f"Неправильное количество нетерминалов {len(self._non_terms)} != {self._non_terms_amount}")

        if len(self._terminals) != self._terminals_amount:
            raise CustomError(f"Неправильное количество терминалов {len(self._terminals)} != {self._terminals_amount}")

        if len(self.rules) != self._rules_amount:
            raise CustomError(f"Неправильное количество правил {len(self.rules)} != {self._rules_amount}")

        if len(list_of_words) != int(list_of_words[0]) + 1:
            raise CustomError(f"Неправильное количество слов {len(list_of_words)} != {int(list_of_words[0]) + 1}")

        file.close()

    def custom_compare(self, obj: Rule):
        if obj.left_part == self._start_non_term:
            return chr(0)
        return obj.left_part

    def print_grammar(self):
        print(f"Non-terminals amount: {self._non_terms_amount}")
        print(f"Terminals amount: {self._terminals_amount}")
        print(f"Rules amount: {self._rules_amount}")
        print(f"Non-terminals: {self._non_terms}")
        print(f"Terminals: {self._terminals}")
        print("Rules:")
        for rule in self._rules:
            rule.print_rule()
        print(f"Start non-terminal: {self._start_non_term}")


# filen = "test_src/test_1.txt"
# words = list()
# grammar = Grammar(filen, words)
#
# print(words)
# grammar.print_grammar()
