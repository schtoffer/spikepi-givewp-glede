import requests
import json
from dotenv import load_dotenv
import os

from buildhat import Motor


# load_dotenv()
# api_key = os.getenv("KEY")
# base_url = 'https://giver.kirkensbymisjon.no'
# response = requests.get(f'{base_url}/ws-julekampanje?x-api-key={api_key}')

# # Convert the text response to JSON
# json_data = json.loads(response.text) 

# Access data in json_data as required
# data = json_data['data']['rows'][0]

data = {'i_antall_i_aar': '17 859', 'm_sum_i_aar': '8 148 978', 'm_max_i_aar': '317 000', 'i_antall_i_fjor': '23 348', 'm_sum_i_fjor': '9 836 933', 'm_max_i_fjor': '100 000', 'n_prosent_sum': '-17,16', 'n_prosent_antall': '-23,51', 'i_antall': '-23,51'}


# Check if the request was successful
# if response.status_code == 200:
#     # Convert the text response to JSON
#     json_data = json.loads(response.text) 
#     # Access data in json_data as required
#     data = json_data['data']['rows'][0]
# else:
#     print(f'Failed to retrieve data. Status Code: {response.status_code}')



def main():
    
    # These are valid keys:
    # 'i_antall_i_aar', Value: 16 782
    # 'm_sum_i_aar'
    # 'm_max_i_aar'
    # 'i_antall_i_fjor'
    # 'm_sum_i_fjor'
    # 'm_max_i_fjor'
    # 'n_prosent_sum'
    # 'n_prosent_antall'
    # 'i_antall'
    print(get_profundo_key_value('i_antall_i_aar'))


    # motor.run_for_degrees(get_profundo_key_value('n_prosent_antall'))
    

def get_profundo_key_value(str='m_sum_i_aar'):
    value = normalize_value(data[str])
    return value

def normalize_value(value):
    # Remove spaces (thousand separators)
    value = value.replace(' ', '')
    # Replace comma with dot (decimal separators)
    value = value.replace(',', '.')
    # Convert to float
    return float(value)

if __name__ == "__main__":
    main()
