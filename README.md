# api_yamdb
api_yamdb
# Командный проект YaMDb
### Описание
роект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
"Несмотря на то, что здесь нет произведений, их дух жив, и поэтому каждый желающий может найти его в соответствующих разделах: «Книги», «Фильмы», «Музыка». Это ни на что не влияет. Произведения вы тут не увидите. Но как приятно будет высказать свое авторитетное мнение, даже, если вы данное произведение не читали.".

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/AlexAvdeev1986/api_yamdb/
cd api_yamdb/
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```
Обновить pip:
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

# Некоторые примеры запросов для неавторизованных пользователей:

Категории:
http://127.0.0.1:8000/api/v1/categories/
{
"name": "str",
"slug": "str"
}

Жанры:
http://127.0.0.1:8000/api/v1/genres/
{
"name": "str",
"slug": "str"
}

Отзыв:
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
{
"word": "str",
"scr": 5
}

### Авторы
[Александр Авдеев](https://github.com/AlexAvdeev1986/)
[Олег Асташкин](https://github.com/Olegsnap)
[Артём Иванов](https://github.com/ArtemIvCyber/)
