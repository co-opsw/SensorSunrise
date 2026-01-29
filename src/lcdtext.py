import smbus
from time import sleep
from datetime import datetime

import loggersetup

logger = loggersetup.logger_setup("fetchweather.log")

from LCD1602 import CharLCD1602

lcd_screen = CharLCD1602()


def loop_x(message, x, y):
    lcd_screen.init_lcd()
    count = 0

    while True:
        lcd_screen.clear()
        lcd_screen.write(count, 0, message)

        sleep(1)

        if count > 15:
            count = 0
        else:
            count += 1


def destroy():
    print("Turning off LCD Screen...")
    lcd_screen.clear()


if __name__ == "__main__":
    print("LCD Screen is starting up...")

    try:
        loop()

    except KeyboardInterrupt:
        destroy()
