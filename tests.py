import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['', 'гипермегаультратипасуперэкстранеобычайность'])
    def test_add_new_book_zero_name_length_and_more_than_40_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    @pytest.mark.parametrize('name', [1, 0.1, ['test'], {1,2}, (0, 1), None])
    def test_add_new_book_name_not_string_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если вы решили стать феей')
        assert len(collector.books_genre) == 2

    def test_set_book_genre_name_in_dict_genre_in_list_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_set_book_genre_name_not_in_dict_genre_in_list_genre_not_added(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert 'Гордость и предубеждение и зомби' not in collector.books_genre

    def test_set_book_genre_name_in_dict_genre_not_in_list_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Антиутопия')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_get_book_genre_name_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_genre_in_list_get_list(self):
        collector = BooksCollector()
        name_list = ['Гордость и предубеждение и зомби',
                     'Ужасы нашего городка',
                     'Что делать, если вы решили стать феей']
        genre_list = ['Ужасы', 'Ужасы', 'Комедия']
        for i in range(len(name_list)):
            collector.add_new_book(name_list[i])
            collector.set_book_genre(name_list[i], genre_list[i])
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_with_specific_genre_genre_not_in_list_not_get_list(self):
        collector = BooksCollector()
        name_list = ['Гордость и предубеждение и зомби',
                     'Ужасы нашего городка',
                     'Что делать, если вы решили стать феей']
        genre_list = ['Ужасы', 'Ужасы', 'Психотерапия']
        for i in range(len(name_list)):
            collector.add_new_book(name_list[i])
            collector.set_book_genre(name_list[i], genre_list[i])
        assert len(collector.get_books_with_specific_genre('Психотерапия')) == 0

    def test_get_books_genre_type_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert type(collector.get_books_genre()) == dict


    def test_get_books_for_children_genre_in_age_rating_get_list(self):
        collector = BooksCollector()
        name_list = ['Мальчик-рыба-конь',
                     'Игорь-смельчак',
                     'Гордость и предубеждение и зомби']
        genre_list = ['Мультфильмы', 'Фантастика', 'Ужасы']
        for i in range(len(name_list)):
            collector.add_new_book(name_list[i])
            collector.set_book_genre(name_list[i], genre_list[i])
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_name_not_in_dict_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_name_exists_in_favors_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_name_in_dict_and_not_in_favs_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_name_not_in_favs_not_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Мальчик-рыба-конь')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Мальчик-рыба-конь')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_name_in_favs_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Мальчик-рыба-конь')
        collector.add_book_in_favorites('Мальчик-рыба-конь')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Мальчик-рыба-конь')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_add_not_added_not_get(self):
        collector = BooksCollector()
        collector.add_new_book('Мальчик-рыба-конь')
        collector.add_book_in_favorites('Мальчик-рыба-конь')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Игорь смельчак')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Мальчик-рыба-конь')
        collector.add_book_in_favorites('Мальчик-рыба-конь')
        assert type(collector.get_list_of_favorites_books()) == list