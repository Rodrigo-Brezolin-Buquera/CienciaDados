-- Tabela: geolocation
CREATE TABLE geolocation (
    geolocation_zip_code_prefix INTEGER,
    geolocation_lat REAL,
    geolocation_lng REAL,
    geolocation_city VARCHAR(17),
    geolocation_state CHAR(2),
    PRIMARY KEY (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng)
);


-- Tabela: category_name
CREATE TABLE category_name (
    product_category_name VARCHAR(50),
    product_category_name_english VARCHAR(50)
);

-- Tabela: sellers
CREATE TABLE sellers (
    seller_id CHAR(32) PRIMARY KEY,
    seller_zip_code_prefix INTEGER,
    seller_city VARCHAR(30),
    seller_state CHAR(2),
    FOREIGN KEY (seller_zip_code_prefix) REFERENCES geolocation(geolocation_zip_code_prefix)
);

-- Tabela: products
CREATE TABLE products (
    product_id CHAR(32) PRIMARY KEY,
    product_category_name VARCHAR(50),
    product_name_lenght SMALLINT,
    product_description_lenght SMALLINT,
    product_photos_qty SMALLINT,
    product_weight_g SMALLINT,
    product_length_cm SMALLINT,
    product_height_cm SMALLINT,
    product_width_cm SMALLINT,
    FOREIGN KEY (product_category_name) REFERENCES category_name(product_category_name)
);

-- Tabela: order_items
CREATE TABLE order_items (
    order_id CHAR(32),
    order_item_id SMALLINT,
    product_id CHAR(32),
    seller_id CHAR(32),
    shipping_limit_date DATETIME,
    price DECIMAL,
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

-- Tabela: customers
CREATE TABLE customers (
    customer_id CHAR(32) PRIMARY KEY,
    customer_unique_id CHAR(32),
    customer_zip_code_prefix INTEGER,
    customer_city VARCHAR(30),
    customer_state CHAR(2),
    FOREIGN KEY (customer_zip_code_prefix) REFERENCES geolocation(geolocation_zip_code_prefix)
);

-- Tabela: orders
CREATE TABLE orders (
    order_id CHAR(32) PRIMARY KEY,
    customer_id CHAR(32),
    order_status VARCHAR(12),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_unique_id)
);

-- Tabela: order_payments
CREATE TABLE order_payments (
    order_id CHAR(32),
    payment_sequential SMALLINT,
    payment_type CHAR(12),
    payment_installments SMALLINT,
    payment_value DECIMAL,
    PRIMARY KEY (order_id, payment_sequential),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Tabela: order_reviews
CREATE TABLE order_reviews (
    review_id CHAR(32) PRIMARY KEY,
    order_id CHAR(32),
    review_score SMALLINT,
    review_comment_title VARCHAR(50),
    review_comment_message TEXT,
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
