from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, DoubleType, StringType

# Define the schema of incoming JSON data
schema = StructType() \
    .add("timestamp", StringType()) \
    .add("distance", DoubleType()) \
    .add("angle", DoubleType())

# Create Spark session
spark = SparkSession.builder \
    .appName("LiDAR Structured Streaming") \
    .getOrCreate()

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "lidar-data") \
    .load()

# Parse the JSON messages
parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Write to Parquet
query = parsed_df.writeStream \
    .format("parquet") \
    .option("path", "/tmp/lidar_output") \
    .option("checkpointLocation", "/tmp/lidar_checkpoint") \
    .outputMode("append") \
    .start()

query.awaitTermination()