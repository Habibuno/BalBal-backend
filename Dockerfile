FROM python:3.10-slim

WORKDIR /app

# Créer un utilisateur non-root
RUN useradd -m appuser
RUN chown -R appuser:appuser /app

# Copier les fichiers
COPY . .

# Installer les dépendances en tant que "appuser"
USER appuser
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# Lancer l'application avec l'utilisateur non-root
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
