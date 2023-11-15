import requests
import json
from dotenv import load_dotenv
import os

def main():
    
    # Example URL
    
    # Make a request (GET or POST as required)
    print(get_profundo_data('n_prosent_antall'))

def get_profundo_data(key='m_sum_i_aar'):
    load_dotenv()
    api_key = os.getenv("KEY")


    base_url = 'https://giver.kirkensbymisjon.no'
    response = requests.get(f'{base_url}/ws-julekampanje?x-api-key={api_key}')

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the text response to JSON
        json_data = json.loads(response.text) 
        # Access data in json_data as required
        return normalize_and_convert_to_float(json_data['data']['rows'][0][key])
    else:
        return f'Failed to retrieve data. Status Code: {response.status_code}'

def normalize_and_convert_to_float(value):
    # Remove spaces (thousand separators)
    value = value.replace(' ', '')
    # Replace comma with dot (decimal separators)
    value = value.replace(',', '.')
    # Convert to float
    return float(value)

if __name__ == "__main__":
    main()
