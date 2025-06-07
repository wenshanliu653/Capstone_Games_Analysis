# Game Pricing Optimization Using Deep Learning
Built a deep learning–based pricing optimization system for video games by combining structured game data with sentiment scores extracted from player reviews. Applied NLP techniques and used a sentiment intensity analyzer to quantify review sentiment as model features. Trained a regression model to predict global sales based on price and sentiment, and simulated price–revenue curves to identify optimal pricing points.
---
## 📌 Problem Statement

Game publishers face a recurring challenge:  
How can they determine the most profitable launch price for a new title **without extensive historical pricing data** or **early market signals**?

This project addresses:
- The lack of fine-grained price-performance data
- The neglect of qualitative factors like **player sentiment**
- The impact of **seasonal release timing** on projected revenue

---

## 📊 Data Sources

Data was collected and merged from:
- 🛒 [VGChartz.com](https://www.vgchartz.com) – Game sales data
- 🌟 [Metacritic.com](https://www.metacritic.com) – User review sentiment
- 💰 [Dekudeals.com](https://www.dekudeals.com) – Nintendo Switch game pricing

**Fuzzy string matching** and TF-IDF cosine similarity were used to align game titles across platforms.

---

## 🔄 Data Preprocessing & NLP Pipeline

Key preprocessing and NLP steps:
- Data normalization: One record per platform per game
- Feature engineering: Extracted release date components, cleaned price values
- Review cleaning: Tokenization, lemmatization, NER
- Sentiment labeling with **VADER** + pseudo-labeling using **Random Forest**
- TF-IDF vectorization for supervised sentiment classification

---


## 📈 Exploratory Data Analysis Highlights

- Right-skewed **sales distribution** with a few major hits
- Popular price clusters at $20, $30, $40, $60
- **Action and Adventure** genres have higher average sales
- Games released in **October** tend to have the highest sales

- ---

## 🤖 Modeling Approach

We used both **classification and regression** models:

### Sentiment Classification
- Model: Random Forest
- Accuracy: **82%**
- F1-score (Positive): **0.90**
- Used pseudo-labeling based on VADER to improve generalizability

### Sales Prediction
Models tested:
- Simple Linear Regressiont achieved **R² = 0.635**
- Random Forest (unturned) achieved **R² = 0.999**
- Random Forest ( tuned with Grid Search) achieved **R² = 0.852**
- Multilayer Perceptrons (MLPs - Model16): **R² = 0.973**


---

## 💡 Case Study: Dragon Quest Builders 3

| Release Month | Price     | Predicted Sales (M) | Revenue (M USD) |
|---------------|-----------|---------------------|------------------|
| Feb 2025      | $49.99    | 0.0169              | $0.84            |
| Feb 2025      | **$36.99**| **0.1327**          | **$4.9**         |
| Nov 2025      | $36.99    | 0.127               | $4.7             |

📌 **Optimal Price:** $36.99  
📌 **Insight:** Revenue is sensitive to **seasonality** and **floating-point precision**, even when predicted sales appear identical.

---

## 🧠 Key Takeaways

1. **Sentiment-Enhanced Forecasting** improves accuracy by incorporating user feedback.
2. **Release Timing** (e.g., holiday season) plays a major role in sales potential.
3. **Simulation-based pricing** can help publishers maximize revenue before release.

---

## 📌 Author

**Wen-shan Liu** –
