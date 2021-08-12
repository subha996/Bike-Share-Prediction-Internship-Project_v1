# creating class to get weather info through latitude and longitude 
import requests, json
from setup_log import setup_logger
from api_class.ipinfo_py import LatLon
# creating log file
log = setup_logger.setup_logger(logger_name="openweatherapi_log", log_file='log_files\openweather_class.log')

# creating class
class OpenWeather():
    def __init__(self):
        try:
            log.info('Initializing OpenWeather Class')
            try:
                # crceating instance of LatLon class
                latlon = LatLon()
                # getting the lat and lon from the user location
                self.lat, self.lon = latlon.get_latlon()
                log.info("Success to get latlon from LatLon class")
            except Exception as e:
                log.info("Failed to recieve lat lon form ipinfo class " + str(e))
            # seetting up the api key for the weather api
            self.api = "APIs key here" # privete api key
            self.url = "https://api.openweathermap.org/data/2.5/weather?" + "lat=" + str(self.lat) + "&lon="+ str(self.lon) +  "&units=metric" + "&appid=" + self.api
            # getting responce form weather api
            try:
                log.info("Starting connection to openweathermap.org")
                self.res = requests.get(self.url).json()
                log.info("Success to get response from openweathermap.org")
            except Exception as e:
                log.error("Error in connection to openweathermap.org:- " + str(e))
                raise Exception("Error in connection to openweathermap.org:- " + str(e))

        except Exception as e:
            log.info("Error at OpenWeather class initilization:- " + str(e))

    def get_weathersit(self):
        """Fuction to get weathersit information form weatherapi"""
        try:
            log.info("Getting weathersit from requests")
            weather_sit = self.res['weather'][0]['main'] # weather_sit from response e.g Clear
            log.info("Success to get weathersit from requests")
            return weather_sit
        except Exception as e:
            log.error("Error in getting weathersit from requests:- " + str(e))

    def get_temp(self):
        """Fuction to get temp information form weatherapi"""
        try:
            log.info("Getting temp from requests")
            temp = self.res['main']['temp'] # getting temp from the response e.g 31
            log.info("Success to get temp from requests")
            return temp
        except Exception as e:
            log.error("Error in getting temp from requests:- " + str(e))

    def get_feels_like(self):
        """Fuction to get feels_like information form weatherapi"""
        try:
            log.info("Getting feels_like from requests")
            feels_like = self.res['main']['feels_like'] # feels like temp from response e.g 39
            log.info("Success to get feels_like from requests")
            return feels_like
        except Exception as e:
            log.error("Error in getting feels_like from requests:- " + str(e))

    def get_humidity(self):
        """Fuction to get humidity information form weatherapi"""
        try:
            log.info("Getting humidity from requests")
            humidity = self.res['main']['humidity'] # humidity from response e.g 70
            log.info("Success to get humidity from requests")
            return humidity
        except Exception as e:
            log.error("Error in getting humidity from requests:- " + str(e))

    def get_wind_speed(self):
        """Fuction to get wind speed information form weatherapi"""
        try:
            log.info("Getting wind speed from requests")
            wind_speed = self.res['wind']['speed'] # wind speed from response e.g 2.1
            log.info("Success to get wind speed from requests")
            return wind_speed
        except Exception as e:
            log.error("Error in getting wind speed from requests:- " + str(e))

    def get_country(self):
        """Fuction to get country information form weatherapi"""
        try:
            log.info("Getting country from requests")
            country = self.res['sys']['country'] # country from response e.g IN
            log.info("Success to get country from requests")
            return country
        except Exception as e:
            log.error("Error in getting country from requests:- " + str(e))

    def get_loc_name(self):
        """Fuction to get location name from weatherapi"""
        try:
            log.info("Getting location name from requests")
            loc_name = self.res['name'] # location name from response e.g Madhyamgram
            log.info("Success to get location name from requests")
            return loc_name
        except Exception as e:
            log.error("Error in getting location name from requests:- " + str(e))
