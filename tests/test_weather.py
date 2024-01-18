import pytest
from unittest.mock import Mock
from ..weatherAPI import get_weather

@pytest.fixture
def mocker():
    from unittest.mock import patch
    return patch('requests.get')

class TestGetWeather:
    def test_get_weather_success(self, mocker):
        # Mocking successful API response
        api_key = "97acacc9c48e4ae723d8b3921c9fcc5d"
        city = "ottawa"
        expected_structure = {
            'main': {'temp': float},
            'weather': [{'description': str}],
            'name': str
        }

        # Mocking API response with dynamically generated data
        mock_data = {
            'main': {'temp': 25.0},
            'weather': [{'description': 'Clear sky'}],
            'name': city.capitalize()
        }
        mocker.return_value = Mock(status_code=200, json=lambda: mock_data)

        # Call the function
        result = get_weather(api_key, city)

        # Assertions for structure and types
        assert isinstance(result, dict)
        assert all(key in result for key in expected_structure)
        for key, value_type in expected_structure.items():
            assert isinstance(result[key], dict)
            assert all(subkey in result[key] and type(result[key][subkey]) is value_subtype
                       for subkey, value_subtype in value_type.items())
        
        # Additional assertions if needed
        assert type(weather[city]) == float










