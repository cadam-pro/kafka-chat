from kafka import KafkaConsumer
import os

consumer = KafkaConsumer(
    "chat",
    bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka:9092"),
    auto_offset_reset="earliest",
    group_id="chat-group",
)

print("En attente des messages…")
for msg in consumer:
    print(f"Message reçu : {msg.value.decode('utf-8')}")
