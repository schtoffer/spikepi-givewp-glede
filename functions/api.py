import requests
import json
from dotenv import load_dotenv
import os



def main():

    pass

def get_profundo_data():
    load_dotenv()
    api_key = os.getenv("KEY")
    base_url = 'https://giver.kirkensbymisjon.no'
    response = requests.get(f'{base_url}/ws-julekampanje?x-api-key={api_key}')

    # Convert the text response to JSON
    json_data = json.loads(response.text) 
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

        return normalized_data
    else:
        return f'Failed to retrieve data. Status Code: {response.status_code}'
    
if __name__ == "__main__":
    main()