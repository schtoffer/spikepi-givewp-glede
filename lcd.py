import time
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


lcd.blink(False)

lcd.message('Sist oppdatert:')
lcd.set_cursor(0, 1)
lcd.message('22. nov kl 22:22')
time.sleep(5)
lcd.clear()
lcd.message('test')
#lcd.message('Thanks \Mechatronics')

time.sleep(2)
lcd.clear()