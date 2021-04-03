from find import counter_word

alphabet = (
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
    'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z'
)

letter = 0
url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
counter = [0] * 55
animals = [[]] * 55

# Запуск счётчика
counter_word(url, counter, letter, animals)

# Вывод на экран колличество животных по каждой букве
for i in range(len(counter)):
    print(alphabet[i], ":", counter[i])

# Запись в файл всех животных по букве
# f = open('animals.txt', 'w')
# f.write(str(animals))
# f.close()

# Запись в файл кол-во животных по каждой букве
# f = open('counter.txt', 'w')
# for i in range(len(counter)):
#     f.write(str(alphabet[i]) + ": " + str(counter[i]) + '\n')
# f.close()
