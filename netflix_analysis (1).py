import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv(r"C:\Users\SINCHANA H M\Downloads\38833FF26BA1D.UnigramPreview_g9c9v27vpyspw!App\Netflix Dataset.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("=== Netflix Dataset Analysis ===\n")
print("Columns:", df.columns.tolist())
print("\nMissing values per column:\n", df.isnull().sum())

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(subset=['category', 'country', 'release_date', 'type'], inplace=True)

# -------------------------------
# 1. Movies vs TV Shows distribution
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='category', palette='pastel')
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Content trend over the years
# -------------------------------
# Extract year from release_date column
df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
yearly_content = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
yearly_content.plot(kind='bar', color='coral')
plt.title('Netflix Content Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Category-wise content over years
# -------------------------------
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='release_year', hue='category', palette='coolwarm')
plt.title('Movies vs TV Shows Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Summary Insights
# -------------------------------
print("\n=== Summary Insights ===")
print(f"Total Titles: {len(df)}")
print(f"Movies: {len(df[df['category'].str.contains('Movie', case=False)])}")
print(f"TV Shows: {len(df[df['category'].str.contains('TV', case=False)])}")
print("\nTop 5 Countries:\n", country_counts.head())

print("\n✅ Analysis Completed Successfully!")