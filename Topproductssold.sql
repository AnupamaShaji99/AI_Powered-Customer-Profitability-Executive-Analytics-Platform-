SELECT
    p.productname,
    SUM(f.orderquantity) AS units_sold
FROM analytics.fact_sales f
JOIN analytics.dim_products p
    ON f.productkey = p.productkey
GROUP BY p.productname
ORDER BY units_sold DESC
LIMIT 10;