import requests
import json

print(requests.get("http://127.0.0.1:5000/books/1").json())
print(requests.get("http://127.0.0.1:5000/api/books/all").json())
print(requests.get("http://127.0.0.1:5000/api/filter?find=АСND&publisher=1").json())

'''f = open("db/country.csv", "r", encoding="UTF-8")
data = [i.split(";") for i in f.readlines()]
res = []
f.close()
for i in range(len(data)):
    res.append([str(int(data[i][0]) + 1), data[i][1], data[i][2]])
with open("db/country.csv", "w", encoding="UTF-8") as file:
    for i in res:
        print(i)
        file.write(";".join(i))
'''

'''b = BOOK()
    b.BOOK_NAME = "Мастер и Маргарита"
    b.DESCRIPTION = "От автора шедевра «Собачье сердце» и «Белая гвардия» Михаила Булгакова. Один из самых известных романов XX века. 1 января 2023 года на экраны выйдет фильм «Воланд» — новое прочтение культового романа, посвящённое взаимоотношениям Мастера и Маргариты, Мастера и Воланда. Бессмертное, загадочное и остроумное «Евангелие от Сатаны» Михаила Булгакова. Роман, уникальный в российской литературе ХХ столетия. Трудно себе представить, какое влияние он оказал на мировую культуру. На основе «Мастера и Маргариты» снимались и продолжают сниматься фильмы и телесериалы, это произведение легло в основу оперы, симфонии, рок-оперы, его иллюстрировали самые знаменитые художники и фотографы. Достаточно перечислить лишь немногих создателей произведений, посвященных шедевру Булгакова и им вдохновленных: Анджей Вайда, Эннио Морриконе, Мик Джаггер, Дэвид Боуи. Чем же заворожила столь разных творческих личностей история о дьяволе и его свите, почтивших своим присутствием Москву 1930-х, о прокураторе Иудеи всаднике Понтии Пилате и нищем философе Иешуа Га-Ноцри, о талантливом и несчастном Мастере и его прекрасной и верной возлюбленной Маргарите?.."
    b.AUTHOR = "Булгаков Михаил Афанасьевич"
    b.PUBLISHER = "АСТ"
    b.OUT_COUNTRY = 172
    b.FILE_NAME = "ABDS"
    b.GENRES = "_1_14_74_"
    b.OUT_COUNTRY = 172
    b.FILE_NAME = "MASTER_I_MARGARITA_BULGAKOV_01"
    b.CODECS = "_4_1_"
    db_sess = db_session.create_session()
    db_sess.add(b)
    db_sess.commit()'''