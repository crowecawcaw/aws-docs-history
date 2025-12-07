# Migrating indexes to Aurora PostgreSQL

This topic provides reference information about migrating indexes from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. It compares and contrasts how indexes are implemented and used in both database systems, highlighting key differences and similarities. You’ll gain insight into the types of indexes supported, their limitations, and specific features available in each platform.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                | Key differences                                                    |
| -------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Three star feature compatibility | Three star automation level        | [Indexes](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.indexes "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.indexes") | PostgreSQL doesn’t support `CLUSTERED INDEX`. Few missing options. |

## SQL Server Usage

Indexes are physical disk structures used to optimize data access. They are associated with tables or materialized views and allow the query optimizer to access rows and individual column values without scanning an entire table.

An index consists of index keys, which are columns from a table or view. They are sorted in ascending or descending order providing quick access to individual values for queries that use equality or range predicates. Database indexes are similar to book indexes that list page numbers for common terms. Indexes created on multiple columns are called composite indexes.

SQL Server implements indexes using the balanced tree algorithm (B-tree).

###### Note

SQL Server supports additional index types such as hash indexes (for memory-optimized tables), spatial indexes, full text indexes, and XML indexes.

Indexes are created automatically to support table primary keys and unique constraints. They are required to efficiently enforce uniqueness. You can create up to 250 indexes on a table to support common queries.

SQL Server provides two types of B-tree indexes: clustered indexes and non-clustered indexes.

### Clustered Indexes

Clustered indexes include all the table’s column data in their leaf level. The entire table data is sorted and logically stored in order on disk. A clustered index is similar to a phone directory index where the entire data is contained for every index entry. Clustered indexes are created by default for primary key constraints. However, a primary key doesn’t necessarily need to use a clustered index if it is explicitly specified as non-clustered.

Clustered indexes are created using the `CREATE CLUSTERED INDEX` statement. You can create only one clustered index for each table because the index itself is the table’s data. A table having a clustered index is called a clustered table (also known as an index-organized table in other relational database management systems). A table with no clustered index is called a heap.

#### Examples

Create a Clustered Index as part of table definition.

```
CREATE TABLE MyTable
(
  Col1 INT NOT NULL
  PRIMARY KEY,
  Col2 VARCHAR(20) NOT NULL
);
```

Create an explicit clustered index using `CREATE INDEX`.

```
CREATE TABLE MyTable
(
  Col1 INT NOT NULL
  PRIMARY KEY NONCLUSTERED,
  Col2 VARCHAR(20) NOT NULL
);
```

```
CREATE CLUSTERED INDEX IDX1
ON MyTable(Col2);
```

### Non-Clustered Indexes

Non-clustered indexes also use the B-tree algorithm but consist of a data structure separate from the table itself. They are also sorted by the index keys, but the leaf level of a non-clustered index contains pointers to the table rows; not the entire row as with a clustered index.

You can create up to 999 non-clustered indexes on a SQL Server table. The type of pointer used at the lead level of a non-clustered index (also known as a row locator) depends on whether the table has a clustered index (clustered table) or not (heap). For heaps, the row locators use a physical pointer (RID). For clustered tables, row locators use the clustering key plus a potential uniquifier. This approach minimizes non-clustered index updates when rows move around, or the clustered index key value changes.

Both clustered and non-clustered indexes may be defined as `UNIQUE` using the `CREATE UNIQUE INDEX` statement. SQL Server maintains indexes automatically for a table or view and updates the relevant keys when table data is modified.

#### Examples

Create a unique non-clustered index as part of table definition.

```
CREATE TABLE MyTable
(
  Col1 INT NOT NULL
  PRIMARY KEY,
  Col2 VARCHAR(20) NOT NULL
  UNIQUE
);
```

Create a unique non-clustered index using CREATE INDEX.

```
CREATE TABLE MyTable
(
  Col1 INT NOT NULL
  PRIMARY KEY CLUSTERED,
  Col2 VARCHAR(20) NOT NULL
);
```

```
CREATE UNIQUE NONCLUSTERED INDEX IDX1 ON MyTable(Col2);
```

### Filtered Indexes and Covering Indexes

SQL Server also supports two special options for non-clustered indexes. You can create filtered indexes to index only a subset of a table’s data. They are useful when it is known that the application will not need to search for specific values such as NULLs.

For queries that typically require searching on particular columns but also need additional column data from the table, you can configure non-clustered indexes. They include additional column data in the index leaf level in addition to the row locator. This may prevent expensive lookup operations, which follow the pointers to either the physical row location (in a heap) or traverse the clustered index key to fetch the rest of the data not part of the index. If a query can get all the data it needs from the non-clustered index leaf level, that index is considered a covering index.

#### Examples

Create a filtered index to exclude NULL values.

```
CREATE NONCLUSTERED INDEX IDX1
ON MyTable(Col2)
WHERE Col2 IS NOT NULL;
```

Create a covering index for queries that search on col2 but also need data from col3.

```
CREATE NONCLUSTERED INDEX IDX1
ON MyTable (Col2)
INCLUDE (Col3);
```

