#from distutils.command.config import config
import pickle
import json
import numpy as np
import pandas as pd
import config


class PuneHousePricePrediction(): 
    def __init__(self, availability, size, new_total_sqft, bath, balcony, site_location, area_type):
        self.availability = availability 
        self.size = size 
        self.new_total_sqft = new_total_sqft
        self.bath = bath 
        self.balcony = balcony
        self.site_location = "site_location_" + site_location
        self.area_type = "area_type_" + area_type

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
        # with open("Pune_model.pkl", "rb") as f:

            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH) as f:
        # with open("Pune_model_dict.json") as f:

            self.json_data = json.load(f)

    def get_Pune_House_price(self):

        self.load_model() # We have to call method >> load_model >> so that we can use their instance variables
        area_type_index = self.json_data["column_names"].index(self.area_type)
        site_location_index = self.json_data["column_names"].index(self.site_location)


        array = np.zeros(len(self.json_data["column_names"]))
        array[0] = self.json_data["availability"][self.availability]
        array[1] = self.json_data["size"][self.size]
        array[9] = self.new_total_sqft
        array[2] = self.bath
        array[3] = self.balcony
        
        array[area_type_index] = 1
        array[site_location_index] = 1

        print("Test Array -->\n",array)
        price = self.model.predict([array])[0] 

        return round(price,2)


if __name__ == "__main__":
    availability = 1
    size = 20.0
    new_total_sqft   = 2000.0
    bath         = 3
    balcony      = 2
    site_location = "Dhole Patil Road"
    area_type     = "Super built-up  Area"


    obj = PuneHousePricePrediction(availability, size, new_total_sqft, bath, balcony, site_location, area_type)
    charges = obj.get_Pune_House_price()
    print()
    print(f"Pune House price prediction is {round(charges,2)}/- Rs. Only")  
