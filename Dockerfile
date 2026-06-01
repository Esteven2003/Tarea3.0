FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ejercicio3.0.0/ ./ejercicio3.0.0/

# Ejecuta pruebas y luego la demostración de la app
CMD ["sh", "-c", "pytest /app/ejercicio3.0.0/ -v && python /app/ejercicio3.0.0/app.py"]