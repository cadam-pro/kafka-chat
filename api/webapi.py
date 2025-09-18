import asyncio
from fastapi import FastAPI, WebSocket
from kafka import KafkaProducer, KafkaConsumer
import json
import threading
import time

app = FastAPI()
TOPIC = "chat"
BROKER = "kafka:9092"

for i in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        break
    except Exception:
        print(f"Kafka non disponible, retry {i + 1}/10...")
        time.sleep(2)


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    # Démarre un consumer dans un thread séparé
    def consume():
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=BROKER,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            group_id="webchat",
        )
        for msg in consumer:
            asyncio.run(ws.send_text(msg.value["text"]))

    threading.Thread(target=consume, daemon=True).start()

    # Boucle pour recevoir les messages du client
    while True:
        data = await ws.receive_text()
        producer.send(TOPIC, {"text": data})
