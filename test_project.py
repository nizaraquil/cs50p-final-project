import pytest
from unittest.mock import MagicMock, patch
from project import get_recipe, get_ingredients, get_instructions

# Mocking the requests module for all tests
@pytest.fixture(autouse=True)
def mock_requests_get(monkeypatch):
    mock_response = MagicMock()

    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("your_module_name.requests.get", mock_get)
    return mock_response


def test_get_recipe(mock_requests_get):
    expected_data = {"results": [{"title": "Recipe 1"}]}  # Example response data
    mock_requests_get.json.return_value = expected_data

    response = get_recipe(query="test", diet="Vegetarian")
    assert response == expected_data

def test_get_ingredients(mock_requests_get):
    expected_data = {"ingredients": [{"name": "Ingredient 1"}]}  # Example response data
    mock_requests_get.json.return_value = expected_data

    response = get_ingredients(recipe_id=123)
    assert response == expected_data


def test_get_instructions(mock_requests_get):
    expected_data = [{"steps": [{"number": 1, "step": "Step 1"}]}]  # Example response data
    mock_requests_get.json.return_value = expected_data

    response = get_instructions(recipe_id=123)
    assert response == expected_data
