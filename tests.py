from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector, book1, book2):
        """"Проверяет, что добавилось именно две книги"""
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2, "В словаре не 2 книги"

    def test_get_book_rating_default_ratin_is_1(self, collector):
        """Проверяет, что рейтинг новой книги возвращается и равен 1"""
        collector.add_new_book('Гарри Поттер и Кубок огня')
        assert collector.get_book_rating('Гарри Поттер и Кубок огня') == 1, "Рейтинг новой книги не равен 1"

    def test_add_new_book_book_is_not_favoutite(self, collector):
        """Проверяет, что при добавлении новой книги она не добавляется в избранное по умолчанию"""
        book = collector.add_new_book('Гарри Поттер и Кубок огня')
        assert 'Гарри Поттер и Кубок огня' not in collector.get_list_of_favorites_books(), "Новая книга оказалась в Избранном"

    def test_set_book_rating_valid_rating_should_be_setted(self, collector):
        """Проверяет, что устанавливается верный рейтинг книги"""
        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.set_book_rating('Гарри Поттер и Кубок огня', 5)
        assert collector.books_rating.get('Гарри Поттер и Кубок огня') == 5, "Рейтинг книги не соответствует установленному"

    def test_set_book_rating_rating_more_10_should_not_to_be_setted(self, collector, book1):
        """Проверяет, что рейтинг больше 10 не устанавливается"""
        collector.set_book_rating(list(collector.books_rating.keys())[0], 11)
        assert list(collector.books_rating.values())[0] == 1, "Можно установить рейтинг книги больше 10"

    def test_set_book_rating_rating_less_1_should_not_to_be_setted(self, collector, book1):
        """Проверяет, что рейтинг меньше 1 не устанавливается"""
        collector.set_book_rating(list(collector.books_rating.keys())[0], 0)
        assert list(collector.books_rating.values())[0] == 1, "Рейтинг книги можно установить меньше 1"

    def test_get_books_with_specific_rating_rating_10_return_one_book(self, collector, book1, book2, book3):
        """Проверяет, что метод возвращает только книги с определенным рейтингом"""
        collector.set_book_rating(list(collector.books_rating.keys())[0], 3)
        collector.set_book_rating(list(collector.books_rating.keys())[1], 9)
        collector.set_book_rating(list(collector.books_rating.keys())[2], 10)
        assert 'Котлован', "Вернулись книги не с тем рейтингом"

    def test_add_book_in_favorites_book_becomes_favourite(self, collector, book1):
        """Проверяет, что книга добавляется в Избранное"""
        collector.add_book_in_favorites(list(collector.books_rating.keys())[0])
        assert list(collector.books_rating.keys())[0] in collector.favorites, "Книга не добавилась в Избранное"

    def test_add_book_in_favorites_nonexistent_book_should_not_to_be_added(self, collector):
        """Проверяет, что несуществующая книга не добавляется в Избранное"""
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites, "Несуществующая книга добавилась в Избранное"

    def test_get_list_of_favorites_books_return_favourite_books(self, collector, book1, book2, book3):
        """Проверяет, что возвращается список избранных книг"""
        collector.add_book_in_favorites(list(collector.books_rating.keys())[0])
        collector.add_book_in_favorites(list(collector.books_rating.keys())[2])
        collector.get_list_of_favorites_books()
        assert len(collector.favorites) == 2 and list(collector.books_rating.keys())[0] in collector.favorites and list(collector.books_rating.keys())[2] in collector.favorites, "В списке избранных книг если лишние или недостающие книги"

    def test_delete_book_from_favorites_book_should_be_deleted(self, collector, book1, book2):
        """Проверяет, что книга удаляется из Избранного"""
        collector.add_book_in_favorites(list(collector.books_rating.keys())[0])
        collector.add_book_in_favorites(list(collector.books_rating.keys())[1])
        collector.delete_book_from_favorites(list(collector.books_rating.keys())[0])
        collector.get_list_of_favorites_books()
        assert len(collector.favorites) == 1 and list(collector.books_rating.keys())[1] in collector.favorites, "Книга не удалилась из избранного"