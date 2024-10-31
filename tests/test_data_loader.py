import pytest
from data_loader import DataLoader


@pytest.fixture
def data_loader():
    return DataLoader()


def test_get_data(data_loader):
    data = data_loader.data
    assert isinstance(data, list)
    assert len(data) > 0
