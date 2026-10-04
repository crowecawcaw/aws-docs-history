

# Getting started
<a name="aurora-analytics-getting-started"></a>

Aurora PostgreSQL includes the analytics feature by default on supported engine versions. To use it, you enable the feature through a DB cluster parameter group setting, then install the `aurora_analytics` extension in each database where you want to use it.

The extension creates a foreign data wrapper and a foreign server named `aurora_analytics_server`. You then create PostgreSQL foreign tables linked to this server that point to your data in Amazon S3 or Amazon S3 Tables.

**Topics**
+ [Prerequisites](aurora-analytics-prerequisites.md)
+ [Installing the extension](#aurora-analytics-getting-started-install)
+ [Running your first query](#aurora-analytics-getting-started-first-query)
+ [Next steps](#aurora-analytics-getting-started-next-steps)

## Installing the extension
<a name="aurora-analytics-getting-started-install"></a>

After `aurora_analytics.enabled` is set to `true`, install the extension in each database where you want to use it.

**To install the extension**

1. Connect to your Aurora PostgreSQL DB cluster using `psql`, another PostgreSQL client, or the [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html).

   ```
   psql --host=your-cluster-endpoint.region.rds.amazonaws.com --port=5432 --username=postgres --password
   ```

1. Install the extension:

   ```
   CREATE EXTENSION aurora_analytics;
   ```

**Note**  
To create the extension, you must have the `rds_superuser` role, or be a user that has been granted the `rds_extension` role and delegated this extension. To delegate the extension to a non-superuser, run the following as `rds_superuser`:  

```
GRANT rds_extension TO your_user;
ALTER USER your_user SET rds.allowed_delegated_extensions = 'aurora_analytics';
```
For more information, see [Using Amazon Relational Database Service delegated extension support for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_delegated_extension_support.html).

You must install the extension separately in each database where you want to use it.

## Running your first query
<a name="aurora-analytics-getting-started-first-query"></a>

After the extension is installed, you can create a foreign table and query your Amazon S3 data using standard SQL. For detailed information about foreign table syntax and options, see [Working with foreign tables](aurora-analytics-foreign-tables.md).

The following example creates a foreign table that points to Parquet files in Amazon S3 and queries it:

```
-- Create a foreign table pointing to Parquet data in S3
CREATE FOREIGN TABLE ft_orders ()
SERVER aurora_analytics_server
OPTIONS (
    location 's3://my-bucket/data/orders/',
    format 'parquet',
    region 'us-east-1'
);

-- Query the foreign table
SELECT COUNT(*) FROM ft_orders;
```

When you specify an empty column list (`()`), the extension automatically infers column names and data types from the remote source.

## Next steps
<a name="aurora-analytics-getting-started-next-steps"></a>

After you verify that the extension is installed, you can create foreign tables that reference your data in Amazon S3. For more information, see [Working with foreign tables](aurora-analytics-foreign-tables.md).