# Customer_Segmentation 
📌 Project Overview

This project focuses on Customer Segmentation using the K-Means Clustering algorithm. The main goal is to group customers based on their annual income and spending score so that businesses can better understand their customers and make smarter marketing decisions.

Instead of treating every customer the same, businesses can divide them into different segments like high-value customers, average customers, and low-spending customers. This helps companies design targeted marketing campaigns, personalized offers, and improve overall business growth.

This project is beginner-friendly and runs smoothly on a normal laptop using Python and basic machine learning libraries.

🎯 Problem Statement

In real life, companies collect a lot of customer data. But raw data alone is not useful unless we analyze it properly.

The problem is:
How can we divide customers into meaningful groups without knowing the categories beforehand?

This is where unsupervised machine learning comes in. Using K-Means clustering, we can automatically group customers based on patterns in their data.

🧠 Concept Used

This project uses:

Unsupervised Learning

K-Means Clustering Algorithm

Data Visualization

K-Means works by:

Choosing a number of clusters (K)

Finding the center (centroid) of each cluster

Assigning customers to the nearest centroid

Updating centroids until stable clusters are formed

It groups customers with similar income and spending behavior together.

📂 Dataset Description

The dataset contains 100 customers with the following features:

CustomerID

Gender

Age

Annual Income (k$)

Spending Score (1–100)

For segmentation, we mainly use:

Annual Income

Spending Score

These two features are enough to identify spending patterns visually.

🛠️ Technologies Used

Python

Pandas (for data handling)

Matplotlib (for visualization)

Scikit-learn (for K-Means algorithm)

VS Code (IDE)

No heavy frameworks like TensorFlow or PyTorch are used. This makes the project lightweight and easy to run on a basic laptop.

▶️ How to Run This Project

Clone the repository:

git clone <your-repo-link>

Navigate to the project folder:

cd Customer_Segmentation

Install required libraries:

pip install pandas matplotlib scikit-learn

Run the project:

python main.py

After running, a graph will appear showing customer clusters in different colors.

📊 Output Explanation

The output is a scatter plot:

X-axis → Annual Income

Y-axis → Spending Score

Different colors → Different customer segments

Each color represents a group of customers with similar behavior.

For example:

One cluster may represent high income and high spending customers (premium customers)

Another cluster may represent low income and low spending customers

Another may represent average customers

This visual segmentation makes it easy to understand customer patterns.

💼 Real-World Applications

Customer segmentation is widely used in:

Retail businesses

E-commerce platforms

Banking sector

Marketing campaigns

Subscription services

Companies use segmentation to:

Offer personalized discounts

Identify loyal customers

Reduce marketing costs

Increase sales efficiency

🚀 Future Improvements

This project can be improved by:

Using the Elbow Method to find optimal K

Adding more features like Age and Gender

Building a Streamlit web app interface

Saving the trained model using Pickle

Deploying it on cloud platforms

📈 What I Learned

While building this project, I learned:

How unsupervised learning works

How K-Means clustering groups data

Data preprocessing basics

Data visualization techniques

How machine learning helps in business decision-making

This project helped me understand the practical side of machine learning rather than just theory.

🧩 Why This Project is Important

Many beginners jump directly into complex deep learning models. But understanding clustering and basic ML algorithms builds a strong foundation.

This project is simple but powerful. It shows how even a basic algorithm can provide meaningful business insights.

🙌 Conclusion

Customer segmentation is a fundamental data science problem. Using K-Means clustering, we successfully grouped customers based on income and spending behavior.

The project is lightweight, beginner-friendly, and practical. It demonstrates how machine learning can solve real business problems using simple logic and visualization.

This is a great starting point for anyone beginning their journey in Machine Learning and Data Science.
<img width="1366" height="728" alt="Image" src="https://github.com/user-attachments/assets/8b3dff72-35b6-443a-8418-d59d85e92738" />






