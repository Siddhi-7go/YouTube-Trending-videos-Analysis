# ▶️ YouTube Trending Analytics — India (Feb 2026)

Interactive, dark-mode Streamlit dashboard built on a real YouTube trending
snapshot dated **26 Feb 2026** (16,199 India trending videos).

Dataset is already cleaned and bundled at `data/youtube_trending_2026.csv` —
nothing to download, it's ready to run as-is.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens automatically at `http://localhost:8501`.

## Put it on GitHub

```bash
git init
git add .
git commit -m "YouTube trending dashboard - India Feb 2026, dark mode"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Deploy so ANYONE can open it (free)

GitHub only stores the code — it can't run the live app for viewers.

1. Go to **https://share.streamlit.io** → sign in with GitHub
2. **New app** → pick this repo → branch `main` → file `app.py`
3. **Deploy**

You'll get a public link like `https://<your-app>.streamlit.app` —
share that with anyone, no login required to view it.

## What's inside

- **Overview** — top categories, top channels, category share, publish-hour pattern
- **Top Videos** — sortable leaderboard by views/likes/comments/engagement
- **Engagement Insights** — views vs engagement scatter, engagement by category,
  most-engaging videos (replaces the old forecast tab — this dataset is a
  single-day snapshot, so time-series forecasting isn't meaningful here)
- **Data** — full filtered table + CSV download

## Note on the data

This is a **one-day snapshot** (26 Feb 2026), not daily-collected history.
That's why there's no forecast/trend-over-time chart — there's nothing to
forecast from a single date. Everything else (rankings, engagement,
category/channel breakdowns) is fully accurate and interactive.
