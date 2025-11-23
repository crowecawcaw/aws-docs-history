# SQL Utilities

The SQL utilities module provides a simple interface for executing SQL queries against various database engines within Amazon SageMaker Unified Studio. When no connection is specified, queries are executed locally using DuckDB.

## Supported Database Engines

The following database engines are supported:

- Amazon Athena
- Amazon Redshift
- MySQL
- PostgreSQL
- Snowflake
- Google BigQuery
- Amazon DynamoDB
- Microsoft SQL Server
- DuckDB (default when no connection specified)

## Basic Usage

Import the SQL utilities:

```

from sagemaker_studio import sqlutils

```

### Execute SQL with DuckDB (No Connection)

When no connection is specified, queries are executed locally using DuckDB:

```

# Simple SELECT query
result = sqlutils.sql("SELECT 1 as test_column")
result

# Query with literal values
result = sqlutils.sql("SELECT * FROM table WHERE id = 123")

```

### Execute SQL with Project Connections

Use existing project connections by specifying either connection name or ID:

```

# Using connection name
result = sqlutils.sql(
    "SELECT * FROM my_table",
    connection_name="my_athena_connection"
)

# Using connection ID
result = sqlutils.sql(
    "SELECT * FROM my_table",
    connection_id="conn_12345"
)

```

## Examples by Database Engine

### Amazon Athena

```

# Query Athena using project connection with parameters
result = sqlutils.sql(
    """
    SELECT customer_id, order_date, total_amount
    FROM orders
    WHERE order_date >= :start_date
    """,
    parameters={"start_date": "2024-01-01"},
    connection_name="project.athena"
)

# Create external table in Athena
sqlutils.sql(
    """
    CREATE EXTERNAL TABLE sales_data (
        customer_id bigint,
        order_date date,
        amount decimal(10,2)
    )
    LOCATION 's3://my-bucket/sales-data/'
    """,
    connection_name="project.athena"
)

# Insert data using Create Table As Select (CTAS)
sqlutils.sql(
    """
    CREATE TABLE monthly_sales AS
    SELECT
        DATE_TRUNC('month', order_date) as month,
        SUM(amount) as total_sales
    FROM sales_data
    GROUP BY DATE_TRUNC('month', order_date)
    """,
    connection_name="project.athena"
)

```

### Amazon Redshift

```

# Query Redshift with parameters
result = sqlutils.sql(
    """
    SELECT product_name, category, price
    FROM products
    WHERE category = :category
    AND price > :min_price
    """,
    parameters={"category": "Electronics", "min_price": 100},
    connection_name="project.redshift"
)

# Create table in Redshift
sqlutils.sql(
    """
    CREATE TABLE customer_summary (
        customer_id INTEGER PRIMARY KEY,
        total_orders INTEGER,
        total_spent DECIMAL(10,2),
        last_order_date DATE
    )
    """,
    connection_name="project.redshift"
)

# Insert aggregated data
sqlutils.sql(
    """
    INSERT INTO customer_summary
    SELECT
        customer_id,
        COUNT(*) as total_orders,
        SUM(amount) as total_spent,
        MAX(order_date) as last_order_date
    FROM orders
    GROUP BY customer_id
    """,
    connection_name="project.redshift"
)

# Update existing records
sqlutils.sql(
    """
    UPDATE products
    SET price = price * 1.1
    WHERE category = 'Electronics'
    """,
    connection_name="project.redshift"
)

```

## Advanced Usage

### Working with DataFrames

The sql function returns pandas DataFrames for SELECT queries, and row counts for DML operations:

```

import pandas as pd

# Execute query and get DataFrame
df = sqlutils.sql("SELECT * FROM sales_data", connection_name="redshift_conn")

# Use pandas operations
summary = df.groupby('region')['sales'].sum()
print(summary)

# Save to file
df.to_csv('sales_report.csv', index=False)

# DML operations return row counts
rows_affected = sqlutils.sql(
    "UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 123",
    connection_name="redshift_conn"
)
print(f"Updated {rows_affected} inventory records")

```

### Parameterized Queries

Use parameters to safely pass values to queries:

```

# Dictionary parameters (recommended)
result = sqlutils.sql(
    "SELECT * FROM orders WHERE customer_id = :customer_id AND status = :status",
    parameters={"customer_id": 12345, "status": "completed"},
    connection_name="redshift_connection"
)

# Athena with named parameters
result = sqlutils.sql(
    "SELECT * FROM products WHERE category = :category AND price > :min_price",
    parameters={"category": "Electronics", "min_price": 100},
    connection_name="athena_connection"
)

```

### Getting Database Engine

You can also get the underlying SQLAlchemy engine for advanced operations:

```

# Get engine for a connection
engine = sqlutils.get_engine(connection_name="redshift_connection")

# Use engine directly with pandas
import pandas as pd

df = pd.read_sql("SELECT * FROM large_table LIMIT 1000", engine)

```

### DuckDB Features

When using DuckDB (no connection specified), you get additional capabilities:

#### Python Integration

```

# DuckDB can access Python variables directly
import pandas as pd

my_df = pd.DataFrame({'id': [1, 2, 3], 'name': ['A', 'B', 'C']})

result = sqlutils.sql("SELECT * FROM my_df WHERE id > 1")

```

### Notes

- All queries return pandas DataFrames for easy data manipulation
- DuckDB is automatically configured with Amazon S3 credentials from the environment
- Connection credentials are managed through Amazon SageMaker Unified Studio project connections
- The module handles connection pooling and cleanup automatically
