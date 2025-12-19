# TASK 7: Basic Sales Summary Using SQLite and Python

## Objective

The goal of this task is to use SQL inside Python to extract basic sales insights from a small SQLite database and visualize the results using a simple bar chart.

Specifically, the task demonstrates:

* Connecting to a SQLite database using Python
* Running SQL aggregation queries
* Displaying results using print statements
* Generating and saving a basic matplotlib bar chart

---

## Tools & Technologies Used

* Python
* SQLite (via `sqlite3`, built into Python)
* pandas
* matplotlib

---

## Dataset

A small SQLite database file named **`sales_data.db`** is created programmatically.
It contains a single table called **`sales`** with the following columns:

* `id` (Primary Key)
* `product` (Product name)
* `quantity` (Units sold)
* `price` (Unit price)

Sample products include Laptop, Mouse, Keyboard, and Monitor.

---

## Steps Performed

### 1. Database Creation & Connection

* Connected to a SQLite database named `sales_data.db`
* Created a `sales` table if it did not already exist
* Inserted sample sales records into the table

### 2. SQL Query Execution

Executed an SQL query inside Python to calculate:

* Total quantity sold per product
* Total revenue per product

```sql
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
```

The query results were loaded into a pandas DataFrame.

---

### 3. Output Display

* Printed the aggregated sales summary to the console using `print(df)`
* Created a simple bar chart showing **revenue by product**

---

### 4. Chart Generation

* Generated a basic matplotlib bar chart using:

```python
df.plot(kind='bar', x='product', y='revenue')
```

* Saved the chart as an image file named **`sales_chart.png`**

---

## Outputs

### Console Output

* A table displaying:

  * Product name
  * Total quantity sold
  * Total revenue

### Visual Output

* **`sales_chart.png`**
  A simple bar chart visualizing total revenue per product.

---

## Files in This Repository

* `sales_summary.py` *(or Jupyter Notebook)* – Python script containing the full implementation
* `sales_data.db` – SQLite database file
* `sales_chart.png` – Generated bar chart image
* `README.md` – Task explanation and documentation

---

## Conclusion

This task demonstrates how SQL can be used inside Python to perform basic data analysis and visualization using a lightweight SQLite database. It fulfills all deliverables by combining database operations, SQL queries, printed output, and graphical representation.

---

