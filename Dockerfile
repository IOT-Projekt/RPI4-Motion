# Verwende ein ARM64-kompatibles Python-Image für Raspberry Pi 4 (64-Bit)
FROM python:3.11-slim

# Installiere die Python-Bibliotheken aus der requirements.txt
WORKDIR /app

# Kopiere Dateien in das Image
COPY app/ /app/
COPY requirements.txt /app/

# Installiere Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Führe das Skript aus
CMD ["python", "main.py"]
