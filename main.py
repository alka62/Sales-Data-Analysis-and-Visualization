import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("/content/sales_data (2).csv")

# Dataset preview
print(data.head())

# Check missing values
print(data.isnull().sum())

# Basic info
print(data.info())

# 1️⃣ Product wise total sales
product_sales = data.groupby("Product")["Total_Sales"].sum()

plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# 2️⃣ Region wise sales
region_sales = data.groupby("Region")["Total_Sales"].sum()

plt.figure()
region_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# 3️⃣ Quantity sold by product
quantity_sales = data.groupby("Product")["Quantity"].sum()

plt.figure()
quantity_sales.plot(kind="line")
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.show()

# Insights
print("Highest selling product:", product_sales.idxmax())
print("Lowest selling product:", product_sales.idxmin())
