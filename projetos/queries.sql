SELECT 
order_status AS Status, 
customer_city AS City, 
customer_state AS State
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;

##