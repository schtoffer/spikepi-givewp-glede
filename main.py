import requests
import json
from dotenv import load_dotenv
import os
import time

from buildhat import ForceSensor, Motor
from buildhat.exc import BuildHATError  # Correctly importing the BuildHATError

from spike_functions import show_on_gauge, show_on_tower

import Adafruit_CharLCD as LCD

lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 12
lcd_d6 = 24
lcd_d7 = 6
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)




def main():
    
    # print(get_profundo_data())
    button_left = initialize_sensor('C')
    button_right = initialize_sensor('D')

    # profundo_data = {'i_antall_i_aar': 17894.0, 'm_sum_i_aar': 8225758.0, 'm_max_i_aar': 317000.0, 'i_antall_i_fjor': 23348.0, 'm_sum_i_fjor': 9836933.0, 'm_max_i_fjor': 100000.0, 'n_prosent_sum': -16.38, 'n_prosent_antall': -23.36, 'i_antall': -23.36}
    sales_goal = 60000000

    while True:
        lcd.blink(False)
        if button_left.is_pressed():
            

            lcd.message('Henter tall')
            lcd.set_cursor(0, 1)
            lcd.message('Vennligst vent.')
            time.sleep(4)
            print("Waiting for Profoundo-data")
            profundo_data = get_profundo_data()
            print("Profoundo-data revieved")
            achived_target = round((profundo_data['m_sum_i_aar'] / sales_goal) * 100)
            yoy_growth = profundo_data['n_prosent_sum']
            lcd.clear()
            lcd.message('Talla er inne')
            lcd.set_cursor(0, 1)
            lcd.message('Viser resultater')
            print(profundo_data)
            show_on_tower(achived_target)
            show_on_gauge(yoy_growth)
            lcd.clear()
            lcd.message('Er du happy?')
            print("Tower and gaughe is updated")
            time.sleep(10)
            lcd.clear()
            
            
            show_on_tower(0)
            show_on_gauge(0)
            print("Tower and gaughe is reset to zero")
        if button_right.is_pressed():

            show_on_tower(0)
            show_on_gauge(0)
    
def initialize_sensor(port, attempts=5, delay=5):
    while attempts > 0:
        try:
            sensor = ForceSensor(port)
            return sensor
        except BuildHATError:
            attempts -= 1
            time.sleep(delay)  # Wait for 5 seconds before retrying
    raise  # Re-raise the last exception after all attempts fail

      
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
