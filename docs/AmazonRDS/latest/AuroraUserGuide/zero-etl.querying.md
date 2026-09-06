

# Adding data to a source Aurora DB cluster and querying it
<a name="zero-etl.querying"></a>

To finish creating a zero-ETL integration that replicates data from Amazon Aurora into Amazon Redshift, you must create a database in the target destination.

For connections with Amazon Redshift, connect to your Amazon Redshift cluster or workgroup and create a database with a reference to your integration identifier. Then, you can add data to your source Aurora DB cluster and see it replicated in Amazon Redshift or Amazon SageMaker.

**Topics**
+ [Creating a target database](#zero-etl.create-db)
+ [Adding data to the source DB cluster](#zero-etl.add-data-rds)
+ [Querying your Aurora data in Amazon Redshift](#zero-etl.query-data-redshift)
+ [Data type differences between Aurora and Amazon Redshift databases](#zero-etl.data-type-mapping)
+ [DDL operations for Aurora PostgreSQL](#zero-etl.ddl-postgres)

## Creating a target database
<a name="zero-etl.create-db"></a>

Before you can start replicating data into Amazon Redshift, after you create an integration, you must create a database in your target data warehouse. This database must include a reference to the integration identifier. You can use the Amazon Redshift console or the Query editor v2 to create the database.

For instructions to create a destination database, see [Create a destination database in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html#zero-etl-using.create-db).

## Adding data to the source DB cluster
<a name="zero-etl.add-data-rds"></a>

After you configure your integration, you can populate the source Aurora DB cluster with data that you want to replicate into your data warehouse.

**Note**  
There are differences between data types in Amazon Aurora and the target analytics warehouse. For a table of data type mappings, see [Data type differences between Aurora and Amazon Redshift databases](#zero-etl.data-type-mapping).

First, connect to the source DB cluster using the MySQL or PostgreSQL client of your choice. For instructions, see [Connecting to an Amazon Aurora DB cluster](Aurora.Connecting.md).

Then, create a table and insert a row of sample data.

**Important**  
Make sure that the table has a primary key. Otherwise, it can't be replicated to the target data warehouse.

The pg\_dump and pg\_restore PostgreSQL utilities initially create tables without a primary key and then add it afterwards. If you're using one of these utilities, we recommend first creating a schema and then loading data in a separate command.

**MySQL**

The following example uses the [MySQL Workbench utility](https://dev.mysql.com/downloads/workbench/).

```
CREATE DATABASE {{my_db}};

USE {{my_db}};

CREATE TABLE {{books_table}} (ID int NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(50) NOT NULL,
Copyright INT NOT NULL, Genre VARCHAR(50) NOT NULL, PRIMARY KEY (ID));

INSERT INTO {{books_table}} VALUES (1, 'The Shining', 'Stephen King', 1977, 'Supernatural fiction');
```

**PostgreSQL**

The following example uses the `[psql](https://www.postgresql.org/docs/current/app-psql.html)` PostgreSQL interactive terminal. When connecting to the cluster, include the named database that you specified when creating the integration.

```
psql -h {{mycluster}}.cluster-{{123456789012}}.us-east-2.rds.amazonaws.com -p 5432 -U {{username}} -d {{named_db}};

named_db=> CREATE TABLE {{books_table}} (ID int NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(50) NOT NULL,
Copyright INT NOT NULL, Genre VARCHAR(50) NOT NULL, PRIMARY KEY (ID));

named_db=> INSERT INTO {{books_table}} VALUES (1, 'The Shining', 'Stephen King', 1977, 'Supernatural fiction');
```

## Querying your Aurora data in Amazon Redshift
<a name="zero-etl.query-data-redshift"></a>

After you add data to the Aurora DB cluster, it's replicated into the destination database and is ready to be queried.

**To query the replicated data**

1. Navigate to the Amazon Redshift console and choose **Query editor v2** from the left navigation pane.

1. Connect to your cluster or workgroup and choose your destination database (which you created from the integration) from the dropdown menu (**destination\_database** in this example). For instructions to create a destination database, see [Create a destination database in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html#zero-etl-using.create-db).

1. Use a SELECT statement to query your data. In this example, you can run the following command to select all data from the table that you created in the source Aurora DB cluster:

   ```
   SELECT * from {{my_db}}."{{books_table}}";
   ```  
![Query editor results showing sample data added to the Amazon RDS database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/zero-etl-redshift-editor.png)
   + `{{my_db}}` is the Aurora database schema name. This option is only needed for MySQL databases.
   + `{{books_table}}` is the Aurora table name.

You can also query the data using the a command line client. For example:

```
destination_database=# select * from {{my_db}}."{{books_table}}";

 ID |       Title |        Author |   Copyright |                  Genre |  txn_seq |  txn_id
----+–------------+---------------+-------------+------------------------+----------+--------+
  1 | The Shining |  Stephen King |        1977 |   Supernatural fiction |        2 |   12192
```

**Note**  
For case-sensitivity, use double quotes (" ") for schema, table, and column names. For more information, see [enable\_case\_sensitive\_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_identifier.html).

## Data type differences between Aurora and Amazon Redshift databases
<a name="zero-etl.data-type-mapping"></a>

The following tables show the mappings of Aurora MySQL and Aurora PostgreSQL data types to corresponding destination data types. *Amazon Aurora currently supports only these data types for zero-ETL integrations.*

If a table in your source DB cluster includes an unsupported data type, the table goes out of sync and isn't consumable by the destination target. Streaming from the source to the target continues, but the table with the unsupported data type isn't available. To fix the table and make it available in the target destination, you must manually revert the breaking change and then refresh the integration by running `[ALTER DATABASE...INTEGRATION REFRESH](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DATABASE.html)`.

**Note**  
You can't refresh zero-ETL integrations with an Amazon SageMaker lakehouse. Instead, delete and try to create the integration again.

**Topics**
+ [Aurora MySQL](#zero-etl.data-type-mapping-mysql)
+ [Aurora PostgreSQL](#zero-etl.data-type-mapping-postgres)

### Aurora MySQL
<a name="zero-etl.data-type-mapping-mysql"></a>


| Aurora MySQL data type | Target data type  | Description  | Limitations | 
| --- | --- | --- | --- | 
| INT  | INTEGER | Signed four-byte integer | None | 
| SMALLINT | SMALLINT | Signed two-byte integer | None | 
| TINYINT | SMALLINT | Signed two-byte integer | None | 
| MEDIUMINT | INTEGER | Signed four-byte integer | None | 
| BIGINT | BIGINT | Signed eight-byte integer | None | 
| INT UNSIGNED | BIGINT | Signed eight-byte integer | None | 
| TINYINT UNSIGNED | SMALLINT | Signed two-byte integer | None | 
| MEDIUMINT UNSIGNED | INTEGER | Signed four-byte integer | None | 
| BIGINT UNSIGNED | DECIMAL(20,0) | Exact numeric of selectable precision | None | 
| DECIMAL(p,s) = NUMERIC(p,s) | DECIMAL(p,s) | Exact numeric of selectable precision | Precision greater than 38 and scale greater than 37 not supported | 
| DECIMAL(p,s) UNSIGNED = NUMERIC(p,s) UNSIGNED | DECIMAL(p,s) | Exact numeric of selectable precision | Precision greater than 38 and scale greater than 37 not supported | 
| FLOAT4/REAL | REAL | Single precision floating-point number | None | 
| FLOAT4/REAL UNSIGNED | REAL | Single precision floating-point number | None | 
| DOUBLE/REAL/FLOAT8 | DOUBLE PRECISION | Double precision floating-point number | None | 
| DOUBLE/REAL/FLOAT8 UNSIGNED | DOUBLE PRECISION | Double precision floating-point number | None | 
| BIT(n) | VARBYTE(8) | Variable-length binary value | None | 
| BINARY(n) | VARBYTE(n) | Variable-length binary value | None | 
| VARBINARY(n) | VARBYTE(n) | Variable-length binary value | None | 
| CHAR(n) | VARCHAR(n) | Variable-length string value | None | 
| VARCHAR(n) | VARCHAR(n) | Variable-length string value | None | 
| TEXT | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| TINYTEXT | VARCHAR(255) | Variable-length string value up to 255 characters | None | 
| MEDIUMTEXT | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| LONGTEXT | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| ENUM | VARCHAR(1020) | Variable-length string value up to 1,020 characters | None | 
| SET | VARCHAR(1020) | Variable-length string value up to 1,020 characters | None | 
| DATE | DATE | Calendar date (year, month, day) | None | 
| DATETIME | TIMESTAMP | Date and time (without time zone) | None | 
| TIMESTAMP(p) | TIMESTAMP | Date and time (without time zone) | None | 
| TIME | VARCHAR(18) | Variable-length string value up to 18 characters | None | 
| YEAR | VARCHAR(4) | Variable-length string value up to 4 characters | None | 
| JSON | SUPER | Semistructured data or documents as values | None | 

### Aurora PostgreSQL
<a name="zero-etl.data-type-mapping-postgres"></a>

Zero-ETL integrations for Aurora PostgreSQL don't support custom data types or data types created by extensions.


| Aurora PostgreSQL data type | Amazon Redshift data type | Description | Limitations | 
| --- | --- | --- | --- | 
| array | SUPER | Semistructured data or documents as values | None | 
| bigint | BIGINT | Signed eight-byte integer | None | 
| bigserial | BIGINT | Signed eight-byte integer | None | 
| bit varying(n) | VARBYTE(n) | Variable-length binary value up to 16,777,216 bytes | None | 
| bit(n) | VARBYTE(n) | Variable-length binary value up to 16,777,216 bytes | None | 
| bit, bit varying | VARBYTE(16777216) | Variable-length binary value up to 16,777,216 bytes | None | 
| boolean | BOOLEAN | Logical boolean (true/false) | None | 
| bytea | VARBYTE(16777216) | Variable-length binary value up to 16,777,216 bytes | None | 
| char(n) | CHAR(n) | Fixed-length character string value up to 65,535 bytes | None | 
| char varying(n) | VARCHAR(65535) | Variable-length character string value up to 65,535 characters | None | 
| cid | BIGINT | Signed eight-byte integer | None | 
| cidr | VARCHAR(19) | Variable-length string value up to 19 characters | None | 
| date | DATE | Calendar date (year, month, day) | Values greater than 294,276 A.D. not supported | 
| double precision | DOUBLE PRECISION | Double precision floating-point numbers | Subnormal values not fully supported | 
| gtsvector | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| inet | VARCHAR(19) | Variable-length string value up to 19 characters | None | 
| integer | INTEGER | Signed four-byte integer | None | 
| int2vector | SUPER | Semistructured data or documents as values. | None | 
| interval | INTERVAL | Duration of time | Only INTERVAL types that specify either a year to month or a day to second qualifier are supported. | 
| json | SUPER | Semistructured data or documents as values | None | 
| jsonb | SUPER | Semistructured data or documents as values | None | 
| jsonpath | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| macaddr | VARCHAR(17) | Variable-length string value up to 17 characters | None | 
| macaddr8 | VARCHAR(23) | Variable-length string value up to 23 characters | None | 
| money | DECIMAL(20,3) | Currency amount | None | 
| name | VARCHAR(64) | Variable-length string value up to 64 characters | None | 
| numeric(p,s) | DECIMAL(p,s) | User-defined fixed precision value |  +  `NaN` values not supported <br />+  Precision and scale must be explicitly defined and not greater than 38 (precision) and 37 (scale) <br />+  Negative scale not supported   | 
| oid | BIGINT | Signed eight-byte integer | None | 
| oidvector | SUPER | Semistructured data or documents as values. | None | 
| pg\_brin\_bloom\_summary | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| pg\_dependencies | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| pg\_lsn | VARCHAR(17) | Variable-length string value up to 17 characters | None | 
| pg\_mcv\_list | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| pg\_ndistinct | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| pg\_node\_tree | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| pg\_snapshot | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| real | REAL | Single precision floating-point number | Subnormal values not fully supported | 
| refcursor | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| smallint | SMALLINT | Signed two-byte integer | None | 
| smallserial | SMALLINT | Signed two-byte integer | None | 
| serial | INTEGER | Signed four-byte integer | None | 
| text | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| tid | VARCHAR(23) | Variable-length string value up to 23 characters | None | 
| time [(p)] without time zone | VARCHAR(19) | Variable-length string value up to 19 characters | Infinity and -Infinity values not supported | 
| time [(p)] with time zone | VARCHAR(22) | Variable-length string value up to 22 characters | Infinity and -Infinity values not supported | 
| timestamp [(p)] without time zone | TIMESTAMP | Date and time (without time zone) |  +  `Infinity` and `-Infinity` values not supported <br />+  Values greater than `9999-12-31` not supported <br />+  B.C. values not supported   | 
| timestamp [(p)] with time zone | TIMESTAMPTZ | Date and time (with time zone) |  +  `Infinity` and `-Infinity` values not supported <br />+  Values greater than `9999-12-31` not supported <br />+  B.C. values not supported   | 
| tsquery | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| tsvector | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| txid\_snapshot | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 
| uuid | VARCHAR(36) | Variable-length 36 character string | None | 
| xid | BIGINT | Signed eight-byte integer | None | 
| xid8 | DECIMAL(20, 0) | Fixed precision decimal | None | 
| xml | VARCHAR(65535) | Variable-length string value up to 65,535 characters | None | 

## DDL operations for Aurora PostgreSQL
<a name="zero-etl.ddl-postgres"></a>

Amazon Redshift is derived from PostgreSQL, so it shares several features with Aurora PostgreSQL due to their common PostgreSQL architecture. Zero-ETL integrations leverage these similarities to streamline data replication from Aurora PostgreSQL to Amazon Redshift, mapping databases by name and utilizing the shared database, schema, and table structure.

Consider the following points when managing Aurora PostgreSQL zero-ETL integrations:
+ Isolation is managed at the database level.
+ Replication occurs at the database level. 
+ Aurora PostgreSQL databases are mapped to Amazon Redshift databases by name, with data flowing to the corresponding renamed Redshift database if the original is renamed.

Despite their similarities, Amazon Redshift and Aurora PostgreSQL have important differences. The following sections outline Amazon Redshift system responses for common DDL operations.

**Topics**
+ [Database operations](#zero-etl.ddl-postgres-database)
+ [Schema operations](#zero-etl.ddl-postgres-schema)
+ [Table operations](#zero-etl.ddl-postgres-table)

### Database operations
<a name="zero-etl.ddl-postgres-database"></a>

The following table shows the system responses for database DDL operations.


| DDL operation | Redshift system response | 
| --- | --- | 
| CREATE DATABASE | No operation | 
| DROP DATABASE | Amazon Redshift drops all the data in the target Redshift database. | 
| RENAME DATABASE | Amazon Redshift drops all the data in the original target database and resynchronize the data in the new target database. If the new database doesn't exist, you must manually create it. For instructions, see [Create a destination database in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html#zero-etl-using.create-db). | 

### Schema operations
<a name="zero-etl.ddl-postgres-schema"></a>

The following table shows the system responses for schema DDL operations.


| DDL operation | Redshift system response | 
| --- | --- | 
| CREATE SCHEMA | No operation | 
| DROP SCHEMA | Amazon Redshift drops the original schema. | 
| RENAME SCHEMA | Amazon Redshift drops the original schema then resynchronizes the data in the new schema. | 

### Table operations
<a name="zero-etl.ddl-postgres-table"></a>

The following table shows the system responses for table DDL operations.


| DDL operation | Redshift system response | 
| --- | --- | 
| CREATE TABLE | Amazon Redshift creates the table.<br />Some operations cause table creation to fail, such as creating a table without a primary key or performing declarative partitioning. For more information, see [Limitations](zero-etl.md#zero-etl.reqs-lims) and [Troubleshooting Aurora zero-ETL integrations](zero-etl.troubleshooting.md). | 
| DROP TABLE | Amazon Redshift drops the table. | 
| TRUNCATE TABLE | Amazon Redshift truncates the table. | 
| ALTER TABLE (RENAME...) | Amazon Redshift renames the table or column. | 
| ALTER TABLE (SET SCHEMA) | Amazon Redshift drops the table in the original schema and resynchronizes the table in the new schema. | 
| ALTER TABLE (ADD PRIMARY KEY) | Amazon Redshift adds a primary key and resynchronizes the table. | 
| ALTER TABLE (ADD COLUMN) | Amazon Redshift adds a column to the table. | 
| ALTER TABLE (DROP COLUMN) | Amazon Redshift drops the column if it's not a primary key column. Otherwise, it resynchronizes the table. | 
| ALTER TABLE (SET LOGGED/UNLOGGED) | If you change the table to logged, Amazon Redshift resynchronizes the table. If you change the table to unlogged, Amazon Redshift drops the table. | 