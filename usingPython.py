import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("eastVantage.db")

# Read all tables into DataFrames
customers = pd.read_sql_query("SELECT * FROM customers", conn)
sales = pd.read_sql_query("SELECT * FROM sales", conn)
orders = pd.read_sql_query("SELECT * FROM orders", conn)
items = pd.read_sql_query("SELECT * FROM items", conn)

# Merge DataFrames based on foreign key relationships
merged_data = customers.merge(sales, on="customer_id")
merged_data = merged_data.merge(orders, on="sales_id")
merged_data = merged_data.merge(items, on="item_id")

# Filter for customers aged 18-35 and non-zero quantities
filtered_data = merged_data[(merged_data["age"] >= 18) & (merged_data["age"] <= 35) & (merged_data["quantity"] > 0)]

# Group by customer, age, and item, then sum quantities
grouped_data = filtered_data.groupby(["customer_id", "age", "item_name"])["quantity"].sum().reset_index()

grouped_data["quantity"] = grouped_data["quantity"].astype(int)

# Close the connection
conn.close()

# Save data to CSV file with semicolon delimiter
grouped_data.to_csv("python_output.csv", index=False, sep=";")
