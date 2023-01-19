import os

import requests

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.r = requests.get(url=SHEETY_ENDPOINT)
        # self.data = self.r.json()["prices"]
        self.data = [{'city': 'Mexico', 'iataCode': 'MX', 'id': 2, 'lowestPrice': 500},
     {'city': 'Jamaica', 'iataCode': 'JM', 'id': 3, 'lowestPrice': 300},
     {'city': 'Japan', 'iataCode': 'JP', 'id': 4, 'lowestPrice': 1300},
     {'city': 'Australia', 'iataCode': 'AU', 'id': 5, 'lowestPrice': 1300},
     {'city': 'Spain', 'iataCode': 'ES', 'id': 6, 'lowestPrice': 900},
     {'city': 'Ireland', 'iataCode': 'IE', 'id': 7, 'lowestPrice': 900},
     {'city': 'France', 'iataCode': 'FR', 'id': 8, 'lowestPrice': 900},
     {'city': 'United Kingdom', 'iataCode': 'GB', 'id': 9, 'lowestPrice': 900},
     {'city': 'Italy', 'iataCode': 'IT', 'id': 10, 'lowestPrice': 900},
     {'city': 'Netherlands', 'iataCode': 'NL', 'id': 11, 'lowestPrice': 900},
     {'city': 'Switzerland', 'iataCode': 'CH', 'id': 12, 'lowestPrice': 900},
     {'city': 'Sweden', 'iataCode': 'SE', 'id': 13, 'lowestPrice': 900},
     {'city': 'Norway', 'iataCode': 'NO', 'id': 14, 'lowestPrice': 900},
     {'city': 'Finland', 'iataCode': 'FI', 'id': 15, 'lowestPrice': 900},
     {'city': 'Iceland', 'iataCode': 'IS', 'id': 16, 'lowestPrice': 900},
     {'city': 'Greece', 'iataCode': 'GR', 'id': 17, 'lowestPrice': 900},
     {'city': 'New Zealand', 'iataCode': 'NZ', 'id': 18, 'lowestPrice': 900},
     {'city': 'Thailand', 'iataCode': 'TH', 'id': 19, 'lowestPrice': 900},
     {'city': 'Egypt', 'iataCode': 'EG', 'id': 20, 'lowestPrice': 900},
     {'city': 'Canada', 'iataCode': 'CA', 'id': 21, 'lowestPrice': 900},
     {'city': 'Singapore', 'iataCode': 'SG', 'id': 22, 'lowestPrice': 900},
     {'city': 'Denmark', 'iataCode': 'DK', 'id': 23, 'lowestPrice': 900},
     {'city': 'Belgium', 'iataCode': 'BE', 'id': 24, 'lowestPrice': 900},
     {'city': 'South Africa', 'iataCode': 'ZA', 'id': 25, 'lowestPrice': 900},
     {'city': 'South Korea', 'iataCode': 'KR', 'id': 26, 'lowestPrice': 1200},
     {'city': 'China', 'iataCode': 'CN', 'id': 27, 'lowestPrice': 1200}]


    def update_destination_code(self, id, iata):
        body = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", json=body)
        return response.json()