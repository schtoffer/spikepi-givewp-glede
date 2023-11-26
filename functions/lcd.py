import Adafruit_CharLCD as LCD
import time

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

# Define custom characters

custom_char_æ = [
    0b00000,
    0b00000,
    0b01110,
    0b00001,
    0b01111,
    0b10001,
    0b01111,
    0b00000
]

custom_char_ø = [
    0b00000,
    0b00000,
    0b01110,
    0b10011,
    0b10101,
    0b11001,
    0b01110,
    0b00000
]

custom_char_å = [
    0b00100,
    0b01010,
    0b00100,
    0b01110,
    0b10001,
    0b10001,
    0b01111,
    0b00000
]
def initialize_lcd():
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    lcd.blink(False)  # Set blink to False upon initialization

    # Create and store the custom characters
    lcd.create_char(2, custom_char_å)
    lcd.create_char(0, custom_char_æ)
    lcd.create_char(1, custom_char_ø)

    return lcd

def welcome_message(lcd):
    lcd.clear()
    lcd.message('Trykk p\x02 den')
    lcd.set_cursor(0, 1)
    lcd.message('r\x01de knappen')

def info_message_fetching(lcd):
    lcd.clear()
    lcd.message('Henter tall')
    lcd.set_cursor(0, 1)
    lcd.message("vennligst vent")

def info_message_ready(lcd):
    lcd.clear()
    lcd.message(f"Ferske tall")
    lcd.set_cursor(0, 1)
    lcd.message(f"er inne")
    time.sleep(2)

def info_message_motor(lcd):
    lcd.clear()
    lcd.message(f"Kj\x01rer motor")

def info_mesage_resetting(lcd):
    lcd.clear()
    lcd.message('Tilbakestiller')
    lcd.set_cursor(0, 1)
    lcd.message("motorer")
    time.sleep(2)
    welcome_message(lcd)
    

def idle_message(lcd):
    lcd.clear()
    lcd.message('Sist oppdatert:')

    # Get current time and format it as '{DD}. {mmm} kl {HH:MM}'
    current_time_formatted = time.strftime("%d. %b kl %H:%M", time.localtime())

    # Convert the month name to lowercase
    current_time_formatted = current_time_formatted.lower()

    lcd.set_cursor(0, 1)
    lcd.message(current_time_formatted)

def results_message(lcd, message):
    lcd.clear()
    lcd.message(f"Totalt innsamlet:")
    lcd.set_cursor(0, 1)
    lcd.message(message)
    time.sleep(8)

def results_message_percent(lcd, percent):
    lcd.clear()
    lcd.message(f"Det er {percent}% av")
    lcd.set_cursor(0, 1)
    lcd.message("Juleaksjon 2022")
    time.sleep(6)

def info_ip_adresse(lcd, function):
    lcd.clear()
    lcd.message("IP Address:")
    lcd.set_cursor(0, 1)
    lcd.message(f"{function}")
    time.sleep(10)
    welcome_message(lcd)

