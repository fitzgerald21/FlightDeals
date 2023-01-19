#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# for data in data_manager.data:
#     if data["iataCode"] == "":
#         data["iataCode"] = flight_search.get_destination_code(data['city'])
#         response = data_manager.update_destination_code(id=data["id"], iata=data["iataCode"])

for location in data_manager.data:
    try:
        kiwi_data = flight_search.search(max_price=location["lowestPrice"], destination=location["iataCode"])["data"][0]
        flight_data = FlightData(kiwi_data)
        print(notification_manager.send_message(flight_data))
    except:
        pass


