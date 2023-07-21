SELECT c.login, COUNT(o.id) AS num_orders_in_delivery
FROM Couriers c
LEFT JOIN Orders o ON c.id = o.courierId
WHERE o.inDelivery = true
GROUP BY c.login;