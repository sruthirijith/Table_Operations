
import psycopg2
import pandas as pd
import crud


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="XPB_Api_dev",
    user="postgres",
    password="ivania2019",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Define the table name
table_name = 'bde'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(r'C:\Users\xpayb\Desktop\XPB Employee ID .xlsx')
cursor = conn.cursor()

for _, row in df.iterrows():
        # Extract column values from the row
    name = row['Name']
    designation = row['Designation']
    employee_id = row['Employee ID']

        # SQL statement to insert data into the table
    insert_query = f"INSERT INTO {table_name} (name, designation, employee_id) VALUES (%s, %s, %s);"

        # Execute the insert query with the column values
    cursor.execute(insert_query, (name, designation, employee_id))

    # Commit the changes to the database
conn.commit()

    # Close the cursor
cursor.close()

