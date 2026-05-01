import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load CSV file
df = pd.read_csv("data.csv")

# Remove houses with price = 0 or bedrooms = 0
df_clean = df[(df['price'] > 0) & (df['bedrooms'] > 0)]

# Show first 5 rows
print(df.head())

# Show basic info
print(df.info())

# Describe numerical data
print(df.describe())
import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# Show first 5 rows
print(df.head())

# Show basic info
print(df.info())

# Describe numerical data
print(df.describe())

# -----------------------------
# Step 4: Calculate averages
# -----------------------------
average_price = df['price'].mean()
print("Average house price:", average_price)

average_bedrooms = df['bedrooms'].mean()
print("Average number of bedrooms:", average_bedrooms)
# -----------------------------
# Step 5: Bar chart
# -----------------------------
import matplotlib.pyplot as plt

df['city'].value_counts().plot(kind='bar', figsize=(10,6))
plt.title('Number of Houses per City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()
# -----------------------------
# Scatter plot: Price vs Square Footage of Living Area
# -----------------------------
plt.scatter(df['sqft_living'], df['price'], alpha=0.5)
plt.title('Price vs Living Area')
plt.xlabel('Square Footage of Living Area')
plt.ylabel('Price')
plt.show()
# -----------------------------
# Heatmap: Correlation of numeric features
# -----------------------------
correlation = df.corr(numeric_only=True)

plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
