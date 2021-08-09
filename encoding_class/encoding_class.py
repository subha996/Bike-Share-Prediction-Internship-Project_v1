# creating encoding class to feed to the model
# creating class to encoding the input data for the model
import datetime
from datetime import datetime
from api_class.openweather_class import OpenWeather
from setup_log import setup_logger

# creating logger instance
log = setup_logger.setup_logger(logger_name="encoding_log", log_file='log_files\encoding_class.log')


# creating the class
class Encoding():
    def __init__(self):
        self.today = datetime.today()
        # creating openweather class instance
        self.ow = OpenWeather()

    # first feature
    def get_season_manually(self, season): # season name (dropdown menu)
        """Function to get the manually seaosn input"""
        try:
            log.info("Returning Manually season output")
            if season=="Spring":
                return 1
            elif season=='Summer':
                return 2
            elif season=='Fall':
                return 3
            elif season=='Winter':
                return 4
        except Exception as e:
            log.info("Failed to return Manually season output:- " + str(e))

    def get_season_auto(self):
        """Function to get the auto season output"""
        # creating a list of months accroding to the season
        spring = [3, 4, 5] # each list element are represnting the month number
        summer = [6, 7, 8]
        fall = [9, 10, 11]   
        winter = [12, 1, 2]
        # getting the current month
        try:
            log.info("Returning the season in automatic option")
            current_month = self.today.month
            if current_month in spring:
                return 1
            elif current_month in summer:
                return 2
            elif current_month in fall:
                return 3
            elif current_month in winter:
                return 4
        except Exception as e:
            log.info("Failed to return the season in automatic option:- " + str(e))


    # second feature
    def get_month_manually(self, month): # month name (dropdown menu)
        """Function to return current monthe in mannualy options"""
        try:
            log.info("Returning Manually month output")
            if month=="January":
                return 1
            elif month=='February':
                return 2
            elif month=='March':
                return 3
            elif month=='April':
                return 4
            elif month=='May':
                return 5
            elif month=='June':
                return 6
            elif month=='July':
                return 7
            elif month=='August':
                return 8
            elif month=='September':
                return 9
            elif month=='October':
                return 10
            elif month=='November':
                return 11
            elif month=='December':
                return 12
        except Exception as e:
            log.info("Failed to return Manually month output:- " + str(e))

    def get_month_auto(self):
        """Function to return the current month in automatic way"""
        try:
            log.info("Returning Current month auto options")
            current_month = self.today.month # return current month numnber, e.g 8
            return current_month
        except Exception as e:
            log.info("Failed to return Current month auto options:- " + str(e))

    # third feature
    def get_weekday_manually(self, day): # day name(dropdown menu)
        """Function to return the weekday in manually options"""
        try:
            log.info("Returning the week day for manually options")
            if day=="Monday":
                return 0
            elif day=='Tuesday':
                return 1
            elif day=='Wednesday':
                return 2
            elif day=='Thursday':
                return 3
            elif day=='Friday':
                return 4
            elif day=='Saturday':
                return 5
            elif day=='Sunday':
                return 6
        except Exception as e:
            log.info("Failed to return the week day for manually options:- " + str(e))

    def get_weekday_auto(self):
        """Function to return weekday in auto options"""
        day = self.today.weekday() # return week day number, e.g 0 for Monday, 1 for Tuesday, so on...
        return day

    # fourth feature
    def get_workingday_manually(self, day): # yes or no (dropdown menu)
        """Function to return working day or not in manually options"""
        try:
            log.info("Returning the working day for manually options")
            if day == "Yes":
                return 1 # when yes then return 1
            elif day == "No": 
                return 0 # in case of no return 0
        except Exception as e:
            log.info("Failed to return the working day for manually options:- " + str(e))

    def get_workingday_auto(self):
        """Function to return working day or not in auto options"""
        try:
            log.info("Returning the working day for auto options")
            day = self.today.weekday()
            if day<5: # saterday(5), sunday(6) are not working days
                return 1
            else:
                return 0 # return 0 for saterday, sunday.
        except Exception as e:
            log.info("Failed to return the working day for auto options:- " + str(e))

    # fifth feature
    def get_weathersit_manually(self, weather): # dropdown menu
        """Function to return the weathersit in manually options"""
        try:
            log.info("Returning the weathersit for manually options")
            if weather=="Clear":
                return 1
            elif weather=='Clouds':
                return 2
            elif weather=='Rain':
                return 3
        except Exception as e:
            log.info("Failed to return the weathersit for manually options:- " + str(e))

    def get_weathersit_auto(self):
        """Function to return weathersit in auto options"""
        try:
            log.info("Returning the weathersit for auto options")
            
            # getting the weather data
            weather_data = self.ow.get_weathersit()
            # creating list for possible outcome from weather api
            automos = ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado", "Rain"] 
            if weather_data in automos:
                return 3
            elif weather_data == "Clear":
                return 1
            elif weather_data == "Clouds":
                return 2
            elif weather_data == "Drizzle":
                return 3
            elif weather_data == "Snow":
                return 3

            return weather_data # return the weather data e.g Clear, Rain
        except Exception as e:
            log.info("Failed to return the weathersit for auto options:- " + str(e))

    # sixth feature
    def get_temp_manually(self, temp): # input section to get float number in celcius
        """Function to get the Temperature form the api"""
        try:
            log.info("Returning the Temperature for manually options")
            if type(temp)!=float or type(temp)!=int: # validation part
                log.info("Bad temp input has passed")
                raise ValueError
            log.info("Returning the normalize temperature")
            return temp/41 # return the normalize temp in celcius 

        except Exception as e:
            log.info("Failed to return the temperature value")

    def get_temp_auto(self):
        """Function to return the temperature in auto options"""
        try:
            log.info("Returning the Temperature for auto options")
            # getting the weather data
            temp = self.ow.get_temp()
            return temp/41 # return the normalize temp in celcius
        except Exception as e:
            log.info("Failed to return the temperature value:- " + str(e))

    # seventh feature
    def get_feelslike_manually(self, temp): # input section to get float number in celcius
        """Function to get the Feels like Temperature form the api"""
        try:
            log.info("Returning the Feels like Temperature for manually options")
            if type(temp)!=float or type(temp)!=int: # validation part  
                log.info("Bad temp input has passed")
                raise ValueError
            atemp = self.ow.get_feels_like()
            return atemp/50 # retrun normalize actual temp in celcius
        except Exception as e:
            log.info("Failed to return the Feels like Temperature value:- " + str(e))

    def get_feelslike_auto(self):
        """Function to return the Feels like Temperature in auto options"""
        try:
            log.info("Returning the Feels like Temperature for auto options")
            # getting the weather data
            temp = self.ow.get_feels_like()
            return temp/50 # return the normalize temp in celcius
        except Exception as e:
            log.info("Failed to return the Feels like Temperature value:- " + str(e))

    # eighth feature
    def get_humidity_manually(self, hum): # input section to get float number or int
        """Function to get the Humidity form the api"""
        try:
            log.info("Returning the Humidity from the api")
            if type(hum)!=float and type(hum)!=int: # validation part
                log.info("Bad humidity input has passed")
                raise ValueError
            return hum/100 # return the normalize humidity
        except Exception as e:
            log.info("Failed to return the humidity value:- " + str(e))

    def get_humidity_auto(self):
        """Function to return the humidity in auto options"""
        try:
            log.info("Returning the Humidity from the api")
            # getting the weather data
            hum = self.ow.get_humidity()
            return hum/100 # return the normalize humidity
        except Exception as e:
            log.info("Failed to return the humidity value:- " + str(e))
        
    # ninth feature
    def get_wind_manually(self, wind): # input section to get float number or int
        """Function to get the Wind form the api"""
        try:
            log.info("Returning the Wind from the api")
            if type(wind)!=float and type(wind)!=int: # validation part
                log.info("Bad wind input has passed")
                raise ValueError
            return wind/67 # return the normalize wind
        except Exception as e:
            log.info("Failed to return the wind value:- " + str(e))

    def get_wind_auto(self):
        """Function to return the wind in auto options"""
        try:
            log.info("Returning the Wind from the api")
            # getting the weather data
            wind = self.ow.get_wind_speed()
            return wind/67 # return the normalize wind
        except Exception as e:
            log.info("Failed to return the wind value:- " + str(e))

        

    





