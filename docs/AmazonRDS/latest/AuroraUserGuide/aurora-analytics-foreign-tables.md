

# Working with foreign tables
<a name="aurora-analytics-foreign-tables"></a>

Foreign tables give your Aurora PostgreSQL database read-only access to Apache Parquet and Apache Iceberg data stored in Amazon S3, without copying it into Aurora. You query a foreign table with standard SQL, on its own or joined with your local PostgreSQL tables, and the data stays in place in Amazon S3.

**Topics**
+ [Supported data formats](#aurora-analytics-foreign-tables-formats)
+ [Foreign table syntax](#aurora-analytics-foreign-tables-syntax)
+ [Creating a foreign table for Parquet data](#aurora-analytics-foreign-tables-parquet)
+ [Creating a foreign table for Iceberg data](#aurora-analytics-foreign-tables-iceberg)
+ [Querying a specific Iceberg snapshot](#aurora-analytics-foreign-tables-snapshot)
+ [Querying an Iceberg table at a specific timestamp](#aurora-analytics-foreign-tables-timestamp)
+ [Bulk table creation (IMPORT FOREIGN SCHEMA)](#aurora-analytics-foreign-tables-import)
+ [Column name restrictions](#aurora-analytics-foreign-tables-column-restrictions)
+ [Modifying foreign tables](#aurora-analytics-foreign-tables-modifying)
+ [Managing permissions for foreign tables](#aurora-analytics-foreign-tables-permissions)
+ [Data formats and type mapping](aurora-analytics-type-mapping.md)

## Supported data formats
<a name="aurora-analytics-foreign-tables-formats"></a>

Aurora PostgreSQL supports the following open data formats for foreign tables:


**Supported data formats for foreign tables**  

| Format | Description | Access path | 
| --- | --- | --- | 
| Apache Parquet | Columnar storage format optimized for analytics | Amazon S3 URI or AWS Glue ARN | 
| Apache Iceberg | Open table format with ACID transactions and schema evolution | Amazon S3 URI, AWS Glue ARN, or Amazon S3 Tables ARN | 

## Foreign table syntax
<a name="aurora-analytics-foreign-tables-syntax"></a>

The following is the syntax for creating a foreign table:

```
CREATE FOREIGN TABLE [ IF NOT EXISTS ] [schema_name.]table_name ( [
    column_name data_type [, ... ]
] )
SERVER aurora_analytics_server
OPTIONS (
    location 'location'
    [, format 'parquet' | 'iceberg' ]
    [, region 'region' ]
    [, snapshot 'snapshot_id' ]
    [, timestamp 'timestamp' ]
);
```

The following parameters are accepted.

`schema_name`  
The PostgreSQL schema in which to create the foreign table.

`table_name`  
The name of the foreign table to create in PostgreSQL.

`column_name data_type`  
Column definitions that match your Amazon S3 data schema. When you omit the column list (leave the parentheses empty), Aurora PostgreSQL automatically infers column names and data types from the Parquet or Iceberg table metadata. Alternatively, you can explicitly specify column names and their compatible PostgreSQL data types. When columns are explicitly specified, only those columns are projected during query execution.

`SERVER aurora_analytics_server`  
The foreign server created automatically by the `aurora_analytics` extension. All foreign tables use this server.

`OPTIONS`  
The `OPTIONS` clause accepts the following options.    
`location`  
Required. The Amazon S3 URI, AWS Glue ARN, or Amazon S3 Tables ARN pointing to your data. For example:  
+ Amazon S3 URI (Parquet): `s3://bucket-name/path/`.
+ Amazon S3 URI (Iceberg): `s3://bucket-name/warehouse/table/`. The path must contain a `version-hint.text`, or point directly to a `metadata.json` file (for example, `s3://bucket/warehouse/table/metadata/00001-abc.metadata.json`).
+ Amazon S3 Tables ARN: `arn:aws:s3tables:region:account:bucket/bucket-name/table/namespace/table`.
+ AWS Glue ARN (standard): `arn:aws:glue:region:account:table/database/table`.
+ AWS Glue ARN (Amazon S3 Tables): `arn:aws:glue:region:account:table/s3tablescatalog/bucket/namespace/table`.
+ AWS Glue ARN (federated catalog): `arn:aws:glue:region:account:table/catalog/database/table`.  
`format`  
Optional. The data format: `'parquet'` or `'iceberg'`. Auto-detected for AWS Glue and Amazon S3 Tables ARNs. Required only for raw Amazon S3 URI locations when the format cannot be inferred.  
`region`  
Optional. The AWS Region where your data source is located. Auto-inferred from ARNs, and resolved from the bucket for Amazon S3 URIs.  
`snapshot`  
Optional. (Iceberg only) The Iceberg snapshot ID to query. If both `snapshot` and `timestamp` are omitted, Aurora PostgreSQL uses the latest snapshot. Mutually exclusive with `timestamp`.  
`timestamp`  
Optional. (Iceberg only) Query the Iceberg table as of a specific point in time. Accepts any PostgreSQL-compatible timestamp format (for example, `'2024-01-01 12:00:00'`), a date (for example, `'2024-01-01'`), epoch milliseconds (for example, `'1704110400000'`), or special keywords (`now`, `today`, `tomorrow`, `yesterday`). Resolved at table creation time. Mutually exclusive with `snapshot`.

## Creating a foreign table for Parquet data
<a name="aurora-analytics-foreign-tables-parquet"></a>

The following example creates a foreign table with explicit column definitions for your data stored in Parquet files in Amazon S3:

```
CREATE FOREIGN TABLE ft_orders (
    order_id INT,
    customer_id INT,
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    status TEXT,
    payment_method TEXT,
    shipping_address TEXT,
    items_count INT
)
SERVER aurora_analytics_server
OPTIONS (
    location 's3://mybucket/data/orders/',
    format 'parquet'
);
```

To query the table:

```
SELECT COUNT(*) FROM ft_orders;
```

## Creating a foreign table for Iceberg data
<a name="aurora-analytics-foreign-tables-iceberg"></a>

The following example creates a foreign table that uses schema auto-inference for an Iceberg table registered in the AWS Glue Data Catalog:

```
CREATE FOREIGN TABLE ft_orders ()
SERVER aurora_analytics_server
OPTIONS (
    location 'arn:aws:glue:us-east-1:123456789012:table/my_database/orders'
);
```

**Note**  
When you use an AWS Glue ARN or Amazon S3 Tables ARN for the `location`, you can omit the `format` option. Aurora PostgreSQL automatically detects the format from the catalog metadata.

To query the table:

```
SELECT COUNT(*) FROM ft_orders;
```

## Querying a specific Iceberg snapshot
<a name="aurora-analytics-foreign-tables-snapshot"></a>

To query a specific point-in-time snapshot of an Iceberg table, specify the snapshot version you want to query with the `snapshot` option:

```
CREATE FOREIGN TABLE ft_orders_snapshot ()
SERVER aurora_analytics_server
OPTIONS (
    location 'arn:aws:glue:us-east-1:123456789012:table/my_database/orders',
    snapshot '3847291056291847'
);
```

## Querying an Iceberg table at a specific timestamp
<a name="aurora-analytics-foreign-tables-timestamp"></a>

To query an Iceberg table as of a specific point in time, specify the `timestamp` option:

```
CREATE FOREIGN TABLE ft_orders_timetravel ()
SERVER aurora_analytics_server
OPTIONS (
    location 'arn:aws:glue:us-east-1:123456789012:table/my_database/orders',
    timestamp '2024-06-15 12:00:00'
);
```

The `timestamp` value is resolved at table creation time. You can use special keywords such as `'yesterday'` or `'now'`, or epoch milliseconds such as `'1704110400000'`.

**Note**  
You can't set both `snapshot` and `timestamp` on the same foreign table. Use one or the other.

## Bulk table creation (IMPORT FOREIGN SCHEMA)
<a name="aurora-analytics-foreign-tables-import"></a>

To register multiple tables at once from an AWS Glue database or Amazon S3 Tables namespace, use `IMPORT FOREIGN SCHEMA`:

```
IMPORT FOREIGN SCHEMA remote_schema
    [ { LIMIT TO | EXCEPT } ( table_name [, ... ] ) ]
    FROM SERVER aurora_analytics_server
    INTO local_schema
    OPTIONS (
        location 'catalog_arn'
    );
```

This command queries the remote catalog, generates a `CREATE FOREIGN TABLE` statement for each discovered table, and executes them within a single transaction. Column definitions, format, and region are auto-resolved for each table using the same logic as `CREATE FOREIGN TABLE` with an empty column list.

Only catalog-based sources (AWS Glue, Amazon S3 Tables) are supported. Raw Amazon S3 URI locations can't be imported because they lack the catalog metadata needed to enumerate tables. The entire operation is transactional: if any individual table creation fails (for example, an unsupported format or a permission denied error), the entire import rolls back.

To import all tables from an AWS Glue database:

```
IMPORT FOREIGN SCHEMA my_analytics_db
    FROM SERVER aurora_analytics_server
    INTO analytics
    OPTIONS (location 'arn:aws:glue:us-east-1:123456789012:catalog');
```

To import all tables from an Amazon S3 Tables namespace:

```
IMPORT FOREIGN SCHEMA my_namespace
    FROM SERVER aurora_analytics_server
    INTO sales_data
    OPTIONS (location 'arn:aws:s3tables:us-east-1:123456789012:bucket/my-bucket');
```

To import only specific tables:

```
IMPORT FOREIGN SCHEMA my_analytics_db
    LIMIT TO (orders, customers, products)
    FROM SERVER aurora_analytics_server
    INTO analytics
    OPTIONS (location 'arn:aws:glue:us-east-1:123456789012:catalog');
```

To exclude specific tables:

```
IMPORT FOREIGN SCHEMA my_analytics_db
    EXCEPT (staging_temp, debug_logs)
    FROM SERVER aurora_analytics_server
    INTO analytics
    OPTIONS (location 'arn:aws:glue:us-east-1:123456789012:catalog');
```

## Column name restrictions
<a name="aurora-analytics-foreign-tables-column-restrictions"></a>

Aurora PostgreSQL rejects foreign table definitions that contain columns whose names differ only in ASCII letter case. For example, you can't have both `"Foo"` and `"foo"` as column names on the same foreign table. If the underlying data contains such columns, rename them in the source data before creating the foreign table.

## Modifying foreign tables
<a name="aurora-analytics-foreign-tables-modifying"></a>

You can modify a foreign table with `ALTER FOREIGN TABLE`, for example, to rename it, move it to another schema, or point it at a new location, format, or Region. Because a foreign table is a definition rather than a copy of your data, these changes update only how PostgreSQL interprets the external data; the underlying data in Amazon S3 is untouched.

To keep queries returning correct results, keep the foreign table definition in sync with the actual schema of your Amazon S3 data. If the source schema changes, update the table (or re-infer it) to match. For an automated way to do this, see `aurora_analytics_refresh_foreign_table`.

The following characteristics apply to these foreign tables:
+ **External storage**: Data resides in Amazon S3, not within PostgreSQL. Aurora PostgreSQL reads directly from Amazon S3 during query execution.
+ **Read-only access**: `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` are not supported. Modify your data through external processes that update the Amazon S3 files or Iceberg tables.
+ **Metadata-only changes**: `ALTER` operations modify PostgreSQL catalog metadata only.
+ **Constraints not enforced**: `NOT NULL`, `CHECK`, and `DEFAULT` constraints are stored in metadata for documentation purposes but are not enforced when reading external data.
+ **Statistics managed externally**: PostgreSQL planner statistics (`SET STATISTICS`) have no effect. The analytics engine uses Parquet and Iceberg metadata for query planning.

Supported `ALTER` operations:


**Supported ALTER operations**  

| Operation | Notes | 
| --- | --- | 
| RENAME TABLE | Changes metadata only. | 
| SET SCHEMA | Moves table to a different schema. | 
| ADD COLUMN | Adds to metadata. Data must exist in source. | 
| DROP COLUMN | Removes from metadata only. | 
| ALTER COLUMN TYPE | Changes metadata. Requires compatible data. | 
| OWNER TO | Changes table ownership. | 
| OPTIONS (SET) | Modifies location, format, region, snapshot or timestamp. | 

The following operations are accepted by PostgreSQL but have no practical effect on these foreign tables:


**ALTER operations with no effect**  

| Operation | Reason | 
| --- | --- | 
| SET STATISTICS | Aurora PostgreSQL uses source metadata for planning. | 
| SET STORAGE | Storage is managed by Amazon S3. | 
| SET/DROP DEFAULT | Stored in metadata but not enforced on external data. | 
| SET/DROP NOT NULL | Stored in metadata but not enforced on external data. | 
| ADD/DROP CONSTRAINT | Stored in metadata but not enforced on external data. | 

The following operations are not supported because these foreign tables are read-only:
+ `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `COPY FROM`
+ Column `OPTIONS`
+ `LIKE` clause
+ `TABLESPACE`
+ `WITH` storage parameters

**Note**  
Row-locking clauses (`FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, and `FOR KEY SHARE`) are accepted in queries against foreign tables, and the query runs and returns rows. However, no row-level lock is taken on the external data. This is standard PostgreSQL foreign data wrapper behavior, not specific to this feature.

## Managing permissions for foreign tables
<a name="aurora-analytics-foreign-tables-permissions"></a>

Foreign tables follow standard PostgreSQL permission controls. Use `GRANT` and `REVOKE` to manage which roles can query specific foreign tables or entire schemas.

### Querying foreign tables
<a name="aurora-analytics-foreign-tables-permissions-query"></a>

```
-- Grant SELECT on a specific foreign table
GRANT SELECT ON TABLE ft_orders TO analyst_role;

-- Grant SELECT on all tables in a schema
GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO analyst_role;
```

### Creating foreign tables
<a name="aurora-analytics-foreign-tables-permissions-create"></a>

To execute `CREATE FOREIGN TABLE`, a user needs both:
+ `CREATE` privilege on the target schema
+ `USAGE` privilege on the foreign server (`aurora_analytics_server`)

```
-- Allow a role to create foreign tables
GRANT CREATE ON SCHEMA analytics TO data_engineer_role;
GRANT USAGE ON FOREIGN SERVER aurora_analytics_server TO data_engineer_role;
```

### Modifying foreign tables
<a name="aurora-analytics-foreign-tables-permissions-modify"></a>

Only the table owner can execute `ALTER FOREIGN TABLE` or `DROP FOREIGN TABLE`. However, changing any option requires `USAGE` privilege on `aurora_analytics_server`, because pointing a foreign table at a new data source is functionally equivalent to creating a new one.

```
-- Table owner with USAGE on server — can change location
ALTER FOREIGN TABLE ft_orders OPTIONS (SET location 's3://new-bucket/orders/');

-- Table owner without USAGE on server — can rename, add/drop columns, and so on
ALTER FOREIGN TABLE ft_orders RENAME TO ft_orders_archive;
ALTER FOREIGN TABLE ft_orders ADD COLUMN new_col TEXT;
```

To transfer ownership:

```
ALTER FOREIGN TABLE ft_orders OWNER TO new_owner_role;
```

For more information about PostgreSQL privilege management, see [GRANT](https://www.postgresql.org/docs/current/sql-grant.html) in the PostgreSQL documentation.