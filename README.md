# Реализованные тесты:

1. Проверка условий длины имен для книг - `test_add_new_book_zero_name_length_and_more_than_40_not_added`
2. Проверка на тип данных для имен книг - `test_add_new_book_name_not_string_not_added`
3. Проверка на отсутствие в словаре жанра книги при первичном добавлении книги - `test_add_new_book_no_genre`
4. Проверка добавления последовательно двух книг - `test_add_new_book_add_two_books`
5. Проверка установки жанра при положительных условиях наличия книги в словаре и жанра в init списке - `test_set_book_genre_name_in_dict_genre_in_list_genre_added`
6. Проверка неустановки жанра при отсутствии книги в словаре - `test_set_book_genre_name_not_in_dict_genre_in_list_genre_not_added`
7. Проверка неустановки жанра при отсутствии жанра в init списке - `test_set_book_genre_name_in_dict_genre_not_in_list_genre_not_added`
8. Проверка изменения жанра - 'test_set_book_genre_change_genre'
9. Проверка получения жанра книги по имени - `test_get_book_genre_name_in_dict`
10. Проверка получения списка книг по жанру при наличии жанра в init списке - `test_get_books_with_specific_genre_genre_in_list_get_list`
11. Проверка получения списка книг по жанру при отсутствии жанра в init списке - `test_get_books_with_specific_genre_genre_not_in_list_not_get_list`
12. Проверка получения словаря с названием и жанром - 'test_get_books_genre_get_dict'
13. Проверка на исключение из словаря для детской аудитории недопустимых жанров книг - `test_get_books_for_children_genre_in_age_rating_get_list`
14. Проверка недобавления в избранное книги, которой нет в словаре - `test_add_book_in_favorites_name_not_in_dict_not_added`
15. Проверка недобавления в избранное книги, которая уже содержится в избранном - `test_add_book_in_favorites_name_exists_in_favors_not_added`
16. Проверка добавления в избранное книги, которая есть в словаре и не содержится в избранном - `test_add_book_in_favorites_name_in_dict_and_not_in_favs_added`
17. Проверка неудаления из избранного книги, которой нет в избранном - `test_delete_book_from_favorites_name_not_in_favs_not_deleted`
18. Проверка удаления книги из избранного - `test_delete_book_from_favorites_name_in_favs_deleted`
19. Проверка получения списка избранного - `test_get_list_of_favorites_books_add_not_added_not_get`
20. Проверка типа данных списка избранного - `test_get_list_of_favorites_books_get_list`
