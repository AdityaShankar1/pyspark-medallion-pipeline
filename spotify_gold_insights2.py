import duckdb
from pyspark.sql import SparkSession
import os

# Use absolute paths
project_dir = os.path.expanduser("~/Documents/pyspark-project")
parquet_path = os.path.join(project_dir, "spotify_silver_processed")
duckdb_path = os.path.join(project_dir, "spotify_warehouse.db")

# 1. Initialize Spark (with your M4 compatibility flags)
spark = SparkSession.builder \
    .appName("SparkToDuckDB") \
    .config("spark.driver.extraJavaOptions", 
            "--add-opens=java.base/java.lang=ALL-UNNAMED " +
            "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED") \
    .getOrCreate()

# 2. Load and Aggregate (Gold Layer Logic)
print("--- Creating Gold Aggregates with Spark ---")
df = spark.read.parquet(parquet_path)
gold_trends = df.groupBy("year").agg({
    "loudness": "avg",
    "energy": "avg",
    "danceability": "avg",
    "id": "count"
}).withColumnRenamed("avg(loudness)", "avg_loudness") \
  .withColumnRenamed("avg(energy)", "avg_energy") \
  .withColumnRenamed("avg(danceability)", "avg_danceability") \
  .withColumnRenamed("count(id)", "song_count")

# 3. Convert to Pandas for DuckDB Ingestion
# (Gold data is small/aggregated, so Pandas is safe and efficient here)
pandas_gold = gold_trends.toPandas()

# 4. Save to DuckDB (Serving Layer)
con = duckdb.connect(duckdb_path)
con.execute("CREATE OR REPLACE TABLE year_stats AS SELECT * FROM pandas_gold")
print(f"--- Success! Data saved to {duckdb_path} ---")

con.close()
spark.stop()
