from logging import lastResort
from flask import Flask, render_template, request
from flask_cors import cross_origin
import joblib
import numpy as np
from setup_log import setup_logger
from encoding_class.encoding_class import Encoding
from DBSend.dbSend import CDB


# setting up logger file
log = setup_logger.setup_logger(logger_name="flask_log",log_file="log_files/flask_api_log.log")
# loading the model
model = joblib.load('model/rnd_rfst_multioutput_71_r2.pkl')

# creating encoding class instance
enc = Encoding()

# cassanda send data from webpage 
# creating cassandra class instance
cdb = CDB()

# creating flask app instance
app = Flask(__name__) 

@app.route('/', methods=['GET'])
# @cross_origin()
def homePage():
    log.info("---------------Home Page Have Shown --------------")
    return render_template('index.html') 


# creating the prediction manually api
@app.route('/predict-manually', methods=["GET","POST"])
# @cross_origin()
def predictManually():
    try:
        log.info("User Choose Predict Manually")
        # getting the data from the webpage
        season = request.form['season']
        # season_enc = enc.get_season_manually(season)
        log.info("1. Season : %s",season)
        month = request.form['month']
        # month_enc = enc.get_month_manually(month)
        log.info("2. Month : %s",month)
        weekday = request.form['weekday']
        # weekday_enc = enc.get_weekday_manually(weekday)
        log.info("3. Weekday : %s",weekday)
        workingday = request.form['workingday']
        # workingday_enc = enc.get_workingday_manually(workingday)
        log.info("4. Working Day : %s",workingday)
        weathersit = request.form['weathersit']
        log.info("5. Weather Site : %s",weathersit)
        temp = request.form['temp']
        log.info("6. Temperature : %s",temp)
        atemp = request.form['atemp']
        log.info("7. Air Temperature : %s",atemp)
        hum = request.form['hum']
        log.info("8. Humidity : %s",hum)
        windspeed = request.form['windspeed']
        log.info("9. Wind Speed : %s",windspeed)
        log.info("Finished taking Input from user")
        # creating data for prediction from above inputs
        log.info("Creating array and doing the prediction")
        data = np.array([[season,month,weekday,workingday,weathersit,temp,atemp,hum,windspeed]])
        pred = model.predict(data)
        log.info("Prediction done Showing the Result")
        log.info("Sending data to Database")
        cdb.data_send("Manually", float(season), 
                        float(month), 
                        float(weekday), 
                        float(workingday),
                         float(weathersit), 
                         float(temp), 
                         float(atemp), 
                         float(hum), 
                         float(windspeed),
                         pred[0][0], 
                         pred[0][1], 
                         pred[0][0]+pred[0][1])
        log.info("Data Sent to Database")
        cdb.update_primarykey()
        log.info("Primary Key Updated")
        log.info("Data Sent to Database")
        return render_template("results.html", 
                                Casual=str(round(pred[0][0],0)),
                                Registered=str(round(pred[0][1],0)), 
                                Total=str(round(pred[0][0]+pred[0][1],0)))
    except Exception as e:
        log.info("Error in Predicti Manually methode" + str(e)) 
        return render_template ("Error_manually.html")    



# creating the prediction automatically api
@app.route('/predict-automatically', methods=['POST'])
# @cross_origin()
def predictAutomatically():
    try:
        log.info("User Choose Automatic Way")
        # getting the data from the API
        season = enc.get_season_auto()
        log.info("1. Season : %s",season)
        month = enc.get_month_auto()
        log.info("2. Month : %s",month)
        weekday = enc.get_weekday_auto()
        log.info("3. Weekday : %s",weekday)
        workingday = enc.get_workingday_auto()
        log.info("4. Working Day : %s",workingday)
        weathersit = enc.get_weathersit_auto()
        log.info("5. Weather Site : %s",weathersit)
        temp = enc.get_temp_auto()
        log.info("6. Temperature : %s",temp)
        atemp = enc.get_feelslike_auto()
        log.info("7. Air Temperature : %s",atemp)
        hum = enc.get_humidity_auto()
        log.info("8. Humidity : %s",hum)
        windspeed = enc.get_wind_auto()
        log.info("9. Wind Speed : %s",windspeed)
        log.info("Finished taking Input from user")
        # creating data for prediction from above inputs
        log.info("Creating array and doing the prediction")
        data = np.array([[season,month,weekday,workingday,weathersit,temp,atemp,hum,windspeed]])
        try:
            pred = model.predict(data) # doing the predicton with captured location data
            log.info("Prediction done, Showing the Result")
        except Exception as e:
            log.info("Error in Predict Automatically methode While doing prediction: " + str(e))
            return render_template("Error_automatic.html") # showing the error page for api error
        log.info("Sending data to Database")
        cdb.data_send("Automatically", 
                        season, 
                        month, 
                        weekday,
                         workingday, 
                         weathersit, 
                         temp, atemp, 
                         hum, 
                         windspeed, 
                         pred[0][0], 
                         pred[0][1], 
                         pred[0][0]+pred[0][1])
        log.info("Data Sent to Database")
        cdb.update_primarykey()
        log.info("Primary Key Updated")
        return render_template("results.html", 
                                Casual=str(round(pred[0][0],0)),
                                Registered=str(round(pred[0][1],0)), 
                                Total=str(round(pred[0][0]+pred[0][1],0)))
    except Exception as e:
        log.info("Error in Predict Automatically methode: " + str(e))


# creating contributor page 
@app.route('/Contributer', methods=['POST'])
# @cross_origin()
def contributor():
    try:
        log.info("Showing the Contributor page")
        return render_template("conttributer.html")
    except Exception as e:
        log.info("Error in showing the contributor page " + str(e))


# running the flask app       
if __name__ == '__main__':
    app.run(debug=True)