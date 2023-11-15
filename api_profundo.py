import requests
import json
from dotenv import load_dotenv
import os

from buildhat import Motor
motor = Motor('A')

load_dotenv()
api_key = os.getenv("KEY")
base_url = 'https://giver.kirkensbymisjon.no'
response = requests.get(f'{base_url}/ws-julekampanje?x-api-key={api_key}')

# Check if the request was successful
if response.status_code == 200:
    # Convert the text response to JSON
    json_data = json.loads(response.text) 
    # Access data in json_data as required
    data = json_data['data']['rows'][0]
else:
    print(f'Failed to retrieve data. Status Code: {response.status_code}')

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


    motor.run_for_degrees(get_profundo_key_value('n_prosent_antall'))
    

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

def normalize_and_convert_to_float(value):
    # Remove spaces (thousand separators)
    value = value.replace(' ', '')
    # Replace comma with dot (decimal separators)
    value = value.replace(',', '.')
    # Convert to float
    return float(value)

if __name__ == "__main__":
    main()
