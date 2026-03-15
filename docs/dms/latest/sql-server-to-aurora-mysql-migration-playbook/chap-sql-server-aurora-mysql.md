# Migrating indexes to Aurora MySQL

This topic provides reference content comparing index features between Microsoft SQL Server and Amazon Aurora MySQL. You can gain valuable insights into the differences in index implementation, capabilities, and limitations when migrating from SQL Server to Aurora MySQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                            | Key differences                                                                                          |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Indexes](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.indexes "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.indexes") | MySQL supports only clustered primary keys. MySQL doesn’t support filtered indexes and included columns. |

## SQL Server Usage

Indexes are physical disk structures used to optimize data access. They are associated with tables or materialized views and allow the query optimizer to access rows and individual column values without scanning an entire table.

An index consists of index keys, which are columns from a table or view. They are sorted in ascending or descending 1order providing quick access to individual values for queries that use equality or range predicates. Database indexes are similar to book indexes that list page numbers for common terms. Indexes created on multiple columns are called Composite Indexes.

SQL Server implements indexes using the Balanced Tree algorithm (B-tree).

###### Note

SQL Server supports additional index types such as hash indexes (for memory-optimized tables), spatial indexes, full text indexes, and XML indexes.

Indexes are created automatically to support table primary keys and unique constraints. They are required to efficiently enforce uniqueness. Up to 250 indexes can be created on a table to support common queries.

SQL Server provides two types of B-Tree indexes: clustered Indexes and nonclustered Indexes.

### Clustered Indexes

Clustered indexes include all the table’s column data in their leaf level. The entire table data is sorted and logically stored in order on disk. A Clustered Index is similar to a phone directory index where the entire data is contained for every index entry. Clustered indexes are created by default for Primary Key constraints. However, a primary key doesn’t necessarily need to use a clustered index if it is explicitly specified as nonclustered.

You can create a clustered index using the `CREATE CLUSTERED INDEX` statement. Only one clustered index can be created for each table because the index itself is the table’s data. A table having a clustered index is called a _clustered table_ (also known as an _index-organized table_ in other relational database management systems). A table with no clustered index is called a _heap_.

#### Examples

The following example creates a clustered index as part of table definition.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL
        PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

The following examples create an explicit clustered index using `CREATE INDEX`.

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

### Nonclustered Indexes

Non-clustered indexes also use the B-Tree algorithm but consist of a data structure separate from the table itself. They are also sorted by the index keys, but the leaf level of a nonclustered index contains pointers to the table rows; not the entire row as with a clustered index.

You can create up to 999 nonclustered indexes on a SQL Server table. The type of pointer used at the lead level of a nonclustered index (also known as a row locator) depends on whether the table has a clustered index (clustered table) or not (heap). For heaps, the row locators use a physical pointer (RID). For clustered tables, row locators use the clustering key plus a potential uniquifier. This approach minimizes nonclustered index updates when rows move around, or the clustered index key value changes.

Both clustered and nonclustered indexes may be defined as UNIQUE using the CREATE UNIQUE INDEX statement. SQL Server maintains indexes automatically for a table or view and updates the relevant keys when table data is modified.

#### Examples

