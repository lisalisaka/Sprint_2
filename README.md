# qa_python
A project "qa_python" is my educational project within the course "Python + Selenium" by Yandex Practicum. File "main.py" contains class Collector and its methods. 
File "tests.py" contains unit tests for class Collector. File "conftest.py" has fixtures for using in tests.

## Tests

| Test                                                               | Description                                                                           |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| test_add_new_book_add_two_books                                    | Проверяет, что добавилось именно две книги                                            |
| test_get_book_rating_default_ratin_is_1                            | Проверяет, что рейтинг новой книги возвращается и равен 1                             |
| test_add_new_book_book_is_not_favoutite                            | Проверяет, что при добавлении новой книги она не добавляется в избранное по умолчанию |
| test_set_book_rating_valid_rating_should_be_setted                 | Проверяет, что устанавливается верный рейтинг книги                                   |
| test_set_book_rating_rating_more_10_should_not_to_be_setted        | Проверяет, что рейтинг больше 10 не устанавливается                                   |
| test_set_book_rating_rating_less_1_should_not_to_be_setted         | Проверяет, что рейтинг меньше 1 не устанавливается                                    |
| test_get_books_with_specific_rating_rating_10_return_one_book      | Проверяет, что метод возвращает только книги с определенным рейтингом                 |
| test_add_book_in_favorites_book_becomes_favourite                  | Проверяет, что книга добавляется в Избранное                                          |
| test_add_book_in_favorites_nonexistent_book_should_not_to_be_added | Проверяет, что несуществующая книга не добавляется в Избранное                        |
| test_get_list_of_favorites_books_return_favourite_books            | Проверяет, что возвращается список избранных книг                                     |
| test_delete_book_from_favorites_book_should_be_deleted             | Проверяет, что книга удаляется из Избранного                                          |

Note: list of tests is not full, because the main idea was to learn write unit tests.

## Running Tests

To run tests, you need to install Python and import pytest. To run use the command: 

```sh
pytest -v tests.py
```

