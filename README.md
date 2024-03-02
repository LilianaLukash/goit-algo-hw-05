# Результати тестування алгоритмів пошуку підрядків

Нижче представлені результати тестування трьох алгоритмів пошуку підрядків: Knuth-Morris-Pratt, Boyer-Moore та Rabin-Karp. Тестування проводилося на двох текстах (`text1` та `text2`) з двома типами підрядків: існуючий у тексті (`existing_substring`) та вигаданий (`made_up_substring`). Час виконання вимірювався в секундах.

## Таблиця результатів

| Algorithm            | Substring Type       | Text ID | Time (s) |
|----------------------|----------------------|---------|----------|
| Knuth-Morris-Pratt   | existing_substring   | text1   | 0.562135 |
| Knuth-Morris-Pratt   | existing_substring   | text2   | 0.393228 |
| Knuth-Morris-Pratt   | made_up_substring    | text1   | 0.534955 |
| Knuth-Morris-Pratt   | made_up_substring    | text2   | 1.172546 |
| Boyer-Moore          | existing_substring   | text1   | 0.249849 |
| Boyer-Moore          | existing_substring   | text2   | 0.159900 |
| Boyer-Moore          | made_up_substring    | text1   | 0.224831 |
| Boyer-Moore          | made_up_substring    | text2   | 0.588106 |
| Rabin-Karp           | existing_substring   | text1   | 1.674359 |
| Rabin-Karp           | existing_substring   | text2   | 1.281236 |
| Rabin-Karp           | made_up_substring    | text1   | 1.673059 |
| Rabin-Karp           | made_up_substring    | text2   | 3.694528 |

## Висновки

- **Boyer-Moore** алгоритм показав найкращі результати за часом виконання серед усіх трьох алгоритмів як для існуючих, так і для вигаданих підрядків у обох текстах.
- **Knuth-Morris-Pratt** алгоритм виявився середнім за швидкістю, показуючи стабільні результати незалежно від наявності підрядка в тексті.
- **Rabin-Karp** продемонстрував найповільніші результати, особливо при пошуку вигаданих підрядків, що може бути пов'язано з високими витратами на обчислення хеш-функцій для великих текстів.

Ці результати допоможуть визначити оптимальний алгоритм для застосування в різних сценаріях пошуку підрядків, залежно від розміру тексту та частоти входжень шуканих підрядків.
