import duckdb
import matplotlib.pyplot as plt
import os

# Set paths
db_path = os.path.expanduser("~/Documents/pyspark-project/spotify_warehouse.db")
output_dir = os.path.expanduser("~/Documents/pyspark-project")

def create_plots():
    # Connect to your Serving Layer
    con = duckdb.connect(db_path)
    df = con.execute("""
        SELECT year, avg_loudness, avg_energy, avg_danceability 
        FROM year_stats 
        WHERE year > 1950 
        ORDER BY year
    """).df()
    con.close()

    # Set Global Style
    plt.style.use('dark_background')
    
    # --- PLOT 1: THE LOUDNESS WAR ---
    plt.figure(figsize=(12, 6))
    plt.plot(df['year'], df['avg_loudness'], color='#1DB954', linewidth=2, label='Avg Loudness (dB)')
    plt.fill_between(df['year'], df['avg_loudness'], color='#1DB954', alpha=0.1)
    plt.title('The Loudness War: Average Decibels Over Time', fontsize=14, pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Loudness (dB)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.savefig(os.path.join(output_dir, 'loudness_trend.png'), dpi=300, bbox_inches='tight')
    print("Saved: loudness_trend.png")

    # --- PLOT 2: ENERGY VS DANCEABILITY ---
    plt.figure(figsize=(12, 6))
    plt.plot(df['year'], df['avg_energy'], color='#1ed760', label='Energy', linewidth=2)
    plt.plot(df['year'], df['avg_danceability'], color='#ffffff', label='Danceability', linewidth=2, linestyle='--')
    plt.title('Acoustic Evolution: Energy vs Danceability', fontsize=14, pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.savefig(os.path.join(output_dir, 'acoustic_evolution.png'), dpi=300, bbox_inches='tight')
    print("Saved: acoustic_evolution.png")

if __name__ == "__main__":
    create_plots()
