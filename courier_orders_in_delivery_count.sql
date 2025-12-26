SELECT
    c.login,
    COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
JOIN "Orders" o
  ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login;