### Indexes On Computed Columns

In SQL Server, you can create indexes on persisted computed columns. Computed columns are table or view columns that derive their value from an expression based on other columns in the table. They aren’t explicitly specified when data is inserted or updated. This feature is useful when a query’s filter predicates aren’t based on the column table data as-is, but on a function or expression.

#### Examples

For example, consider the following table that stores phone numbers for customers, but the format isn’t consistent for all rows; some include country code and some don’t:

```
CREATE TABLE PhoneNumbers
(
  PhoneNumber VARCHAR(15) NOT NULL
  PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL
);
```

```
INSERT INTO PhoneNumbers
VALUES
('+1-510-444-3422','Dan'),
('644-2442-3119','John'),
('1-402-343-1991','Jane');
```

The following query to look up the owner of a specific phone number must scan the entire table because the index can’t be used due to the preceding % wild card.

```
SELECT Customer
FROM PhoneNumbers
WHERE PhoneNumber LIKE '%510-444-3422';
```

A potential solution would be to add a computed column that holds the phone number in reverse order.

```
ALTER TABLE PhoneNumbers
ADD ReversePhone AS REVERSE(PhoneNumber)
PERSISTED;
```

```
CREATE NONCLUSTERED INDEX IDX1
ON PhoneNumbers (ReversePhone)
INCLUDE (Customer);
```

Now, you can use the following query to search for the customer based on the reverse string, which places the wild card at the end of the `LIKE` predicate. This approach provides an efficient index seek to retrieve the customer based on the phone number value.

```
DECLARE @ReversePhone VARCHAR(15) = REVERSE('510-444-3422');
SELECT Customer
FROM PhoneNumbers
WHERE ReversePhone LIKE @ReversePhone + '%';
```

