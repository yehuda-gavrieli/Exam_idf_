from pymongo import Mongo_client
from logger import log_event

client = Mongo_client("mongodb://localhost:27017/")
db = client["hunter_db"]
collection1 = db["stations"]
collection2 = db["measurements"]

