# Imports
from time import sleep

# Import my own packages
from functions.api import get_profundo_data
from functions.spike_functions import *
from functions.lcd import *
from functions.ip import *

sleep(1)

# Constants
sales_goal = 58200000

# Initialize the LCD display
lcd = initialize_lcd()

# Initialize BuildHAT
button_front = initialize_sensor('C')
button_back = initialize_sensor('D')

# Print idle message
welcome_message(lcd)

def main():

    # Initialize the Buildhat
    while True:
        
        # Fetching and showing result to the user

        if button_front.is_pressed() == True:

            # Inform the user that we are fetching the data, please wait
            info_message_fetching(lcd)

            # Get data
            data = get_profundo_data()
            # sleep(1)
            # data = {'i_antall_i_aar': 32291.0, 'm_sum_i_aar': 13821941.0, 'm_max_i_aar': 317000.0, 'i_antall_i_fjor': 36586.0, 'm_sum_i_fjor': 15474086.0, 'm_max_i_fjor': 100000.0, 'n_prosent_sum': -10.68, 'n_prosent_antall': -11.74, 'i_antall': -11.74}
            
            # Inform the user that the results are ready
            info_message_ready(lcd)
            info_message_motor(lcd)
            sleep(1)

            # Run motor_tower
            achived_target = round((data['m_sum_i_aar'] / sales_goal) * 100)
            show_on_tower(achived_target)
            #print(achived_target)

            # Show results on display
            results_message(lcd, f"{data['m_sum_i_aar']:,.0f}".replace(',', ' '))
            results_message_percent(lcd, achived_target)

            # Runn motor_tower back to 0
            show_on_tower(0)

            # Revert back to idle message
            lcd.clear()
            welcome_message(lcd)

        if button_back.is_pressed() == True:
            sleep(3)
            if button_back.is_pressed() == True:
                info_ip_adresse(lcd, get_ip_address())
            else:
                info_mesage_resetting(lcd)
                show_on_tower(0)

        sleep(0.1)

if __name__ == "__main__":
    main()
