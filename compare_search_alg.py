




import timeit


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1


def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


with open("article 1.txt", "r", encoding="utf-8") as ph:
 text1 = ph.read()
with open("article 2.txt", "r", encoding="utf-8") as h:
 text2 = h.read()

# Підрядки для пошуку
existing_substring = "triangulation model"  # Існує в 2му тексті
made_up_substring = "nonexistent"  # Не існує в текстах

# Функція для вимірювання часу виконання алгоритму пошуку
def measure_search_time(algorithm_function, text, substring):
    # Використовуємо лямбда-функцію для передачі аргументів безпосередньо
    test_code = lambda: algorithm_function(text, substring)
    # Вимірювання часу виконання
    times = timeit.repeat(setup="pass", stmt=test_code, repeat=3, number=100)
    return sum(times) / len(times)

# Функції пошуку, які ми використовуємо
search_functions = {
    "Knuth-Morris-Pratt": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search
}

# Вимірювання і виведення часу для кожного алгоритму та обох типів підрядків
results = {}
for name, function in search_functions.items():
    results[name] = {
        "existing_substring": {
            "text1": measure_search_time(function, text1, existing_substring),
            "text2": measure_search_time(function, text2, existing_substring)
        },
        "made_up_substring": {
            "text1": measure_search_time(function, text1, made_up_substring),
            "text2": measure_search_time(function, text2, made_up_substring)
        }
    }

#print(results)
#results = {'Knuth-Morris-Pratt': {'existing_substring': {'text1': 0.0014383667148649693, 'text2': 0.0010089000376562278}, 'made_up_substring': {'text1': 0.0014614999915162723, 'text2': 0.0015724333158383768}}, 'Boyer-Moore': {'existing_substring': {'text1': 0.0005979666796823343, 'text2': 0.0004485667838404576}, 'made_up_substring': {'text1': 0.0006249333576609691, 'text2': 0.0007611999753862619}}, 'Rabin-Karp': {'existing_substring': {'text1': 0.0028773666514704623, 'text2': 0.0021915666293352842}, 'made_up_substring': {'text1': 0.0049483999609947205, 'text2': 0.0046123000017056865}}}

# Виводимо заголовок таблиці
print(f"{'Algorithm':<20} | {'Substring Type':<20} | {'Text ID':<8} | {'Time (s)':<10}")
print("-" * 70)  # Виводимо розділову лінію

# Виводимо дані
for algo, data in results.items():
    for sub_type, texts in data.items():
        for text, time in texts.items():
            print(f"{algo:<20} | {sub_type:<20} | {text:<8} | {time:<10.6f}")