from kafka import KafkaConsumer
import json
import my_engine

def byts_to_json(data):
    if data is None:
        return None
    return json.loads(data.decode('utf-8'))

consumer = KafkaConsumer('intel', 'attack', 'damage',
    bootstrap_servers='localhost:9092',
    value_deserializer=byts_to_json 
)

if __name__ == "__main__":
    for message in consumer:
        if message.value:
            my_engine.handle_data(message.value)