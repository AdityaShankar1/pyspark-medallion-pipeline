# 🚀 Vibe Voyage: Music-Based Travel Recommendation System:
This project is classifies the emotional "vibe" of a song using Machine Learning and recommends matching travel destinations. 

## 🗺️ Real-world use:

1. Deep Personalization Through Implicit Signals: Uses music preferences to infer emotional state and deliver personalized travel recommendations without forcing users through complex preference selections.
   This reduces choice fatigue while creating stronger emotional engagement and higher conversion rates.

2. Scalable Integration Model: Provides a modular framework for connecting with streaming platforms (Spotify, Gaana, JioSaavn) to build recommendation engines.
   This approach creates a competitive advantage through creative data integration without requiring complex API infrastructures.

3. Cross-Domain Application: Demonstrates how implicit behavioral data can drive personalization across industries—from travel and e-commerce to content platforms and lifestyle services.
   The core methodology transfers to any product requiring intelligent, user-centric recommendations.

## ⚙️ Tech Stack & Tools used:
Language: Python
Machine Learning: Scikit-Learn 
Data Storage: SQLite
Data handling: Polars (for fallback dataset), PySpark (for scalability)
Other libraries: Spotipy (to interact with Spotify Web API), NumPy, Matplotlib & Seaborn (Vizualization), Requests
Execution Environment: Google Colab

## ✨ Project Features:
1. Vibe Classification: Uses a K-Nearest Neighbors (KNN) model, trained on 114,000 tracks, to classify music into Introspective, Mellow, Intense, or Jubilant.

2. Spotify Integration: The system architecture relies on the Spotify Web API to retrieve song audio features (e.g., valence, energy).

### Note: 
Due to runtime restrictions, the final execution utilized a robust Fallback Mode relying on the local backup dataset.

3. Recommendation Engine: Queries a local SQLite database to find destinations pre-labeled with the predicted song Vibe.

4. Visualization: A scatter plot shows the 114k Vibe distribution, highlighting the user's predicted track within the Vibe space.

## 🗺️ Data Sources:

### Note:
Initially worked successfully with Spotify API however due to API issues resorted to SQLite data. For code involving Spotify API data refer to: SpotifySpark.ipynb (https://github.com/AdityaShankar1/WanderBeat-Spark/blob/main/SpotifySpark.ipynb)

1. ML Training Data: Sourced from a large CSV file (dataset.csv) sourced from Kaggle containing 114k+ Spotify tracks and their audio features.

2. Travel Destinations: Sourced from Kaggle CSV file (travel\_data.csv). This static file was loaded into the SQLite database.

3. Destinations like Rio and Ibiza, used in early tests, were hardcoded placeholders.

## ⚙️ Execution Flow:
1. Dependencies are installed (spotipy, scikit-learn, etc.).

2. KNN Model is trained on the 114k tracks and features are Scaled.

3. User Input (Song Title/Artist) is processed.

4. Fallback Mode activates, fetching the track's features from the local backup data.

5. Vibe is Predicted by the trained ML model.

6. SQLite Database is queried to match the predicted Vibe to a destination.

7. Final Recommendation and Visualization are displayed.

## 🎯 Example Results:

Input Song: "Malang (Title Track)" by Ved Sharma
Predicted Vibe: Jubiliant
Recommended Destinations: Rio, Ibiza

## ℹ️ Additional Info:
Feedback Welcome!
Let's dicuss: https://www.linkedin.com/in/aditya-shankar-35a85a247
Built with ❤️ for Travel 
