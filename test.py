import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_empty_name(self):

        collector = BooksCollector()

        collector.add_new_book("")

        assert "" not in collector.get_books_genre()

# Проверяем, что книга добавляется корректно
    def test_add_new_book_success(self):

        collector = BooksCollector()

        collector.add_new_book("Последнее желание")

        assert "Последнее желание" in collector.get_books_genre()

# Проверяем, что книга не добавляется, если её имя слишком длинное
    def test_add_new_book_with_long_title(self):

        collector = BooksCollector()

        collector.add_new_book("Пытаемся добавить книгу с большим количеством символов в имени")

        assert "Пытаемся добавить книгу с большим количеством символов в имени" not in collector.get_books_genre()

# Проверяем, что книга не добавляется, если её имя уже существует
    def test_add_new_book_name_already_exists(self):

        collector = BooksCollector()

        collector.add_new_book("Сильмариллион")
        collector.add_new_book("Сильмариллион")

        assert len(collector.get_books_genre()) == 1

# Тесты для метода set_book_genre
# Проверяем, что жанр книги устанавливается корректно
    def test_set_book_genre_success(self):

        collector = BooksCollector()

        collector.add_new_book("Братство кольца")
        collector.set_book_genre("Братство кольца", "Фантастика")

        assert collector.get_book_genre("Братство кольца") == "Фантастика"

# Проверяем, что жанр книги не устанавливается, если книга не существует
    def test_set_book_genre_book_not_exists(self):

        collector = BooksCollector()

        collector.set_book_genre("книга не существует", "Фантастика")

        assert collector.get_book_genre("книга не существует") is None

# Проверяем, что жанр книги не устанавливается, если жанр не существует
    def test_set_book_genre_genre_not_exists(self):

        collector = BooksCollector()

        collector.add_new_book("Дети Хурина")
        collector.set_book_genre("Дети Хурина", "Фэнтези")

        assert collector.get_book_genre("Дети Хурина") == ''

    @pytest.mark.parametrize("initial_books_genre, name, genre, expected_books_genre", [
    ({'Властелин колец': 'Фантастика', 'Кладбище домашних животных': 'Ужасы'}, 'Властелин колец', 'Детективы', {'Властелин колец': 'Детективы', 'Кладбище домашних животных': 'Ужасы'}),
    ({'Властелин колец': 'Фантастика', 'Кладбище домашних животных': 'Ужасы'}, 'NonExistentBook', 'Детективы', {'Властелин колец': 'Фантастика', 'Кладбище домашних животных': 'Ужасы'}),
    ({'Властелин колец': 'Фантастика', 'Кладбище домашних животных': 'Ужасы'}, 'Властелин колец', 'NonExistentGenre', {'Властелин колец': 'Фантастика', 'Кладбище домашних животных': 'Ужасы'}),
    ])
# Выделяем параметризованный тест и добавляем параметры
    def test_set_book_genre(self, fixture_method, initial_books_genre, name, genre, expected_books_genre):
        fixture_method.books_genre = initial_books_genre
        fixture_method.set_book_genre(name, genre)
        assert fixture_method.books_genre == expected_books_genre

# Тесты для метода get_book_genre
    def test_get_book_genre_name_success(self):

        collector = BooksCollector()

        collector.add_new_book("BookName")
        collector.set_book_genre("BookName", "Фантастика")

        assert collector.get_book_genre("BookName") == "Фантастика"

# Тесты для метода get_books_with_specific_genre
# Проверяем, что получаем список книг с определённым жанром корректно
    def test_get_books_with_specific_genre_success(self):

        collector = BooksCollector()

        collector.add_new_book("Дары смерти")
        collector.add_new_book("Гарри Поттер и кубок огня")
        collector.set_book_genre("Дары смерти", "Фантастика")
        collector.set_book_genre("Гарри Поттер и кубок огня", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Дары смерти", "Гарри Поттер и кубок огня"]

# Проверяем, что получаем пустой список, если жанр не существует
    def test_get_books_with_specific_genre_genre_not_exists(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и узник Азкабана")
        collector.add_new_book("Пила")
        collector.set_book_genre("Гарри Поттер и узник Азкабана", "Фантастика")
        collector.set_book_genre("Пила", "Ужасы")

        assert collector.get_books_with_specific_genre("Комедии") == []

# Тесты для метода get_books_genre
    def test_get_books_genre_success(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_new_book("Гарри Поттер и Филосовский камень")
        collector.set_book_genre("Гарри Поттер и Тайная комната", "Фантастика")
        collector.set_book_genre("Гарри Поттер и Филосовский камень", "Фантастика")

        assert collector.get_books_genre() == {"Гарри Поттер и Тайная комната": "Фантастика",
                                               "Гарри Поттер и Филосовский камень": "Фантастика"}

# Тесты для метода get_books_for_children
# Проверяем, что получаем список книг, подходящих детям, корректно
    def test_get_books_for_children_success(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_new_book("Гарри Поттер и Филосовский камень")
        collector.add_new_book("Живая шляпа")
        collector.set_book_genre("Гарри Поттер и Тайная комната", "Фантастика")
        collector.set_book_genre("Гарри Поттер и Филосовский камень", "Ужасы")
        collector.set_book_genre("Живая шляпа", "Комедии")

        assert collector.get_books_for_children() == ['Гарри Поттер и Тайная комната', 'Живая шляпа']

# Тесты для метода add_book_in_favorites
# Проверяем, что книга добавляется в избранное корректно
    def test_add_book_in_favorites_success(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")

        assert collector.get_list_of_favorites_books() == ["Гарри Поттер и Тайная комната"]

# Проверяем, что книга не добавляется в избранное, если она не существует
    def test_add_book_in_favorites_book_not_exists(self):

        collector = BooksCollector()

        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")

        assert collector.get_list_of_favorites_books() == []

# Проверяем, что книга не добавляется в избранное, если она уже там есть
    def test_add_book_in_favorites_already_in_favorites(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")
        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")

        assert len(collector.get_list_of_favorites_books()) == 1

# Тесты для метода delete_book_from_favorites
# Проверяем, что книга удаляется из избранного корректно
    def test_delete_book_from_favorites_success(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")
        collector.delete_book_from_favorites("Гарри Поттер и Тайная комната")

        assert collector.get_list_of_favorites_books() == []

# Проверяем, что книга не удаляется из избранного, если она не там
    def test_delete_book_from_favorites_not_in_favorites(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.delete_book_from_favorites("Гарри Поттер и Тайная комната")

# Тесты для метода get_list_of_favorites_books
# Проверяем список избранного
    def test_get_list_of_favorites_books_success(self):

        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_book_in_favorites("Гарри Поттер и Тайная комната")

        assert collector.get_list_of_favorites_books() == ["Гарри Поттер и Тайная комната"]

# Тесты параметризованные

    @pytest.mark.parametrize('name', ['abcde', '1abcd', '123$#', '    ', '123 4'])
    def test_add_new_book_list_success(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert name in collector.get_books_genre()
