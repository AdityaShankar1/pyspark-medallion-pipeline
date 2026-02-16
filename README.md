# 🎵 Spotify Data Engineering: 1.2M Record Medallion Pipeline

## 🚀 Overview
This project demonstrates a production-grade Data Engineering workflow using **PySpark** and **DuckDB**. It processes a dataset of 1.2 million Spotify tracks through a **Medallion Architecture**, transforming raw CSV data into an optimized, queryable analytical serving layer.

## 📂 Deep Dive
For a detailed breakdown of the trends and data quality observations, see the [Insights Directory](./insights/DATA_ANALYSIS.md).

## 🏗️ Technical Architecture
* **Bronze Layer (Ingestion):** Raw CSV ingestion of 1.2M records using Spark with strict schema enforcement (avoiding `inferSchema` overhead).
* **Silver Layer (Transformation):** Data cleaning and feature engineering. Data is persisted in **Partitioned Parquet** format (partitioned by `year`) to enable **Predicate Pushdown**.
* **Gold Layer (Serving):** Analytical aggregations moved from Spark to **DuckDB**. This decouples heavy batch processing from the low-latency requirements of the frontend.
* **Visual Layer:** An interactive **Gradio** dashboard providing real-time insights into music trends via Plotly.



## 🛠️ Performance & Environment
* **Hardware:** Optimized for **Apple Silicon (M4)**.
* **JVM Tuning:** Resolved Java 17+ encapsulation issues by configuring explicit JVM module access (`--add-opens`) for Spark's Hadoop dependencies.
* **Storage Efficiency:** Reduced data footprint by ~45% by migrating from CSV to Parquet.
* **Query Latency:** Reduced analytical query time from seconds (Spark) to milliseconds (DuckDB) for the end-user.

## 📂 How to Run
1.  **Environment:** Managed via SDKMAN! (Java 17.0.10-tem).
2.  **ETL:** `python3 scripts/spotify_pipeline.py`
3.  **Serving:** `python3 scripts/spotify_gold_insights2.py`
4.  **UI:** `python3 scripts/spotify_dashboard.py`

---
*Developed as a demonstration of scalable data architecture and systems thinking.*
## 🐳 Docker Quickstart
To run the entire pipeline and dashboard in a containerized environment:
```bash
docker-compose up
```
