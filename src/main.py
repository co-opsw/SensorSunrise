import lcdtext
import fetchweather

from datetime import datetime
from time import sleep
import threading

def fetch_weather():
    """Runs in the background, fetching and storing the days weather data at 4am"""
    weather_fetched_today = False
    weather_fetch_time = (18, 49)

    while True:
        try:
            current_time = datetime.now().time()
            
            if (current_time.hour == weather_fetch_time[0] and current_time.minute == weather_fetch_time[1]) and not weather_fetched_today:
                fetchweather.retrieve_weather_data()
                weather_fetched_today = True
                
            elif current_time.hour == weather_fetch_time[0] and current_time.minute == (weather_fetch_time[1] + 1):
                weather_fetched_today = False
                
        except Exception as e:
            print(f"Weather fetch error: {e}")


def main():
    weather_thread = threading.Thread(target=fetch_weather, daemon=True)
    
    weather_thread.start()
    
    while True:
        sleep(1)


if __name__ == "__main__":
    try:
        print("Starting SensorSunrise...")
        main()
    except KeyboardException:
        pass
    finally:
        print("Stopping SensorSunrise...")
        