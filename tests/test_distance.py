import pytest

from pyzcode import ZipCode
from pyzcode.distance import DistanceCalculator


# Mocking the ZipCode class for testing purposes
class MockZipCode:
    def __init__(self, zip_code, lat, lon):
        self.zip_code = zip_code
        self.lat = lat
        self.lon = lon


@pytest.fixture
def mock_zipcode(monkeypatch):
    def mock_init(self, zip_code):
        if zip_code == "12345":
            self.lat = 40.7128
            self.lon = -74.0060
        elif zip_code == "67890":
            self.lat = 34.0522
            self.lon = -118.2437
        else:
            self.lat = None
            self.lon = None

    monkeypatch.setattr(ZipCode, "__init__", mock_init)


def test_calculate_distance_valid():
    distance = DistanceCalculator.calculate_distance("12345", "20037")
    assert distance == pytest.approx(508.185, 0.1)


def test_calculate_distance_invalid_zip_code():
    with pytest.raises(ValueError, match="No data found for zip code: 00000"):
        DistanceCalculator.calculate_distance("12345", "00000")


def test_calculate_distance_same_zip_code():
    distance = DistanceCalculator.calculate_distance("12345", "12345")
    assert distance == 0.0
