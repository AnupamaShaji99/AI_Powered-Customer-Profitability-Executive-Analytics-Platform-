CREATE OR REPLACE VIEW analytics.vw_product_profitability AS

SELECT
    productname,

    SUM(revenue) AS revenue,
    SUM(cost) AS cost,
    SUM(profit) AS profit,

    SUM(orderquantity) AS units_sold

FROM analytics.fact_profitability

GROUP BY productname;