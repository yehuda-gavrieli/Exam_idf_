from pymongo import *
import logger
import haversine

client = MongoClient("mongodb://localhost:27017/")
db = client["hunter_db"]
collection = db["hunter_data"]


def sort_by_time(document):
    return document["timestamp"]


def find_last_location(entity_id):
    all_intel_reports = []

    cursor = collection.find({"entity_id":entity_id,"signal_id":{"exists":True}})

    for document in cursor:
        all_intel_reports.append(document)

    if len(all_intel_reports) == 0:
        return 0.0,0.0
    
    all_intel_reports.sort(key=sort_by_time , reverse=True)

    latest = all_intel_reports[0]

    return latest["reported_lat"] , latest["reported_lon"]


def handle_data(data):
    entity_id = data.get("entity_id")

    if "signal_id" in data:
        old_lat,old_lon = find_last_location(entity_id)

        new_lat = data.get("reported_lat")
        new_lon = data.get("reported_lon")

        if old_lat != 0:
            distance = haversine.haversine_km(old_lat , old_lon , new_lat , new_lon)
            print(f"target {entity_id} moved {distance} km")
        else:
            print("this is the first target report", entity_id)

    elif ("result" not in data) and ("attck_id" in data):
        print("warning attck on target" , {entity_id})

    elif "result" in data:
        res = data.get("result")
        print(f"danage report for {entity_id} result= {res}")


    collection.insert_one(data)

