import pytest
from query import ZipCodeQuery


@pytest.fixture
def zip_code_query():
    return ZipCodeQuery()


def test_get_zipcode(zip_code_query):
    zip_code = zip_code_query.get_zipcode(90210)
    assert zip_code is not None
    assert zip_code["zip"] == 90210


def test_get_zipcodes(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes("Beverly Hills", "CA")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"].lower() == "beverly hills"
        assert zip_code["state"].lower() == "ca"


def test_get_zipcodes_by_state(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state("CA")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"


def test_get_zipcodes_by_city(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city("Beverly Hills")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"


def test_get_zipcodes_by_state_and_city(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_city(
        "CA", "Beverly Hills"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"


def test_get_zipcodes_by_state_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_type("CA", "STANDARD")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_city_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city_and_type(
        "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_state_and_city_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_city_and_type(
        "CA", "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["type"] == "STANDARD"


def test_get_zipcodes_by_state_and_city_and_zipcode(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_city_and_zipcode(
        "CA", "Beverly Hills", 90210
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["zip"] == 90210


def test_get_zipcodes_by_state_and_zipcode(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_zipcode("CA", 90210)
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"] == "CA"
        assert zip_code["zip"] == 90210


def test_get_zipcodes_by_city_and_zipcode(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city_and_zipcode(
        "Beverly Hills", 90210
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"] == "Beverly Hills"
        assert zip_code["zip"] == 90210
