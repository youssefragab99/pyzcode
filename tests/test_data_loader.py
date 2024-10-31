import pytest
from data_loader import DataLoader, convert_to_int


@pytest.fixture
def data_loader():
    return DataLoader()


def test_convert_to_int():
    assert convert_to_int("123") == 123
    assert convert_to_int(123) == 123
    with pytest.raises(ValueError):
        convert_to_int("abc")


def test_get_data(data_loader):
    data = data_loader.get_data()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_zipcode(data_loader):
    zip_code = data_loader.get_zipcode(90210)
    assert zip_code is not None
    assert zip_code["zip"] == 90210


def test_get_zipcodes(data_loader):
    zip_codes = data_loader.get_zipcodes("Beverly Hills", "CA")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"].lower() == "beverly hills"
        assert zip_code["state"].lower() == "ca"


def test_get_zipcodes_by_state(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state("CA")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"


def test_get_zipcodes_by_city(data_loader):
    zip_codes = data_loader.get_zipcodes_by_city("Beverly Hills")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"


def test_get_zipcodes_by_state_and_city(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state_and_city(
        "CA", "Beverly Hills"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"


def test_get_zipcodes_by_state_and_type(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state_and_type("CA", "STANDARD")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_city_and_type(data_loader):
    zip_codes = data_loader.get_zipcodes_by_city_and_type(
        "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_state_and_city_and_type(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state_and_city_and_type(
        "CA", "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_state_and_city_and_zipcode(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state_and_city_and_zipcode(
        "CA", "Beverly Hills", 90210
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["zip"] == 90210


def test_get_zipcodes_by_state_and_zipcode(data_loader):
    zip_codes = data_loader.get_zipcodes_by_state_and_zipcode("CA", 90210)
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["zip"] == 90210


def test_get_zipcodes_by_city_and_zipcode(data_loader):
    zip_codes = data_loader.get_zipcodes_by_city_and_zipcode(
        "Beverly Hills", 90210
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["zip"] == 90210
