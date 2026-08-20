import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.io as pio

# ===========================================================
# PAGE CONFIG
# ===========================================================
st.set_page_config(
    page_title="YouTube Trending Analytics — India 2026",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===========================================================
# THEME
# ===========================================================
THEMES = {
    "Neon Pink":     {"a": "#ff2e63", "b": "#ff8a00", "grad": "linear-gradient(135deg,#ff2e63 0%,#ff8a00 100%)"},
    "Electric Blue": {"a": "#00c6ff", "b": "#7b2ff7", "grad": "linear-gradient(135deg,#00c6ff 0%,#7b2ff7 100%)"},
    "Cyber Green":   {"a": "#00f5a0", "b": "#00d9f5", "grad": "linear-gradient(135deg,#00f5a0 0%,#00d9f5 100%)"},
    "Sunset":        {"a": "#f857a6", "b": "#ff5858", "grad": "linear-gradient(135deg,#f857a6 0%,#ff5858 100%)"},
}
if "theme_name" not in st.session_state:
    st.session_state.theme_name = "Neon Pink"

pio.templates.default = "plotly_dark"
theme = THEMES[st.session_state.theme_name]

# ===========================================================
# GLOBAL DARK CSS
# ===========================================================
st.markdown(f"""
<style>
    html, body, [class*="css"] {{
        background-color: #0b0e14 !important;
        color: #eaeaf0 !important;
    }}
    .stApp {{
        background: radial-gradient(circle at top left, #141824 0%, #0b0e14 60%);
    }}
    .block-container {{ padding-top: 1.2rem; padding-bottom: 2rem; }}
    .hero {{
        padding: 1.4rem 1.8rem;
        border-radius: 20px;
        background: {theme['grad']};
        color: white;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 30px rgba(0,0,0,.45);
    }}
    .hero h1 {{ margin: 0; font-size: 2.2rem; font-weight: 800; }}
    .hero p {{ margin: .4rem 0 0 0; opacity: .95; font-size: 1.02rem; }}
    div[data-testid="stMetric"] {{
        background: linear-gradient(160deg, #161b28 0%, #10131c 100%);
        border: 1px solid rgba(255,255,255,.08);
        padding: 14px 18px;
        border-radius: 16px;
        box-shadow: 0 4px 18px rgba(0,0,0,.35);
        transition: transform .15s ease;
    }}
    div[data-testid="stMetric"]:hover {{ transform: translateY(-3px); border-color: {theme['a']}; }}
    div[data-testid="stMetricValue"] {{ color: {theme['a']} !important; }}
    section[data-testid="stSidebar"] {{ background: #0d1017; border-right: 1px solid rgba(255,255,255,.06); }}
    section[data-testid="stSidebar"] * {{ color: #eaeaf0 !important; }}
    .stButton>button, .stDownloadButton>button {{
        background: {theme['grad']};
        color: white; border: none; border-radius: 12px;
        font-weight: 700; padding: .6rem 1rem;
        transition: transform .12s ease, box-shadow .12s ease;
        box-shadow: 0 4px 14px rgba(0,0,0,.35);
    }}
    .stButton>button:hover, .stDownloadButton>button:hover {{
        transform: scale(1.02); box-shadow: 0 6px 22px rgba(0,0,0,.5);
    }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 6px; }}
    .stTabs [data-baseweb="tab"] {{
        background: #141824; border-radius: 10px 10px 0 0;
        padding: 8px 16px; color: #cfd3dc;
    }}
    .stTabs [aria-selected="true"] {{
        background: {theme['grad']} !important; color: white !important; font-weight: 700;
    }}
    div[data-testid="stDataFrame"] {{
        border-radius: 14px; overflow: hidden; border: 1px solid rgba(255,255,255,.08);
    }}
    hr {{ border-color: rgba(255,255,255,.08); }}
</style>
""", unsafe_allow_html=True)

# ===========================================================
# DATA LOADING
# ===========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "youtube_trending_2026.csv"


@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        return pd.DataFrame()
    df = pd.read_csv(DATA_FILE)
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce", utc=True)
    df["trending_date"] = pd.to_datetime(df["trending_date"], errors="coerce", utc=True)
    return df


def format_number(value):
    value = float(value)
    if abs(value) >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"
    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:.2f}M"
    if abs(value) >= 1_000:
        return f"{value/1_000:.1f}K"
    return f"{value:,.0f}"


