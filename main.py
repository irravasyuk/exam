# 1. Напишіть програму, яка приймає два цілих числа від користувача
# і виводить суму діапазону чисел між ними.
# def sum_range():
#     while True:
#         try:
#             start = int(input("Введіть перше число: "))
#             break
#         except ValueError:
#             print('Будь ласка, введіть ціле число.')
#
#     while True:
#         try:
#             end = int(input("Введіть друге число: "))
#             break
#         except ValueError:
#             print('Будь ласка, введіть ціле число.')
#     if start > end:
#         start, end = end, start
#     total = sum(range(start, end + 1))
#     print(f"Сума чисел від {start} до {end} = {total}")
#
#
# sum_range()

# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.
# def sum_even_num():
#     total = 0
#     for i in range(1, 101):
#         if i % 2 == 0:
#             total += i
#
#     print(f'Сума всіх парних чисел в діапазоні від 1 до 100 = {total}')
#
# sum_even_num()

# 3. Напишіть програму, яка приймає рядок
# від користувача і виводить кожну літеру рядка на окремому рядку.
# def print_letter():
#     row = input('Введіть рядок: ')
#     for char in row:
#         print(char)
#
# print_letter()

# 4. Напишіть програму, яка створює список цілих чисел та виводить новий список,
# який містить лише парні числа з вихідного списку.
# def even_num():
#     while True:
#         try:
#             initial_list = input('Введіть список цілих чисел через пробіл: ').split()
#             original_list = [int(num) for num in initial_list]
#             break
#         except ValueError:
#             print('Будь ласка, введіть ціле число.')
#
#     even_list = []
#     for num in original_list:
#         if num % 2 == 0:
#             even_list.append(num)
#
#     print(f'Список парних чисел: {even_list}')
#
# even_num()

# 5. Напишіть функцію, яка приймає список рядків від користувача і повертає новий
# список, що містить лише рядки, що починаються з великої літери.
# def capital_letter(strings):
#     capital_strings = [s for s in strings if s and s[0].isupper()]
#     return capital_strings
#
# row = input('Введіть список рядків через кому: ').split(", ")
# result = capital_letter(row)
#
# print(f'Рядки, що починаються з великої літери: {result}')

# 6. Напишіть функцію, яка приймає список рядків від користувача і повертає
# новий список, що містить лише рядки, які містять слово "Python".
# def filter_by_python(strings):
#     python_strings = [s for s in strings if "Python" in s]
#     return python_strings
#
# row_list = input("Введіть список рядків через кому: ").split(", ")
# result = filter_by_python(row_list)
# print(f"Рядки, які містять слово 'Python': {result}")


# 7. (додаткове на кристалики) Напишіть програму, яка створює словник, де ключами є слова, а значеннями їхні визначення.
# Дозвольте користувачу додавати, видаляти та шукати слова у цьому словнику.
# def dictionary():
#     dictionary = {}
#
#     while True:
#         print('1. Додати слово')
#         print('2. Видалити слово')
#         print('3. Знайти слово')
#         print('4. Вийти')
#
#         choice = int(input('Введіть свій вибір: '))
#
#         if choice == 1:
#             word = input("Введіть слово: ")
#             definition = input("Введіть визначення: ")
#             dictionary[word] = definition
#             print(f"Слово: {word} додано до словника.")
#
#         elif choice == 2:
#             word = input('Введіть слово для видалення: ')
#             if word in dictionary:
#                 del dictionary[word]
#                 print(f"Слово: {word} видалено. ")
#             else:
#                 print("Такого слова немає в словнику.")
#
#         elif choice == 3:
#             word = input("Введіть слово для пошуку: ")
#             if word in dictionary:
#                 print(f"{word} - {dictionary[word]}")
#             else:
#                 print("Такого слова немає в словнику.")
#
#         elif choice == 4:
#             break
#
#         else:
#             print("Невірний вибір, спробуйтк ще раз.")
#
# dictionary()


# 8. (додаткове на кристалики) Використовуючи лямбда- функцію, напишіть вираз, який сортує
# список кортежів за другим елементом кожного кортежу (наприклад, [(1, 3), (3, 2), (2, 1)]).
# list = [(1, 3), (3, 2), (2, 1)]
# sorted_list = sorted(list, key=lambda x: x[1])
# print(f"Відсортований список: {sorted_list}")

# 2 частина
from datetime import datetime


class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date_publication = datetime.now()

    def display(self):
        print(f"Заголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self.date_publication.strftime('%Y-%m-%d %H:%M:%S')}")
        print()


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        page = WebPage(title, content)
        self.pages.append(page)
        print(f"Сторінка '{title}' додана до сайту '{self.name}'")

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print(f"Сторінку '{title}' видалено з сайту '{self.name}'")
                return
        print(f"Сторінку з таким заголовком '{title}' не знайдено.")

    def display(self):
        print(f'Назва сайту: {self.name}')
        print(f'URL: {self.url}')
        print("Сторінки:")
        if not self.pages:
            print('Немає сторінок.')
        for page in self.pages:
            page.display()
        print()

    def search_pages(self, keyword):
        found_pages = []
        for page in self.pages:
            if keyword.lower() in page.title.lower() or keyword.lower() in page.content.lower():
                found_pages.append(page)
        return found_pages


def main():
    websites = {}

    while True:
        print("1. Створити новий сайт")
        print("2. Додати сторінку до сайту")
        print("3. Видалити сторінку з сайту")
        print("4. Відобразити інформацію про сайт")
        print("5. Пошук слів за ключем.")
        print("6. Вийти")

        choice = input("Введіть ваш вибір: ")

        if choice == '1':
            name = input("Введіть назву сайту: ")
            url = input("Введіть URL сайту: ")
            if name in websites:
                print(f"Сайт з назвою '{name}' вже існує.")
            else:
                websites[name] = WebSite(name, url)
                print(f"Сайт '{name}' створено.")

        elif choice == '2':
            name = input("Введіть назву сайту: ")
            if name not in websites:
                print(f"Сайт з назвою '{name}' не знайдено.")
            else:
                title = input("Введіть заголовок сторінки: ")
                content = input("Введіть вміст сторінки: ")
                websites[name].add_page(title, content)

        elif choice == '3':
            name = input("Введіть назву сайту: ")
            if name not in websites:
                print(f"Сайт з назвою '{name}' не знайдено.")
            else:
                title = input("Введіть заголовок сторінки для видалення: ")
                websites[name].remove_page(title)

        elif choice == '4':
            name = input("Введіть назву сайту: ")
            if name not in websites:
                print(f"Сайт з назвою '{name}' не знайдено.")
            else:
                websites[name].display()
        elif choice == '5':
            name = input("Введіть назву сайту: ")
            if name not in websites:
                print(f"Сайт з назвою '{name}' не знайдено.")
            else:
                keyword = input("Введіть ключове слово для пошуку: ")
                found_pages = websites[name].search_pages(keyword)
                if found_pages:
                    print(f"Сторінки, знайдені за ключовим словом {keyword}: ")
                    for page in found_pages:
                        page.display()
                else:
                    print("На сайті немає сторінок за цим ключовим словом.")

        elif choice == '6':
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
