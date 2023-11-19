import requests
import json
from dotenv import load_dotenv
import os
import time

from buildhat import ForceSensor

button_left = ForceSensor('C')
button_right = ForceSensor('D')

load_dotenv()
api_key = os.getenv("KEY")
base_url = 'https://giver.kirkensbymisjon.no'
response = requests.get(f'{base_url}/ws-julekampanje?x-api-key={api_key}')

# Convert the text response to JSON
json_data = json.loads(response.text) 

from spike_functions import show_on_gauge, show_on_tower

def main():

    # Print values for all valid keys
    valid_keys = ['i_antall_i_aar', 'm_sum_i_aar', 'm_max_i_aar', 'i_antall_i_fjor', 'm_sum_i_fjor', 'm_max_i_fjor', 'n_prosent_sum', 'n_prosent_antall', 'i_antall']
    for key in valid_keys:
        print(f"{key}: {get_profundo_data(key)}")

    while True:
        if button_left.is_pressed():
            time.sleep(1)
            if button_left.get_force() > 50:
                show_on_gauge(0)
                show_on_tower(0)
                break
            else:
                show_on_gauge(get_profundo_data('n_prosent_sum'))
                show_on_tower((get_profundo_data('m_sum_i_aar') / 45000000)*100)
                print(f"prosent {show_on_tower((get_profundo_data('m_sum_i_aar') / 45000000)*100)}")
            


def get_profundo_data(key_str):
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the text response to JSON
        json_data = json.loads(response.text)
        json_data_striped = json_data['data']['rows'][0]
        # Normalize the data to be all float
        normalized_data = {}
        for key, value in json_data_striped.items():
            value = value.replace(' ', '')
            value = value.replace(',', '.')
            normalized_data.update({key: float(value)})
                        
            # print(normalized_data)

        return normalized_data[key_str]
    else:
        return f'Failed to retrieve data. Status Code: {response.status_code}'

if __name__ == "__main__":
    main()
