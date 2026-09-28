-- KPI query patterns for a normalized retail_orders table.
SELECT COUNT(DISTINCT order_id) AS total_orders FROM retail_orders;

SELECT SUM(quantity*unit_price) AS gross_sales
FROM retail_orders WHERE quantity>0 AND unit_price>=0;

SELECT SUM(quantity*unit_price*discount_pct/100.0) AS discount_amount
FROM retail_orders
WHERE quantity>0 AND unit_price>=0 AND discount_pct BETWEEN 0 AND 100;

SELECT SUM(quantity*unit_price*(1-discount_pct/100.0)) AS net_sales
FROM retail_orders
WHERE quantity>0 AND unit_price>=0 AND discount_pct BETWEEN 0 AND 100;

SELECT SUM(quantity) AS units_sold
FROM retail_orders WHERE quantity>0;

SELECT customer_segment,COUNT(DISTINCT order_id) AS orders
FROM retail_orders GROUP BY customer_segment;

SELECT payment_status,COUNT(DISTINCT order_id) AS orders
FROM retail_orders GROUP BY payment_status;
