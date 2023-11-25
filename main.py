# Imports
from time import sleep

# Import my own packages
from functions.api import get_profundo_data
from functions.spike_functions import *
from functions.lcd import *

sleep(10)

# Constants
sales_goal = 60000000

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
      
        if button_front.is_pressed() == True:

            # Inform the user
            info_message(lcd)

            # Get data
            data = get_profundo_data()
            # sleep(1)
            # data = {'i_antall_i_aar': 32291.0, 'm_sum_i_aar': 13821941.0, 'm_max_i_aar': 317000.0, 'i_antall_i_fjor': 36586.0, 'm_sum_i_fjor': 15474086.0, 'm_max_i_fjor': 100000.0, 'n_prosent_sum': -10.68, 'n_prosent_antall': -11.74, 'i_antall': -11.74}
            
            # Inform the user
            lcd.clear()
            lcd.message(f"Resultatene")
            lcd.set_cursor(0, 1)
            lcd.message(f"er inne")
            sleep(3)

            # Run motor_gauge
            # show_on_gauge(data['n_prosent_sum'])

            # Run motor_tower
            achived_target = round((data['m_sum_i_aar'] / sales_goal) * 100)
            show_on_tower(achived_target)

            # Show results on display
            lcd.clear()
            lcd.message(f"Totalt innsamlet:")
            lcd.set_cursor(0, 1)
            lcd.message(f"{data['m_sum_i_aar']:,.0f}".replace(',', ' '))
            sleep(8)
            lcd.clear()

            # Revert back to idle message
            idle_message(lcd)

        if button_back.is_pressed() == True:
            lcd.clear()
            lcd.message('Tilbakestiller')
            lcd.set_cursor(0, 1)
            lcd.message("motorer")
            show_on_tower(0)
            # show_on_gauge(0)

            welcome_message(lcd)
        
        sleep(0.2)




if __name__ == "__main__":
    main()
