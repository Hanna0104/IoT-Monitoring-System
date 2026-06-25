import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

# --- Configurare Conexiune ---
BROKER_ADDRESS = "mqtt.beia-telemetrie.ro"
PORT = 1883
TOPIC = "training/device/Ana-Hurtupan/senzori"
CLIENT_ID = "Senzor_Virtual_Ana"

# Inițializare client MQTT 
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER_ADDRESS, PORT)

print(f"[{CLIENT_ID}] Conexiune reușită! Începe transmiterea datelor...")

try:
    while True:
        # Generare date simulate 
        temperatura = round(random.uniform(21.5, 28.5), 2)
        umiditate = round(random.uniform(45.0, 55.0), 2)
        
        # Preluarea orei exacte a sistemului
        timp_curent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Creare payload JSON structurat profesional
        payload = json.dumps({
            "temperatura": temperatura,
            "umiditate": umiditate
        })
        
        # Publicare mesaj pe broker
        client.publish(TOPIC, payload)
        
        # Afișare în consolă pentru verificare
        print(f"[TRIMIS] -> {TOPIC} | {payload}")
        
        # Pauză de 5 secunde între citiri
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\n[STOP] Transmisia a fost oprită manual.")
    client.disconnect()