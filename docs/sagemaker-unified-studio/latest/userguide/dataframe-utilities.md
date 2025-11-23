# DataFrame Utilities

Read from and write to catalog tables using pandas DataFrames with automatic format detection and database management.

Supported catalog types:

- AwsDataCatalog
- S3CatalogTables

## Basic Usage

Import the DataFrame utilities:

```

from sagemaker_studio import dataframeutils

```

## Reading from Catalog Tables

Required Inputs:

- database (str): Database name within the catalog
- table (str): Table name

Optional Parameters:

- catalog (str): Catalog identifier (defaults to AwsDataCatalog if not specified)
- format (str): Data format - auto-detects from table metadata, falls back to parquet
- \*\*kwargs: Additional arguments
  - for AwsDataCatalog, kwargs can be columns, chunked, etc
  - for S3Tables, kwargs can be limit, row_filter, selected_fields, etc

```

import pandas as pd

# Read from AwsDataCatalog
df = pd.read_catalog_table(
    database="my_database",
    table="my_table"
)

# Read from S3 Tables
df = pd.read_catalog_table(
   database="my_database",
   table="my_table",
   catalog="s3tablescatalog/my_s3_tables_catalog",
)

```

### Usage with optional parameters

```

import pandas as pd

# Read from AwsDataCatalog by explicitly specifying catalogID and format
df = pd.read_catalog_table(
    database="my_database",
    table="my_table",
    catalog="123456789012",
    format="parquet"
)

# Read from AwsDataCatalog by explicitly specifying catalogID, format, and additional args -> columns
df = pd.read_catalog_table(
    database="my_database",
    table="my_table",
    catalog="123456789012",
    format="parquet",
    columns=['<column_name_1>, <column_name_2>']
)

# Read from S3 Tables with additional args -> limit
df = pd.read_catalog_table(
   database="my_database",
   table="my_table",
   catalog="s3tablescatalog/my_s3_tables_catalog",
   limit=500
)

# Read from S3 Tables with additional args -> selected_fields
df = pd.read_catalog_table(
   database="my_database",
   table="my_table",
   catalog="s3tablescatalog/my_s3_tables_catalog",
   selected_fields=['<field_name_1>, <field_name_2>']
)

```

## Writing to Catalog Tables

Required Inputs:

- database (str): Database name within the catalog
- table (str): Table name

Optional Parameters:

- catalog (str): Catalog identifier (defaults to AwsDataCatalog if not specified)
- format (str): Data format used for AwsDataCatalog (default: parquet)
- path (str): Custom Amazon S3 path for writing to AwsDataCatalog (auto-determined if not provided)
- \*\*kwargs: Additional arguments

Path Resolution Priority - Amazon S3 path is determined in this order:

- User-provided path parameter
- Existing database location + table name
- Existing table location
- Project default Amazon S3 location

```

import pandas as pd

# Create sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'value': [10.5, 20.3, 15.7]
})

# Write to AwsDataCatalog
df.to_catalog_table(
    database="my_database",
    table="my_table"
)

# Write to S3 Table Catalog
df.to_catalog_table(
    database="my_database",
    table="my_table",
    catalog="s3tablescatalog/my_s3_tables_catalog"
)

```

### Writing to Catalog Tables

```

# Write to AwsDataCatalog with csv format
df.to_catalog_table(
    database="my_database",
    table="my_table",
    format="csv"
)

# Write to AwsDataCatalog at user specified s3 path
df.to_catalog_table(
    database="my_database",
    table="my_table",
    path="s3://my-bucket/custom/path/"
)

# Write to AwsDataCatalog with additional argument -> compression
df.to_catalog_table(
    database="my_database",
    table="my_table",
    compression='gzip'
)

```
