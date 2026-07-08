# IoT Monitoring and Alerting System

This repository contains the implementation of an end-to-end Internet of Things (IoT) system designed for real-time environmental monitoring, data processing, and automated alerting. Developed as a pre-internship project at BEIA Consult International, the system demonstrates a highly scalable, dual-phase data pipeline[cite: 1].

## 📖 Project Overview

The project bridges the gap between raw data generation and actionable insights, built across two main phases[cite: 1]:
* **Phase 1 (Simulated SoS Environment):** A local Proof of Concept (PoC) utilizing Python to simulate virtual sensor nodes, transmitting telemetry via MQTT[cite: 1]. The backend is fully containerized and orchestrated using the Arrowhead Framework to establish a System-of-Systems (SoS) architecture[cite: 1].
* **Phase 2 (Enterprise Hardware):** Deployment of a physical industrial node (Libelium Smart Agriculture Xtreme) transmitting real-world environmental metrics over a 4G cellular network to a central Meshlium enterprise server[cite: 1].

## 🛠️ Technology Stack

The system relies on a robust, modern technology stack[cite: 1]:
* **Data Generation:** Python (Virtual Sensor), Libelium Waspmote C++ (Physical Node)[cite: 1]
* **Protocols:** MQTT, HTTP[cite: 1]
* **Data Processing & Routing:** Node-RED[cite: 1]
* **Time-Series Storage:** InfluxDB[cite: 1]
* **Visualization & Alerts:** Grafana[cite: 1]
* **Orchestration & Discovery:** Docker, Docker Compose, Arrowhead Framework (Service Registry & MySQL)[cite: 1]
* **Security & Interaction:** Custom Python Blockchain Microservice, Telegram API[cite: 1]

##  Key Features

1. **Automated Data Pipeline:** Seamless ingestion, parsing (JSON), and storage of environmental data (Temperature, Humidity)[cite: 1].
2. **Containerized Orchestration:** The entire Phase 1 backend operates in isolated Docker containers, managed via `docker-compose`[cite: 1].
3. **Data Integrity (Blockchain):** A dedicated local microservice utilizes SHA-256 cryptographic hashing to encapsulate incoming data into an immutable chain, preventing unauthorized tampering[cite: 1].
4. **Remote Telegram ChatBot:** An interactive bot allowing users to query live database metrics (e.g., `/temperatura`, `/umiditate`) on demand from any mobile device[cite: 1].
5. **Real-time Alerting:** Automated Grafana threshold alerts that dispatch email notifications when environmental parameters exceed safe boundaries (e.g., > 25°C)[cite: 1].

##  Repository Structure

* `generare_senzori.py`: Python script simulating the MQTT sensor node[cite: 1].
* `blockchain_service.py`: Microservice for local storage and cryptographic data immutability[cite: 1].
* `telegram_bot.py`: Python script for the interactive Telegram querying interface[cite: 1].
* `Dockerfile` / `Dockerfile.simulator` / `Dockerfile.bot`: Instructions for containerizing the individual Python microservices[cite: 1].
* `docker-compose.yml`: The orchestration file linking Node-RED, InfluxDB, Arrowhead Core Systems, and custom microservices[cite: 1].
