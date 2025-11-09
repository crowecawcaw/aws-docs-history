# Oracle local and global partitioned indexes and PostgreSQL partitioned indexes

With AWS DMS, you can migrate partitioned tables from Oracle and PostgreSQL databases to Amazon Aurora. Oracle local and global partitioned indexes and PostgreSQL partitioned indexes are database objects that improve query performance by dividing large tables into smaller, more manageable pieces called partitions.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| Four star feature compatibility | No automation                      | [Indexes](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes") | N/A             |

## Oracle usage

Local and global indexes are used for partitioned tables in Oracle databases. Each index created on a partitioned table can be specified as either local or global.

- **Local partitioned index** maintains a one-to-one relationship between the index partitions and the table partitions. For each table partition, Oracle creates a separate index partition. This type of index is created using the `LOCAL` clause. Because each index partition is independent, index maintenance operations are easier and can be performed independently. Local partitioned indexes are managed automatically by Oracle during creation or deletion of table partitions.
- **Global partitioned index** contains keys from multiple table partitions in a single index partition. This type of index is created using the `GLOBAL` clause during index creation. A global index can be partitioned or non-partitioned (default). Certain restrictions exist when creating global partitioned indexes on partitioned tables, specifically for index management and maintenance. For example, dropping a table partition causes the global index to become unusable without an index rebuild.

**Examples**

Create a local index on a partitioned table.

```
CREATE INDEX IDX_SYS_LOGS_LOC ON SYSTEM_LOGS (EVENT_DATE)
  LOCAL
    (PARTITION EVENT_DATE_1,
    PARTITION EVENT_DATE_2,
    PARTITION EVENT_DATE_3);
```

Create a global index on a partitioned table.

```
CREATE INDEX IDX_SYS_LOGS_GLOB ON SYSTEM_LOGS (EVENT_DATE)
  GLOBAL PARTITION BY RANGE (EVENT_DATE) (
    PARTITION EVENT_DATE_1 VALUES LESS THAN (TO_DATE('01/01/2015','DD/MM/YYYY')),
    PARTITION EVENT_DATE_2 VALUES LESS THAN (TO_DATE('01/01/2016','DD/MM/YYYY')),
    PARTITION EVENT_DATE_3 VALUES LESS THAN (TO_DATE('01/01/2017','DD/MM/YYYY')),
    PARTITION EVENT_DATE_4 VALUES LESS THAN (MAXVALUE);
```

For more information, see [Partitioning Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html#GUID-EA7EF5CB-DD49-43AF-889A-F83AAC0D7D51 "https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html#GUID-EA7EF5CB-DD49-43AF-889A-F83AAC0D7D51") and [Index Partitioning](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/index-partitioning.html#GUID-569F94D0-E6E5-45BB-9626-5506DE18FF00 "https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/index-partitioning.html#GUID-569F94D0-E6E5-45BB-9626-5506DE18FF00") in the _Oracle documentation_.

## PostgreSQL usage

The table partitioning mechanism in PostgreSQL is different when compared to Oracle. There is no direct equivalent for Oracle local and global indexes. The implementation of partitioning in PostgreSQL (table inheritance) includes the use of a parent table with child tables used as the table partitions. Also, when using declarative partitions, global index is still not supported while creating a global index will create an index for each partition, there is a parent index referring to all sub indexes but there is no actual global indexes.

Indexes created on the child tables behave similarly to local indexes in the Oracle database, with portable indexes (partitions). Creating an index on the parent table, such as a global index in Oracle, has no effect.

While concurrent indexes on partitioned tables build are currently not supported, you may concurrently build the index on each partition individually and then finally create the partitioned index non-concurrently in order to reduce the time where writes to the partitioned table will be locked out. In this case, building the partitioned index is a meta-data only operation.

A `CREATE INDEX` command invoked on a partitioned table, will `RECURSE` (default) to all partitions to ensure they all have matching indexes. Each partition is first checked to determine whether an equivalent index already exists, and if so, that index will become attached as a partition index to the index being created, which will become its parent index. If no matching index exists, a new index will be created and automatically attached.

**Examples**

Create the parent table.

```
CREATE TABLE SYSTEM_LOGS
  (EVENT_NO NUMERIC NOT NULL,
  EVENT_DATE DATE NOT NULL,
  EVENT_STR VARCHAR(500),
  ERROR_CODE VARCHAR(10));
```

Create child tables (partitions) with a check constraint.

```
CREATE TABLE SYSTEM_LOGS_WARNING (
  CHECK (ERROR_CODE IN('err1', 'err2', 'err3')))
  INHERITS (SYSTEM_LOGS);

CREATE TABLE SYSTEM_LOGS_CRITICAL (
CHECK (ERROR_CODE IN('err4', 'err5', 'err6')))
  INHERITS (SYSTEM_LOGS);
```

Create Indexes on all child tables (partitions).

```
CREATE INDEX IDX_SYSTEM_LOGS_WARNING ON
  SYSTEM_LOGS_WARNING(ERROR_CODE);

CREATE INDEX IDX_SYSTEM_LOGS_CRITICAL ON
  SYSTEM_LOGS_CRITICAL(ERROR_CODE);
```

PostgreSQL doesn’t have direct equivalents for local and global indexes in Oracle. However, indexes that have been created on the child tables behave similarly to local indexes in Oracle.

For more information, see [Table Partitioning](https://www.postgresql.org/docs/13/ddl-partitioning.html "https://www.postgresql.org/docs/13/ddl-partitioning.html") in the _PostgreSQL documentation_.
