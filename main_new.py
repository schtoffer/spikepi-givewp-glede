# Imports
from time import sleep

# Import my own packages
from functions.api import get_profundo_data
from functions.spike_functions import *
from functions.lcd import *

# Get data from Profundo

# Initialize the LCD display
lcd = initialize_lcd()

# Initialize BuildHAT
button_left = initialize_sensor('C')

# Print idle message
welcome_message(lcd)

def main():
    # Initialize the Buildhat
    while True:
      
        if button_left.is_pressed() == True:

            # Print to the LCD
            info_message(lcd)
            # data = get_profundo_data()
            data = {'i_antall_i_aar': 32291.0, 'm_sum_i_aar': 13821941.0, 'm_max_i_aar': 317000.0, 'i_antall_i_fjor': 36586.0, 'm_sum_i_fjor': 15474086.0, 'm_max_i_fjor': 100000.0, 'n_prosent_sum': -10.68, 'n_prosent_antall': -11.74, 'i_antall': -11.74}
            sleep(2)

            # Run motor_gauge
            show_on_gauge(data['n_prosent_sum'])
            lcd.set_cursor(0, 1)
            lcd.clear()
            lcd.message(f"Aarlig utvikling:")
            lcd.set_cursor(0, 1)
            lcd.message(f"{data['n_prosent_sum']} %")
            sleep(5)
            lcd.clear()

            # Revert back to idle message
            welcome_message(lcd)
        sleep(0.2)




if __name__ == "__main__":
    main()
