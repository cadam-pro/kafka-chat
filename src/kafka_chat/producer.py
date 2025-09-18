from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="kafka:9092")

while True:
    message = input("Votre message : ")
    producer.send("chat", value=message.encode("utf-8"))
    producer.flush()
