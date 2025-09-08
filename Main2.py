import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('data/raw/Trending_Movies.csv')  # Replace with your file name

print("Columns in DataFrame:", df.columns.tolist())  # Debug: print column names    

# Now you can run all your summaries or sorting on this subset
top_rated = df.sort_values(by='vote_average', ascending=False)
top_10 = top_rated[['title', 'vote_average', 'vote_count', 'release_date']].head(10)
print("\n🌟 Top 10 Highest Rated (First 50):\n", top_10)
print ('=' * 10)

# Make sure release_date is datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['release_year'] = df['release_date'].dt.year

# Drop missing years
df = df.dropna(subset=['release_year'])

# Convert to int
df['release_year'] = df['release_year'].astype(int)

# Create 5-year bins
bin_size = 5
start_year = df['release_year'].min() // bin_size * bin_size
end_year = df['release_year'].max() // bin_size * bin_size + bin_size
bins = list(range(start_year, end_year + bin_size, bin_size))
labels = [f"{b}-{b+bin_size-1}" for b in bins[:-1]]

# Bin the years
df['year_interval'] = pd.cut(df['release_year'], bins=bins, labels=labels, right=False)

# Count movies per interval
interval_counts = df['year_interval'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 5))
interval_counts.plot(kind='bar', color='mediumseagreen', edgecolor='black')
plt.title('🎬 Movie Releases by 5-Year Interval')
plt.xlabel('Year Interval')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

print ('=' * 10)
# Choose thresholds
popularity_median = df['popularity'].median()
rating_threshold = 7.5  # You can tweak this

# Filter hidden gems
hidden_gems = df[(df['popularity'] < popularity_median) & (df['vote_average'] >= rating_threshold)]

# Preview
print("💎 Hidden Gems:\n", hidden_gems[['title', 'vote_average', 'popularity', 'release_date']])
print ('=' * 10)

# Top languages by count
language_counts = df['original_language'].value_counts()
print("\n🗣️ Language Counts:\n", language_counts.head())

# Average rating per language
language_ratings = df.groupby('original_language')['vote_average'].mean().sort_values(ascending=False)
print("\n🌐 Avg Rating by Language:\n", language_ratings.head())