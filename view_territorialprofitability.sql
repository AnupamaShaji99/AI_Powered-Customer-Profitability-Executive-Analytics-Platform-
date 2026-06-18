CREATE OR REPLACE VIEW analytics.vw_territory_profitability AS

SELECT
    t.country,
    t.region,

    ROUND(SUM(fp.revenue)::numeric, 2) AS revenue,
    ROUND(SUM(fp.profit)::numeric, 2) AS profit,

    ROUND(
    (
        SUM(fp.profit)
        /
        NULLIF(SUM(fp.revenue),0)
        * 100
    )::numeric,
    2
) AS profit_margin_pct

FROM analytics.fact_profitability fp

JOIN analytics.dim_territories t
    ON fp.territorykey = t.salesterritorykey

GROUP BY
    t.country,
    t.region;