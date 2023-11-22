import pytest


from main import BooksCollector

@pytest.fixture
def fixture_method():
# Добавляем фикстуру для параметризированного теста
    return BooksCollector()
