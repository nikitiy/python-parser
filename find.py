import requests
from bs4 import BeautifulSoup as bs4


def counter_word(url, counter, letter, animals):
    last_operation = False
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    session = requests.Session()
    try:
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            soup = bs4(req.content, 'html.parser')
            # Подсчёт div'ов, если кол-во больше 1, значит на странице больше одной буквы
            if len(soup.find_all('div', attrs={'class': 'mw-category-group'})) > 1:
                # Выделяем все div'ы по классу mw-category-group
                divs = soup.find_all('div', attrs={'class': 'mw-category-group'})
                for div in divs:
                    # У каждого div'a находим ul'ы
                    uls = div.find_all('ul')
                    for ul in uls:
                        # Находим у каждого ul элементы li
                        lis = ul.find_all('li')
                        for li in lis:
                            # Увеличиваем счётчик и добавляем элемент к массиву животных
                            counter[letter] += 1
                            animals[letter].append(li.text)

                    # Смена буквы
                    letter += 1
                # Удаление лишнего смещения массива
                letter -= 1
            # Случай когда одна буква на странице
            else:
                div = soup.find('div', attrs={'class': 'mw-category-group'})
                lis = div.find_all('li')
                for li in lis:
                    counter[letter] += 1
                    animals[letter].append(li.text)

            # Поиск кнопки "Следующая страница" и взятие ссылки с неё
            div = soup.find('div', attrs={'class': 'mw-content-ltr'})
            a = div.find_all('a')
            for i in a:
                if i.text == "Следующая страница":
                    url = 'https://ru.wikipedia.org' + i['href']
                    break
            else:
                last_operation = True

        else:
            print('Ошибка')
    except Exception:
        print('Ошибка в URL адресе')

    print(counter)
    if last_operation:
        return counter
    # Вызываем рекурсию, пока не будет выполнено last_operation
    return counter_word(url, counter, letter, animals)
