from kafka import KafkaConsumer
from students_part_1.simulator import run_simulator
import my_engine
import json


consumer = KafkaConsumer("digital_hanter",
        bootstrap_servers="localhost:9092",
        value_serializer=lambda m:json.loads(m.decode("utf-8"))
    )

if __name__ == "__main__":
    print("the consumer running")
    for message in consumer:
        
    run_simulator(my_engine)