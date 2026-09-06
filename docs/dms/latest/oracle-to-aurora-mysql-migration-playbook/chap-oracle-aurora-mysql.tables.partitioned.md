

# Oracle local and global partitioned indexes and MySQL partitioned indexes
<a name="chap-oracle-aurora-mysql.tables.partitioned"></a>

With AWS DMS, you can migrate data from Oracle databases using local and global partitioned indexes and from MySQL databases using partitioned indexes. Partitioned indexes facilitate operations on large datasets by logically dividing data into smaller subsets, improving performance and manageability.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Indexes](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.indexes)  | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.partitioned.oracle"></a>

Local and global indexes are used for partitioned tables in Oracle databases. Each index created on a partitioned table can be specified as either local or global.
+  **Local partitioned index** maintains a one-to-one relationship between the index partitions and the table partitions. For each table partition, Oracle creates a separate index partition. This type of index is created using the `LOCAL` clause. Because each index partition is independent, index maintenance operations are easier and can be performed independently. Local partitioned indexes are managed automatically by Oracle during creation or deletion of table partitions.
+  **Global partitioned index** contains keys from multiple table partitions in a single index partition. This type of index is created using the `GLOBAL` clause during index creation. A global index can be partitioned or non-partitioned. The default option is non-partitioned. When you create global partitioned indexes on partitioned tables, certain restrictions exist for index management and maintenance. For example, dropping a table partition causes the global index to become unusable without an index rebuild.

### Examples
<a name="chap-oracle-aurora-mysql.tables.partitioned.oracle.examples"></a>

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

For more information, see [Partitioning Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html#GUID-EA7EF5CB-DD49-43AF-889A-F83AAC0D7D51) and [Index Partitioning](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/index-partitioning.html#GUID-569F94D0-E6E5-45BB-9626-5506DE18FF00) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.partitioned.mysql"></a>

Indexes created on partitioned tables are similar to local indexes in Oracle. MySQL doesn’t provide an equivalent for Oracle global indexes because in MySQL, partitioning applies to all data and indexes of a table. It is not possible to partition only the data and not the indexes. All indexes on partitioned tables behave like an Oracle local index.

### Examples
<a name="chap-oracle-aurora-mysql.tables.partitioned.mysql.examples"></a>

Drop a partition (the index that is used without a rebuild). Note that the run plan shows the scanned partitions.

```
ALTER TABLE SYSTEM_LOGS add INDEX EVENT_NO_IDX (EVENT_NO);

EXPLAIN SELECT * from SYSTEM_LOGS where EVENT_NO=2;

id  select_type  table        partitions        type  possible_keys  key           key_len  ref    rows  filtered
1   SIMPLE       SYSTEM_LOGS  warning,critical  ref   EVENT_NO_IDX   EVENT_NO_IDX  4        const  1     100

ALTER TABLE SYSTEM_LOGS DROP PARTITION critical;
EXPLAIN SELECT * from SYSTEM_LOGS where EVENT_NO=2;

id  select_type  table        partitions  type  possible_keys  key           key_len  ref    rows  filtered
1   SIMPLE       SYSTEM_LOGS  warning     ref   EVENT_NO_IDX   EVENT_NO_IDX  4        const  1     100
```

For more information, see [Overview of Partitioning in MySQL](https://dev.mysql.com/doc/refman/5.7/en/partitioning-overview.html) in the *MySQL documentation*.