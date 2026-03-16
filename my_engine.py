from pymongo import MongoClient
from logger import log_event

client = MongoClient("mongodb://localhost:27017/")
db = client["hunter_db"]
collection1 = db["stations"]
collection2 = db["measurements"]

def add_station(id,lat,lon):
    station_document = {"id":id , "lat":lat , "lon":lon}
    db.collection1.insert_one(station_document)
    print(f"{id} saved succeesfuly")


data_station = db.collection1.find_one({id})

if data_station:
    