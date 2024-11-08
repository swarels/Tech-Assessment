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

# 2. Data Analysis: Provide a summary of the dataset, including:
# - Total number of transactions
# - Total revenue for each transaction (price x quantity)
# - The number of unique products sold 
# - The most common product categories 

# Provide some visualisation of the following two insights from the dataset:
# - Total sales per category 
# - How sales have changed over time

# 3. Customer Segmentation: Group customers into three segments based on total 
# spending habits: low, medium, and high spenders. Explain why you defined the 
# thresholds for each segment. 

# 4. Machine Learning: Build a simple machine learning model using the data 
# (e.g. linear regression, decision tree) to predict customer spending behaviour 
# or identify patterns.

# We encourage candidates to refrain from using large language models (LLMs) 
# like ChatGPT when coding their solutions, as we would prefer to assess their
# individual coding skills directly.