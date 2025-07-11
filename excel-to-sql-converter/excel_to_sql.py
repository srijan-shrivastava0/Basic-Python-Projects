import pandas as pd

# Load Excel file
excel_file = "data.xlsx"
sheet_name = "Sheet1"  # Change if needed
table_name = "students"  # SQL table name

# Read Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Create SQL file
with open("output.sql", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        values = "', '".join(str(x).replace("'", "''") for x in row.values)
        sql = f"INSERT INTO {table_name} VALUES ('{values}');\n"
        f.write(sql)

print("✅ SQL file generated: output.sql")
