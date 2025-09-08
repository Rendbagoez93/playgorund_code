import pandas as pd

# Load the CSV
df = pd.read_csv('data/raw/Trending_Movies.csv')  # Replace with your file name

# Preview the data
print("\nSample Data:\n", df.head())

# Total entries
print("\nTotal Movies:", len(df))

# Most popular movies
top_popularity = df[['title', 'popularity']].sort_values(by='popularity', ascending=False).head(10)
print("\n🔥 Top 10 Most Popular Movies:\n", top_popularity)

# Highest-rated movies
top_rated = df[['title', 'vote_average', 'vote_count']].sort_values(by='vote_average', ascending=False).head(10)
print("\n🌟 Top 10 Highest Rated Movies:\n", top_rated)

# Release date range
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')  # Handle invalid dates
print("\n📅 Date Range:", df['release_date'].min(), "to", df['release_date'].max())

# Language distribution
language_counts = df['original_language'].value_counts().head(5)
print("\n🗣️ Most Common Original Languages:\n", language_counts)

# Adult content analysis
adult_counts = df['adult'].value_counts()
print("\n🔞 Adult vs Non-Adult:\n", adult_counts)

# Average rating and vote count
avg_rating = df['vote_average'].mean()
avg_votes = df['vote_count'].mean()
print("\n📊 Average Rating:", round(avg_rating, 2))
print("🗳️ Average Vote Count:", int(avg_votes))
#=========== " Data Analysis Complete" ===========

