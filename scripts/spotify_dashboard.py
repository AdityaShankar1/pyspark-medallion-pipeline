import gradio as gr
import duckdb
import plotly.express as px
import os

db_path = os.path.expanduser("~/Documents/pyspark-project/spotify_warehouse.db")

def get_stats():
    # Connect to DuckDB
    con = duckdb.connect(db_path)
    df = con.execute("SELECT * FROM year_stats ORDER BY year").df()
    con.close()
    
    # Create Trend Chart
    fig = px.line(df, x="year", y=["avg_energy", "avg_danceability"], 
                  title="Music Evolution Over Time",
                  template="plotly_dark",
                  labels={"value": "Score", "variable": "Feature"})
    return fig

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Spotify Data Engineering serving layer")
    gr.Markdown("Architecture: **Spark (Processing)** → **DuckDB (Storage)** → **Gradio (UI)**")
    
    with gr.Row():
        plot = gr.Plot(value=get_stats())
    
    refresh_btn = gr.Button("Refresh Data")
    refresh_btn.click(fn=get_stats, outputs=plot)

demo.launch()
