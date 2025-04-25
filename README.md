# Smart Lidar Streaming Car

This is a personal project to build a robot car that streams LiDAR and sensor data to a backend system using Kafka and processes it in real-time using Apache Spark Streaming. The final result will be a map of the environment, similar to how robot vacuum cleaners create room layouts.

## Goals
- Build a real-time IoT streaming pipeline using a robot and sensors
- Use **Apache Kafka** + **Spark Streaming** to process and analyze sensor data
- Visualize the result (a 2D map of the environment)
- Gradually expand the system with more features (e.g., optional ML)

---

## Technologies Used
| Layer | Tech |
|-------|------|
| Hardware | Arduino, LiDAR, Wi-Fi Shield |
| Communication | Wi-Fi (Socket or HTTP) |
| Streaming | Apache Kafka, Kafka Connect, KSQLDB |
| Processing | Apache Spark Structured Streaming |
| Visualization | Flask / Streamlit (Simple UI) |
| Storage | JSON, PNG, or SVG |
| Optional Later | MLlib, S3, PostgreSQL, GitHub Actions (DevOps) |

---

## System Requirements

**Minimum Dev Environment:**
- 1 machine (or VM) running Ubuntu or MacOS/Linux
- 8GB RAM minimum (for Spark + Kafka)
- Docker (optional, for easier Kafka setup)
- Python 3.10+
- Java 8 or 11 (for Spark)

**Hardware Required:**
- Arduino + LiDAR sensor + Wi-Fi Shield
- Laptop or Raspberry Pi (optional) for robot control

---

## Project Roadmap

### **Phase 1: MVP (2 weeks)**
- [ ] Setup Arduino and basic Wi-Fi data sending
- [ ] Setup Kafka locally or using Confluent Platform
- [ ] Create Spark Structured Streaming job to read Kafka topic
- [ ] Store raw sensor data in simple JSON format
- [ ] Build a small web page with Start/Stop buttons

### **Phase 2: Real-Time Processing + Mapping (2 weeks)**
- [ ] Enhance data schema (angle, distance, timestamp)
- [ ] Process LiDAR data to convert into 2D coordinates
- [ ] Generate a 2D map as SVG/PNG from sensor data
- [ ] Expose result via web interface ("Download Map" button)

### **Phase 3: Advanced Features + DevOps (2 weeks)**
- [ ] Add logging, monitoring (Prometheus, Grafana - optional)
- [ ] Package Spark job as Docker container
- [ ] Deploy on remote Linux server
- [ ] Optional: add basic ML model to predict or improve movement

---

## Architecture Diagram

![Architecture](docs/architecture.png)

> Diagram shows data flow from Arduino → Kafka → Spark → Map Generator → Web UI

---

## Folder Structure

presents and guests list