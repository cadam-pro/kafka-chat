# Image de base légère
FROM python:3.11-slim

# Créer un dossier de travail
WORKDIR /app

# Installer les dépendances système utiles (optionnel mais recommandé)
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances Python
COPY requirements.in .

RUN pip install --no-cache-dir -r requirements.in

# Copier le code du chat (producer.py, consumer.py…)
COPY . .

# Par défaut, on démarre le consumer
CMD ["python", "src/kafka_chat/consumer.py"]
