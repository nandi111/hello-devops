# Egyszerű Python alapú image
FROM python:3.11-slim

# Mappa a konténeren belül
WORKDIR /app

# Függőségek bemásolása és telepítése
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazáskód bemásolása
COPY . .

# A Flask app 8080-as porton fut
EXPOSE 8080

# Indítási parancs
CMD ["python", "app.py"]
