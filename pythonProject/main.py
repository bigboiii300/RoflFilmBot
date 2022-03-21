# Импорт браузера, для открытия ссылок
# https://docs.python.org/3/library/webbrowser.html
import webbrowser


# Функция для открытия ссылок
def open_link(link):
    # Используется для выделения ключевых слов красным.
    print("Хотите перейти по ссылке? Введите" +
          " \033[31m {}\033[0m".format("да / нет"))
    global open_link_str
    open_link_str = ""
    while open_link_str != 'да' and open_link_str != 'нет':
        # Приведение к нижнему регистру чтобы было проще проверять
        open_link_str = input().lower()
        # Проверка на открытие ссылки в браузере
        if open_link_str == 'да':
            # Открытие ссылки в браузере
            webbrowser.open(link)
        elif open_link_str == 'нет':
            print("Оставлю ссылку. Может вы захотите посмотреть это позже")
            print(link)
        else:
            print("Введена неверная команда! Повторите ввод")


# Функция для открытие подборки по жанра
def select_genre():
    global input_str, start
    input_str = ""
    print("\nВведите номер интересующего жанра: \n1. Детектив \n2."
          " Мультфильмы \n3. Фантастика \n4. Ужасы \n5. "
          "Комедии \n6. Триллеры \n7. Боевики \n8. Мелодрамы \n9."
          " Приключения \n10. Фэнтэзи \n11. Семейные \n"
          "12. Аниме \n13. Криминал \n14. Биография \n15. Вестерны")
    print("Для навигации введите" + " \033[31m {}\033[0m".format("меню"))
    print(
        "Если вы уже определились или не хотите продолжать общение введите" +
        " \033[31m {}\033[0m".format("выход"))
    while input_str != 'выход':
        # Приведение к нижнему регистру чтобы было проще проверять
        input_str = input().lower()
        # Серия проверок на номер жанра
        if input_str == '1':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--mystery/?b=top")
        elif input_str == '2':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--animation/?b=top")
        elif input_str == '3':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--sci-fi/?b=top")
        elif input_str == '4':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--horror/?b=top")
        elif input_str == '5':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--comedy/?b=top")
        elif input_str == '6':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--thriller/?b=top")
        elif input_str == '7':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--action/?b=top")
        elif input_str == '8':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--romance/?b=top")
        elif input_str == '9':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--adventure/?b=top")
        elif input_str == '10':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--fantasy/?b=top")
        elif input_str == '11':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--family/?b=top")
        elif input_str == '12':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--anime/?b=top")
        elif input_str == '13':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--crime/?b=top")
        elif input_str == '14':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--biography/?b=top")
        elif input_str == '15':
            open_link("https://www.kinopoisk.ru/lists/"
                      "movies/genre--western/?b=top")
        elif input_str == 'выход':
            start = False
            break
        elif input_str == 'меню':
            break
        else:
            print("Введен неверный номер. Повторите ввод!")
            continue

        print("Хотите посмотреть другие жанры? Введите" +
              " \033[31m {}\033[0m".format("да / нет"))
        input_str = input().lower()
        if input_str == 'да':
            print("\nВведите номер интересующего жанра: \n1. Детектив"
                  " \n2. Мультфильмы \n3. Фантастика \n4. Ужасы \n5. "
                  "Комедии \n6. Триллеры \n7. Боевики \n8. Мелодрамы"
                  " \n9. Приключения \n10. Фэнтэзи \n11. Семейные \n"
                  "12. Аниме \n13. Криминал \n14. Биография \n15."
                  " Вестерны")
            continue
        elif input_str == 'нет':
            break
        else:
            print("Введена неверная команда. Повторите ввод!")
            continue


print("Здравствуйте! Я - бот, который поможет с выбором фильмов")
input_str = ""
open_link_str = ""
start = False
# Запуск бота
while input_str != 'выход':
    print("Чтобы начать работу со мной введите" +
          " \033[31m {}\033[0m".format("старт"))
    print("Если вы уже определились или не хотите продолжать "
          "общение введите" + " \033[31m {}\033[0m".format("выход"))
    input_str = input().lower()
    if input_str == 'старт':
        start = True
        break


# Начало взаимодействия с пользователем
def greeting():
    print(
        "Если вы уже определились или не хотите продолжать"
        " общение введите" + " \033[31m {}\033[0m".format("выход"))
    global input_str, start
    while input_str != 'да' and input_str != 'нет':
        print("Вы часто смотрите фильмы или увлекаетесь кино?")
        # Приведение к нижнему регистру чтобы было проще проверять
        input_str = input().lower()
        if input_str == 'нет':
            print("Предлагаю посмотреть подборку лучших фильмов")
            open_link('https://www.kinopoisk.ru/lists/movies/top500/')
        elif input_str == 'да':
            print("Предлагаю ознакомиться с подборками, где"
                  " вы можете найти много интересного контента")
            open_link("https://www.kinopoisk.ru/lists/categories/movies/1/")
        elif input_str == 'выход':
            start = False
            break
        # Возвращение в меню бота
        elif input_str == 'меню':
            break
        else:
            print("Введена неверная команда! Повторите ввод")


