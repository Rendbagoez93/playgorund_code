import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Sample data pools
customers = ['Alice Tan', 'Budi Santoso', 'Clara Wijaya', 'Dewi Lestari', 'Eko Prasetyo']
regions = ['North', 'South', 'East', 'West']
products = [
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 450},
    {'name': 'Laptop', 'category': 'Electronics', 'price': 900},
    {'name': 'Office Chair', 'category': 'Furniture', 'price': 120},
    {'name': 'Desk Lamp', 'category': 'Furniture', 'price': 40},
    {'name': 'Notebook', 'category': 'Stationery', 'price': 5}
]

# Generate data
data = []
for i in range(1, 51):
    order_id = f"ORD-{1000 + i}"
    date = datetime.today() - timedelta(days=random.randint(0, 365))
    customer = random.choice(customers)
    region = random.choice(regions)
    product_info = random.choice(products)
    product = product_info['name']
    category = product_info['category']
    unit_price = product_info['price']
    units_sold = random.randint(1, 10)
    total_revenue = unit_price * units_sold

    data.append([
        order_id, date.date(), customer, region,
        product, category, units_sold, unit_price, total_revenue
    ])

# Create DataFrame
columns = ['Order ID', 'Date', 'Customer', 'Region', 'Product', 'Category', 'Units Sold', 'Unit Price', 'Total Revenue']
df = pd.DataFrame(data, columns=columns)

print(df.info())
print(df.describe())

# Total Revenue by Region
revenue_by_region = df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False)
print(revenue_by_region)

df ['Date'] = pd.to_datetime(df['Date'])
df ['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Total Revenue'].sum()
print(monthly_revenue)

top_customers = df.groupby('Customer')['Total Revenue'].sum().sort_values(ascending=False)
print(top_customers)

# Bar chart: Revenue by Region
revenue_by_region.plot(kind='bar', title='Total Revenue by Region', ylabel='Revenue ($)', xlabel='Region')
plt.tight_layout()
plt.show()