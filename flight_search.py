import requests
from datetime import datetime, timedelta
import os

KIWI_API_KEY = os.environ["KIWI_API_KEY"]
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
KIWI_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    def __init__(self):
        self.header = {
            "apikey": KIWI_API_KEY
        }
        self.today = datetime.today()
        self.later = self.today + timedelta(days=180)

    def search(self, max_price, destination):
        parameters = {
            "fly_from": "DFW",
            "fly_to": destination,
            # "date_from": self.today.strftime("%d/%m/%Y"),
            "date_from": "16/04/2023",
            # "date_to": self.later.strftime("%d/%m/%Y"),
            "date_to": "10/06/2023",
            # "return_from": (self.today + timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_from": "25/04/2023",
            # "return_to": (self.later + timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_to": "20/06/2023",
            "nights_in_dst_from": 8,
            "nights_in_dst_to": 15,
            "flight_type": "round",
            "adults": 2,
            "selected_cabins": "M",
            "adult_gold_bag": "0,0",
            "curr": "USD",
            # "price_to": max_price,
            "price_to": 2000,
            "limit": 1,
            "max_stopovers": 2
        }
        r = requests.get(url=KIWI_ENDPOINT, params=parameters, headers=self.header)
        return r.json()

    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_LOCATION_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "country"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


