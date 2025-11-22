"""
Social Media Analysis Project
A beginner-friendly data analysis script to explore social media engagement data.
This script loads data, performs basic analysis, and visualizes key insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_data(file_path):
    """
    Load the social media data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def clean_data(df):
    """
    Clean the dataframe by stripping spaces and replacing them with underscores in column names.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]
    print("Column names cleaned.")
    return df

def analyze_data(df):
    """
    Perform basic analysis on the dataframe: compute stats, top posts, etc.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        tuple: (df, platform_engagement, top_posts, top_verified, stats)
    """
    # Calculate total engagement
    df["Total_Engagement"] = df["Likes/Reactions"] + df["Comments"] + df["Shares/Retweets"]

    # Basic statistics
    stats = df[["Likes/Reactions", "Comments", "Shares/Retweets"]].describe()

    # Top 5 most engaging posts
    top_posts = df.sort_values(by="Total_Engagement", ascending=False)[["Username", "Platform", "Total_Engagement"]].head()

    # Average engagement by platform
    platform_engagement = df.groupby("Platform")["Total_Engagement"].mean()

    # Top 5 verified users by followers
    verified_users = df[df["Account_Verification"] == "Verified"]
    top_verified = verified_users.sort_values(by="User_Followers", ascending=False)[["Username", "User_Followers"]].head()

    return df, platform_engagement, top_posts, top_verified, stats

def visualize_data(df, platform_engagement):
    """
    Create visualizations for the data.

    Args:
        df (pd.DataFrame): Input dataframe.
        platform_engagement (pd.Series): Average engagement by platform.

    Returns:
        list: List of matplotlib figures.
    """
    figures = []

    # Bar plot for average engagement by platform
    fig1, ax1 = plt.subplots()
    platform_engagement.plot(kind="bar", color='skyblue', ax=ax1)
    ax1.set_title("Average Engagement by Platform")
    ax1.set_xlabel("Platform")
    ax1.set_ylabel("Average Engagement")
    plt.xticks(rotation=45)
    plt.tight_layout()
    figures.append(fig1)

    # Scatter plot for followers vs engagement
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["User_Followers"], df["Total_Engagement"], alpha=0.5, color='green')
    ax2.set_title("Followers vs Total Engagement")
    ax2.set_xlabel("User Followers")
    ax2.set_ylabel("Total Engagement")
    plt.tight_layout()
    figures.append(fig2)

    # Histogram for total engagement
    fig3, ax3 = plt.subplots()
    ax3.hist(df["Total_Engagement"], bins=20, color='orange', edgecolor='black')
    ax3.set_title("Distribution of Total Engagement")
    ax3.set_xlabel("Total Engagement")
    ax3.set_ylabel("Frequency")
    plt.tight_layout()
    figures.append(fig3)

    # Histogram for likes/reactions
    fig4, ax4 = plt.subplots()
    ax4.hist(df["Likes/Reactions"], bins=20, color='purple', edgecolor='black')
    ax4.set_title("Distribution of Likes/Reactions")
    ax4.set_xlabel("Likes/Reactions")
    ax4.set_ylabel("Frequency")
    plt.tight_layout()
    figures.append(fig4)

    return figures

def main():
    """
    Main function to run the analysis.
    """
    file_path = "social_media_data.csv"
    df = load_data(file_path)
    df = clean_data(df)
    df, platform_engagement, top_posts, top_verified, stats = analyze_data(df)
    figures = visualize_data(df, platform_engagement)
    print("\nAnalysis complete!")
    return df, platform_engagement, top_posts, top_verified, stats, figures

if __name__ == "__main__":
    main()
