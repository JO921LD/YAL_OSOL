from flask import Flask
from data import db_session
from data.books_api import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/main.db")
    app.register_blueprint(API_GET_BOOK_ON_ID)
    app.register_blueprint(API_GET_ALL_BOOKS)
    app.register_blueprint(BOOKS_BLUEPRINT_FILTER)
    b = BOOK()
    b.BOOK_NAME = "Мастер и Маргарита"
    b.OUT_COUNTRY = 172
    b.DESCRIPTION = "От автора шедевра «Собачье сердце» и «Белая гвардия» Михаила Булгакова. Один из самых известных романов XX века. 1 января 2023 года на экраны выйдет фильм «Воланд» — новое прочтение культового романа, посвящённое взаимоотношениям Мастера и Маргариты, Мастера и Воланда. Бессмертное, загадочное и остроумное «Евангелие от Сатаны» Михаила Булгакова. Роман, уникальный в российской литературе ХХ столетия. Трудно себе представить, какое влияние он оказал на мировую культуру. На основе «Мастера и Маргариты» снимались и продолжают сниматься фильмы и телесериалы, это произведение легло в основу оперы, симфонии, рок-оперы, его иллюстрировали самые знаменитые художники и фотографы. Достаточно перечислить лишь немногих создателей произведений, посвященных шедевру Булгакова и им вдохновленных: Анджей Вайда, Эннио Морриконе, Мик Джаггер, Дэвид Боуи. Чем же заворожила столь разных творческих личностей история о дьяволе и его свите, почтивших своим присутствием Москву 1930-х, о прокураторе Иудеи всаднике Понтии Пилате и нищем философе Иешуа Га-Ноцри, о талантливом и несчастном Мастере и его прекрасной и верной возлюбленной Маргарите?.."
    b.DOWNLOADS = 0
    app.run()


if __name__ == '__main__':
    main()