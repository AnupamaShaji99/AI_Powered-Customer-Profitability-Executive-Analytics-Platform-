CREATE TABLE analytics.fact_profitability AS

SELECT
    f.orderdate,
    f.customerkey,
    f.territorykey,

    p.productkey,
    p.productname,

    f.orderquantity,

    p.productprice,
    p.productcost,

    (f.orderquantity * p.productprice) AS revenue,

    (f.orderquantity * p.productcost) AS cost,

    (
        (f.orderquantity * p.productprice)
        -
        (f.orderquantity * p.productcost)
    ) AS profit

FROM analytics.fact_sales f

JOIN analytics.dim_products p
    ON f.productkey = p.productkey;