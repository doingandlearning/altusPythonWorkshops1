import os
import pytest

def my_add(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (10, -5, 5),
    (0, 0, 0),
    (-3, -2, -5),
], ids=["case1", "case2", "case3", "case4"])
def test_add(a, b, expected):
    assert my_add(a, b) == expected


def divide(a, b):
    return a/b


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1/0)


# @pytest.mark.parametrize("input_value", "expected_result", [
#     ((1, 2), 3),
#     ((0, 3), 3),
#     ((-2, 2), 0),
#     ((10, 10), 20)
# ])
# def test_my_function_adds(input_value, expected_result):
#     assert my_add(input_value[0], input_value[1]) == expected_result

@pytest.fixture()
def todos():
    return [{"id": 1, "title": "Use TDD", "completed": True}]


def test_some_data(todos):
		todos.append({"id": 2, "title": "Use TDD", "completed": True})
		assert len(todos) == 2

@pytest.mark.xfail()
def test_some_other_data(todos):
	assert len(todos) != 1

@pytest.fixture(scope="module")
def database_connection():
	return {"connection": True}


# Monkey Patching
def example():
	current_path = os.getcwd()
	return current_path

def test_get_current_directory(monkeypatch):
	"""
	Arrange: monkeypatch os.getcwd()  - have a predictable result!
	Act: call example()
	Assert: result will be monkeypatch has set it to be
	"""
	def mock_getcwd():
		return '/data/user/1234'
	
	monkeypatch.setattr(os, 'getcwd', mock_getcwd)

	assert example() == '/data/user/1234'


