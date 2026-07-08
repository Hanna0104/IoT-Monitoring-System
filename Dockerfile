# 1. Folosim o imagine oficiala si usoara de Python
FROM python:3.9-slim

# 2. Setam directorul de lucru in interiorul containerului
WORKDIR /app

# 3. Copiem scriptul nostru de blockchain in container
COPY blockchain_service.py /app/

# 4. Instalam libraria necesara pentru a comunica cu brokerul BEIA
RUN pip install paho-mqtt

# 5. Comanda pe care containerul o ruleaza cand se aprinde
CMD ["python", "blockchain_service.py"]