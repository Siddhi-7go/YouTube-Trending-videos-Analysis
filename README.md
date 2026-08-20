
# 📊 YouTube Trending Analytics — India 🇮🇳

An interactive **YouTube Trending Videos Analytics Dashboard** built using **Python, Pandas, Plotly, and Streamlit**.

The dashboard analyzes **16,199 India YouTube trending videos** from **26 February 2026** and provides interactive insights into popular videos, channels, categories, engagement, views, likes, comments, and publishing patterns.

## 🚀 Live Dashboard

🔗 **Live Demo:** (https://youtube-trending-videos-analysis-krbsx7m9b2zdfqywe52r5u.streamlit.app/)

---

## 📌 Project Overview

YouTube generates a huge amount of video data every day. This project provides an interactive way to explore and understand the characteristics of trending videos in India.

The dashboard allows users to:

* 📈 Explore trending video statistics
* 🔥 Identify top-performing videos
* 👤 Analyze popular YouTube channels
* 🏷️ Compare video categories
* ❤️ Analyze likes and comments
* 💬 Study audience engagement
* 🕐 Analyze publishing-hour patterns
* 📊 Compare views and engagement
* 📥 Download filtered data as CSV

The dataset is already cleaned and included in the project, so no additional dataset download is required.

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze YouTube trending videos in India.
2. Identify videos with the highest views, likes, and comments.
3. Understand which categories and channels perform better.
4. Analyze audience engagement.
5. Visualize relationships between views and engagement.
6. Provide an easy-to-use interactive dashboard.
7. Allow users to filter and download the analyzed data.

---

## 🖥️ Dashboard Features

### 🏠 Overview

Provides a high-level summary of the dataset, including:

* Top categories
* Top YouTube channels
* Category distribution
* Publishing-hour patterns
* Overall video statistics

### 🔥 Top Videos

Interactive leaderboard for identifying top-performing videos based on:

* Views
* Likes
* Comments
* Engagement

The leaderboard can be sorted to easily compare video performance.

### 📊 Engagement Insights

This section analyzes:

* Views vs. engagement
* Engagement by category
* Most-engaging videos
* Audience interaction patterns

### 📁 Data Explorer

Users can explore the filtered dataset directly through the dashboard and download the results as a CSV file.

---

## 🛠️ Technologies Used

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| 🐍 Python    | Data analysis and application development |
| 🐼 Pandas    | Data cleaning and analysis                |
| 📊 Plotly    | Interactive data visualization            |
| 🎨 Streamlit | Interactive dashboard                     |
| 📄 CSV       | Dataset storage                           |
| 🐙 GitHub    | Version control and project hosting       |

---

## 📂 Project Structure

```text
YouTube-Trending-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── youtube_trending_2026.csv
│
└── .streamlit/
    └── config.toml
```

The Streamlit configuration uses a dark theme with a custom primary color and background styling.

---

## 📊 Dataset

**Dataset:** YouTube Trending Videos — India

**Date:** 26 February 2026

**Records:** 16,199 videos

**Region:** India 🇮🇳

**File:**

```text
data/youtube_trending_2026.csv
```

### Important Dataset Note

This project uses a **single-day snapshot**, not a collection of daily historical data.

Therefore, a traditional time-series forecasting model is not appropriate for this dataset. Instead, the project focuses on accurate analysis of:

* Rankings
* Views
* Likes
* Comments
* Engagement
* Categories
* Channels
* Publishing patterns

This limitation is important because forecasting requires multiple historical time points.


## 💡 Key Insights

The dashboard can be used to understand:

* Which videos attract the most views
* Which channels frequently appear among trending videos
* Which categories receive higher engagement
* How likes and comments relate to views
* Which publishing hours are associated with trending content
* Which videos have the strongest audience engagement

---

## 🔮 Future Improvements

Possible future improvements include:

* 📅 Collecting multiple days of YouTube trending data
* 🤖 Building a genuine time-series forecasting model
* 🔮 Predicting future video views
* 🧠 Applying machine learning for trending prediction
* 🔍 Adding sentiment analysis of video titles/comments
* 🌍 Adding multiple countries
* ☁️ Connecting to the YouTube Data API
* 📈 Adding real-time data updates

---

## 👩‍💻 Author

**Manali Kachale**

**Siddhi Tambe**

TE — Artificial Intelligence & Data Science
