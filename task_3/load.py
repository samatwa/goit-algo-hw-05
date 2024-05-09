import requests

def load_articles():
    url_1 = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
    url_2 = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    article1_text = response_1.text
    article2_text = response_2.text

    # Записываем содержимое файлов в локальные файлы
    with open('article1.txt', 'w', encoding='utf-8') as file_1:
        file_1.write(article1_text)

    with open('article2.txt', 'w',  encoding='utf-8') as file_2:
        file_2.write(article2_text)