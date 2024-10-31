"""
pyzipcode - A Python package for handling ZIP code related operations.
"""

__version__ = "0.1.0"
__author__ = "Youssef Ragab"

from data_loader import DataLoader


class ZipCode:
    def __init__(self, zip_code: dict):
        self.zip_code = zip_code["zip_code"]
        self.type = zip_code["type"]
        self.primary_city = zip_code["primary_city"]
        self.acceptable_cities = zip_code["acceptable_cities"]
        self.unacceptable_cities = zip_code["unacceptable_cities"]
        self.state = zip_code["state"]
        self.county = zip_code["county"]
        self.timezone = zip_code["timezone"]
        self.area_codes = zip_code["area_codes"]
        self.world_region = zip_code["world_region"]
        self.country = zip_code["country"]
        self.latitude = zip_code["latitude"]
        self.longitude = zip_code["longitude"]
        self.population = zip_code["irs_estimated_population"]


if __name__ == "__main__":
    dl = DataLoader()

    test = dl.data[0]

    print(dl.get_zipcode("20037"))

    print(dl.get_zipcodes("Washington", "DC"))
