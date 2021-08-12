# creating a class to send data to the database DataStaxAstra(cassandra)

import cassandra
# print(cassandra.__version__) # checking for the version or cassandra library
from setup_log import setup_logger

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# setting up log
log = setup_logger.setup_logger('dbSend', log_file='log_files/CDB.log')

class CDB(): # creating a class CDB: Cassandra DataBase
    def __init__(self):
        try:
            # connecting to the database
            log.info('Connecting to cassandra database')
            self.cloud_config= {
                            'secure_connect_bundle': 'DBSend/secure-connect-database1.zip'
                        } 
            self.auth_provider = PlainTextAuthProvider(<privet key here>)
            self.cluster = Cluster(cloud=self.cloud_config, auth_provider=self.auth_provider)
            self.session = self.cluster.connect()
            self.row = self.session.execute("select release_version from system.local").one()
            if self.row:
                log.info('Connected to cassandra database Successfull: ' + str(self.row[0]))
            else:
                log.error('Connection to cassandra database failed')
        except Exception as e:
            log.info('Error connecting to cassandra database: ' + str(e))

        try:
            log.info("Opening primary key text file to read primary key")
            with open("DBSend/primary_key.txt", "r") as fr:
                self.primary_key = int(fr.read())
                log.info("Primary key: " + str(self.primary_key))
                fr.close()
        except Exception as e:
            log.info("Error opening primary key text file: " + str(e))


        
    def data_send(self, mode, season, month,weekday,working_day,weathersit,temp,atemp,hum,wind_speed, casual_cust, regis_cust, total):
        """Function that will data to the database"""
        try:
            log.info("Sending data to the database")
            # creating list of values
            val = [self.primary_key, mode, season, month,weekday,working_day,weathersit,temp,atemp,hum,wind_speed, casual_cust, regis_cust, total]
            pre = self.session.prepare("insert into bike_share.data_info(id,mode,season, month,weekday,working_day,weathersit,temp,atemp,hum,wind_speed, casual_cust, regis_cust, total) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            self.session.execute(pre.bind(val))
            log.info("Data sent to the database")
        except Exception as e:
            log.info("Error sending data to the database: " + str(e))


    def update_primarykey(self):
        """Funtcion that will update the primary key frequently"""
        try:
            # updating primary key by 1
            self.primary_key = self.primary_key + 1
            # writing the primary key to the text file
            with open("DBSend/primary_key.txt", "w") as fw:
                fw.write(str(self.primary_key))
                fw.close()
                log.info("Primary key updated " + str(self.primary_key))
        except Exception as e:
            log.info("Error updating primary key: " + str(e))
