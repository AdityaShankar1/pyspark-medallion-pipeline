from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("SpotifyGoldInsights").getOrCreate()

# Load the optimized SILVER data
df = spark.read.parquet("spotify_silver_processed")

# Create GOLD Insight: Average loudness and energy per year
# This is a 'Wide' transformation (Shuffle)
loudness_trend = df.groupBy("year") \
    .agg(
        F.avg("loudness").alias("avg_loudness"),
        F.avg("energy").alias("avg_energy"),
        F.count("id").alias("song_count")
    ) \
    .orderBy("year")

# Show the results
print("--- GOLD LAYER: The Loudness War Over Time ---")
loudness_trend.filter(F.col("year") > 1950).show(20)

spark.stop()
