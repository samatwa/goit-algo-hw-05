import timeit
from bm import boyer_moore
from kmp import kmp
from rk import rabin_karp
from load import load_articles

def main():
    load_articles()
    with open('article1.txt', 'r', encoding='utf-8') as file:
        text = file.read()

        pattern1 = "пошук"  # подстрока, которую нужно найти
        pattern2 = "делегація"   # вигаданий підрядок

        # Вимірюємо час для реального підрядка у article1.txt
        time_real_1_1 = timeit.timeit(lambda: boyer_moore(text, pattern1), number=1000)
        time_real_1_2 = timeit.timeit(lambda: kmp(text, pattern1), number=1000)
        time_real_1_3 = timeit.timeit(lambda: rabin_karp(text, pattern1), number=1000)

        # Вимірюємо час для вигаданого підрядка у article1.txt
        time_fake_1_1 = timeit.timeit(lambda: boyer_moore(text, pattern2), number=1000)
        time_fake_1_2 = timeit.timeit(lambda: kmp(text, pattern2), number=1000)
        time_fake_1_3 = timeit.timeit(lambda: rabin_karp(text, pattern2), number=1000)

        print('Test 1: article1.txt')
        print("Real time Boyer-Moore:", time_real_1_1)
        print("Fake time Boyer-Moore:", time_fake_1_1)
        print()
        print("Real time KMP:", time_real_1_2)
        print("Fake time KMP:", time_fake_1_2)
        print()
        print("Real time Rabin-Karp:", time_real_1_3)
        print("Fake time Rabin-Karp:", time_fake_1_3)

    with open('article2.txt', 'r', encoding='utf-8') as file:
        text = file.read()

        pattern1 = "структура"  # подстрока, которую нужно найти
        pattern2 = "делегація"   # вигаданий підрядок

        # Вимірюємо час для реального підрядка у article2.txt
        time_real_2_1 = timeit.timeit(lambda: boyer_moore(text, pattern1), number=1000)
        time_real_2_2 = timeit.timeit(lambda: kmp(text, pattern1), number=1000)
        time_real_2_3 = timeit.timeit(lambda: rabin_karp(text, pattern1), number=1000)

        # Вимірюємо час для вигаданого підрядка у article2.txt
        time_fake_2_1 = timeit.timeit(lambda: boyer_moore(text, pattern2), number=1000)
        time_fake_2_2 = timeit.timeit(lambda: kmp(text, pattern2), number=1000)
        time_fake_2_3 = timeit.timeit(lambda: rabin_karp(text, pattern2), number=1000)

        print()
        print('Test 2: article2.txt')
        print("Real time Boyer-Moore:", time_real_2_1)
        print("Fake time Boyer-Moore:", time_fake_2_1)
        print()
        print("Real time KMP:", time_real_2_2)
        print("Fake time KMP:", time_fake_2_2)
        print()
        print("Real time Rabin-Karp:", time_real_2_3)
        print("Fake time Rabin-Karp:", time_fake_2_3)

if __name__ == "__main__":
    main()