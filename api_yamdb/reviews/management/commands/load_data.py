import csv

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (
    Category,
    Comment,
    Genre,
    GenreTitle,
    Review,
    Title,
    User,
)


class UsersLoader:
    fields = (
        'id',
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name'
    )
    model = User


class CategoryLoader:
    fields = ('id', 'name', 'slug')
    model = Category


class GenreLoader:
    fields = ('id', 'name', 'slug')
    model = Genre


class TitleLoader:
    fields = ('id', 'name', 'year', 'category')
    model = Title


class GenreTitleLoader:
    fields = ('id', 'title_id', 'genre_id')
    model = GenreTitle


class ReviewLoader:
    fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
    model = Review


class CommentLoader:
    fields = ('id', 'review_id', 'author', 'pub_date')
    model = Comment


MAPPING = {
    'users.csv': UsersLoader,
    'category.csv': CategoryLoader,
    'genre.csv': GenreLoader,
    'titles.csv': TitleLoader,
    'genre_title.csv': GenreTitle,
    'review.csv': ReviewLoader,
    'comments.csv': CommentLoader,
}


class Command(BaseCommand):
    """
    Команда выполняет импорт данных
    из csv-файлов в базу данных проекта
    """

    def handle(self, *args, **kwargs):
        for file_name, loader in MAPPING.items():
            file_location = f'{settings.BASE_DIR}/static/data/{file_name}'
            with open(file_location, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    data = {field: row[field] for field in loader.fields}
                    loader.model.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Все данные загружены'))
