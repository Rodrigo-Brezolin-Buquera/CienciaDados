import sqlite3
import csv

conn = sqlite3.connect('projetos/database.db')
cursor = conn.cursor()

query = """
SELECT 
    order_status AS Status, 
    customer_city AS City, 
    customer_state AS State
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
"""

cursor.execute(query)

with open('dados_exportados.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([desc[0] for desc in cursor.description])  
    writer.writerows(cursor.fetchall())

conn.close()
