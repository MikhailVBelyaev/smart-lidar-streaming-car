# Step 1: Start Kafka
docker-compose up -d

# Step 2: (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Step 3: Run Kafka producer (simulates LiDAR data)
python backend/kafka_producer.py

# Step 4: In a new terminal, run Spark streaming
spark-submit spark/streaming_job.py

# step 5: web UI
cd web
python3 app.py