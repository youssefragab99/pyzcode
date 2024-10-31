import pandas as pd

def convert_to_int(value):
    if isinstance(value, int):
        return value
    else:
        value = value.strip()
    try:
        return int(value)
    except:
        return None

class DataLoader:
    def __init__(self):
        self.data = pd.read_csv('data/zip_code_database.csv').to_dict(orient='records')

    def get_data(self):
        return self.data

    def get_zipcode(self, zip_code):
        zip_code = convert_to_int(zip_code)
        res = [x for x in self.data if x['zip'] == zip_code]
        return res[0] if res else None
    
    def get_zipcodes(self, city, state):
        res = [x for x in self.data if x['primary_city'].lower() == city.lower() and x['state'].lower() == state.lower()]
        return res

    def get_zipcodes_by_state(self, state):
        return self.data[self.data['state'] == state]

    def get_zipcodes_by_city(self, city):
        return self.data[self.data['city'] == city]

    def get_zipcodes_by_state_and_city(self, state, city):
        return self.data[(self.data['state'] == state) & (self.data['city'] == city)]

    def get_zipcodes_by_state_and_type(self, state, type):
        return self.data[(self.data['state'] == state) & (self.data['type'] == type)]

    def get_zipcodes_by_city_and_type(self, city, type):
        return self.data[(self.data['city'] == city) & (self.data['type'] == type)]

    def get_zipcodes_by_state_and_city_and_type(self, state, city, type):
        return self.data[(self.data['state'] == state) & (self.data['city'] == city) & (self.data['type'] == type)]

    def get_zipcodes_by_state_and_city_and_zipcode(self, state, city, zipcode):
        return self.data[(self.data['state'] == state) & (self.data['city'] == city) & (self.data['zip'] == zipcode)]

    def get_zipcodes_by_state_and_zipcode(self, state, zipcode):
        return self.data[(self.data['state'] == state) & (self.data['zip'] == zipcode)]

    def get_zipcodes_by_city_and_zipcode(self, city, zipcode):
        return self.data[(self.data['city'] == city) & (self.data['zip'] == zipcode)]
