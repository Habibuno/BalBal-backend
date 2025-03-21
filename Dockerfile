FROM python:3.10-slim

WORKDIR /app

# Créer un utilisateur non-root
RUN useradd -m appuser
RUN chown -R appuser:appuser /app

# Copier explicitement les fichiers requis
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier ensuite le reste des fichiers
COPY . .

# Changer l'utilisateur pour une exécution sécurisée
USER appuser

# Lancer l'application FastAPI sur le port Render par défaut (10000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
