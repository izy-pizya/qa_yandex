Добавил тесты для класса "BooksCollector".

1. # Проверяем возможность добавление книги с пустым именем
test_add_new_book_empty_name

2. # Проверяем, что книга добавляется корректно
test_add_new_book_success


3. # Проверяем, что книга не добавляется, если её имя слишком длинное
test_add_new_book_with_long_title


3. # Проверяем, что книга не добавляется, если её имя уже существует
test_add_new_book_name_already_exists

# Тесты для метода set_book_genre

4. # Проверяем, что жанр книги устанавливается корректно
test_set_book_genre_success

5. # Проверяем, что жанр книги не устанавливается, если книга не существует
test_set_book_genre_book_not_exists

6. # Проверяем, что жанр книги не устанавливается, если жанр не существует
test_set_book_genre_genre_not_exists


7. # Параметризированеый автотест для проверки присвоения жанра
test_set_book_genre


8. # Тесты для метода get_book_genre
test_get_book_genre_name_success


# Тесты для метода get_books_with_specific_genre
9. # Проверяем, что получаем список книг с определённым жанром корректно
test_get_books_with_specific_genre_success


10. # Проверяем, что получаем пустой список, если жанр не существует
test_get_books_with_specific_genre_not_exists


11. # Тесты для метода get_books_genre
test_get_books_genre_success


# Тесты для метода get_books_for_children
12. # Проверяем, что получаем список книг, подходящих детям, корректно
test_get_books_for_children_success


# Тесты для метода add_book_in_favorites
13. # Проверяем, что книга добавляется в избранное корректно
test_add_book_in_favorites_success


14. # Проверяем, что книга не добавляется в избранное, если она не существует
test_add_book_in_favorites_book_not_exists


15. # Проверяем, что книга не добавляется в избранное, если она уже там есть
test_add_book_in_favorites_already_in_favorites


# Тесты для метода delete_book_from_favorites
16. # Проверяем, что книга удаляется из избранного корректно
test_delete_book_from_favorites_success


17. # Проверяем, что книга не удаляется из избранного, если она не там
test_delete_book_from_favorites_not_in_favorites


# Тесты для метода get_list_of_favorites_books
18. # Проверяем список избранного
test_get_list_of_favorites_books_success


19. # Тесты параметризованные
test_add_new_book_list_success
