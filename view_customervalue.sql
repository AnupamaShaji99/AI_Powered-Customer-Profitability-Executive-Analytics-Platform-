CREATE OR REPLACE VIEW analytics.vw_customer_value AS

SELECT
    customerkey,

    ROUND(SUM(revenue)::numeric,2) AS total_revenue,

    ROUND(SUM(profit)::numeric,2) AS total_profit,

    COUNT(*) AS purchase_events,

    SUM(orderquantity) AS total_units

FROM analytics.fact_profitability

GROUP BY customerkey;

