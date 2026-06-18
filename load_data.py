from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# PostgreSQL Connection
# -----------------------------

PASSWORD = quote_plus("Minnuseema@123")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{PASSWORD}@localhost:5432/Adventureworks_ai"
)
# -----------------------------
# File Locations
# -----------------------------

base_path = r"C:\Users\Anupama S\Downloads\adventureworks files"

files = {
    "customers": "AdventureWorks_Customers.csv",
    "products": "AdventureWorks_Products.csv",
    "product_categories": "AdventureWorks_Product_Categories.csv",
    "product_subcategories": "AdventureWorks_Product_Subcategories.csv",
    "territories": "AdventureWorks_Territories.csv",
    "sales_2015": "AdventureWorks_Sales_2015.csv",
    "sales_2016": "AdventureWorks_Sales_2016.csv",
    "sales_2017": "AdventureWorks_Sales_2017.csv",
    "returns": "AdventureWorks_Returns.csv",
    "calendar": "AdventureWorks_Calendar.csv"
}

# -----------------------------
# Load Files
# -----------------------------

for table_name, file_name in files.items():

    full_path = f"{base_path}\\{file_name}"

    print(f"Loading {table_name}...")

    df = pd.read_csv(full_path, encoding="latin1")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df.to_sql(
        table_name,
        engine,
        schema="staging",
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df):,} rows into staging.{table_name}")

print("\nAll files loaded successfully.")