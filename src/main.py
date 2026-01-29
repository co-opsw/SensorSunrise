import lcdtext
import weather

from datetime import datetime
import threading


def fetch_weather():
    """Runs in the background, fetching and storing the days weather data at 4am"""

    while True:
        try:
            current_time = datetime.now().time
            if current_time.hour() == 4 and current_time.minute == 0:
                weather.retrieve_weather_data()
        except Exception:
            print(Exception)
