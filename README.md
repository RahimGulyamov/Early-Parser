# Early parser
___
## Описание:
Парсер работает по [Алгоритму Эрли](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%AD%D1%80%D0%BB%D0%B8)
**Алгоритм Эрли** позволяет определить, выводится ли данное слово **w** в данной контекстно-свободной грамматике **G**.

#### Вход для алгоритма: КС грамматика **G = ⟨N, Σ, P, S⟩** и слова w.
#### Выход: `true`, если **w** выводится в **G**; `false` — иначе.

### Формат входных данных для тестирования кода

1. Первая строка: три целых числа - ∣N∣, ∣Σ∣ и ∣P∣, обозначающие количество нетерминальных символов, терминальных символов и правил в грамматике соответственно (0 ≤ ∣N∣, ∣Σ∣, ∣P∣ ≤ 100).
2. Вторая строка: ∣N∣ нетерминальных символов, представленных заглавными латинскими буквами.
3. Третья строка: ∣Σ∣ символов алфавита, включая строчные латинские буквы, цифры, скобки и знаки арифметических операций.
4. Следующие ∣P∣ строк: каждая строка содержит одно правило грамматики в формате "левая_часть_правила -> правая_часть_правила", где ε обозначает отсутствие правой части.
5. Строка, следующая за правилами, содержит один нетерминальный символ - стартовый символ грамматики.
6. Следующая строка: одно целое число 𝑚 (1 ≤ 𝑚 ≤ 100000) - количество слов для проверки.
7. Последующие 𝑚 строк: каждая строка содержит одно слово, состоящее из символов алфавита грамматики. Суммарная длина всех слов не превышает 1000000.

### Формат выходных данных для тестирования кода

Выводится 𝑚 строк. Каждая строка содержит "Yes", если соответствующее слово из входных данных принадлежит языку, порождаемому грамматикой, и "No" в противном случае.


Тестирование осуществлялось c помощью модуля `Pytest`.

## Запуск программы:
Чтобы запустить программу достаточно ввести следующую команду в терминале:

```shell
python3 main.py
```
или 
```shell
python main.py
```

Для запуска тестов введите:
```shell
python3 tests.py
```

