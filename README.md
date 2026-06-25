# IoT Monitoring and Alerting System
This repository contains the implementation of an end-to-end IoT monitoring system, developed during a pre-internship project at BEIA Consult International. The project bridges the gap between raw data generation and actionable insights.

## Project Architecture
The system follows a modular architecture based on containerized services:

## Technology Stack
* Data Generation: Python scripts simulating sensor data (Temperature, Humidity).
* Communication: MQTT protocol for real-time telemetry.
* Processing: Node-RED for data parsing and logic flow.
* Storage: InfluxDB as the Time-Series database.
* Visualization: Grafana for real-time dashboards and threshold-based alerts.
* Interrogation: Python-based Telegram Bot for remote data access.

## Repository Structure
/python_scripts: Contains the data simulation and the Telegram bot logic.
/node-red: Contains the exported JSON flows used for data processing.
/docs: Project documentation and reports.
