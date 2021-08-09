# creating class to get user information for 
from requests import get
from datetime import datetime
from setup_log import setup_logger

# setting up logger
log = setup_logger.setup_logger("user_info_class", 'DBSend/user_info.log')

# creating the class
class UserInfo():
    def __init__(self):
        try:
            log.info("UserInfo Class Initilization Started")
            log.info("Connectiing to ipapi.co")
            self.res = get('https://ipapi.co/json/').json()
            log.info("Connected to ipapi.co Successful")
            self.now = datetime.now()
            self.time = self.now.strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            log.error("Error in UserInfo Class Initilization " + str(e))

    def get_info(self):
        """Function to return the user public IP and other information"""
        try:
            log.info("UserInfo Class get_info() Started")
            ip = self.res['ip']
            city = self.res['city']
            region = self.res['region']
            country = self.res['country']
            postal = self.res['postal']
            lat = self.res['latitude']
            lon = self.res['longitude']
            time_zone = self.res['timezone']
            country_call_code = self.res['country_calling_code']
            currency = self.res['currency']
            log.info("User Information Collected")
            info = [ip, city, region, country, postal, lat, lon, time_zone, country_call_code, currency, self.time]
            return list(info)

        except Exception as e:
            log.error("Error in UserInfo Class get_info() " + str(e))
     
            

            
    