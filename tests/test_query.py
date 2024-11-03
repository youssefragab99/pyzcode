import pytest

from pyzcode.query import ZipCode, ZipCodeQuery


@pytest.fixture
def zip_code_query():
    return ZipCodeQuery()


def test_get_zipcode(zip_code_query):
    zip_code = zip_code_query.get_zipcode(90210)
    assert zip_code is not None
    assert zip_code["zip"] == 90210


def test_get_zipcodes_by_city(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city("Beverly Hills")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"].lower() == "beverly hills"


def test_get_zipcodes_by_state(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state("CA")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"].lower() == "ca"


def test_get_zipcodes_by_city_and_state(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city_and_state(
        "Beverly Hills", "CA"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"].lower() == "beverly hills"
        assert zip_code["state"].lower() == "ca"


def test_get_zipcodes_by_state_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_and_type("CA", "STANDARD")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"].lower() == "ca"
        assert zip_code["type"].lower() == "standard"


def test_get_zipcodes_by_city_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city_and_type(
        "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["primary_city"].lower() == "beverly hills"
        assert zip_code["type"].lower() == "standard"


def test_get_zipcodes_by_state_city_and_type(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state_city_and_type(
        "CA", "Beverly Hills", "STANDARD"
    )
    assert isinstance(zip_codes, list)
    assert len(zip_codes) > 0
    for zip_code in zip_codes:
        assert zip_code["state"].lower() == "ca"
        assert zip_code["primary_city"].lower() == "beverly hills"
        assert zip_code["type"].lower() == "standard"


def test_get_zipcode_not_found(zip_code_query):
    zip_code = zip_code_query.get_zipcode(99999)
    assert zip_code is None


def test_get_zipcodes_by_city_not_found(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_city("Nonexistent City")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) == 0


def test_get_zipcodes_by_state_not_found(zip_code_query):
    zip_codes = zip_code_query.get_zipcodes_by_state("XX")
    assert isinstance(zip_codes, list)
    assert len(zip_codes) == 0


def test_zip_code_class_initialization():
    with pytest.raises(ValueError):
        ZipCode("99999")

    zip_code = ZipCode("90210")
    assert zip_code.zip.__str__() == "90210"
    assert zip_code.primary_city.lower() == "beverly hills"
    assert zip_code.county.lower() == "los angeles county"
