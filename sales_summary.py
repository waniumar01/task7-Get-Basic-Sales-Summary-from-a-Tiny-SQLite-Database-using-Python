# TASK 7: Basic Sales Summary using SQLite and Python

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Connect to SQLite DB
# -----------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# -----------------------------
# Step 2: Create sales table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# -----------------------------
# Step 3: Insert sample data
# -----------------------------
cursor.execute("DELETE FROM sales")  # Clear old data if script reruns

sample_data = [
    ("Laptop", 2, 60000),
    ("Laptop", 1, 60000),
    ("Mouse", 10, 500),
    ("Keyboard", 5, 1500),
    ("Monitor", 3, 12000),
    ("Mouse", 8, 500)
]

cursor.executemany(
    "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
    sample_data
)

conn.commit()

# -----------------------------
# Step 4: Run SQL query
# -----------------------------
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

# -----------------------------
# Step 5: Display output
# -----------------------------
print("Basic Sales Summary:\n")
print(df)

# -----------------------------
# Step 6: Plot bar chart
# -----------------------------
df.plot(kind="bar", x="product", y="total_revenue", legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()

# Save chart (optional)
plt.savefig("sales_chart.png")

plt.show()

# -----------------------------
# Step 7: Close connection
# -----------------------------
conn.close()
