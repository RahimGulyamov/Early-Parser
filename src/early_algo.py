from src.grammar import Grammar, Rule


class EarlyAlgo:
    def __init__(self, grammar: Grammar):
        self._levels = []
        self._grammar = grammar

    class _State:
        rule: Rule
        rule_pos = int()
        str_pos = int()

        def __init__(self, rule: Rule, rule_pos: int, str_pos: int):
            self.rule = rule
            self.rule_pos = rule_pos
            self.str_pos = str_pos

        def __eq__(self, other):
            return self.rule == other.rule and self.rule_pos == other.rule_pos and self.str_pos == other.str_pos

        def __hash__(self):
            p = 13
            hash_ = self.str_pos
            hash_ += (self.rule_pos * (p ** 2)) % 567892342117
            k = 1
            for c in self.rule.str:
                hash_ += ord(c) * (p ** (2 + k))
                k += 1
            return hash_

    def _scan(self, it: _State, level_id: int, letter: str) -> bool:
        if len(it.rule.str) > it.rule_pos and it.rule.str[it.rule_pos] == letter:
            state_previous_size = len(self._levels[level_id + 1])
            self._levels[level_id + 1].add(self._State(it.rule, it.rule_pos + 1, it.str_pos))
            return len(self._levels[level_id + 1]) != state_previous_size
        return False

    def _predict(self, _it: _State, level_id: int) -> bool:
        if _it.rule_pos < len(_it.rule.str):
            if self._grammar.is_non_terminal(_it.rule.str[_it.rule_pos]):
                non_term = _it.rule.str[_it.rule_pos]
                new_states = [self._State(it, 3, level_id) for it in self._grammar.rules if it.str[0] == non_term]
                rules_in_situation = len(self._levels[level_id])
                for state in new_states:
                    self._levels[level_id].add(state)
                return len(self._levels[level_id]) != rules_in_situation
        return False

    def _complete(self, it: _State, level_id: int) -> bool:
        if it.rule_pos == len(it.rule.str):
            non_terminal = it.rule.str[0]
            lvl = it.str_pos
            new_states = []
            for prev_it in self._levels[lvl]:
                if prev_it.rule_pos < len(prev_it.rule.str) and prev_it.rule.str[prev_it.rule_pos] == non_terminal:
                    new_states.append(self._State(prev_it.rule, prev_it.rule_pos + 1, prev_it.str_pos))
            prev_sz = len(self._levels[level_id])
            for new_state in new_states:
                self._levels[level_id].add(new_state)
            return len(self._levels[level_id]) != prev_sz
        return False

    def scan(self, _id: int, letter: str):
        changed = False
        for it in self._levels[_id]:
            changed |= self._scan(it, _id, letter[_id])
        return changed

    def predict(self, _id: int) -> bool:
        changed = False
        its = [i for i in self._levels[_id]]
        for it in its:
            changed |= self._predict(it, _id)
        return changed

    def complete(self, _id: int) -> bool:
        changed = False
        its = [i for i in self._levels[_id]]
        for it in its:
            changed |= self._complete(it, _id)
        return changed

    def has_word(self, word: str) -> bool:
        self.init_levels(word)
        changed = True
        while changed:
            changed = self.complete(0)
            changed |= self.predict(0)
        for _id in range(len(word)):
            self.scan(_id, word)
            changed = True
            while changed:
                changed = self.complete(_id + 1)
                changed |= self.predict(_id + 1)
        result = self._State(Rule('#->S'), 4, 0)
        for state in self._levels[len(word)]:
            if state == result:
                return True
        return False

    def start_rule(self):
        start_rule = '#->S'
        self._levels[0].add(self._State(Rule(start_rule), 3, 0))

    def init_levels(self, word: str):
        self._levels = [set() for _ in range(len(word) + 1)]
        self.start_rule()


# filen = "test_src/test_0.txt"
# words = list()
# grammar = Grammar(filen, words)
#
# print(words)
# grammar.print_grammar()
#
# early_algo = EarlyAlgo(grammar)
# for i in range(1, int(words[0]) + 1):
#     print(early_algo.has_word(words[i]))
