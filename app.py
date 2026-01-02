"""
Social Media Analysis Web App
A Streamlit-based web application for analyzing social media engagement data.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from social_analysis import load_data, clean_data, analyze_data, visualize_data

st.set_page_config(page_title="Social Media Analysis", page_icon="📊", layout="wide")

st.title("📊 Social Media Engagement Analysis")
st.markdown("Upload your social media data CSV to analyze engagement metrics, top posts, and more!")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load and clean data
    df = pd.read_csv(uploaded_file, engine='python')
    df = clean_data(df)

    # Analyze data
    df, platform_engagement, top_posts, top_verified, stats = analyze_data(df)

    # Generate visualizations
    figures = visualize_data(df, platform_engagement)

    # Display sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Data Overview")
        st.dataframe(df.head(), use_container_width=True)
        st.subheader("📈 Basic Statistics")
        st.dataframe(stats, use_container_width=True)

    with col2:
        st.subheader("🏆 Top 5 Engaging Posts")
        st.dataframe(top_posts, use_container_width=True)
        st.subheader("✅ Top 5 Verified Users")
        st.dataframe(top_verified, use_container_width=True)

    st.subheader("📊 Visualizations")

    # Display plots
    plot_cols = st.columns(2)
    plot_names = ["Average Engagement by Platform", "Followers vs Engagement", "Total Engagement Distribution", "Likes/Reactions Distribution"]

    for i, fig in enumerate(figures):
        with plot_cols[i % 2]:
            st.pyplot(fig)

    st.subheader("📋 Average Engagement by Platform")
    st.bar_chart(platform_engagement)

else:
    st.info("Please upload a CSV file to start the analysis.")

st.markdown("---")
st.markdown("Built with Streamlit for easy data analysis!")
