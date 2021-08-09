# class that will be used to get the information from the ipinfo.io website
import ipinfo
from setup_log import setup_logger
# token = "7269b8c71f592f" # my privet token

# setting up log File
log = setup_logger.setup_logger(logger_name="ipinfo_py", log_file='log_files\ipinfo_class.log')

# creating a class to get lat and log
class LatLon():
    def __init__(self):
        try:
            log.info("Connecting to ipinfo api")
            # connection to ipinof api through the api token
            self.token = "7269b8c71f592f" # my secret token
            self.handler = ipinfo.getHandler(self.token)
            self.res = self.handler.getDetails()
            log.info("Connection to ipinfo api successful")
        except Exception as e:
            log.info("Connection to ipinfo api FAILED:- " + str(e))
          

    def get_latlon(self):
        """Function will return Latitude and Longitude"""
        try:
            log.info("Getting Latitude and Longitude")
            # getting the latitude and longitude from the ipinfo api
            lat = self.res.latitude
            lon = self.res.longitude
            return lat, lon
        except Exception as e:
            log.info("Failed to returning Latitude Longitude:- " + str(e))
