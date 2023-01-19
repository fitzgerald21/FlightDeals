import re
from datetime import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, kiwi_data):
        self.leaving_from = kiwi_data["cityFrom"] + "-" + kiwi_data["flyFrom"]
        self.destination = kiwi_data["cityTo"] + ", " + kiwi_data["countryTo"]["name"] + " (" + kiwi_data["flyTo"] + ")"
        self.price = kiwi_data["price"]
        self.arrival_day = kiwi_data["route"][0]["local_departure"][:10]
        self.departure_day = kiwi_data["route"][-1]["local_arrival"][:10]
        self.starting_city = kiwi_data["cityFrom"]
        self.ending_city = kiwi_data["cityTo"]
        self.layovers = {flight["cityFrom"]: {
            "to": str(self.date_convert(flight["local_arrival"]) - self.date_convert(flight["local_departure"]) if flight["return"] == 0 else "")[:-3],
            "from": str(self.date_convert(flight["local_arrival"]) - self.date_convert(flight["local_departure"]) if flight["return"] == 1 else "")[:-3],
        }
            for flight in kiwi_data["route"] if
            flight["cityFrom"] != self.starting_city and flight["cityFrom"] != self.ending_city
        }
        self.layover_message = self.create_layover_message(self.layovers)


    def date_convert(self, date_text):
        date_list = re.split("\W+|T", date_text)
        date_list = [int(num) for num in date_list[:5]]
        return datetime(year=date_list[0], month=date_list[1], day=date_list[2],
                                hour=date_list[3], minute=date_list[4])


    def create_layover_message(self, layovers):
        to_message = ""
        from_message = ""
        for city in layovers:
            if layovers[city]["to"]:
                to_message += f"{city} ({layovers[city]['to']}), "
            if layovers[city]["from"]:
                from_message += f"{city} ({layovers[city]['from']}), "
        return [to_message[:-2], from_message[:-2]]

