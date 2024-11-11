# ---------------------------------------------------------------------------- #
#                         Customer Transaction Analysis                        #
# ---------------------------------------------------------------------------- #

# -------------------------------- BACKGROUND -------------------------------- #

# The file fake_customer_transactions.csv contains a customer transaction 
# database from a fake retail store that contains the following columns: 
# - customer_id: a unique identifier for each customer 
# - transaction_date: a timestamp of the transaction 
# - product_id: a unique identifier for each product 
# - quantity: the quantity of the product purchased
# - price: the price of the product 
# - category: the category of the product 

# Please use this data to complete the tasks below.

# -------------------------------- REQUIREMENTS ------------------------------- #

# 1. Data Cleaning: Using Python, load the data into a Pandas DataFrame. Check 
# for any missing values and provide a strategy for how to handle them. Ensure 
# that all entries in the `transaction_date` column are in the correct format 
# (datetime).


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kmeans1d
from sklearn import linear_model



pd.set_option('display.max_rows', 100)

# Read data
df = pd.read_csv("fake_customer_transactions.csv")


## Part 1 - Data Cleaning

og_df_len = len(df.index)

# Change time to datetime datatype
mask = df['transaction_date'].str.contains(r'^\d{4}/\d{2}/\d{2}$')
df.loc[mask, 'transaction_date'] = pd.to_datetime(df.loc[mask, 'transaction_date'], format='%Y/%m/%d').dt.strftime('%Y-%m-%d')
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

# Remove rows missing "quantity" value
df = df.dropna(subset=['quantity'])

# Calculate the average price of each category
averages = df.groupby('category')["price"].mean()

# Replace price nan values with the average price of the corresponding category
for index, row in df.iterrows():
    if (np.isnan(df["price"][index])):
        df.loc[index, "price"] = averages[row["category"]]



# 2. Data Analysis: Provide a summary of the dataset, including:
# - Total number of transactions
# - Total revenue for each transaction (price x quantity)
# - The number of unique products sold 
# - The most common product categories 

print("---------------------------------------------------")
## Part 2 - Data Analysis
print("**PT.2 - SUMMARY**")
print("")

print("The total number of transactions (before cleaning): ", og_df_len)
print("The total number of transactions (after cleaning): ", len(df.index))
print("")

print("Total revenue for each transaction:")
for index, row in df.iterrows():
    print("For index:", index, ", Customer ID:", row["customer_id"], ", Total revenue: $", round(row["price"] * row["quantity"], 2))
print("")

print("Number of unique products sold:", len(df["product_id"].unique()))
print("")

print("Most common product categories:")
print(df["product_id"].value_counts())


# Graph of Total Sales per Category
df["total_sales"] = df["quantity"] * df["price"]
category_sales = df.groupby('category')["total_sales"].sum()
categories = df["category"].unique()

# plt.bar(categories, category_sales)
# plt.show()
## ^ I CAN'T GET MATPLOTLIB TO WORK ON MY DEVICE, BUT IT SHOULD BE SOMETHING LIKE THIS?
## "This probably means that Tcl wasn't installed properly" error

# Grapho of how sales has changed over time
# plt.plot(df["transaction_date"], df["total_sales"])
# plt.show()
## ^ Again, I CAN'T GET MATPLOTLIB TO WORK, SHOULD BE SOMETHING LIKE THIS


# Provide some visualisation of the following two insights from the dataset:
# - Total sales per category 
# - How sales have changed over time

# Part 3 - Customer Segmentation: Group customers into three segments based on total 
#           spending habits: low, medium, and high spenders. Explain why you defined the 
#           thresholds for each segment. 
print("-------------------------------------------------------")

# Find average spend, per customer, each time they come
cust_avg_spend = df.groupby('customer_id')["total_sales"].mean()
# print(cust_avg_spend)

# customer_total_sales = df.groupby('customer_id')["total_sales"].sum()
k = 3

clusters, centroids = kmeans1d.cluster(cust_avg_spend, k)

# print(customer_total_sales)
# print(clusters)
# print(centroids)

spender = {
    0: "Low Spender",
    1: "Medium Spender",
    2: "High Spender"
}

for customer_index in range(len(sorted(df["customer_id"].unique()))):

    print("customer:", sorted(df["customer_id"].unique())[customer_index], "is considered a", spender[clusters[customer_index]])
    # print("customer: ", sorted(df["customer_id"][customer_index]), "is considered a ", clusters[customer_index])


# This was done through K-means clustering, with k = 3



# Part 4 - Machine Learning: Build a simple machine learning model using the data 
#           (e.g. linear regression, decision tree) to predict customer spending behaviour 
#           or identify patterns.

# Add Dummy variables for categorical linear regression
df["is_HomeAppliances"] = (df["category"] == "Home Appliances").astype(int)
df["is_Clothing"] = (df["category"] == "Clothing").astype(int)
df["is_Sports"] = (df["category"] == "Sports").astype(int)
df["is_Groceries"] = (df["category"] == "Groceries").astype(int)
df["is_Electronics"] = (df["category"] == "Electronics").astype(int)
df["is_Furniture"] = (df["category"] == "Furniture").astype(int)

# Create a linear regression to estimate the total spend, depending on the category, and the quantity of items spend
y = df["total_sales"]
x = df[["quantity", "is_HomeAppliances", "is_Clothing", "is_Sports", "is_Groceries", "is_Electronics", "is_Furniture"]]

regr = linear_model.LinearRegression()
regr.fit(x, y) 

# The coefficients of the linear model
print(regr.coef_)

# What do we predict the total spending would be if the customer bought 2 items, in the Home Appliances category?
print(regr.predict([[2, 1, 0, 0, 0, 0, 0,]]))


# Our coefficients output tells us, as expected, increasing the number of items purchased
# is the largest contributing factor to increased sales, on average increasing the price spent by ~$50
# It also seems that the groceries category correlates to the most amount of money spend, on average
# increasing the amoutn spent by ~$18, whereas if the category is Furniture, you could expect the money spent
# to decrease by ~$24




# We encourage candidates to refrain from using large language models (LLMs) 
# like ChatGPT when coding their solutions, as we would prefer to assess their
# individual coding skills directly.