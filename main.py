import requests


def get_country_number(country_name, received_data):
    number = 0
    for data in received_data['data']:
        if country_name == data['location']:
            print(data)
            return number
        number += 1


API = 'https://www.trackcorona.live/api/countries'


received_data = requests.get(API).json()
country = 'India'
# print(received_data['data'][12])

country_no = get_country_number(country, received_data)

print(country_no)
# Using loop
# for data in received_data['data'][country_no]:
#     print(f"{data} : {received_data['data'][country_no][data]}")

