from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

# Consume messages from the 'test' topic
for message in consumer:
    print(message)
