# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("dataset.csv")

# Select important columns
X = data[['Annual Income', 'Spending Score']]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Add cluster column
data['Cluster'] = kmeans.labels_

# Plot clusters
plt.scatter(X['Annual Income'], X['Spending Score'], c=kmeans.labels_)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()