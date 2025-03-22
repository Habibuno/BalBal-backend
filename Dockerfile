FROM python:3.10-slim

WORKDIR /app

# Copier tous les fichiers d’un coup
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
