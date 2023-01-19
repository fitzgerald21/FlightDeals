from flight_data import FlightData
import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
BOT_CHAT_ID = os.environ["BOT_CHAT_ID"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.test = "test"

    def send_message(self, flight_data: FlightData):
        message = f"Low price alert! Only ${flight_data.price} to fly from {flight_data.leaving_from} to" \
                  f" {flight_data.destination}, from {flight_data.arrival_day} to {flight_data.departure_day}."
        if flight_data.layover_message[0] != "":
            message += f"\nLayovers on the way include: {flight_data.layover_message[0]}."
        if flight_data.layover_message[1] != "":
            message += f"\nLayovers on the way back include: {flight_data.layover_message[1]}."
        send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + message
        r = requests.get(send_text)
        return f"{message}\n"