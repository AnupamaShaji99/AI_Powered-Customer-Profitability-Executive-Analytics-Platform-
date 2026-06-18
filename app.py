import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Generative AI Executive Insights",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🤖 Generative AI Executive Decision Support Dashboard")

st.caption(
    "Generative AI layer built on top of SQL, PostgreSQL and Power BI analytics outputs to automatically generate executive insights and strategic recommendations."
)

# -----------------------------------
# EXECUTIVE METRICS
# -----------------------------------

revenue = 24914586
profit = 10457715
profit_margin = 42
high_value_pct = 25
top_segment = "At Risk"
top_territory = "Australia"
top_occupation = "Professional"
top_income_segment = "Middle Income"

# -----------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------

st.header("Executive Summary")

st.write(
    f"""
Revenue reached **${revenue:,.0f}** with total profit of **${profit:,.0f}**
and a profit margin of **{profit_margin}%**.

The highest-performing territory was **{top_territory}**.

The most profitable occupation group was **{top_occupation}**.

The strongest income segment was **{top_income_segment}**.

High Value customers represent **{high_value_pct}%** of the customer base.
"""
)

# -----------------------------------
# AI INSIGHTS
# -----------------------------------

st.header("🧠 AI Insights")

if top_segment == "At Risk":
    st.warning(
        "A large proportion of customers are classified as At Risk, indicating elevated customer churn risk and the need for targeted retention initiatives."
    )

if profit_margin > 40:
    st.success(
        "Strong profitability provides opportunities for reinvestment, customer acquisition, and business growth initiatives."
    )

if high_value_pct < 30:
    st.info(
        "Only 25% of customers belong to the High Value segment. Increasing customer lifetime value should be a strategic priority."
    )

st.info(
    "Australia is the highest-performing territory and may provide a benchmark for expansion strategies across other regions."
)

st.info(
    "Professional customers generate the highest profitability and represent a valuable segment for future marketing campaigns."
)

# -----------------------------------
# EXECUTIVE RECOMMENDATIONS
# -----------------------------------

st.header("📋 Executive Recommendations")

recommendations = [
    "Launch retention campaigns targeting At Risk customers.",
    "Increase loyalty incentives for medium-value customers.",
    "Replicate successful strategies from Australia's high-performing market.",
    "Develop customer value growth initiatives to expand the High Value segment.",
    "Prioritise Professional customer segments in future marketing strategies.",
    "Invest excess profitability into customer retention and acquisition programs."
]

for rec in recommendations:
    st.write("✅", rec)

# -----------------------------------
# AI GENERATED ACTION PLAN
# -----------------------------------

st.header("🚀 AI Generated Action Plan")

st.markdown("""
### Immediate Actions (0-3 Months)

- Target At Risk customers with retention campaigns.
- Introduce loyalty and rewards programs.
- Identify churn drivers through customer behaviour analysis.

### Medium-Term Actions (3-6 Months)

- Increase High Value customer conversion rates.
- Expand successful Australian business strategies to other territories.
- Strengthen engagement with Professional customer segments.

### Long-Term Actions (6-12 Months)

- Develop predictive customer lifetime value models.
- Implement AI-driven customer retention monitoring.
- Optimise marketing spend toward high-profit customer groups.
""")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Project Stack: PostgreSQL | SQL Analytics | Customer Segmentation (RFM & CLV) | Power BI | Streamlit | Generative AI Insights"
)