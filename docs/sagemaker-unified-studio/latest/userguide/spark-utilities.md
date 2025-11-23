# Spark Utilities

The Spark utilities module provides a simple interface for working with Spark Connect sessions and managing Spark configurations for various data sources within Amazon SageMaker Unified Studio. When no connection is specified, a Spark Connect session is created using the default Amazon Athena Spark connection.

## Basic Usage

Import the Spark utilities:

```

from sagemaker_studio import sparkutils

```

## Initialize Spark Session

Supported connection types:

- Spark connect

Optional Parameters:

- connection_name (str): Name of the connection to execute query against (e.g., "my_redshift_connection")

When no connection is specified, a default Amazon Athena Spark session is created:

```

# Default session
spark = sparkutils.init()

# Session with specific connection
spark = sparkutils.init(connection_name="my_spark_connection")

```

## Working with Spark Options

Supported connection types:

- Amazon DocumentDB
- Amazon DynamoDB
- Amazon Redshift
- Aurora MySQL
- Aurora PostgreSQL
- Azure SQL
- Google BigQuery
- Microsoft SQL Server
- MySQL
- PostgreSQL
- Oracle
- Snowflake

Required Inputs:

- connection_name (str): Name of the connection to get Spark options for (e.g., "my_redshift_connection")

Get formatted Spark options for connecting to data sources:

```

# Get options for Redshift connection
options = sparkutils.get_spark_options("my_redshift_connection")

```

## Examples by Operation Type

### Reading and Writing Data

```

# Create sample DataFrame
df_to_write = spark.createDataFrame(
    [(1, "Alice"), (2, "Bob")],
    ["id", "name"]
)

# Get spark options for Redshift connection
spark_options = sparkutils.get_spark_options("my_redshift_connection")

# Write DataFrame using JDBC
df_to_write.write \
    .format("jdbc") \
    .options(**spark_options) \
    .option("dbtable", "sample_table") \
    .save()

# Read DataFrame using JDBC
df_to_read = spark.read \
    .format('jdbc') \
    .options(**spark_options) \
    .option('dbtable', 'sample_table') \
    .load()

# Display results
df_to_read.show()

```

## Notes

- Spark sessions are automatically configured for Amazon Athena spark compute
- Connection credentials are managed through Amazon SageMaker Unified Studio project connections
- The module handles session management and cleanup automatically
- Spark options are formatted appropriately for each supported data source
- When get_spark_options is used in EMR-S or EMR-on-EC2 compute, and the connection has EnforceSSL enabled, the formatted spark options will not have the sslrootcert value and hence that would need to be passed explicitly.
