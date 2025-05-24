"""
This app delpoyed on Hugging Face. 
https://huggingface.co/spaces/WenshanL/TestApp-Games






"""

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib

import pandas as pd
df = pd.read_csv('df_with_sentiment.csv')  

'''
app = Flask(__name__)


# load the models 
model = joblib.load('rf_model.pkl')
imputer = joblib.load('imputer.pkl')

# load the features
model_features = ['score', 'original_price', 'total_sales', 'release_year', 'genre', 'developer', 'publisher', 'platform', 'sentiment_score']  # 填入你的 feature 列表

# Need 2 stages : First, need to find the price range. Then, use the price range to get the best price and revenue

# 1st API
@app.route('/get_price_range', methods=['POST'])
def get_price_range():
    data = request.json
    genre = data['genre']

    # filter the genre
    genre_games = df[df['genres'] == genre]
    
    if genre_games.empty:
        return jsonify({'error': f"No data found for genre: {genre}"}), 404

    min_price = genre_games['original_price'].min()
    max_price = genre_games['original_price'].max()

    return jsonify({
        'genre': genre,
        'min_price': float(min_price),
        'max_price': float(max_price)
    })

# 2rd API


# Test
if __name__ == '__main__':
    app.run(debug=True)

'''



import gradio as gr
import joblib
import pandas as pd
import numpy as np

# load the models
model = joblib.load("rf_model.pkl")
imputer = joblib.load("imputer.pkl")
model_features = joblib.load("model_features.pkl")  

def get_price_range_gradio(genre):
    genre_games = df[df['genres'] == genre]
    if genre_games.empty:
        return "No data found for that genre", None, None

    min_price = genre_games['original_price'].min()
    max_price = genre_games['original_price'].max()
    return f"{genre} games found.", float(min_price), float(max_price)

if __name__ == '__main__':
    
    gr.Interface(fn=get_price_range_gradio, inputs=["text"], outputs=["text", "number", "number"], title="Game Price Predictor", description="Enter a genre to get the price range of similar games. Example: Sandbox").launch()