The following example creates a unique nonclustered index as part of table definition.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL
        PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
        UNIQUE
);
```

The following examples create a unique nonclustered index using `CREATE INDEX`.

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

SQL Server also supports two special options for nonclustered indexes. Filtered indexes can be created to index only a subset of the table’s data. They are useful when it is known that the application will not need to search for specific values such as NULLs.

For queries that typically require searching on particular columns but also need additional column data from the table, nonclustered indexes can be configured to include additional column data in the index leaf level in addition to the row locator. This may prevent expensive lookup operations, which follow the pointers to either the physical row location (in a heap) or traverse the clustered index key to fetch the rest of the data not part of the index. If a query can get all the data it needs from the nonclustered index leaf level, that index is considered a covering index.

#### Examples

The following example creates a filtered index to exclude NULL values.

```
CREATE NONCLUSTERED INDEX IDX1
ON MyTable(Col2)
WHERE Col2 IS NOT NULL;
```

The following example creates a covering index for queries that search on `col2` but also need data from `col3`.

```
CREATE NONCLUSTERED INDEX IDX1
ON MyTable (Col2)
INCLUDE (Col3);
```

### Indexes on Computed Columns

In SQL Server, you can create indexes on persisted computed columns. Computed columns are table or view columns that derive their value from an expression based on other columns in the table. They aren’t explicitly specified when data is inserted or updated. This feature is useful when a query filter predicates aren’t based on the column table data as-is but on a function or expression.

#### Examples

For example, consider the following table that stores phone numbers for customers. The format isn’t consistent for all rows. Particularly, some rows include country code and some don’t:

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

The following query to look up the owner of a specific phone number must scan the entire table because the index can’t be used due to the preceding `%` wildcard:

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

Now, you can use the following query to search for the customer based on the reverse string, This revers string places the wildcard at the end of the `LIKE` predicate. This approach provides an efficient index seek to retrieve the customer based on the phone number value:

```
DECLARE @ReversePhone VARCHAR(15) = REVERSE('510-444-3422');
SELECT Customer
FROM PhoneNumbers
WHERE ReversePhone LIKE @ReversePhone + '%';
```

For more information, see [Clustered and nonclustered indexes described](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15") and [CREATE INDEX (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports Balanced Tree (b-tree) indexes similar to SQL Server. However, the terminology, use, and options for these indexes are different.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports invisible indexes. An invisible index isn’t used by the optimizer at all but is otherwise maintained normally. Indexes are visible by default. Invisible indexes make it possible to test the effect of removing an index on query performance without making a destructive change that must be undone should the index turn out to be required. For more information, see [Invisible Indexes](https://dev.mysql.com/doc/refman/8.0/en/invisible-indexes.html "https://dev.mysql.com/doc/refman/8.0/en/invisible-indexes.html") in the _MySQL documentation_.

###### Note

Amazon RDS for MySQL 8 supports descending indexes: `DESC` in an index definition is no longer ignored but causes storage of key values in descending order. Previously, indexes could be scanned in reverse order but at a performance penalty. A descending index can be scanned in forward order which is more efficient. Descending indexes also make it possible for the optimizer to use multiple-column indexes when the most efficient scan order mixes ascending order for some columns and descending order for others. For more information, see [Descending Indexes](https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html "https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html") in the _MySQL documentation_.

### Primary Key Indexes

Primary key indexes are created automatically by Aurora MySQL to support Primary Key constraints. They are the equivalent of SQL Server clustered indexes and contain the entire row in the leaf level of the index. Unlike SQL Server, primary key indexes aren’t configurable; you can’t use a non-clustered index to support a primary key. In Aurora MySQL, a primary key index consisting of multiple columns is called _Multiple Column index_. It is the equivalent of an SQL Server composite index.

The MySQL query optimizer can use b-tree indexes to efficiently filter equality and range predicates. The Aurora MySQL optimizer considers using b-tree indexes to access data especially when queries use one or more of the following operators: `>`, `>=`, `<`, `⇐`, `=`, or `IN`, `BETWEEN`, `IS NULL`, or `IS NOT NULL` predicates.

Primary key indexes in Aurora MySQL can’t be created with the CREATE INDEX statement. Since they are part of the primary key, they can only be created as part of the `CREATE TABLE` statement or with the `ALTER TABLE…​ ADD CONSTRAINT…​ PRIMARY KEY` statement. To drop a primary key index, use the `ALTER TABLE…​ DROP PRIMARY KEY` statement.

The relational model specifies that every table must have a primary key, but Aurora MySQL and most other relational database systems don’t enforce it. If a table doesn’t have a primary key specified, Aurora MySQL locates the first unique index where all key columns are specified as NOT NULL and uses that as the clustered index.

###### Note

If no primary key or suitable unique index can be found, Aurora MySQL creates a hidden `GEN_CLUST_INDEX` clustered index with internally generated row ID values. These auto-generated row IDs are based on a six-byte field that increases monotonically (similar to `IDENTITY` or `SEQUENCE`).

#### Examples

The following example creates a primary key index as part of the table definition.

```
CREATE TABLE MyTable (Col1 INT NOT NULL PRIMARY KEY, Col2 VARCHAR(20) NOT NULL);
```

The following example creates a primary key index for an existing table with no primary key.

```
ALTER TABLE MyTable ADD CONSTRAINT PRIMARY KEY (Col1);
```

###### Note

You don’t need to explicitly name constraints in Aurora MySQL such as in SQL Server.

### Column and Multiple Column Secondary Indexes

Aurora MySQL single column indexes are called _column indexes_ and are the equivalent of SQL Server single column non-clustered indexes. Multiple column indexes are the equivalent of composite non-clustered indexes in SQL Server. They can be created as part of the table definition when creating unique constraints or explicitly using the `INDEX` or `KEY` keywords. For more information, see [Creating Tables](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

Multiple column indexes are useful when queries filter on all or leading index key columns. Specifying the optimal order of columns in a multiple column index can improve the performance of multiple queries accessing the table with similar predicates.

#### Examples

The following example creates a unique b-tree index as part of the table definition.

```
CREATE TABLE MyTable (Col1 INT NOT NULL PRIMARY KEY, Col2 VARCHAR(20) UNIQUE);
```

The following example creates a non-unique multiple column index on an existing table.

```
CREATE INDEX IDX1 ON MyTable (Col1, Col2) USING BTREE;
```

###### Note

The `USING` clause isn’t mandatory. The default index type for Aurora MySQL is `BTREE`.

### Secondary Indexes on Generated Columns

Aurora MySQL supports creating indexes on generated columns. They are the equivalent of SQL Server computed columns. Generated columns derive their values from the result of an expression. Creating an index on a generated column enables generated columns to be used as part of a filter predicate and may use the index for data access.

Generated columns can be created as `STORED` or `VIRTUAL`, but indexes can only be created on `STORED` generated columns.

Generated expressions can’t exceed 64 KB for the entire table. For example, you can create a single generated column with an expression length of 64 KB or create 12 fields with a length of 5 KB each. For more information, see [Creating Tables](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

### Prefix Indexes

Aurora MySQL also supports indexes on partial string columns. Indexes can be created that use only the leading part of column values using the following syntax:

```
CREATE INDEX <Index Name> ON <Table Name> (<col name>(<prefix length>));
```

Prefixes are optional for `CHAR`, `VARCHAR`, `BINARY`, and `VARBINARY` column indexes, but must be specified for `BLOB` and `TEXT` column indexes.

Index prefix length is measured in bytes. The prefix length for `CREATE TABLE`, `ALTER TABLE`, and `CREATE INDEX` statements is interpreted as the number of characters for non-binary string types (`CHAR`, `VARCHAR`, `TEXT`) or the number of bytes for binary string types (`BINARY`, `VARBINARY`, `BLOB`).

#### Example

The following example creates a prefix index for the first ten characters of a customer name.

```
CREATE INDEX PrefixIndex1 ON Customers (CustomerName(10));
```

## Summary

The following table summarizes the key differences to consider when migrating b-tree indexes from SQL Server to Aurora MySQL.

| Index feature                        | SQL Server                                                                       | Aurora MySQL                                                                                      | Comments                                                           |
| ------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Clustered indexes supported for:     | Table keys, composite or single column, unique and non-unique, null or not null. | Primary keys only.                                                                                |                                                                    |
| Non clustered index supported for:   | Table keys, composite or single column, unique and non-unique, null or not null. | Unique constraints, single column and multicolumn.                                                |                                                                    |
| Max number of non clustered indexes. | 999.                                                                             | 64.                                                                                               |                                                                    |
| Max total index key size.            | 900 bytes.                                                                       | 3072 bytes for a 16 KB page size, 1536 bytes for a 8 KB page size 768 bytes for a 4 KB page size. |                                                                    |
| Max columns for each index.          | 32.                                                                              | 16.                                                                                               |                                                                    |
| Index Prefix.                        | N/A.                                                                             | Optional for `CHAR`, `VARCHAR`, `BINARY`, and `VARBINARY`. Mandatory for `BLOB` and `TEXT`.       |                                                                    |
| Filtered Indexes.                    | Supported.                                                                       | N/A.                                                                                              |                                                                    |
| Included columns.                    | Supported.                                                                       | N/A.                                                                                              | Add the required columns as index key columns instead of included. |
| Indexes on BLOBS                     | N/A.                                                                             | Supported, limited by maximal index key size.                                                     |                                                                    |

For more information, see [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html "https://dev.mysql.com/doc/refman/5.7/en/create-index.html"), [Column Indexes](https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html "https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html"), and [Multiple-Column Indexes](https://dev.mysql.com/doc/refman/5.7/en/multiple-column-indexes.html "https://dev.mysql.com/doc/refman/5.7/en/multiple-column-indexes.html") in the _MySQL documentation_.
