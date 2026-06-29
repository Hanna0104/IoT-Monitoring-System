import paho.mqtt.client as mqtt
import hashlib
import json
import time
import os

# --- SETARI MQTT ---
BROKER = "mqtt.beia-telemetrie.ro"
PORT = 1883
TOPIC = "training/device/Ana-Hurtupan/senzori"

# --- SETARI STOCARE LOCALA ---
# Cerinta: "stocare locala date intr-un folder cu nume candidat"
FOLDER_NUME = "Ana_Local_Storage"
FISIER_BLOCKCHAIN = f"{FOLDER_NUME}/blockchain_data.json"

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Transformam datele in format text pentru a fi criptate cu SHA-256
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        
        # 1. Creare folder cu numele candidatului daca nu exista
        if not os.path.exists(FOLDER_NUME):
            os.makedirs(FOLDER_NUME)
            print(f"📁 Folder local creat: {FOLDER_NUME}")
            
        # 2. Incarcare date existente sau creare bloc de start (Genesis)
        if os.path.exists(FISIER_BLOCKCHAIN):
            with open(FISIER_BLOCKCHAIN, 'r') as f:
                try:
                    self.chain = json.load(f)
                    print(f"🔗 Blockchain incarcat din stocarea locala. Blocuri curente: {len(self.chain)}")
                except json.JSONDecodeError:
                    self.create_genesis_block()
        else:
            self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block - Inceputul", "0")
        self.chain.append(self.block_to_dict(genesis_block))
        self.save_chain()
        print("🔗 Genesis Block a fost creat.")

    def block_to_dict(self, block):
        return {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        }

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_index = latest_block["index"] + 1
        
        # Crearea noului bloc si legarea de hash-ul anterior (Imuabilitate)
        new_block = Block(new_index, time.time(), data, latest_block["hash"])
        
        self.chain.append(self.block_to_dict(new_block))
        self.save_chain()
        
        print(f"✅ Blocul #{new_index} adaugat in siguranta! Hash: {new_block.hash}")

    def save_chain(self):
        # Salvarea intregului lant pe hard disk-ul local
        with open(FISIER_BLOCKCHAIN, 'w') as f:
            json.dump(self.chain, f, indent=4)

# Initializam sistemul Blockchain
iot_blockchain = Blockchain()

# --- FUNCTII MQTT ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"🌐 Conectat la brokerul MQTT. Ascultam topicul: {TOPIC}")
        client.subscribe(TOPIC)
    else:
        print(f"Eroare conexiune. Cod: {rc}")

def on_message(client, userdata, msg):
    try:
        # Preluam datele de la senzori (simulate acum, reale mai tarziu)
        payload = msg.payload.decode('utf-8')
        data = json.loads(payload)
        
        print(f"\n📡 Date noi receptionate: Temp={data.get('temperatura')}°C, Umid={data.get('umiditate')}%")
        
        # Le trimitem direct in procesul de Blockchain
        iot_blockchain.add_block(data)
        
    except Exception as e:
        print(f"Eroare procesare: {e}")

# Pornim serviciul
client = mqtt.Client(client_id="Ana_Blockchain_Service")
client.on_connect = on_connect
client.on_message = on_message

print("🚀 Pornire serviciu Securitate & Blockchain...")
client.connect(BROKER, PORT, 60)
client.loop_forever()