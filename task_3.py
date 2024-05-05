import timeit
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    last = {}
    for k, c in enumerate(pattern):
        last[c] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1
    prime = 101  # просте число
    p = 0  # hash pattern
    t = 0  # hash text
    h = 1
    d = 256  # розмір алфавіту
    for i in range(m - 1):
        h = (h * d) % prime
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime
    return -1

text = "simsalabim"
pattern1 = "bim"  # підрядок, який існує
pattern2 = "god"   # вигаданий підрядок

# Вимірюємо час для реального підрядка
time_real_1 = timeit.timeit(lambda: boyer_moore(text, pattern1), number=10000)
time_real_2 = timeit.timeit(lambda: kmp(text, pattern1), number=10000)
time_real_3 = timeit.timeit(lambda: rabin_karp(text, pattern1), number=10000)

# Вимірюємо час для вигаданого підрядка
time_fake_1 = timeit.timeit(lambda: boyer_moore(text, pattern2), number=10000)
time_fake_2 = timeit.timeit(lambda: kmp(text, pattern2), number=10000)
time_fake_3 = timeit.timeit(lambda: rabin_karp(text, pattern2), number=10000)

print("Real time Boyer-Moore:", time_real_1)
print("Fake time Boyer-Moore:", time_fake_1)
print()
print("Real time KMP:", time_real_2)
print("Fake time KMP:", time_fake_2)
print()
print("Real time Rabin-Karp:", time_real_3)
print("Fake time Rabin-Karp:", time_fake_3)