# Response Example:
# {
#   'id': '1b3620a14c1000008b549a69_0|20a125c34c110000218ae790_0|25c31b364c1d4c2987d4be04_0|25c31b364c1d4c2987d4be04_1|25c31b364c1d4c2987d4be04_2',
#   'flyFrom': 'DFW',
#   'flyTo': 'CDG',
#   'cityFrom': 'Dallas',
#   'cityCodeFrom': 'DFW',
#   'cityTo': 'Paris',
#   'cityCodeTo': 'PAR',
#   'countryFrom': {
#     'code': 'US',
#     'name': 'United States'
#   },
#   'countryTo': {
#     'code': 'FR',
#     'name': 'France'
#   },
#   'nightsInDest': 12,
#   'quality': 2429.351631,
#   'distance': 7952.8,
#   'duration': {
#     'departure': 84060,
#     'return': 37500,
#     'total': 121560
#   },
#   'price': 1993,
#   'conversion': {
#     'EUR': 1841.086435,
#     'USD': 1993
#   },
#   'fare': {
#     'adults': 996.5,
#     'children': 996.5,
#     'infants': 996.5
#   },
#   'bags_price': {
#     '1': 332.475
#   },
#   'baglimit': {
#     'hand_height': 35,
#     'hand_length': 55,
#     'hand_weight': 10,
#     'hand_width': 23,
#     'hold_dimensions_sum': 157,
#     'hold_height': 52,
#     'hold_length': 78,
#     'hold_weight': 23,
#     'hold_width': 27,
#     'personal_item_height': 30,
#     'personal_item_length': 40,
#     'personal_item_weight': 2,
#     'personal_item_width': 10
#   },
#   'availability': {
#     'seats': 8
#   },
#   'airlines': [
#     'N0',
#     'DL'
#   ],
#   'route': [
#     {
#       'id': '1b3620a14c1000008b549a69_0',
#       'combination_id': '1b3620a14c1000008b549a69',
#       'flyFrom': 'DFW',
#       'flyTo': 'JFK',
#       'cityFrom': 'Dallas',
#       'cityCodeFrom': 'DFW',
#       'cityTo': 'New York',
#       'cityCodeTo': 'NYC',
#       'airline': 'DL',
#       'flight_no': 330,
#       'operating_carrier': 'DL',
#       'operating_flight_no': '330',
#       'fare_basis': 'VAVNH3BQ',
#       'fare_category': 'M',
#       'fare_classes': 'E',
#       'fare_family': '',
#       'return': 0,
#       'bags_recheck_required': False,
#       'vi_connection': False,
#       'guarantee': False,
#       'equipment': None,
#       'vehicle_type': 'aircraft',
#       'local_arrival': '2023-04-25T12:29:00.000Z',
#       'utc_arrival': '2023-04-25T16:29:00.000Z',
#       'local_departure': '2023-04-25T07:44:00.000Z',
#       'utc_departure': '2023-04-25T12:44:00.000Z'
#     },
#     {
#       'id': '20a125c34c110000218ae790_0',
#       'combination_id': '20a125c34c110000218ae790',
#       'flyFrom': 'JFK',
#       'flyTo': 'CDG',
#       'cityFrom': 'New York',
#       'cityCodeFrom': 'NYC',
#       'cityTo': 'Paris',
#       'cityCodeTo': 'PAR',
#       'airline': 'N0',
#       'flight_no': 302,
#       'operating_carrier': '',
#       'operating_flight_no': '',
#       'fare_basis': '',
#       'fare_category': 'M',
#       'fare_classes': '',
#       'fare_family': '',
#       'return': 0,
#       'bags_recheck_required': True,
#       'vi_connection': True,
#       'guarantee': True,
#       'equipment': None,
#       'vehicle_type': 'aircraft',
#       'local_arrival': '2023-04-26T14:05:00.000Z',
#       'utc_arrival': '2023-04-26T12:05:00.000Z',
#       'local_departure': '2023-04-26T00:30:00.000Z',
#       'utc_departure': '2023-04-26T04:30:00.000Z'
#     },
#     {
#       'id': '25c31b364c1d4c2987d4be04_0',
#       'combination_id': '25c31b364c1d4c2987d4be04',
#       'flyFrom': 'CDG',
#       'flyTo': 'DFW',
#       'cityFrom': 'Paris',
#       'cityCodeFrom': 'PAR',
#       'cityTo': 'Dallas',
#       'cityCodeTo': 'DFW',
#       'airline': 'DL',
#       'flight_no': 8548,
#       'operating_carrier': 'AF',
#       'operating_flight_no': '146',
#       'fare_basis': 'VK09UILB',
#       'fare_category': 'M',
#       'fare_classes': 'E',
#       'fare_family': '',
#       'return': 1,
#       'bags_recheck_required': False,
#       'vi_connection': False,
#       'guarantee': False,
#       'equipment': '789',
#       'vehicle_type': 'aircraft',
#       'local_arrival': '2023-05-08T13:35:00.000Z',
#       'utc_arrival': '2023-05-08T18:35:00.000Z',
#       'local_departure': '2023-05-08T10:10:00.000Z',
#       'utc_departure': '2023-05-08T08:10:00.000Z'
#     }
#   ],
#   'booking_token': 'E335-5lBaKCL4DfufOgBXVBgFGTM5bJ2-QKew-8A3rogcFstMjbBmvS0DSmIvp14evOjK7E_EUx5QQ5V0_4PvXtGt35XDINPmu0oGC2PQtc7zxT1xNl3llfVntoZbURLmjyrrGf9L5wFg3N51XYQzKywzszgpUN9PJVJVbIHABvF0itxyFFInpDNxMJkA0s0oPVFGFBN6RtfLahs5rKukng4GgkxqCilcnmiMry7GpFW-lc6xzpI4H2Pg9IPXDBUWrNh0dMXFkkcMEgVESbprSLNbqqa6-hMbB0dLyBIzD1ldRYMNLw-DZHVMaM_Z8vbsDmxfsKbj4NbWo6Q_gpsZR4ZQsYYwtCAH_72zlf_lV9qDtqdK9FAdJqNhJAZIdU02ef79WYrVlx1Z__5MSAKZHCP3HSFol16isiZwZsScG91HEXaUPQ01z4BhtGdA2Pk6eJut56o_V_rD0bYqmRXMCGSTUaGAKKLwdg6DB-Jh0vE_wfR8LZXzVpraNKQCxMlrJ66soz8V43zcVoC3RZ2kNHjd2j_vLwYqi2_oZnbOoqkiE-99tR8S9IxB_fJjKPuAVhqXFEn3b4fI0AT1e39lFRFgO-76QvNJYFer-z6ptX95LSFvDlTDlNqVB-jaVbebaDfbUbmN_1fbm1cqZOKJGo8b2oQi7_EJRxTUdeb3FQiem-Emt7ddJY46VrnfkxWbA-Fsks9yTrL15Lp-p-Av7IL4p7Cv6XasCB41jiM-nkQ=',
#   'deep_link': 'https://www.kiwi.com/deep?affilid=fitzgerald21flightsearch&currency=USD&flightsId=1b3620a14c1000008b549a69_0%7C20a125c34c110000218ae790_0%7C25c31b364c1d4c2987d4be04_0%7C25c31b364c1d4c2987d4be04_1%7C25c31b364c1d4c2987d4be04_2&from=DFW&lang=en&passengers=2&to=CDG&booking_token=E335-5lBaKCL4DfufOgBXVBgFGTM5bJ2-QKew-8A3rogcFstMjbBmvS0DSmIvp14evOjK7E_EUx5QQ5V0_4PvXtGt35XDINPmu0oGC2PQtc7zxT1xNl3llfVntoZbURLmjyrrGf9L5wFg3N51XYQzKywzszgpUN9PJVJVbIHABvF0itxyFFInpDNxMJkA0s0oPVFGFBN6RtfLahs5rKukng4GgkxqCilcnmiMry7GpFW-lc6xzpI4H2Pg9IPXDBUWrNh0dMXFkkcMEgVESbprSLNbqqa6-hMbB0dLyBIzD1ldRYMNLw-DZHVMaM_Z8vbsDmxfsKbj4NbWo6Q_gpsZR4ZQsYYwtCAH_72zlf_lV9qDtqdK9FAdJqNhJAZIdU02ef79WYrVlx1Z__5MSAKZHCP3HSFol16isiZwZsScG91HEXaUPQ01z4BhtGdA2Pk6eJut56o_V_rD0bYqmRXMCGSTUaGAKKLwdg6DB-Jh0vE_wfR8LZXzVpraNKQCxMlrJ66soz8V43zcVoC3RZ2kNHjd2j_vLwYqi2_oZnbOoqkiE-99tR8S9IxB_fJjKPuAVhqXFEn3b4fI0AT1e39lFRFgO-76QvNJYFer-z6ptX95LSFvDlTDlNqVB-jaVbebaDfbUbmN_1fbm1cqZOKJGo8b2oQi7_EJRxTUdeb3FQiem-Emt7ddJY46VrnfkxWbA-Fsks9yTrL15Lp-p-Av7IL4p7Cv6XasCB41jiM-nkQ=',
#   'facilitated_booking_available': True,
#   'pnr_count': 3,
#   'has_airport_change': False,
#   'technical_stops': 0,
#   'throw_away_ticketing': True,
#   'hidden_city_ticketing': False,
#   'virtual_interlining': True,
#   'local_arrival': '2023-04-26T14:05:00.000Z',
#   'utc_arrival': '2023-04-26T12:05:00.000Z',
#   'local_departure': '2023-04-25T07:44:00.000Z',
#   'utc_departure': '2023-04-25T12:44:00.000Z'
# }