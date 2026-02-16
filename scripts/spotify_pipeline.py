import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, BooleanType

# 1. SETUP SESSION WITH COMPATIBILITY FLAGS
# These flags are mandatory for Java 17+ and modern Spark environments
spark = SparkSession.builder \
    .appName("SpotifyEngineeringProject") \
    .config("spark.driver.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "8") \
    .config("spark.driver.extraJavaOptions", 
            "--add-opens=java.base/java.lang=ALL-UNNAMED " +
            "--add-opens=java.base/java.util=ALL-UNNAMED " +
            "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED " +
            "--add-opens=java.base/sun.security.action=ALL-UNNAMED " +
            "--add-opens=java.base/javax.security.auth=ALL-UNNAMED") \
    .getOrCreate()

# 2. DEFINE SCHEMA
schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("album", StringType(), True),
    StructField("album_id", StringType(), True),
    StructField("artists", StringType(), True),
    StructField("artist_ids", StringType(), True),
    StructField("track_number", IntegerType(), True),
    StructField("disc_number", IntegerType(), True),
    StructField("explicit", BooleanType(), True),
    StructField("danceability", DoubleType(), True),
    StructField("energy", DoubleType(), True),
    StructField("key", IntegerType(), True),
    StructField("loudness", DoubleType(), True),
    StructField("mode", IntegerType(), True),
    StructField("speechiness", DoubleType(), True),
    StructField("acousticness", DoubleType(), True),
    StructField("instrumentalness", DoubleType(), True),
    StructField("liveness", DoubleType(), True),
    StructField("valence", DoubleType(), True),
    StructField("tempo", DoubleType(), True),
    StructField("duration_ms", DoubleType(), True),
    StructField("time_signature", DoubleType(), True),
    StructField("year", IntegerType(), True),
    StructField("release_date", StringType(), True)
])

# 3. LOAD DATA
raw_path = "/Users/adityashankar/Downloads/tracks_features.csv"

if not os.path.exists(raw_path):
    print(f"ERROR: File not found at {raw_path}")
    spark.stop()
else:
    print(f"--- Loading 1.2M songs from {raw_path} ---")
    
    # Read the CSV
    df = spark.read.csv(raw_path, header=True, schema=schema)

    # 4. TRANSFORMATION (Silver Layer)
    # Cleaning nulls and creating a 'Party Song' flag based on audio features
    silver_df = df.dropna(subset=["id", "name"]) \
        .withColumn("duration_min", F.round(F.col("duration_ms") / 60000, 2)) \
        .withColumn("is_party_song", (F.col("danceability") > 0.7) & (F.col("energy") > 0.7)) \
        .drop("duration_ms")

    # 5. WRITE TO PARQUET (The 'Good' DE standard)
    output_path = "spotify_silver_processed"
    print(f"--- Saving optimized Parquet data to: {os.path.abspath(output_path)} ---")
    
    silver_df.write \
        .mode("overwrite") \
        .partitionBy("year") \
        .parquet(output_path)

    # 6. ACTION: Show results
    print("--- PREVIEW: 1990s Party Songs ---")
    silver_df.filter((F.col("year") >= 1990) & (F.col("year") < 2000)) \
             .filter(F.col("is_party_song") == True) \
             .select("name", "artists", "year", "energy") \
             .show(10, truncate=False)

    print("Success! Data Engineering pipeline completed.")
    spark.stop()
