# Oracle and PostgreSQL B-tree indexes

With AWS DMS, you can efficiently migrate your databases between different database platforms while optimizing query performance through B-tree indexes. B-tree indexes are tree data structures that store pointers to rows in a table based on key values, facilitating faster data retrieval for queries involving those keys.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## Oracle usage

B-tree indexes (B stands for balanced), are the most common index type in a relational database and are used for a variety of common query performance enhancing tasks. You can define B-tree indexes as an ordered list of values divided into ranges. They provide superior performance by associating a key with a row or range of rows.

B-tree indexes contain two types of blocks: branch blocks for searching and leaf blocks for storing values. The branch blocks also contain the root branch, which points to lower-level index blocks in the B-tree index structure.

B-tree indexes are useful for primary keys and other high-cardinality columns. They provide excellent data access performance for a variety of query patterns such as exact match searches and range searches. B-tree indexes are the default when you create a new index.

**Examples**

Create a B-Tree index.

```
CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG(EVENT_ID);
```

For more information, see [CREATE INDEX](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE") in the _Oracle documentation_.

## PostgreSQL usage

When you create an index in PostgreSQL, a B-tree index is created by default. This behavior is similar to the behavior in the Oracle Database. PostgreSQL B-tree indexes have the same characteristics as Oracle and these types of indexes can handle equality and range queries on data. The PostgreSQL optimizer considers using B-tree indexes especially when using one or more of the following operators in queries: `>`, `>=`, `<`, `⇐`, `=`.

In addition, you can achieve performance improvement when using `IN`, `BETWEEN`, `IS NULL` or `IS NOT NULL`.

**Examples**

Create a PostgreSQL B-tree Index.

```
CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG(EVENT_ID);
OR
CREATE INDEX IDX_EVENT_ID1 ON SYSTEM_LOG USING BTREE (EVENT_ID);
```

For more information, see [CREATE INDEX](https://www.postgresql.org/docs/13/sql-createindex.html "https://www.postgresql.org/docs/13/sql-createindex.html") in the _PostgreSQL documentation_.
