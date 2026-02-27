import lcdtext
import weather

from datetime import datetime
from time import sleep
import json
import threading


def fetch_file_contents(filename):
    """Read contents of file given"""
    with open("../data/"+filename, "r") as file:
        return file.read()
   
        
def format_weather_data(data):
    """Format the hourly weather data"""
    temp = round(weather_data.get("temperature", 0), 1)
    wind_ms = weather_data.get("wind_speed", 0)
    wind_mph = round(wind_ms * 2.237, 1)  # Convert m/s to mph
    humidity = int(weather_data.get("relative_humidity", 0))
    rain_prob = int(weather_data.get("precipitation_probability", 0))
    rain_mm = round(weather_data.get("precipitation", 0), 1)
    
    line_1 = f"{temp}°C   d  ".l

    
    


def fetch_weather():
    """Runs in the background, fetching and storing the days weather data at 4am"""
    weather_fetched_today = False
    weather_fetch_time = (4, 00)

    while True:
        try:
            current_time = datetime.now().time()

            if (
                current_time.hour == weather_fetch_time[0]
                and current_time.minute == weather_fetch_time[1]
            ) and not weather_fetched_today:
                weather.retrieve_weather_data()
                weather_fetched_today = True

            elif current_time.hour == weather_fetch_time[0] and current_time.minute == (
                weather_fetch_time[1] + 1
            ):
                weather_fetched_today = False

        except Exception as e:
            print(f"Weather fetch error: {e}")


def lcd_screen():
    """Runs the LCD screen function, to display hourly weather"""
    
    while True:
        try:
            current_time = datetime.now().time()
            current_hour = current_time.hour
            
            weather_data = json.loads(fetch_file_contents("weather_data.json"))
            
            hourly_weather_data = weather_data["hourly_data"][f"hour_{current_hour}"]
            
            print(hourly_weather_data, f"hour_{current_hour}")
            
            formatted_data = format_weather_data()
            
            #lcdtext.loop_x(
            
        except Exception as err:
            print(err)
        finally:
            sleep(300)
        
    
    # while loop
    # Find current hour using date time
    # retrieve file contents using helper function above
    # find this hours data
    # format it
    # display it on lcd
    # wait 5 mins before updating time.sleep(300)
    


def main():
    """Main handler for all threads for the program"""
    weather_thread = threading.Thread(target=fetch_weather, daemon=True)
    lcd_thread = threading.Thread(target=lcd_screen, daemon=True)

    # Fetch initial weather for day
    weather.retrieve_weather_data()
    
    # Reset LCD
    lcdtext.clear()

    weather_thread.start()
    lcd_thread.start()

    while True:
        sleep(1)


if __name__ == "__main__":
    try:
        print("Starting SensorSunrise...")
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("Stopping SensorSunrise...")
