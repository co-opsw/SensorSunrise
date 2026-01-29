import openmeteo_requests
from retry_requests import retry

import numpy

import os
from dotenv import load_dotenv

load_dotenv()

import storedata
import loggersetup

logger = loggersetup.logger_setup("fetchweather.log")


def weather_data_from_api():

    # Setup the Open-Meteo API client with retry on error
    retry_session = retry(retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 51.4888,
        "longitude": -3.177,
        "hourly": [
            "temperature_2m",
            "precipitation_probability",
            "precipitation",
            "visibility",
            "wind_speed_10m",
            "relative_humidity_2m",
        ],
        "timezone": os.getenv("LOCATION"),
        "wind_speed_unit": "mph",
        "forecast_days": 1,
    }
    return openmeteo.weather_api(url, params=params)


def format_hourly_data(data):
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = data.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy().tolist()
    hourly_precipitation_probability = hourly.Variables(1).ValuesAsNumpy().tolist()
    hourly_precipitation = hourly.Variables(2).ValuesAsNumpy().tolist()
    hourly_visibility = hourly.Variables(3).ValuesAsNumpy().tolist()
    hourly_wind_speed_10m = hourly.Variables(4).ValuesAsNumpy().tolist()
    hourly_relative_humidity_2m = hourly.Variables(5).ValuesAsNumpy().tolist()

    json_data = {}
    variables = [
        ["temperature", hourly_temperature_2m],
        ["precipitation_probability", hourly_precipitation_probability],
        ["precipitation", hourly_precipitation],
        ["visibility", hourly_visibility],
        ["wind_speed", hourly_wind_speed_10m],
        ["relative_humidity", hourly_relative_humidity_2m],
    ]

    for hour in range(len(hourly_temperature_2m)):
        hourly_data = {}
        for variable in variables:
            hourly_data[variable[0]] = variable[1][hour]

        json_data[f"hour_{hour}"] = hourly_data

    return json_data


def retrieve_weather_data():

    logger.info("Fetching weather data...")

    responses = weather_data_from_api()
    json_data = {}
    response = responses[0]

    json_data["coordinates"] = {
        "latitude": response.Latitude(),
        "longitude": response.Longitude(),
    }
    json_data["elevation"] = response.Elevation()
    json_data["timezone"] = response.Timezone().decode("utf-8")

    json_data["hourly_data"] = format_hourly_data(response)

    # How to store data
    storedata.store_json_data(json_data, "weather_data")


# Uncomment if working on individual development of this file
# if __name__ == "__main__":
# retrieve_weather_data()
