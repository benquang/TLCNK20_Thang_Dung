from kafka import KafkaConsumer
import json

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    'testtopic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8-sig'))
)

# Start consuming messages
for message in consumer:
    # Get the message value
    value = message.value

    # Process the message as needed
    print(value)