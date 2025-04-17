import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'lidar-data'

def generate_sensor_data():
    return {
        "angle": random.randint(0, 360),
        "distance": round(random.uniform(0.5, 5.0), 2),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        producer.send(topic, value=data)
        print(f"Sent: {data}")
        time.sleep(0.5)  # half-second between readings