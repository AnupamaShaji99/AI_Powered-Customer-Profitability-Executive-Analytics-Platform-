CREATE OR REPLACE VIEW analytics.vw_customer_demographics AS

SELECT
    c.customerkey,
    c.gender,
    c.occupation,
    c.educationlevel,
    c.annualincome,

    SUM(fp.revenue) AS revenue,
    SUM(fp.profit) AS profit

FROM analytics.fact_profitability fp

JOIN analytics.dim_customers c
ON fp.customerkey = c.customerkey

GROUP BY
    c.customerkey,
    c.gender,
    c.occupation,
    c.educationlevel,
    c.annualincome;