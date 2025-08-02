import csv
import sqlite3
import pandas as pd


conn = sqlite3.connect('projetos/database.db')
cursor = conn.cursor()


# with open("projetos/archive/olist_geolocation_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:

#         geolocation_zip_code_prefix = int(line[0])  
#         geolocation_lat = float(line[1])           
#         geolocation_lng = float(line[2])           
#         geolocation_city = line[3]                 
#         geolocation_state = line[4]                

#         cursor.execute('''
#             INSERT OR IGNORE INTO geolocation (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state))


# with open("projetos/archive/product_category_name_translation.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         product_category_name = line[0]
#         product_category_name_english = line[1]

#         cursor.execute('''
#             INSERT INTO category_name (product_category_name, product_category_name_english)
#             VALUES (?, ?)
#         ''', (product_category_name, product_category_name_english))

# with open("projetos/archive/olist_sellers_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         seller_id = line[0]
#         seller_zip_code_prefix = int(line[1])
#         seller_city = line[2]
#         seller_state = line[3]

#         cursor.execute('''
#             INSERT INTO sellers (seller_id, seller_zip_code_prefix, seller_city, seller_state)
#             VALUES (?, ?, ?, ?)
#         ''', (seller_id, seller_zip_code_prefix, seller_city, seller_state))

# with open("projetos/archive/olist_products_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         product_id = line[0]
#         product_category_name = line[1]
#         product_name_lenght = int(line[2]) if line[2] else 0
#         product_description_lenght = int(line[3]) if line[3] else 0
#         product_photos_qty = int(line[4]) if line[4] else 0
#         product_weight_g = int(line[5]) if line[5] else 0
#         product_length_cm = int(line[6]) if line[6] else 0
#         product_height_cm = int(line[7]) if line[7] else 0
#         product_width_cm = int(line[8]) if line[8] else 0

#         cursor.execute('''
#             INSERT INTO products (
#                 product_id, product_category_name, product_name_lenght, 
#                 product_description_lenght, product_photos_qty, product_weight_g, 
#                 product_length_cm, product_height_cm, product_width_cm)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (product_id, product_category_name, product_name_lenght, product_description_lenght,
#               product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm))

# with open("projetos/archive/olist_order_items_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
        # order_id = line[0]
        # order_item_id = int(line[1])
        # product_id = line[2]
        # seller_id = line[3]
        # shipping_limit_date = line[4]
        # price = float(line[5])

        # cursor.execute('''
        #     INSERT INTO order_items (
        #         order_id, order_item_id, product_id, seller_id, shipping_limit_date, price)
        #     VALUES (?, ?, ?, ?, ?, ?)
        # ''', (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price))

# with open("projetos/archive/olist_customers_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         customer_id = line[0]
#         customer_unique_id = line[1]
#         customer_zip_code_prefix = int(line[2])
#         customer_city = line[3]
#         customer_state = line[4]

#         cursor.execute('''
#             INSERT INTO customers (
#                 customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state))

# with open("projetos/archive/olist_orders_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         order_id = line[0]
#         customer_id = line[1]
#         order_status = line[2]
#         order_purchase_timestamp = line[3]
#         order_approved_at = line[4]
#         order_delivered_carrier_date = line[5]
#         order_delivered_customer_date = line[6]
#         order_estimated_delivery_date = line[7]

#         cursor.execute('''
#             INSERT INTO orders (
#                 order_id, customer_id, order_status, order_purchase_timestamp, 
#                 order_approved_at, order_delivered_carrier_date, 
#                 order_delivered_customer_date, order_estimated_delivery_date)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (order_id, customer_id, order_status, order_purchase_timestamp, 
#               order_approved_at, order_delivered_carrier_date, 
#               order_delivered_customer_date, order_estimated_delivery_date))

# with open("projetos/archive/olist_order_payments_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         order_id = line[0]
#         payment_sequential = int(line[1])
#         payment_type = line[2]
#         payment_installments = int(line[3])
#         payment_value = float(line[4])

#         cursor.execute('''
#             INSERT INTO order_payments (
#                 order_id, payment_sequential, payment_type, payment_installments, payment_value)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (order_id, payment_sequential, payment_type, payment_installments, payment_value))

# with open("projetos/archive/olist_order_reviews_dataset.csv", "r") as table:
#     reader = csv.reader(table)
#     next(reader) 
#     for line in reader:
#         review_id = line[0]
#         order_id = line[1]
#         review_score = int(line[2])
#         review_comment_title = line[3]
#         review_comment_message = line[4]
#         review_creation_date = line[5]
#         review_answer_timestamp = line[6]

#         cursor.execute('''
#             INSERT OR IGNORE INTO order_reviews (
#                 review_id, order_id, review_score, review_comment_title, 
#                 review_comment_message, review_creation_date, review_answer_timestamp)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (review_id, order_id, review_score, review_comment_title, 
#               review_comment_message, review_creation_date, review_answer_timestamp))


conn.commit()
conn.close()
