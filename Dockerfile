FROM python:3.10-slim

WORKDIR /app

# Copier tous les fichiers du dépôt
COPY . .

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Lancer le backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
