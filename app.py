from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("flight_rf.pkl", "rb"))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
     
    # Airline
    Airline = request.form["Airline"]
    a = ["Air Asia", "Air India", "GoAir", "IndiGo", "Jet Airways",
     "Jet Airways Business", "Multiple carriers", "Multiple carriers Premium economy",
       "SpiceJet", "Trujet", "Vistara", "Vistara Premium economy"]

    for i in range(len(a)):
        if a[i] == Airline:
            a[i] = 1
        else:
            a[i] = 0
            
    # Destination
    destination = request.form["Destination"]
    d = ["Banglore", "Cochin", "Delhi","Hyderabad", "Kolkata", "New Delhi"]

    for i in range(len(d)):
        if d[i] == destination:
            d[i] = 1
        else:
            d[i] = 0

    # Source
    source = request.form["Source"]
    s = ["Banglore", "Chennai", "Delhi", "Kolkata", "Mumbai"]

    for i in range(len(s)):
         if s[i] == source:
             s[i] = 1
         else:
             s[i] = 0

    # Stops
    stops = int(request.form["stops"])

    # Departure date
    dep_date = request.form["date_of_dep"]
    dep_day = int(str(dep_date).split("-")[0])
    dep_month =int(str(dep_date).split("-")[1])


    # departure time
    dep_time = request.form["dep_time"]
    dep_hour = int(str(dep_time).split(":")[0])
    dep_minute = int(str(dep_time).split(":")[1])

    # arrival time
    arr_time = request.form["arr_time"]
    arr_hour = int(str(arr_time).split(":")[0])
    arr_minute = int(str(arr_time).split(":")[1])

    # variables for prediction
    values = [[stops,
    dep_day,
    dep_month,
    dep_hour,
    dep_minute,
    arr_hour,
    arr_minute,
    a[i],
    s[i],
    d[i]
    ]]

    # prediction
    prediction = model.predict(values)
    output=(prediction)

    # returning the results to the home.html
    return render_template("home.html", pred = "Flight ticket price is RS{}" .format(output))

if __name__ == "__main__":
    app.run(debug = True)
