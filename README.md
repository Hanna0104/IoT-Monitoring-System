# IoT Monitoring and Alerting System

This repository contains the implementation of an end-to-end Internet of Things (IoT) system designed for real-time environmental monitoring, data processing, and automated alerting. Developed as a pre-internship project at BEIA Consult International, the system demonstrates a highly scalable, dual-phase data pipeline.

## Project Overview

The project bridges the gap between raw data generation and actionable insights, built across two main phases:
* **Phase 1 (Simulated SoS Environment):** A local Proof of Concept (PoC) utilizing Python to simulate virtual sensor nodes, transmitting telemetry via MQTT. The backend is fully containerized and orchestrated using the Arrowhead Framework to establish a System-of-Systems (SoS) architecture.
* **Phase 2 (Enterprise Hardware):** Deployment of a physical industrial node (Libelium Smart Agriculture Xtreme) transmitting real-world environmental metrics over a 4G cellular network to a central Meshlium enterprise server.

## Technology Stack

The system relies on a robust, modern technology stack:
* **Data Generation:** Python (Virtual Sensor), Libelium Waspmote C++ (Physical Node)
* **Protocols:** MQTT, HTTP
* **Data Processing & Routing:** Node-RED
* **Time-Series Storage:** InfluxDB
* **Visualization & Alerts:** Grafana
* **Orchestration & Discovery:** Docker, Docker Compose, Arrowhead Framework (Service Registry & MySQL)
* **Security & Interaction:** Custom Python Blockchain Microservice, Telegram API

##  Key Features

1. **Automated Data Pipeline:** Seamless ingestion, parsing (JSON), and storage of environmental data (Temperature, Humidity).
2. **Containerized Orchestration:** The entire Phase 1 backend operates in isolated Docker containers, managed via `docker-compose`.
3. **Data Integrity (Blockchain):** A dedicated local microservice utilizes SHA-256 cryptographic hashing to encapsulate incoming data into an immutable chain, preventing unauthorized tampering.
4. **Remote Telegram ChatBot:** An interactive bot allowing users to query live database metrics (e.g., `/temperatura`, `/umiditate`) on demand from any mobile device.
5. **Real-time Alerting:** Automated Grafana threshold alerts that dispatch email notifications when environmental parameters exceed safe boundaries (e.g., > 25°C).

##  Repository Structure

* `generare_senzori.py`: Python script simulating the MQTT sensor node.
* `blockchain_service.py`: Microservice for local storage and cryptographic data immutability.
* `telegram_bot.py`: Python script for the interactive Telegram querying interface.
* `Dockerfile` / `Dockerfile.simulator` / `Dockerfile.bot`: Instructions for containerizing the individual Python microservices.
* `docker-compose.yml`: The orchestration file linking Node-RED, InfluxDB, Arrowhead Core Systems, and custom microservices.
