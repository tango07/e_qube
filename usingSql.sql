SELECT c.age, i.item_name, COALESCE(SUM(o.quantity), 0) AS quantity
FROM customers AS c
INNER JOIN sales s ON c.customer_id = s.customer_id
INNER JOIN orders o ON s.sales_id = o.sales_id
INNER JOIN items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
AND o.quantity IS NOT NULL
GROUP BY c.customer_id, c.age, i.item_id, i.item_name
ORDER BY c.customer_id, c.age, i.item_name;
