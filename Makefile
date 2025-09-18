ruff :
	@echo "Running ruff..."
	ruff check --fix
	ruff format

send :
	@echo "Running src/kafka_chat/producer.py..."
	python src/kafka_chat/producer.py

receive :
	@echo "Running src/kafka_chat/consumer.py..."
	python src/kafka_chat/consumer.py
