# sales_data.py
# This script loads sales data, cleans it, saves the cleaned data. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- Streamlit Dashboard ---
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Data Dashboard")

# Load and clean data
df = pd.read_csv('data/raw/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)
df['Month'] = df['Date'].dt.to_period('M')

# Save cleaned data
df.to_excel("data/processed/cleaned_sales_data.xlsx", index=False)

st.success("Data cleaned and saved to 'data/processed/cleaned_sales_data.xlsx'.")


# --- Streamlit Dashboard Visualizations ---
# 1. Total Revenue by Product
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(x=product_sales.values, y=product_sales.index, ax=ax1)
ax1.set_title("Total Revenue by Product")
ax1.set_xlabel("Revenue")
ax1.set_ylabel("Product")
st.subheader("Total Revenue by Product")
st.pyplot(fig1)

# 2. Monthly Revenue Trend
monthly_sales = df.groupby('Month')['Revenue'].sum()
fig2, ax2 = plt.subplots(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', ax=ax2)
ax2.set_title("Monthly Revenue Trend")
ax2.set_ylabel("Revenue")
ax2.grid(True)
st.subheader("Monthly Revenue Trend")
st.pyplot(fig2)

# 3. Top 5 Customers by Revenue
top_customers = df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False).head(5)
fig3, ax3 = plt.subplots(figsize=(7,4))
top_customers.plot(kind='bar', color='teal', ax=ax3)
ax3.set_title("Top 5 Customers by Revenue")
ax3.set_ylabel("Revenue")
ax3.set_xticklabels(top_customers.index, rotation=45)
st.subheader("Top 5 Customers by Revenue")
st.pyplot(fig3)

# 4. Revenue Share by Region
region_sales = df.groupby('Region')['Revenue'].sum()
fig4, ax4 = plt.subplots()
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax4)
ax4.set_title("Revenue Share by Region")
ax4.set_ylabel("")
st.subheader("Revenue Share by Region")
st.pyplot(fig4)


# --- Matplotlib/Seaborn Only Visualizations ---
if __name__ == "__main__":
	print("\nDisplaying charts using matplotlib/seaborn only (no Streamlit)...\n")
	# 1. Total Revenue by Product
	plt.figure(figsize=(8,5))
	sns.barplot(x=product_sales.values, y=product_sales.index)
	plt.title("Total Revenue by Product")
	plt.xlabel("Revenue")
	plt.ylabel("Product")
	plt.tight_layout()
	plt.show()

	# 2. Monthly Revenue Trend
	plt.figure(figsize=(10,5))
	monthly_sales.plot(kind='line', marker='o')
	plt.title("Monthly Revenue Trend")
	plt.ylabel("Revenue")
	plt.grid(True)
	plt.tight_layout()
	plt.show()

	# 3. Top 5 Customers by Revenue
	plt.figure(figsize=(7,4))
	top_customers.plot(kind='bar', color='teal')
	plt.title("Top 5 Customers by Revenue")
	plt.ylabel("Revenue")
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()

	# 4. Revenue Share by Region
	plt.figure()
	region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140)
	plt.title("Revenue Share by Region")
	plt.ylabel("")
	plt.tight_layout()
	plt.show()