df = load_data()

if df.empty:
    st.error(
        "⚠️ Dataset not found. Make sure `data/youtube_trending_2026.csv` "
        "exists in your project folder."
    )
    st.stop()

snapshot_date = df["trending_date"].max().strftime("%d %b %Y")

# ===========================================================
# HERO
# ===========================================================
st.markdown(f"""
<div class="hero">
    <h1>▶️ YouTube Trending Analytics — India</h1>
    <p>Snapshot from {snapshot_date} • {len(df):,} trending videos • Dark mode dashboard</p>
</div>
""", unsafe_allow_html=True)

# ===========================================================
# SIDEBAR
# ===========================================================
st.sidebar.title("🎛️ Dashboard Controls")
st.sidebar.selectbox("🎨 Color theme", list(THEMES.keys()), key="theme_name")
st.sidebar.caption(f"Data snapshot date: **{snapshot_date}**")

if st.sidebar.button("🔄 Refresh cached data", use_container_width=True):
    st.cache_data.clear()
    st.rerun()

categories = ["All"] + sorted(df["category_name"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("📂 Category", categories)

channel_search = st.sidebar.text_input("🔎 Search channel name")

min_views = int(df["views"].min())
max_views = int(df["views"].max())
views_range = st.sidebar.slider(
    "👁️ Views range",
    min_value=min_views, max_value=max_views,
    value=(min_views, max_views),
    format="%d",
)

st.sidebar.button("🚀 APPLY FILTERS", use_container_width=True)

# ===========================================================
# FILTER
# ===========================================================
filtered = df.copy()
if selected_category != "All":
    filtered = filtered[filtered["category_name"] == selected_category]
if channel_search:
    filtered = filtered[filtered["channel_title"].str.contains(channel_search, case=False, na=False)]
filtered = filtered[(filtered["views"] >= views_range[0]) & (filtered["views"] <= views_range[1])]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# ===========================================================
# KPI CARDS
# ===========================================================
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("👁️ Total Views", format_number(filtered["views"].sum()))
c2.metric("👍 Total Likes", format_number(filtered["likes"].sum()))
c3.metric("💬 Comments", format_number(filtered["comments"].sum()))
c4.metric("🎬 Videos", f"{filtered['video_id'].nunique():,}")
c5.metric("📺 Channels", f"{filtered['channel_title'].nunique():,}")

st.divider()

# ===========================================================
# TABS
# ===========================================================
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔥 Top Videos", "💡 Engagement Insights", "📋 Data"])

with tab1:
    left, right = st.columns(2)

    with left:
        cat_chart = (
            filtered.groupby("category_name", as_index=False)["views"]
            .sum().sort_values("views", ascending=False).head(10)
        )
        fig1 = px.bar(
            cat_chart.sort_values("views"), x="views", y="category_name",
            orientation="h", title="📂 Top Categories by Views",
            color="views", color_continuous_scale=[theme["b"], theme["a"]],
        )
        fig1.update_layout(height=420, xaxis_title="Views", yaxis_title="",
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            coloraxis_showscale=False)
        st.plotly_chart(fig1, use_container_width=True)

    with right:
        channel_chart = (
            filtered.groupby("channel_title", as_index=False)["views"]
            .sum().sort_values("views", ascending=False).head(10)
        )
        fig2 = px.bar(
            channel_chart.sort_values("views"), x="views", y="channel_title",
            orientation="h", title="📺 Top 10 Channels by Views",
            color="views", color_continuous_scale=[theme["b"], theme["a"]],
        )
        fig2.update_layout(height=420, xaxis_title="Views", yaxis_title="",
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            coloraxis_showscale=False)
        st.plotly_chart(fig2, use_container_width=True)

    left2, right2 = st.columns(2)

    with left2:
        pie = filtered.groupby("category_name")["video_id"].count().sort_values(ascending=False).head(8)
        fig3 = px.pie(
            names=pie.index, values=pie.values, hole=0.45,
            title="🍩 Trending Videos Share by Category",
            color_discrete_sequence=px.colors.sequential.Plasma,
        )
        fig3.update_layout(height=420, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig3, use_container_width=True)

    with right2:
        hour_chart = (
            filtered.groupby("publish_hour", as_index=False)["video_id"]
            .count().rename(columns={"video_id": "videos"}).sort_values("publish_hour")
        )
        fig4 = px.bar(
            hour_chart, x="publish_hour", y="videos",
            title="🕐 What Hour Were Trending Videos Published? (UTC)",
            color="videos", color_continuous_scale=[theme["b"], theme["a"]],
        )
        fig4.update_layout(height=420, xaxis_title="Publish Hour (UTC)", yaxis_title="Videos",
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            coloraxis_showscale=False)
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    top_n = st.slider("Show top N videos", 5, 50, 10)
    sort_by = st.radio("Sort by", ["views", "likes", "comments", "engagement_rate"], horizontal=True)

    top_videos = (
        filtered[["title", "channel_title", "category_name", "views", "likes",
                  "comments", "engagement_rate"]]
        .sort_values(sort_by, ascending=False).head(top_n).copy()
    )
    top_videos["views"] = top_videos["views"].map(format_number)
    top_videos["likes"] = top_videos["likes"].map(format_number)
    top_videos["comments"] = top_videos["comments"].map(format_number)
    top_videos["engagement_rate"] = top_videos["engagement_rate"].astype(str) + "%"

    st.dataframe(top_videos, use_container_width=True, hide_index=True)

with tab3:
    st.subheader("💡 Engagement Insights")
    st.caption(
        "This dataset is a single-day snapshot, so trend forecasting over time "
        "isn't possible — instead, here's how videos compare on engagement."
    )

    left, right = st.columns(2)

    with left:
        fig5 = px.scatter(
            filtered, x="views", y="engagement_rate", color="category_name",
            hover_name="title", size="likes", size_max=35,
            title="🎯 Views vs Engagement Rate",
            log_x=True,
        )
        fig5.update_layout(height=460, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig5, use_container_width=True)

    with right:
        eng_by_cat = (
            filtered.groupby("category_name", as_index=False)["engagement_rate"]
            .mean().sort_values("engagement_rate", ascending=False).head(10)
        )
        fig6 = px.bar(
            eng_by_cat.sort_values("engagement_rate"), x="engagement_rate", y="category_name",
            orientation="h", title="📈 Avg Engagement Rate by Category (%)",
            color="engagement_rate", color_continuous_scale=[theme["b"], theme["a"]],
        )
        fig6.update_layout(height=460, xaxis_title="Engagement Rate (%)", yaxis_title="",
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            coloraxis_showscale=False)
        st.plotly_chart(fig6, use_container_width=True)

    st.markdown("### 🏆 Most Engaging Videos")
    most_engaging = (
        filtered[filtered["views"] > 10000]
        [["title", "channel_title", "category_name", "views", "engagement_rate"]]
        .sort_values("engagement_rate", ascending=False).head(10).copy()
    )
    most_engaging["views"] = most_engaging["views"].map(format_number)
    most_engaging["engagement_rate"] = most_engaging["engagement_rate"].astype(str) + "%"
    st.dataframe(most_engaging, use_container_width=True, hide_index=True)

with tab4:
    st.subheader("📋 Filtered Dataset")
    st.caption(f"{len(filtered):,} records")
    st.dataframe(
        filtered.drop(columns=["tags", "description"], errors="ignore").head(500),
        use_container_width=True, hide_index=True,
    )
    csv_data = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Filtered Data", data=csv_data,
                        file_name="filtered_youtube_trending_india_2026.csv", mime="text/csv")

st.divider()
st.caption(f"YouTube Trending Analytics — India • Snapshot {snapshot_date} • Built with Python, Pandas, Plotly & Streamlit")
