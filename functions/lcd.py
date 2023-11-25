import Adafruit_CharLCD as LCD
from time import sleep

# Define GPIO pins
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

# Other constant variables
sleep_time = 1

def initialize_lcd():
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    lcd.blink(False)  # Set blink to False upon initialization
    return lcd

def welcome_message(lcd):
    lcd.clear()
    lcd.blink(False)  # Set blink to False upon initialization
    lcd.message('Trykk på knappen')
    lcd.set_cursor(0, 1)
    lcd.message('for resultater')

def info_message(lcd):
    lcd.clear()
    lcd.message('Henter')
    lcd.set_cursor(0, 1)
    lcd.message("ferske data")