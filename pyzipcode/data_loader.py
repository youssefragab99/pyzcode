import pandas as pd


def convert_to_int(value):
    if isinstance(value, int):
        return value
    else:
        value = value.strip()
    try:
        return int(value)
    except Exception as e:
        raise ValueError(f"Invalid value: {value}") from e


class DataLoader:
    def __init__(self):
        self.data = pd.read_csv("data/zip_code_database.csv").to_dict(
            orient="records"
        )

    def get_data(self):
        return self.data

    def get_zipcode(self, zip_code):
        zip_code = convert_to_int(zip_code)
        res = [x for x in self.data if x["zip"] == zip_code]
        return res[0] if res else None

    def get_zipcodes(self, city, state):
        res = [
            x
            for x in self.data
            if x["primary_city"].lower() == city.lower()
            and x["state"].lower() == state.lower()
        ]
        return res

    def get_zipcodes_by_state(self, state):
        res = [x for x in self.data if x["state"].lower() == state.lower()]
        return res

    def get_zipcodes_by_city(self, city):
        res = [
            x for x in self.data if x["primary_city"].lower() == city.lower()
        ]
        return res

    def get_zipcodes_by_state_and_city(self, state, city):
        res = [
            x
            for x in self.data
            if x["state"].lower() == state.lower()
            and x["primary_city"].lower() == city.lower()
        ]
        return res

    def get_zipcodes_by_state_and_type(self, state, type):
        res = [
            x
            for x in self.data
            if x["state"].lower() == state.lower()
            and x["type"].lower() == type.lower()
        ]
        return res

    def get_zipcodes_by_city_and_type(self, city, type):
        res = [
            x
            for x in self.data
            if x["primary_city"].lower() == city.lower()
            and x["type"].lower() == type.lower()
        ]
        return res

    def get_zipcodes_by_state_and_city_and_type(self, state, city, type):
        res = [
            x
            for x in self.data
            if x["state"].lower() == state.lower()
            and x["primary_city"].lower() == city.lower()
            and x["type"].lower() == type.lower()
        ]
        return res

    def get_zipcodes_by_state_and_city_and_zipcode(self, state, city, zipcode):
        res = [
            x
            for x in self.data
            if x["state"].lower() == state.lower()
            and x["primary_city"].lower() == city.lower()
            and x["zip"] == zipcode
        ]
        return res

    def get_zipcodes_by_state_and_zipcode(self, state, zipcode):
        res = [
            x
            for x in self.data
            if x["state"].lower() == state.lower() and x["zip"] == zipcode
        ]
        return res

    def get_zipcodes_by_city_and_zipcode(self, city, zipcode):
        res = [
            x
            for x in self.data
            if x["primary_city"].lower() == city.lower()
            and x["zip"] == zipcode
        ]
        return res
