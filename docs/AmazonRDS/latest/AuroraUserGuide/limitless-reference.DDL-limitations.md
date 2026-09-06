

# DDL limitations and other information for Aurora PostgreSQL Limitless Database
<a name="limitless-reference.DDL-limitations"></a>

The following topics describe limitations or provide more information for DDL SQL commands in Aurora PostgreSQL Limitless Database.

**Topics**
+ [ALTER TABLE](#limitless-reference.DDL-limitations.ALTER_TABLE)
+ [CREATE DATABASE](#limitless-reference.DDL-limitations.CREATE_DATABASE)
+ [CREATE INDEX](#limitless-reference.DDL-limitations.CREATE_INDEX)
+ [CREATE SCHEMA](#limitless-reference.DDL-limitations.CREATE_SCHEMA)
+ [CREATE TABLE](#limitless-reference.DDL-limitations.CREATE_TABLE)
+ [CREATE TABLE AS](#limitless-reference.DDL-limitations.CREATE_TABLE_AS)
+ [DROP DATABASE](#limitless-reference.DDL-limitations.DROP_DATABASE)
+ [SELECT INTO](#limitless-reference.DDL-limitations.SELECT_INTO)
+ [Constraints](#limitless-reference.DDL-limitations.Constraints)
+ [Default values](#limitless-reference.DDL-limitations.DefaultValues)
+ [Extensions](#limitless-reference.DDL-limitations.Extensions)
+ [Foreign keys](#limitless-reference.DDL-limitations.FKs)
+ [Functions](#limitless-reference.DDL-limitations.Functions)
+ [Sequences](#limitless-reference.DDL-limitations.Sequences)

## ALTER TABLE
<a name="limitless-reference.DDL-limitations.ALTER_TABLE"></a>

The `ALTER TABLE` command is generally supported in Aurora PostgreSQL Limitless Database. For more information, see [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) in the PostgreSQL documentation.

### Limitations
<a name="limitless-reference.ALTER_TABLE.limitations"></a>

`ALTER TABLE` has the following limitations for supported options.

**Removing a column**  
+ On sharded tables, you can't remove columns that are part of the shard key.
+ On reference tables, you can't remove primary key columns.

**Changing a column's data type**  
+ The `USING` expression isn't supported.
+ On sharded tables, you can't change the type for columns that are part of the shard key.

**Adding or removing a constraint**  
For details on what isn't supported, see [Constraints](#limitless-reference.DDL-limitations.Constraints).

**Changing a column's default value**  
Default values are supported. For more information, see [Default values](#limitless-reference.DDL-limitations.DefaultValues).

### Unsupported options
<a name="limitless-reference.ALTER_TABLE.unsupported"></a>

Some options aren't supported because they depend on unsupported features, such as triggers.

The following table-level options for `ALTER TABLE` aren't supported:
+ `ALL IN TABLESPACE`
+ `ATTACH PARTITION`
+ `DETACH PARTITION`
+ `ONLY` flag
+ `RENAME CONSTRAINT`

The following column-level options for `ALTER TABLE` aren't supported:
+ ADD GENERATED
+ DROP EXPRESSION [ IF EXISTS ]
+ DROP IDENTITY [ IF EXISTS ]
+ RESET
+ RESTART
+ SET
+ SET COMPRESSION
+ SET STATISTICS

## CREATE DATABASE
<a name="limitless-reference.DDL-limitations.CREATE_DATABASE"></a>

In Aurora PostgreSQL Limitless Database, only limitless databases are supported.

While `CREATE DATABASE` is running, databases that were successfully created in one or more nodes might fail in other nodes, because database creation is a nontransactional operation. In this case, the database objects that were successfully created are automatically removed from all of the nodes within a predetermined amount of time to keep consistency in the DB shard group. During this time, re-creation of a database with the same name might result in an error indicating that the database already exists.

The following options are supported:
+ Collation:

  ```
  CREATE DATABASE {{name}} WITH 
      [LOCALE = {{locale}}]
      [LC_COLLATE = {{lc_collate}}]
      [LC_CTYPE = {{lc_ctype}}]
      [ICU_LOCALE = {{icu_locale}}]
      [ICU_RULES = {{icu_rules}}]
      [LOCALE_PROVIDER = {{locale_provider}}]
      [COLLATION_VERSION = {{collation_version}}];
  ```
+ `CREATE DATABASE WITH OWNER`:

  ```
  CREATE DATABASE {{name}} WITH OWNER = {{user_name}};
  ```

The following options aren't supported:
+ `CREATE DATABASE WITH TABLESPACE`:

  ```
  CREATE DATABASE {{name}} WITH TABLESPACE = {{tablespace_name}};
  ```
+ `CREATE DATABASE WITH TEMPLATE`:

  ```
  CREATE DATABASE {{name}} WITH TEMPLATE = {{template}};
  ```

## CREATE INDEX
<a name="limitless-reference.DDL-limitations.CREATE_INDEX"></a>

`CREATE INDEX CONCURRENTLY` is supported for sharded tables:

```
CREATE INDEX CONCURRENTLY {{index_name}} ON {{table_name}}({{column_name}});
```

`CREATE UNIQUE INDEX` is supported for all table types:

```
CREATE UNIQUE INDEX {{index_name}} ON {{table_name}}({{column_name}});
```

`CREATE UNIQUE INDEX CONCURRENTLY` isn't supported:

```
CREATE UNIQUE INDEX CONCURRENTLY {{index_name}} ON {{table_name}}({{column_name}});
```

For more information, see [UNIQUE](#unique-constraint). For general information on creating indexes, see [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) in the PostgreSQL documentation.

**Showing indexes**  
Not all indexes are visible on routers when you use `\d {{table_name}}` or similar commands. Instead, use the `pg_catalog.pg_indexes` view to get indexes, as shown in the following example.  

```
SET rds_aurora.limitless_create_table_mode='sharded';
SET rds_aurora.limitless_create_table_shard_key='{"id"}';
CREATE TABLE items (id int PRIMARY KEY, val int);
CREATE INDEX items_my_index on items (id, val);

postgres_limitless=> SELECT * FROM pg_catalog.pg_indexes WHERE tablename='items';

 schemaname | tablename |   indexname    | tablespace |                                indexdef
------------+-----------+----------------+------------+------------------------------------------------------------------------
 public     | items     | items_my_index |            | CREATE INDEX items_my_index ON ONLY public.items USING btree (id, val)
 public     | items     | items_pkey     |            | CREATE UNIQUE INDEX items_pkey ON ONLY public.items USING btree (id)
(2 rows)
```

## CREATE SCHEMA
<a name="limitless-reference.DDL-limitations.CREATE_SCHEMA"></a>

`CREATE SCHEMA` with a schema element isn't supported:

```
CREATE SCHEMA {{my_schema}} CREATE TABLE ({{column_name}} INT);
```

This generates an error similar to the following:

```
ERROR: CREATE SCHEMA with schema elements is not supported
```

## CREATE TABLE
<a name="limitless-reference.DDL-limitations.CREATE_TABLE"></a>

Relations in `CREATE TABLE` statements aren't supported, for example:

```
CREATE TABLE orders (orderid int, customerId int, orderDate date) WITH (autovacuum_enabled = false);
```

`IDENTITY` columns aren't supported, for example:

```
CREATE TABLE orders (orderid INT GENERATED ALWAYS AS IDENTITY);
```

Aurora PostgreSQL Limitless Database supports up to 54 characters for sharded table names.

## CREATE TABLE AS
<a name="limitless-reference.DDL-limitations.CREATE_TABLE_AS"></a>

To create a table using `CREATE TABLE AS`, you must use the `rds_aurora.limitless_create_table_mode` variable. For sharded tables, you must also use the `rds_aurora.limitless_create_table_shard_key` variable. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md).

```
-- Set the variables.
SET rds_aurora.limitless_create_table_mode='sharded';
SET rds_aurora.limitless_create_table_shard_key='{"a"}';

CREATE TABLE ctas_table AS SELECT 1 a;

-- "source" is the source table whose columns and data types are used to create the new "ctas_table2" table.
CREATE TABLE ctas_table2 AS SELECT a,b FROM source;
```

You can't use `CREATE TABLE AS` to create reference tables, because they require primary key constraints. `CREATE TABLE AS` doesn't propagate primary keys to new tables.

For general information, see [CREATE TABLE AS](https://www.postgresql.org/docs/current/sql-createtableas.html) in the PostgreSQL documentation.

## DROP DATABASE
<a name="limitless-reference.DDL-limitations.DROP_DATABASE"></a>

You can drop databases that you've created.

The `DROP DATABASE` command runs asynchronously in the background. While it's running, you will receive an error if you try to create a new database with the same name.

## SELECT INTO
<a name="limitless-reference.DDL-limitations.SELECT_INTO"></a>

`SELECT INTO` is functionally similar to [CREATE TABLE AS](#limitless-reference.DDL-limitations.CREATE_TABLE_AS). You must use the `rds_aurora.limitless_create_table_mode` variable. For sharded tables, you must also use the `rds_aurora.limitless_create_table_shard_key` variable. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md).

```
-- Set the variables.
SET rds_aurora.limitless_create_table_mode='sharded';
SET rds_aurora.limitless_create_table_shard_key='{"a"}';

-- "source" is the source table whose columns and data types are used to create the new "destination" table.
SELECT * INTO destination FROM source;
```

Currently, the `SELECT INTO` operation is performed through the router, not directly through the shards. Therefore, performance can be slow.

For general information, see [SELECT INTO](https://www.postgresql.org/docs/current/sql-selectinto.html) in the PostgreSQL documentation.

## Constraints
<a name="limitless-reference.DDL-limitations.Constraints"></a>

The following limitations apply to constraints in Aurora PostgreSQL Limitless Database.

**CHECK**  
Simple constraints that involve comparison operators with literals are supported. More complex expressions and constraints that require function validations aren't supported, as shown in the following examples.  

```
CREATE TABLE my_table (
    id  INT CHECK (id > 0)                                     -- supported
  , val INT CHECK (val > 0 AND val < 1000)                     -- supported
  , tag TEXT CHECK (length(tag) > 0)                           -- not supported: throws "Expression inside CHECK constraint is not supported"
  , op_date TIMESTAMP WITH TIME ZONE CHECK (op_date <= now())  -- not supported: throws "Expression inside CHECK constraint is not supported"
);
```
You can give constraints explicit names, as shown in the following example.  

```
CREATE TABLE my_table (
    id  INT CONSTRAINT positive_id  CHECK (id > 0)
  , val INT CONSTRAINT val_in_range CHECK (val > 0 AND val < 1000)
);
```
You can use table-level constraint syntax with the `CHECK` constraint, as shown in the following example.  

```
CREATE TABLE my_table (
    id INT CONSTRAINT positive_id  CHECK (id > 0)
  , min_val INT CONSTRAINT min_val_in_range CHECK (min_val > 0 AND min_val < 1000)
  , max_val INT
  , CONSTRAINT max_val_in_range CHECK (max_val > 0 AND max_val < 1000 AND max_val > min_val)
);
```

**EXCLUDE**  
Exclusion constraints aren't supported in Aurora PostgreSQL Limitless Database.

**FOREIGN KEY**  
For more information, see [Foreign keys](#limitless-reference.DDL-limitations.FKs).

**NOT NULL**  
`NOT NULL` constraints are supported with no restrictions.

**PRIMARY KEY**  
Primary key implies unique constraints and therefore the same restrictions on unique constraints apply on primary key. This means:  
+ If a table is converted into a sharded table, the shard key must be a subset of the primary key. That is, the primary key contains all columns of the shard key.
+ If a table is converted into a reference table, it must have a primary key.
The following examples illustrate the use of primary keys.  

```
-- Create a standard table.
CREATE TABLE public.my_table (
    item_id INT
  , location_code INT
  , val INT
  , comment text
);

-- Change the table to a sharded table using the 'item_id' and 'location_code' columns as shard keys.
CALL rds_aurora.limitless_alter_table_type_sharded('public.my_table', ARRAY['item_id', 'location_code']);
```
Trying to add a primary key that doesn't contain a shard key:  

```
-- Add column 'item_id' as the primary key.
-- Invalid because the primary key doesnt include all columns from the shard key:
-- 'location_code' is part of the shard key but not part of the primary key
ALTER TABLE public.my_table ADD PRIMARY KEY (item_id); -- ERROR

-- add column "val" as primary key
-- Invalid because primary key does not include all columns from shard key:
--  item_id and location_code iare part of shard key but not part of the primary key
ALTER TABLE public.my_table ADD PRIMARY KEY (item_id); -- ERROR
```
Trying to add a primary key that does contain a shard key:  

```
-- Add the 'item_id' and 'location_code' columns as the primary key.
-- Valid because the primary key contains the shard key.
ALTER TABLE public.my_table ADD PRIMARY KEY (item_id, location_code); -- OK

-- Add the 'item_id', 'location_code', and 'val' columns as the primary key.
-- Valid because the primary key contains the shard key.
ALTER TABLE public.my_table ADD PRIMARY KEY (item_id, location_code, val); -- OK
```
Change a standard table to a reference table.  

```
-- Create a standard table.
CREATE TABLE zipcodes (zipcode INT PRIMARY KEY, details VARCHAR);

-- Convert the table to a reference table.
CALL rds_aurora.limitless_alter_table_type_reference('public.zipcode');
```
For more information on creating sharded and reference tables, see [Creating Aurora PostgreSQL Limitless Database tables](limitless-creating.md).

**UNIQUE**  
In sharded tables, the unique key must contain the shard key, that is, the shard key must be a subset of the unique key. This is checked when changing the table type to sharded. In reference tables there's no restriction.  

```
CREATE TABLE customer (
    customer_id INT NOT NULL
  , zipcode INT
  , email TEXT UNIQUE
);
```
Table-level `UNIQUE` constraints are supported, as shown in the following example.  

```
CREATE TABLE customer (
    customer_id INT NOT NULL
  , zipcode INT
  , email TEXT
  , CONSTRAINT zipcode_and_email UNIQUE (zipcode, email)
);
```
The following example shows the use of a primary key and a unique key together. Both keys must include the shard key.  

```
SET rds_aurora.limitless_create_table_mode='sharded';
SET rds_aurora.limitless_create_table_shard_key='{"p_id"}';
CREATE TABLE t1 (
p_id BIGINT NOT NULL,
c_id BIGINT NOT NULL,
PRIMARY KEY (p_id),
UNIQUE (p_id, c_id)
);
```

For more information, see [Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) in the PostgreSQL documentation.

## Default values
<a name="limitless-reference.DDL-limitations.DefaultValues"></a>

Aurora PostgreSQL Limitless Database supports expressions in default values.

The following example shows the use of default values.

```
CREATE TABLE t (
    a INT DEFAULT 5,
    b TEXT DEFAULT 'NAN',
    c NUMERIC
);

CALL rds_aurora.limitless_alter_table_type_sharded('t', ARRAY['a']);
INSERT INTO t DEFAULT VALUES;
SELECT * FROM t;

 a |  b  | c 
---+-----+---
 5 | NAN |
(1 row)
```

Expressions are supported, as shown in the following example.

```
CREATE TABLE t1 (a NUMERIC DEFAULT random());
```

The following example adds a new column that is `NOT NULL` and has a default value.

```
ALTER TABLE t ADD COLUMN d BOOLEAN NOT NULL DEFAULT FALSE;
SELECT * FROM t;

 a |  b  | c | d 
---+-----+---+---
 5 | NAN |   | f
(1 row)
```

The following example alters an existing column with a default value.

```
ALTER TABLE t ALTER COLUMN c SET DEFAULT 0.0;
INSERT INTO t DEFAULT VALUES;
SELECT * FROM t;

 a |  b  | c   |  d  
---+-----+-----+-----
 5 | NAN |     | f
 5 | NAN | 0.0 | f
(2 rows)
```

The following example drops a default value.

```
ALTER TABLE t ALTER COLUMN a DROP DEFAULT;
INSERT INTO t DEFAULT VALUES;
SELECT * FROM t;

 a |  b  | c   |  d  
---+-----+-----+-----
 5 | NAN |     | f
 5 | NAN | 0.0 | f
   | NAN | 0.0 | f
(3 rows)
```

For more information, see [Default values](https://www.postgresql.org/docs/current/ddl-default.html) in the PostgreSQL documentation.

## Extensions
<a name="limitless-reference.DDL-limitations.Extensions"></a>

The following PostgreSQL extensions are supported in Aurora PostgreSQL Limitless Database:
+ `aurora_limitless_fdw` – This extension is preinstalled. You can't drop it.
+ `aws_s3` – This extension works in Aurora PostgreSQL Limitless Database similar to the way it does in Aurora PostgreSQL.

  You can import data from an Amazon S3 bucket to an Aurora PostgreSQL Limitless Database DB cluster, or export data from an Aurora PostgreSQL Limitless Database DB cluster to an Amazon S3 bucket. For more information, see [Importing data from Amazon S3 into an Aurora PostgreSQL DB cluster](USER_PostgreSQL.S3Import.md) and [Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](postgresql-s3-export.md).
+ `btree_gin`
+ `citext`
+ `ip4r`
+ `pg_buffercache` – This extension behaves differently in Aurora PostgreSQL Limitless Database from community PostgreSQL. For more information, see [pg\_buffercache differences in Aurora PostgreSQL Limitless Database](#limitless-reference.DDL-limitations.Extensions.pg_buffercache).
+ `pg_stat_statements`
+ `pg_trgm`
+ `pgcrypto`
+ `pgstattuple` – This extension behaves differently in Aurora PostgreSQL Limitless Database from community PostgreSQL. For more information, see [pgstattuple differences in Aurora PostgreSQL Limitless Database](#limitless-reference.DDL-limitations.Extensions.pgstattuple).
+ `pgvector`
+ `plpgsql` – This extension is preinstalled, but you can drop it.
+ `PostGIS` – Long transactions and table management functions aren't supported. Modifying the spatial reference table isn't supported.
+ `unaccent`
+ `uuid`

Most PostgreSQL extensions currently aren't supported in Aurora PostgreSQL Limitless Database. However, you can still use the [shared\_preload\_libraries](https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-PRELOAD) (SPL) configuration setting to load extensions into the Aurora PostgreSQL primary DB cluster. They are also loaded into Aurora PostgreSQL Limitless Database, but might not function correctly.

For example, you can load the `pg_hint_plan` extension, but loading it doesn't guarantee that the hints passed in query comments are used.

**Note**  
You can't modify objects associated with the [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) extension. For information on installing `pg_stat_statements`, see [limitless\_stat\_statements](limitless-monitoring-views.md#limitless_stat_statements).

You can use the `pg_available_extensions` and `pg_available_extension_versions` functions to find the extensions that are supported in Aurora PostgreSQL Limitless Database.

The following DDLs are supported for extensions:

**CREATE EXTENSION**  
You can create extensions, as in PostgreSQL.  

```
CREATE EXTENSION [ IF NOT EXISTS ] {{extension_name}}
    [ WITH ] [ SCHEMA {{schema_name}} ]
             [ VERSION {{version}} ]
             [ CASCADE ]
```
For more information, see [CREATE EXTENSION](https://www.postgresql.org/docs/current/sql-createextension.html) in the PostgreSQL documentation.

**ALTER EXTENSION**  
The following DDLs are supported:  

```
ALTER EXTENSION {{name}} UPDATE [ TO {{new_version}} ]

ALTER EXTENSION {{name}} SET SCHEMA {{new_schema}}
```
For more information, see [ALTER EXTENSION](https://www.postgresql.org/docs/current/sql-alterextension.html) in the PostgreSQL documentation.

**DROP EXTENSION**  
You can drop extensions, as in PostgreSQL.  

```
DROP EXTENSION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```
For more information, see [DROP EXTENSION](https://www.postgresql.org/docs/current/sql-dropextension.html) in the PostgreSQL documentation.

The following DDLs aren't supported for extensions:

**ALTER EXTENSION**  
You can't add or drop member objects from extensions.  

```
ALTER EXTENSION {{name}} ADD {{member_object}}

ALTER EXTENSION {{name}} DROP {{member_object}}
```

### pg\_buffercache differences in Aurora PostgreSQL Limitless Database
<a name="limitless-reference.DDL-limitations.Extensions.pg_buffercache"></a>

In Aurora PostgreSQL Limitless Database, when you install the [pg\_buffercache](https://www.postgresql.org/docs/current/pgbuffercache.html) extension and use the `pg_buffercache` view, you receive buffer-related information only from the node to which you're currently connected: the router. Similarly, using the function `pg_buffercache_summary` or `pg_buffercache_usage_counts` provides information only from the connected node.

You can have numerous nodes and might need to access buffer information from any node to diagnose issues effectively. Therefore, Limitless Database provides the following functions:
+ `rds_aurora.limitless_pg_buffercache({{subcluster_id}})`
+ `rds_aurora.limitless_pg_buffercache_summary({{subcluster_id}})`
+ `rds_aurora.limitless_pg_buffercache_usage_counts({{subcluster_id}})`

By inputting the subcluster ID of any node, whether it's a router or shard, you can easily access the buffer information specific to that node. These functions are directly available when you install the `pg_buffercache` extension in the limitless database.

**Note**  
Aurora PostgreSQL Limitless Database supports these functions for version 1.4 and higher of the `pg_buffercache` extension.

The columns shown in the `limitless_pg_buffercache` view differ slightly from those in the `pg_buffercache` view:
+ `bufferid` – Remains unchanged from `pg_buffercache`.
+ `relname` – Instead of displaying the file node number as in `pg_buffercache`, `limitless_pg_buffercache` presents the associated `relname` if available in the current database or shared system catalogs, otherwise `NULL`.
+ `parent_relname` – This new column, not present in `pg_buffercache`, displays the parent `relname` if the value in the `relname` column represents a partitioned table (in the case of sharded tables). Otherwise, it displays `NULL`.
+ `spcname` – Instead of displaying the tablespace object identifier (OID) as in `pg_buffercache`, `limitless_pg_buffercache` displays the tablespace name.
+ `datname` – Instead of displaying the database OID as in `pg_buffercache`, `limitless_pg_buffercache` displays the database name.
+ `relforknumber` – Remains unchanged from `pg_buffercache`.
+ `relblocknumber` – Remains unchanged from `pg_buffercache`.
+ `isdirty` – Remains unchanged from `pg_buffercache`.
+ `usagecount` – Remains unchanged from `pg_buffercache`.
+ `pinning_backends` – Remains unchanged from `pg_buffercache`.

The columns in `limitless_pg_buffercache_summary` and `limitless_pg_buffercache_usage_counts` views are the same as those in the regular `pg_buffercache_summary` and `pg_buffercache_usage_counts` views, respectively.

By using these functions, you can access detailed buffer cache information across all nodes in your Limitless Database environment, facilitating more effective diagnosis and management of your database systems.

### pgstattuple differences in Aurora PostgreSQL Limitless Database
<a name="limitless-reference.DDL-limitations.Extensions.pgstattuple"></a>

In Aurora PostgreSQL, the [pgstattuple](https://www.postgresql.org/docs/current/pgstattuple.html) extension currently doesn't support foreign tables, partitioned tables, or partitioned indexes. However, in Aurora PostgreSQL Limitless Database, user-created objects are often among these unsupported types. While there are regular tables and indexes (for example, catalog tables and their indexes), most objects reside on foreign nodes, making them foreign objects for the router.

We recognize the importance of this extension for obtaining tuple-level statistics, which is crucial for tasks such as removing bloat and gathering diagnostic information. Therefore, Aurora PostgreSQL Limitless Database provides support for the `pgstattuple` extension in limitless databases.

Aurora PostgreSQL Limitless Database includes the following functions in the `rds_aurora` schema:

**Tuple-level statistics functions**  
**`rds_aurora.limitless_pgstattuple({{relation_name}})`**  
+ Purpose: Extract tuple-level statistics for standard tables and their indexes
+ Input: `relation_name` (text) – The name of the relation
+ Output: Columns consistent with those returned by the `pgstattuple` function in Aurora PostgreSQL
**`rds_aurora.limitless_pgstattuple({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract tuple-level statistics for reference tables, sharded tables, catalog tables, and their indexes
+ Input:
  + `relation_name` (text) – The name of the relation
  + `subcluster_id` (text) – The subcluster ID of the node where the statistics are to be extracted
+ Output:
  + For reference and catalog tables (including their indexes), columns are consistent with those in Aurora PostgreSQL.
  + For sharded tables, the statistics represent only the partition of the sharded table residing on the specified subcluster.

**Index statistics functions**  
**`rds_aurora.limitless_pgstatindex({{relation_name}})`**  
+ Purpose: Extract statistics for B-tree indexes on standard tables
+ Input: `relation_name` (text) – The name of the B-tree index
+ Output: All columns except `root_block_no` are returned. The returned columns are consistent with the `pgstatindex` function in Aurora PostgreSQL.
**`rds_aurora.limitless_pgstatindex({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract statistics for B-tree indexes on reference tables, sharded tables, and catalog tables.
+ Input:
  + `relation_name` (text) – The name of the B-tree index
  + `subcluster_id` (text) – The subcluster ID of the node where the statistics are to be extracted
+ Output:
  + For reference and catalog table indexes, all columns (except `root_block_no`) are returned. The returned columns are consistent with Aurora PostgreSQL.
  + For sharded tables, the statistics represent only the partition of the sharded table index residing on the specified subcluster. The `tree_level` column shows the average across all table slices on the requested subcluster.
**`rds_aurora.limitless_pgstatginindex({{relation_name}})`**  
+ Purpose: Extract statistics for Generalized Inverted Indexes (GINs) on standard tables
+ Input: `relation_name` (text) – The name of the GIN
+ Output: Columns consistent with those returned by the `pgstatginindex` function in Aurora PostgreSQL
**`rds_aurora.limitless_pgstatginindex({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract statistics for GIN indexes on reference tables, sharded tables, and catalog tables.
+ Input:
  + `relation_name` (text) – The name of the index
  + `subcluster_id` (text) – The subcluster ID of the node where the statistics are to be extracted
+ Output:
  + For reference and catalog table GIN indexes, columns are consistent with those in Aurora PostgreSQL.
  + For sharded tables, the statistics represent only the partition of the sharded table index residing on the specified subcluster.
**`rds_aurora.limitless_pgstathashindex({{relation_name}})`**  
+ Purpose: Extract statistics for hash indexes on standard tables
+ Input: `relation_name` (text) – The name of the hash index
+ Output: Columns consistent with those returned by the `pgstathashindex` function in Aurora PostgreSQL
**`rds_aurora.limitless_pgstathashindex({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract statistics for hash indexes on reference tables, sharded tables, and catalog tables.
+ Input:
  + `relation_name` (text) – The name of the index
  + `subcluster_id` (text) – The subcluster ID of the node where the statistics are to be extracted
+ Output:
  + For reference and catalog table hash indexes, columns are consistent with Aurora PostgreSQL.
  + For sharded tables, the statistics represent only the partition of the sharded table index residing on the specified subcluster.

**Page count functions**  
**`rds_aurora.limitless_pg_relpages({{relation_name}})`**  
+ Purpose: Extract the page count for standard tables and their indexes
+ Input: `relation_name` (text) – The name of the relation
+ Output: Page count of the specified relation
**`rds_aurora.limitless_pg_relpages({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract the page count for reference tables, sharded tables, and catalog tables (including their indexes)
+ Input:
  + `relation_name` (text) – The name of the relation
  + `subcluster_id` (text) – The subcluster ID of the node where the page count is to be extracted
+ Output: For sharded tables, the page count is the sum of pages across all table slices on the specified subcluster.

**Approximate tuple-level statistics functions**  
**`rds_aurora.limitless_pgstattuple_approx({{relation_name}})`**  
+ Purpose: Extract approximate tuple-level statistics for standard tables and their indexes
+ Input: `relation_name` (text) – The name of the relation
+ Output: Columns consistent with those returned by the pgstattuple\_approx function in Aurora PostgreSQL
**`rds_aurora.limitless_pgstattuple_approx({{relation_name}}, {{subcluster_id}})`**  
+ Purpose: Extract approximate tuple-level statistics for reference tables, sharded tables, and catalog tables (including their indexes)
+ Input:
  + `relation_name` (text) – The name of the relation
  + `subcluster_id` (text) – The subcluster ID of the node where the statistics are to be extracted
+ Output:
  + For reference and catalog tables (including their indexes), columns are consistent with those in Aurora PostgreSQL.
  + For sharded tables, the statistics represent only the partition of the sharded table residing on the specified subcluster.

**Note**  
Currently, Aurora PostgreSQL Limitless Database doesn't support the `pgstattuple` extension on materialized views, TOAST tables, or temporary tables.  
In Aurora PostgreSQL Limitless Database, you must provide the input as text, although Aurora PostgreSQL supports other formats.

## Foreign keys
<a name="limitless-reference.DDL-limitations.FKs"></a>

Foreign key (`FOREIGN KEY`) constraints are supported with some limitations:
+ `CREATE TABLE` with `FOREIGN KEY` is supported only for standard tables. To create a sharded or reference table with `FOREIGN KEY`, first create the table without a foreign key constraint. Then modify it using the following statement:

  ```
  ALTER TABLE ADD CONSTRAINT;
  ```
+ Converting a standard table to a sharded or reference table isn't supported when the table has a foreign key constraint. Drop the constraint, then add it after conversion.
+ The following limitations apply to table types for foreign key constraints:
  + A standard table can have a foreign key constraint to another standard table.
  + A sharded table can have a foreign key constraint if the parent and child tables are collocated and the foreign key is a superset of the shard key.
  + A sharded table can have a foreign key constraint to a reference table.
  + A reference table can have a foreign key constraint to another reference table.

**Topics**
+ [Foreign key options](#limitless-reference.DDL-limitations.FKs.options)
+ [Examples](#limitless-reference.DDL-limitations.FKs.examples)

### Foreign key options
<a name="limitless-reference.DDL-limitations.FKs.options"></a>

Foreign keys are supported in Aurora PostgreSQL Limitless Database for some DDL options. The following table lists options that are supported and not supported between Aurora PostgreSQL Limitless Database tables.


| DDL option | Reference to reference | Sharded to sharded (collocated) | Sharded to reference | Standard to standard | 
| --- | --- | --- | --- | --- | 
| `DEFERRABLE` | Yes | Yes | Yes | Yes | 
| `INITIALLY DEFERRED` | Yes | Yes | Yes | Yes | 
| `INITIALLY IMMEDIATE` | Yes | Yes | Yes | Yes | 
| `MATCH FULL` | Yes | Yes | Yes | Yes | 
| `MATCH PARTIAL` | No | No | No | No | 
| `MATCH SIMPLE` | Yes | Yes | Yes | Yes | 
| `NOT DEFERRABLE` | Yes | Yes | Yes | Yes | 
| `NOT VALID` | Yes | No | No | Yes | 
| `ON DELETE CASCADE` | Yes | Yes | Yes | Yes | 
| `ON DELETE NO ACTION` | Yes | Yes | Yes | Yes | 
| `ON DELETE RESTRICT` | Yes | Yes | Yes | Yes | 
| `ON DELETE SET DEFAULT` | No | No | No | No | 
| `ON DELETE SET NULL` | Yes | No | No | Yes | 
| `ON UPDATE CASCADE` | No | No | No | Yes | 
| `ON UPDATE NO ACTION` | Yes | Yes | Yes | Yes | 
| `ON UPDATE RESTRICT` | Yes | Yes | Yes | Yes | 
| `ON UPDATE SET DEFAULT` | No | No | No | No | 
| `ON UPDATE SET NULL` | Yes | No | No | Yes | 

### Examples
<a name="limitless-reference.DDL-limitations.FKs.examples"></a>
+ Standard to standard:

  ```
  set rds_aurora.limitless_create_table_mode='standard';
  
  CREATE TABLE products(
      product_no integer PRIMARY KEY,
      name text,
      price numeric
  );
  
  CREATE TABLE orders (
      order_id integer PRIMARY KEY,
      product_no integer REFERENCES products (product_no),
      quantity integer
  );
  
  SELECT constraint_name, table_name, constraint_type 
  FROM information_schema.table_constraints WHERE constraint_type='FOREIGN KEY';
  
   constraint_name         | table_name  | constraint_type 
  -------------------------+-------------+-----------------
   orders_product_no_fkey  | orders      | FOREIGN KEY
  (1 row)
  ```
+ Sharded to sharded (collocated):

  ```
  set rds_aurora.limitless_create_table_mode='sharded';
  set rds_aurora.limitless_create_table_shard_key='{"product_no"}'; 
  CREATE TABLE products(
      product_no integer PRIMARY KEY,
      name text,
      price numeric
  );
  
  set rds_aurora.limitless_create_table_shard_key='{"order_id"}'; 
  set rds_aurora.limitless_create_table_collocate_with='products';
  CREATE TABLE orders (
      order_id integer PRIMARY KEY,
      product_no integer,
      quantity integer
  );
  
  ALTER TABLE orders ADD CONSTRAINT order_product_fk FOREIGN KEY (product_no) REFERENCES products (product_no);
  ```
+ Sharded to reference:

  ```
  set rds_aurora.limitless_create_table_mode='reference';
  CREATE TABLE products(
      product_no integer PRIMARY KEY,
      name text,
      price numeric
  );
  
  set rds_aurora.limitless_create_table_mode='sharded';
  set rds_aurora.limitless_create_table_shard_key='{"order_id"}'; 
  CREATE TABLE orders (
      order_id integer PRIMARY KEY,
      product_no integer,
      quantity integer
  );
  
  ALTER TABLE orders ADD CONSTRAINT order_product_fk FOREIGN KEY (product_no) REFERENCES products (product_no);
  ```
+ Reference to reference:

  ```
  set rds_aurora.limitless_create_table_mode='reference';
  CREATE TABLE products(
      product_no integer PRIMARY KEY,
      name text,
      price numeric
  );
  CREATE TABLE orders (
      order_id integer PRIMARY KEY,
      product_no integer,
      quantity integer
  );
  
  ALTER TABLE orders ADD CONSTRAINT order_product_fk FOREIGN KEY (product_no) REFERENCES products (product_no);
  ```

## Functions
<a name="limitless-reference.DDL-limitations.Functions"></a>

Functions are supported in Aurora PostgreSQL Limitless Database.

The following DDLs are supported for functions:

**CREATE FUNCTION**  
You can create functions, as in Aurora PostgreSQL, with the exception of changing their volatility while replacing them.  
For more information, see [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html) in the PostgreSQL documentation.

**ALTER FUNCTION**  
You can alter functions, as in Aurora PostgreSQL, with the exception of changing their volatility.  
For more information, see [ALTER FUNCTION](https://www.postgresql.org/docs/current/sql-alterfunction.html) in the PostgreSQL documentation.

**DROP FUNCTION**  
You can drop functions, as in Aurora PostgreSQL.  

```
DROP FUNCTION [ IF EXISTS ] {{name}} [ ( [ [ {{argmode}} ] [ {{argname}} ] {{argtype}} [, ...] ] ) ] [, ...]
    [ CASCADE | RESTRICT ]
```
For more information, see [DROP FUNCTION](https://www.postgresql.org/docs/current/sql-dropfunction.html) in the PostgreSQL documentation.

**Topics**
+ [Function distribution](#limitless-function-distribution)
+ [Function volatility](#limitless-function-volatility)

### Function distribution
<a name="limitless-function-distribution"></a>

When all of the statements of a function are targeted to a single shard, it's beneficial to push the entire function down to the target shard. Then the result is propagated back to the router, rather than unraveling the function at the router itself. Function and stored procedure pushdown capability is useful for customers who want to run their function or stored procedure closer to the data source, that is the shard.

To distribute a function, first create the function, then call the `rds_aurora.limitless_distribute_function` procedure to distribute it. This function uses the following syntax:

```
SELECT rds_aurora.limitless_distribute_function('{{function_prototype}}', ARRAY['{{shard_key}}'], '{{collocating_table}}');
```

The function takes the following parameters:
+ `{{function_prototype}}` – The function to be distributed. Mention only the input arguments, and not any of the output arguments.

  If any of the arguments are defined as `OUT` parameters, don't include their type in the arguments of `function_prototype`.
+ `ARRAY['{{shard_key}}']` – The list of function arguments that are identified as the shard key for the function.
+ `{{collocating_table}}` – The sharded table that contains the range of data on the target shard.

To identify the shard where to push down this function for running, the system takes the `ARRAY['{{shard_key}}']` argument, hashes it, and finds the shard from `{{collocating_table}}` that hosts the range containing this hash value.

**Restrictions**  
When you distribute a function or procedure, it only deals with data that's bounded by the shard key range in that shard. In cases where the function or procedure tries to access data from a different shard, the results returned by the distributed function or procedure will be different compared to one that isn't distributed.  
For example, you create a function containing queries that will touch multiple shards, but then call the `rds_aurora.limitless_distribute_function` procedure to distribute it. When you invoke this function by providing arguments for a shard key, it is likely that the results of running it will be bounded by the values present in that shard. These results are different from ones produced without distributing the function.

**Examples**  
 Consider the following function `func` where we have the sharded table `customers` with the shard key `customer_id`.  

```
postgres_limitless=> CREATE OR REPLACE FUNCTION func(c_id integer, sc integer) RETURNS int
    language SQL
    volatile
    AS $$
    UPDATE customers SET score = sc WHERE customer_id = c_id RETURNING score;
    $$;
```
Now we distribute this function:  

```
SELECT rds_aurora.limitless_distribute_function('func(integer, integer)', ARRAY['c_id'], 'customers');
```
The following are example query plans.  

```
EXPLAIN(costs false, verbose true) SELECT func(27+1,10);

                    QUERY PLAN
 --------------------------------------------------
  Foreign Scan
    Output: (func((27 + 1), 10))
    Remote SQL:  SELECT func((27 + 1), 10) AS func
  Single Shard Optimized
 (4 rows)
```

```
EXPLAIN(costs false, verbose true)
 SELECT * FROM customers,func(customer_id, score) WHERE customer_id=10 AND score=27;

                          QUERY PLAN
 ---------------------------------------------------------------------
  Foreign Scan
    Output: customer_id, name, score, func
    Remote SQL:  SELECT customers.customer_id,
      customers.name,
      customers.score,
      func.func
     FROM public.customers,
      LATERAL func(customers.customer_id, customers.score) func(func)
    WHERE ((customers.customer_id = 10) AND (customers.score = 27))
  Single Shard Optimized
 (10 rows)
```
The following example shows a procedure with `IN` and `OUT` parameters as arguments.  

```
CREATE OR REPLACE FUNCTION get_data(OUT id INTEGER, IN arg_id INT)
    AS $$
    BEGIN
        SELECT customer_id,
        INTO id
        FROM customer
        WHERE customer_id = arg_id;
    END;
    $$ LANGUAGE plpgsql;
```
The following example distributes the procedure using only `IN` parameters.  

```
EXPLAIN(costs false, verbose true) SELECT * FROM get_data(1);

             QUERY PLAN
 -----------------------------------
  Foreign Scan
    Output: id
    Remote SQL:  SELECT customer_id
     FROM get_data(1) get_data(id)
  Single Shard Optimized
 (6 rows)
```

### Function volatility
<a name="limitless-function-volatility"></a>

You can determine whether a function is immutable, stable, or volatile by checking the `provolatile` value in the [pg\_proc](https://www.postgresql.org/docs/current/catalog-pg-proc.html) view. The `provolatile` value indicates whether the function's result depends only on its input arguments, or is affected by outside factors.

The value is one of the following:
+ `i` – Immutable functions, which always deliver the same result for the same inputs
+ `s` – Stable functions, whose results (for fixed inputs) don't change within a scan
+ `v` – Volatile functions, whose results might change at any time. Also use `v` for functions with side effects, so that calls to them can't be optimized away.

The following examples show volatile functions.

```
SELECT proname, provolatile FROM pg_proc WHERE proname='pg_sleep';

 proname  | provolatile
----------+-------------
 pg_sleep | v
(1 row)

SELECT proname, provolatile FROM pg_proc WHERE proname='uuid_generate_v4';

     proname      | provolatile
------------------+-------------
 uuid_generate_v4 | v
(1 row)

SELECT proname, provolatile FROM pg_proc WHERE proname='nextval';

 proname | provolatile
---------+-------------
 nextval | v
(1 row)
```

Changing the volatility of an existing function isn't supported in Aurora PostgreSQL Limitless Database. This applies to both `ALTER FUNCTION` and `CREATE OR REPLACE FUNCTION` commands, as shown in the following examples.

```
-- Create an immutable function
CREATE FUNCTION immutable_func1(name text) RETURNS text language plpgsql
AS $$
BEGIN
    RETURN name;
END;
$$IMMUTABLE;

-- Altering the volatility throws an error
ALTER FUNCTION immutable_func1 STABLE;

-- Replacing the function with altered volatility throws an error
CREATE OR REPLACE FUNCTION immutable_func1(name text) RETURNS text language plpgsql
AS $$
BEGIN
    RETURN name;
END;
$$VOLATILE;
```

We highly recommend that you assign the correct volatilities to functions. For example, if your function uses `SELECT` from multiple tables or references database objects, don't set it as `IMMUTABLE`. If the table contents ever change, the immutability is broken.

Aurora PostgreSQL allows `SELECT` inside immutable functions, but the results might be incorrect. Aurora PostgreSQL Limitless Database can return both errors and incorrect results. For more information on function volatility, see [Function volatility categories](https://www.postgresql.org/docs/current/xfunc-volatility.html) in the PostgreSQL documentation.

## Sequences
<a name="limitless-reference.DDL-limitations.Sequences"></a>

Named sequences are database objects that generate unique numbers in ascending or descending order. `CREATE SEQUENCE` creates a new sequence number generator. Sequence values are guaranteed to be unique.

When you create a named sequence in Aurora PostgreSQL Limitless Database, a distributed sequence object is created. Then Aurora PostgreSQL Limitless Database distributes non-overlapping chunks of sequence values across all Distributed Transaction Routers (routers). Chunks are represented as local sequence objects on routers; therefore, sequence operations such as `nextval` and `currval` are run locally. Routers operate independently, and request new chunks from the distributed sequence when needed.

For more information on sequences, see [CREATE SEQUENCE](https://www.postgresql.org/docs/current/sql-createsequence.html) in the PostgreSQL documentation.

**Topics**
+ [Requesting a new chunk](#limitless-reference.DDL-limitations.Sequences.request-chunk)
+ [Limitations](#limitless-reference.DDL-limitations.Sequences.limitations)
+ [Unsupported options](#limitless-reference.DDL-limitations.Sequences.unsupported)
+ [Examples](#limitless-reference.DDL-limitations.Sequences.examples)
+ [Sequence views](#limitless-reference.DDL-limitations.Sequences.views)
+ [Troubleshooting sequence issues](#limitless-reference.DDL-limitations.Sequences.troubleshooting)

### Requesting a new chunk
<a name="limitless-reference.DDL-limitations.Sequences.request-chunk"></a>

You configure the sizes of chunks allocated on routers by using the `rds_aurora.limitless_sequence_chunk_size` parameter. The default value is `250000`. Each router initially owns two chunks: active and reserved. Active chunks are used to configure local sequence objects (setting `minvalue` and `maxvalue`), and reserved chunks are stored in an internal catalog table. When an active chunk reaches the minimum or maximum value, it's replaced by the reserved chunk. To do that, `ALTER SEQUENCE` is used internally, meaning that `AccessExclusiveLock` is acquired.

Background workers run every 10 seconds on router nodes to scan sequences for used reserved chunks. If a used chunk is found, the worker requests a new chunk from the distributed sequence. Make sure to set the chunk size large enough that the background workers have enough time to request new ones. Remote requests never happen in the context of user sessions, which means that you can't request a new sequence directly.

### Limitations
<a name="limitless-reference.DDL-limitations.Sequences.limitations"></a>

The following limitations apply to sequences in Aurora PostgreSQL Limitless Database:
+ The `pg_sequence` catalog, `pg_sequences` function, and `SELECT * FROM {{sequence_name}}` statement all show only the local sequence state, not the distributed state.
+ Sequence values are guaranteed to be unique, and are guaranteed to be monotonic within a session. But they can be out of order with `nextval` statements run in other sessions, if those sessions are connected to other routers.
+ Make sure that the sequence size (number of available values) is large enough to be distributed across all routers. Use the `rds_aurora.limitless_sequence_chunk_size` parameter to configure the `chunk_size`. (Each router has two chunks.)
+ The `CACHE` option is supported, but the cache must be smaller than `chunk_size`.

### Unsupported options
<a name="limitless-reference.DDL-limitations.Sequences.unsupported"></a>

The following options aren't supported for sequences in Aurora PostgreSQL Limitless Database.

**Sequence manipulation functions**  
The `setval` function isn't supported. For more information, see [Sequence Manipulation Functions](https://www.postgresql.org/docs/current/functions-sequence.html) in the PostgreSQL documentation.

**CREATE SEQUENCE**  
The following options aren't supported.  

```
CREATE [{ TEMPORARY | TEMP} | UNLOGGED] SEQUENCE
    [[ NO ] CYCLE]
```
For more information, see [CREATE SEQUENCE](https://www.postgresql.org/docs/current/sql-createsequence.html) in the PostgreSQL documentation.

**ALTER SEQUENCE**  
The following options aren't supported.  

```
ALTER SEQUENCE
    [[ NO ] CYCLE]
```
For more information, see [ALTER SEQUENCE](https://www.postgresql.org/docs/current/sql-altersequence.html) in the PostgreSQL documentation.

**ALTER TABLE**  
The `ALTER TABLE` command isn't supported for sequences.

### Examples
<a name="limitless-reference.DDL-limitations.Sequences.examples"></a>

**CREATE/DROP SEQUENCE**  

```
postgres_limitless=> CREATE SEQUENCE s;
CREATE SEQUENCE

postgres_limitless=> SELECT nextval('s');

 nextval
---------
       1
(1 row)

postgres_limitless=> SELECT * FROM pg_sequence WHERE seqrelid='s'::regclass;

 seqrelid | seqtypid | seqstart | seqincrement | seqmax | seqmin | seqcache | seqcycle 
----------+----------+----------+--------------+--------+--------+----------+----------
    16960 |       20 |        1 |            1 |  10000 |      1 |        1 | f
(1 row)

% connect to another router
postgres_limitless=> SELECT nextval('s');

 nextval 
---------
   10001
(1 row)

postgres_limitless=> SELECT * FROM pg_sequence WHERE seqrelid='s'::regclass;

 seqrelid | seqtypid | seqstart | seqincrement | seqmax | seqmin | seqcache | seqcycle 
----------+----------+----------+--------------+--------+--------+----------+----------
    16959 |       20 |    10001 |            1 |  20000 |  10001 |        1 | f
(1 row)

postgres_limitless=> DROP SEQUENCE s;
DROP SEQUENCE
```

**ALTER SEQUENCE**  

```
postgres_limitless=> CREATE SEQUENCE s;
CREATE SEQUENCE

postgres_limitless=> ALTER SEQUENCE s RESTART 500;
ALTER SEQUENCE

postgres_limitless=> SELECT nextval('s');

 nextval
---------
     500
(1 row)

postgres_limitless=> SELECT currval('s');

 currval
---------
     500
(1 row)
```

**Sequence manipulation functions**  

```
postgres=# CREATE TABLE t(a bigint primary key, b bigint);
CREATE TABLE

postgres=# CREATE SEQUENCE s minvalue 0 START 0;
CREATE SEQUENCE

postgres=# INSERT INTO t VALUES (nextval('s'), currval('s'));                                                                                             
INSERT 0 1

postgres=# INSERT INTO t VALUES (nextval('s'), currval('s'));
INSERT 0 1

postgres=# SELECT * FROM t;

 a | b
---+---
 0 | 0
 1 | 1
(2 rows)

postgres=# ALTER SEQUENCE s RESTART 10000;
ALTER SEQUENCE

postgres=# INSERT INTO t VALUES (nextval('s'), currval('s'));                                                                                             
INSERT 0 1

postgres=# SELECT * FROM t;

   a   |   b
-------+-------
     0 |     0
     1 |     1
 10000 | 10000
(3 rows)
```

### Sequence views
<a name="limitless-reference.DDL-limitations.Sequences.views"></a>

Aurora PostgreSQL Limitless Database provides the following views for sequences.

**rds\_aurora.limitless\_distributed\_sequence**  
This view shows a distributed sequence state and configuration. The `minvalue`, `maxvalue`, `start`, `inc`, and `cache` columns have the same meaning as in the [pg\_sequences](https://www.postgresql.org/docs/current/view-pg-sequences.html) view, and show the options with which the sequence was created. The `lastval` column shows the latest allocated or reserved value in a distributed sequence object. This doesn't mean that the value was already used, as routers keep sequence chunks locally.  

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_distributed_sequence WHERE sequence_name='test_serial_b_seq';

 schema_name |   sequence_name   | lastval | minvalue |  maxvalue  | start | inc | cache
-------------+-------------------+---------+----------+------------+-------+-----+-------
 public      | test_serial_b_seq | 1250000 |        1 | 2147483647 |     1 |   1 |     1
(1 row)
```

**rds\_aurora.limitless\_sequence\_metadata**  
This view shows distributed sequence metadata and aggregates sequence metadata from cluster nodes. It uses the following columns:  
+ `subcluster_id` – The cluster node ID that owns a chunk.
+ Active chunk – A chunk of a sequence that is being used (`active_minvalue`, `active_maxvalue`).
+ Reserved chunk – The local chunk that will be used next (`reserved_minvalue`, `reserved_maxvalue`).
+ `local_last_value` – The last observed value from a local sequence.
+ `chunk_size` – The size of a chunk, as configured on creation.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_sequence_metadata WHERE sequence_name='test_serial_b_seq' order by subcluster_id;

 subcluster_id |   sequence_name   | schema_name | active_minvalue | active_maxvalue | reserved_minvalue | reserved_maxvalue | chunk_size | chunk_state | local_last_value 
---------------+-------------------+-------------+-----------------+-----------------+-------------------+-------------------+------------+-------------+------------------
 1             | test_serial_b_seq | public      |          500001 |          750000 |           1000001 |           1250000 |     250000 |           1 |           550010
 2             | test_serial_b_seq | public      |          250001 |          500000 |            750001 |           1000000 |     250000 |           1 |                 
(2 rows)
```

### Troubleshooting sequence issues
<a name="limitless-reference.DDL-limitations.Sequences.troubleshooting"></a>

The following issues can occur with sequences.

**Chunk size not large enough**  
If the chunk size isn't set large enough and the transaction rate is high, the background workers might not have enough time to request new chunks before the active chunks are exhausted. This can lead to contention and wait events such as `LIMITLESS:AuroraLimitlessSequenceReplace`, `LWLock:LockManager` , `Lockrelation`, and `LWlock:bufferscontent`.  
Increase the value of the `rds_aurora.limitless_sequence_chunk_size` parameter.

**Sequence cache set too high**  
In PostgreSQL, sequence caching happens at the session level. Each session allocates successive sequence values during one access to the sequence object, and increases the sequence object's `last_value` accordingly. Then, the next uses of `nextval` within that session simply return the pre-allocated values without touching the sequence object.  
Any numbers allocated but not used within a session are lost when that session ends, resulting in "holes" in the sequence. This can consume the sequence\_chunk quickly and lead to to contention and wait events such as `LIMITLESS:AuroraLimitlessSequenceReplace`, `LWLock:LockManager` , `Lockrelation`, and `LWlock:bufferscontent`.  
Reduce the sequence cache setting.

The following figure shows wait events caused by sequence issues.

![Wait events caused by sequence issues.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/limitless_sequence_waits.png)