# Просмотр релизов
def check_releases():
    global input_str
    while input_str != 'выход':
        print("Введите дату")
        print("Пример:\nГод:2022\nМесяц:03\nДень:12\n")
        date_list = []
        repeat = True
        while repeat:
            # Обработка исключений
            try:
                # Заполнение списка
                for i in range(3):
                    if i == 0:
                        date_list.append(input('Год: '))
                    if i == 1:
                        date_list.append(input('Месяц: '))
                    if i == 2:
                        date_list.append(input('День: '))
                # Приведение элементов листа к int
                date_list = [int(i) for i in date_list]
                # Проверка на корректность даты
                if 2023 > date_list[0] > 2009 and \
                        13 > date_list[1] > 0 and 32 > date_list[2] > 0:
                    repeat = False
                else:
                    # Очищение некоректных элементов
                    date_list.clear()
                    print("Неверно задана дата! Повторите ввод\n")
                    repeat = True
            except Exception:
                # Очищение некоректных элементов
                date_list.clear()
                print("Неверно задана дата! Повторите ввод\n")
                repeat = True

        # Создание ссылки
        open_link("https://www.kinopoisk.ru/comingsoon/digital/?year=" +
                  str(date_list[0]) + "&month=" +
                  str(date_list[1]) + "&day=" + str(date_list[2]))
        print("Хотите посмотреть другие даты? Введите" +
              " \033[31m {}\033[0m".format("да / нет"))
        input_str = input().lower()
        # Проверка на повторение ввода, если пользователь
        if input_str == 'да':
            continue
        elif input_str == 'нет':
            break


# Получение подбортки лучших фильмов за год, который вводит пользователь
def get_year_compilation():
    global input_str, year
    # Цикл, пока пользователь не введет слово выход
    while input_str != 'выход':
        print("Введите дату")
        repeat = True
        # Цикличное повторение пока пользователь не введет корректную дату
        while repeat:
            # Обработка исключений
            try:
                year = int(input("Введите год: "))
                # Проверка на корректность
                if 2023 > year > 1920:
                    repeat = False
                else:
                    print("Неверно задана дата! Повторите ввод\n")
                    repeat = True
            except Exception:
                print("Неверно задана дата! Повторите ввод\n")
                repeat = True
        # Открытие ссылки
        open_link("https://www.kinopoisk.ru/lists/movies/year--" +
                  str(year) + "/?b=top")
        print("Хотите посмотреть другие даты? Введите" +
              " \033[31m {}\033[0m".format("да / нет"))
        input_str = input().lower()
        # Повтор ввода даты в случае, если пользователь хочет
        # посмотреть другие даты
        if input_str == 'да':
            continue
        elif input_str == 'нет':
            break


# Создание анкеты пользователя на основе введенных ответов
def make_profile():
    print("Сколько примерно фильмов вы просмотрели за все время?")
    count_films = input()
    print("Какой ваш любимый жанр?")
    genre = input()
    print("Действительно, " + genre + " - прекрасный жанр.")
    print("А кто ваш любимый режиссер?")
    director = input()
    print("У вас хороший вкус! " + director +
          " мне тоже очень нравится")
    print("Давайте теперь узнаем имя вашего"
          " любимого актера. Кто же он?")
    actor = input()
    print("Прекрасный выбор! Интересно еще задать"
          " вам пару вопросов")
    print("Как вы считаете какая страна снимает "
          "лучшее кино?")
    country = input()
    print(username + ", вам нравятся только новые или"
                     " популярные фильмы или для вас это неважно?")
    input()
    print("И последний вопрос. Вы хотите посмотреть"
          " на свою анкету? Введите" +
          " \033[31m {}\033[0m".format("да / нет"))
    show = input().lower()
    # Проверка на создание анкеты
    if show == 'да':
        print("\nИмя: " + username)
        print("Любимый жанр: " + genre)
        print("Любимый режисер: " + director)
        print("Любимый актер: " + actor)
        print("Страна с любимым кино: " + country)
        print("Фильмов просмотрено: " + str(count_films) + "\n")
        # Обработка исключений приведения типа
        try:
            if int(count_films) > 500:
                print(
                    "Вы просмотрели довольно много фильмов!"
                    " Но все еще есть много интересного контента"
                    " и я могу помочь его найти")
            else:
                print("Вы посмотрели не так уж много фильмов,"
                      " но я помогу вам это исправить")
        except Exception:
            print("Вы посмотрели не так уж много фильмов,"
                  " но я помогу вам это исправить")


# Основной функционал программы
while start:
    input_str = ""
    while input_str != 'выход':
        try:
            print(
                "\nВыберите номер команды:\n1. Введение\n2."
                " Поиск по жанрам\n3. Просмотр релизов\n"
                "4. Подборка лучших фильмов за год")
            print("Для навигации или выхода из режимов введите" +
                  " \033[31m {}\033[0m".format("меню"))
            print(
                "Если вы уже определились или не хотите продолжать"
                " общение введите" + " \033[31m {}\033[0m".format(
                    "выход"))
            # Приведение к нижнему регистру чтобы было проще проверять
            input_str = input().lower()
            if input_str == '1':
                print("Как вас зовут?")
                username = input()
                greeting()
                make_profile()
            elif input_str == '2':
                select_genre()
            elif input_str == '3':
                check_releases()
            elif input_str == '4':
                get_year_compilation()
            elif input_str == 'выход':
                start = False
                break
        except Exception:
            print("Произошла ошибка!")
            continue
    if not start:
        print("Надеюсь, что я вам помог! Пока!")
        break
