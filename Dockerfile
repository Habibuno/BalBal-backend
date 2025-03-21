FROM python:3.10-slim

WORKDIR /app

# Créer un utilisateur non-root
RUN useradd -m appuser
RUN chown -R appuser:appuser /app

# Copier les fichiers du projet
COPY . .

# Passer à l'utilisateur non-root
USER appuser

# Configurer PATH pour l'utilisateur non-root
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# Lancer l'application FastAPI (sur le port par défaut Render 10000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