For more information, see [Clustered and nonclustered indexes described](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15") and [CREATE INDEX (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports balanced tree (B-tree) indexes similar to SQL Server. However, the terminology, use, and options for these indexes are different.

Aurora PostgreSQL is missing the `CLUSTERED INDEX` feature but has other options which SQL Server doesn’t have, index prefix, and binary large object (BLOB) indexing.

Starting with PostgreSQL 10, there are many improvements in performance, related to joins and parallel scans of the indexes.

Starting with PostgreSQL 12, you can monitor progress of `CREATE INDEX` and `REINDEX` operations by querying the `pg_stat_progress_create_index` system view.

### Cluster Table

PostgreSQL doesn’t support cluster tables directly, but provides similar functionality using the `CLUSTER` feature. The PostgreSQL `CLUSTER` statement specifies table sorting based on an index already associated with the table. When using the PostgreSQL `CLUSTER` command, the data in the table is physically sorted based on the index, possibly using a primary key column.

You can use the `CLUSTER` statement to re-cluster the table.

#### Examples

```
CREATE TABLE SYSTEM_EVENTS (
  EVENT_ID NUMERIC,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME DATE NOT NULL,
  CONSTRAINT PK_EVENT_ID PRIMARY KEY(EVENT_ID));

INSERT INTO SYSTEM_EVENTS VALUES(9, 'EV-A1-10', 'Critical', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(1, 'EV-C1-09', 'Warning', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(7, 'EV-E1-14', 'Critical', '01-JAN-2017');

CLUSTER SYSTEM_EVENTS USING PK_EVENT_ID;
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01

INSERT INTO SYSTEM_EVENTS VALUES(2, 'EV-E2-02', 'Warning', '01-JAN-2017');
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01
2         EVNT-E2-02  Warning           2017-01-01

CLUSTER SYSTEM_EVENTS USING PK_EVENT_ID; -- Run CLUSTER again to re-cluster
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
2         EVNT-E2-02  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01
```

### B-tree Indexes

When you create an index in PostgreSQL, a B-tree index is created by default, similar to the behavior in SQL Server. PostgreSQL B-tree indexes have the same characteristics as SQL Server and can handle equality and range queries on data. The PostgreSQL optimizer considers using B-tree indexes especially for one or more of the following operators in queries: `>`, `>=`, `<`, `⇐`, `=`.

In addition, you can achieve performance improvements when using `IN`, `BETWEEN`, `IS NULL`, or `IS NOT NULL`.

Starting with PostgreSQL 10, there is a support of parallel B-tree index scans. This change allows this index type pages to be searched by separate parallel workers.

#### Example

Create a PostgreSQL B-Tree Index.

```
CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG(EVENT_ID);
OR
CREATE INDEX IDX_EVENT_ID1 ON SYSTEM_LOG USING BTREE (EVENT_ID);
```

For more information, see [CREATE INDEX](https://www.postgresql.org/docs/13/sql-createindex.html "https://www.postgresql.org/docs/13/sql-createindex.html") in the _PostgreSQL documentation_.

### Column and Multiple Column Secondary Indexes

Currently, only B-tree, GiST, GIN, and BRIN support multicolumn indexes. You can specify 32 columns when you create a multicolumn index.

PostgreSQL uses the same syntax as SQL Server to create multicolumn indexes.

#### Examples

Create a multicolumn index on the `EMPLOYEES` table.

```
CREATE INDEX IDX_EMP_COMPI
ON EMPLOYEES (FIRST_NAME, EMAIL, PHONE_NUMBER);
```

Drop a multicolumn index.

```
DROP INDEX IDX_EMP_COMPI;
```

For more information, see [Multicolumn Indexes](https://www.postgresql.org/docs/13/indexes-multicolumn.html "https://www.postgresql.org/docs/13/indexes-multicolumn.html") in the _PostgreSQL documentation_.

### Expression Indexes and Partial Indexes

Create an Expression Index in PostgreSQL.

```
CREATE TABLE SYSTEM_EVENTS(
  EVENT_ID NUMERIC PRIMARY KEY,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME TIMESTAMP NOT NULL);

CREATE INDEX EVNT_BY_DAY ON SYSTEM_EVENTS(EXTRACT(DAY FROM EVENT_TIME));
```

Insert records into the `SYSTEM_EVENTS` table, gathering table statistics using the `ANALYZE` statement and verifying that the `EVNT_BY_DAY` expression index is being used for data access.

```
INSERT INTO SYSTEM_EVENTS
  SELECT ID AS event_id,
    'EVNT-A'||ID+9||'-'||ID AS event_code,
    CASE WHEN mod(ID,2) = 0 THEN 'Warning' ELSE 'Critical' END AS event_desc,
    now() + INTERVAL '1 minute' * ID AS event_time
    FROM
    (SELECT generate_series(1,1000000) AS ID) A;
INSERT 0 1000000

ANALYZE SYSTEM_EVENTS;
ANALYZE

EXPLAIN
  SELECT * FROM SYSTEM_EVENTS
  WHERE EXTRACT(DAY FROM EVENT_TIME) = '22';

QUERY PLAN

Bitmap Heap Scan on system_events (cost=729.08..10569.58 rows=33633 width=41)
Recheck Cond: (date_part('day'::text, event_time) = '22'::double precision)
-> Bitmap Index Scan on evnt_by_day (cost=0.00..720.67 rows=33633 width=0)
Index Cond: (date_part('day'::text, event_time) = '22'::double precision)
```

### Partial Indexes

PostgreSQL also provides partial indexes, which are indexes that use a `WHERE` clause when created. The most significant benefit of using partial indexes is a reduction of the overall subset of indexed data, allowing users to index relevant table data only. You can use partial indexes to increase efficiency and reduce the size of the index.

#### Example

The following example creates a PostgreSQL partial Index.

```
CREATE TABLE SYSTEM_EVENTS(
  EVENT_ID NUMERIC PRIMARY KEY,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME DATE NOT NULL);

CREATE INDEX IDX_TIME_CODE ON SYSTEM_EVENTS(EVENT_TIME)
  WHERE EVENT_CODE like '01-A%';
```

For more information, see [Building Indexes Concurrently](https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY "https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY") in the _PostgreSQL documentation_.

### BRIN Indexes

PostgreSQL doesn’t provide native support for BITMAP indexes. However, you can use a BRIN index, which splits table records into block ranges with `MIN/MAX` summaries. A BRIN index is a partial alternative for certain analytic workloads. For example, BRIN indexes are suited for queries that rely heavily on aggregations to analyze large numbers of records.

#### Example

The following example creates a PostgreSQL BRIN index.

```
CREATE INDEX IDX_BRIN_EMP ON EMPLOYEES USING BRIN(salary);
```

## Summary

The following table summarizes the key differences to consider when migrating b-tree indexes from SQL Server to Aurora PostgreSQL.

| Index feature                       | SQL Server                                                                       | Aurora PostgreSQL                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Clustered indexes supported for     | Table keys, composite or single column, unique and non-unique, null or not null. | On indexes.                                                                      |
| Non-clustered indexes supported for | Table keys, composite or single column, unique and non-unique, null or not null. | Table keys, composite or single column, unique and non-unique, null or not null. |
| Max number of non-clustered indexes | 999                                                                              | N/A                                                                              |
| Max total index key size            | 900 bytes                                                                        | N/A                                                                              |
| Max columns for each index          | 32                                                                               | 32                                                                               |
| Index prefix                        | N/A                                                                              | Supported                                                                        |
| Filtered indexes                    | Supported                                                                        | Supported (partial indexes)                                                      |
| Indexes on BLOBs                    | N/A                                                                              | Supported                                                                        |

For more information, see [Index Types](https://www.postgresql.org/docs/13/indexes-types.html "https://www.postgresql.org/docs/13/indexes-types.html"), [CREATE INDEX](https://www.postgresql.org/docs/13/sql-createindex.html "https://www.postgresql.org/docs/13/sql-createindex.html"), [CLUSTER](https://www.postgresql.org/docs/13/sql-cluster.html "https://www.postgresql.org/docs/13/sql-cluster.html"), and [Building Indexes Concurrently](https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY "https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY") in the _PostgreSQL documentation_.
