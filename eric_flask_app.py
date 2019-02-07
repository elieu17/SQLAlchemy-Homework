# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:21:04 2019

@author: Eric
"""

from flask import Flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector = inspect(engine)
inspector.get_table_names()


prcp_data = pd.read_csv("precipitation.csv")
prcp_dict = prcp_data.to_dict('records')

station_data = pd.read_csv("stations.csv")
station_dict = station_data.to_dict('records')

tobs_data = pd.read_csv("tobs.csv")
tobs_dict = tobs_data.to_dict('records')

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to my Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs_dict)

if __name__ == "__main__":
    app.run(debug=True)
    


