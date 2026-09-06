

# Storage for Aurora MySQL
<a name="chap-sql-server-aurora-mysql.storage"></a>

This topic provides reference content comparing partitioning features between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can gain insights into the similarities and differences in partitioning capabilities, including partition types, scope, boundary direction, and management.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Partitioning](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.partitioning)  | More partition types in Aurora MySQL with more restrictions on partitioned tables. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.storage.sqlserver"></a>

SQL Server provides a logical and physical framework for partitioning table and index data. Each table and index are partitioned, but may have only one partition. SQL Server 2017 supports up to 15,000 partitions.

Partitioning separates data into logical units that can be stored in more than one file group. SQL Server partitioning is horizontal, where data sets of rows are mapped to individual partitions. A partitioned table or index is a single object and must reside in a single schema within a single database. Composing objects of disjointed partitions isn’t allowed.

All DQL and DML operations are partition agnostic except for the special predicate $partition, which can be used for explicit partition elimination.

Partitioning is typically needed for large tables to ease the following management and performance challenges:
+ Deleting or inserting large amounts of data in a single operation, with partition switching instead of individual row processing, while maintaining logical consistency.
+ Maintenance operations can be split and customized for each partition. For example, older data partitions can be compressed and more active partitions can be rebuilt or reorganized more frequently.
+ Partitioned tables may use internal query optimization techniques such as collocated and parallel partitioned joins.
+ Physical storage performance optimization by distributing IO across partitions and physical storage channels.
+ Concurrency improvements due to the engine’s ability to escalate locks to the partition level and not the whole table.

Partitioning in SQL Server uses the following three objects:
+  **Partitioning column** — A partitioning column is the column or columns that partition function uses to partition the table or index. The value of this column determines the logical partition to which it belongs. You can use computed columns in a partition function as long as they are explicitly `PERSISTED`. Partitioning may be any data type that is a valid index column with less than 900 bytes for each key, except timestamp and LOB data types.
+  **Partition function** — A partition function is a database object that defines how the values of the partitioning columns for individual tables or index rows are mapped to a logical partition. The partition function describes the partitions for the table or index and their boundaries.
+  **Partition scheme** — A partition scheme is a database object that maps individual logical partitions of a table or an index to a set of file groups, which in turn consist of physical operating system files. Placing individual partitions on individual file groups enables backup operations for individual partitions by backing their associated file groups.

### Syntax
<a name="chap-sql-server-aurora-mysql.storage.sqlserver.syntax"></a>

```
CREATE PARTITION FUNCTION <Partition Function>(<Data Type>)
AS RANGE [ LEFT | RIGHT ]
FOR VALUES (<Boundary Value 1>,...)[;]
```

```
CREATE PARTITION SCHEME <Partition Scheme>
AS PARTITION <Partition Function>
[ALL] TO (<File Group> | [ PRIMARY ] [,...])[;]
```

```
CREATE TABLE <Table Name> (<Table Definition>)
ON <Partition Schema> (<Partitioning Column>);
```

### Examples
<a name="chap-sql-server-aurora-mysql.storage.sqlserver.examples"></a>

The following examples create a partitioned table.

```
CREATE PARTITION FUNCTION PartitionFunction1 (INT)
AS RANGE LEFT FOR VALUES (1, 1000, 100000);
```

```
CREATE PARTITION SCHEME PartitionScheme1
AS PARTITION PartitionFunction1
ALL TO (PRIMARY);
```

```
CREATE TABLE PartitionTable (
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20)
)
ON PartitionScheme1 (Col1);
```

For more information, see [Partitioned Tables and Indexes](https://docs.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver15), [CREATE TABLE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver15), [CREATE PARTITION SCHEME (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-partition-scheme-transact-sql?view=sql-server-ver15), and [CREATE PARTITION FUNCTION (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-partition-function-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.storage.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports a much richer framework for table partitioning than SQL Server with many additional options such as hash partitioning, sub partitioning and other features. However, it also introduces many restrictions on the tables that participate in partitioning.

**Note**  
The maximum number of partitions for a table is 8,192, including subpartitions. Although smaller than 15,000 partitions in SQL Server, practical partitioning rarely contains more than a few hundred partitions.

**Note**  
In Amazon Relational Database Service (Amazon RDS) for MySQL 8, `ADD PARTITION`, `DROP PARTITION`, `COALESCE PARTITION`, `REORGANIZE PARTITION`, and `REBUILD PARTITION ALTER TABLE` options are supported by native partitioning in-place APIs and may be used with `ALGORITHM={COPY|INPLACE}` and `LOCK` clauses. `DROP PARTITION` with `ALGORITHMM=INPLACE` deletes data stored in the partition and drops the partition. However, `DROP PARTITION` with `ALGORITHM=COPY` or `old_alter_table=ON` rebuilds the partitioned table and attempts to move data from the dropped partition to another partition with a compatible `PARTITION …​ VALUES` definition. Data that can’t be moved to another partition is deleted.

The following sections describe the types of partitions supported by Aurora MySQL.

### Range Partitioning
<a name="chap-sql-server-aurora-mysql.storage.mysql.range"></a>

Range partitions are the equivalent of SQL Server `RANGE` partition functions, which are the only type currently supported. A range partitioned table has explicit boundaries defined. Each partition contains only rows for which the partitioning expression value lies within the boundaries. Value ranges must be contiguous and can’t overlap. Partition boundaries are defined using the `VALUES LESS THAN` operator.

### List Partitioning
<a name="chap-sql-server-aurora-mysql.storage.mysql.list"></a>

List partitioning somewhat resembles range partitioning. Similar to range, each partition must be defined explicitly. The main difference between list and range partitioning is that list partitions are defined using a set of value lists instead of a contiguous range.

Use the `PARTITION BY LIST(<Column Expression>)` to define the type and the partitioning column. Make sure that `<Column Expression>` returns an integer value.

Afterward, every partition is defined using the `VALUES IN (<Value List>)` where `<Value List>` consists of a comma-separated list of integer values.

### Range and List Columns Partitioning
<a name="chap-sql-server-aurora-mysql.storage.mysql.rangelist"></a>

Columns partitioning is a variant of both range and list partitioning. However, for columns partitioning, you can use multiple columns in partitioning keys. All column values are considered for matching to a particular partition.

Both range columns partitioning and list columns partitioning enable you to use non-integer values for defining value ranges and value lists. The following data types are supported for columns partitioning:
+ All integer types.
+  `DATE` and `DATETIME`.
+  `CHAR`, `VARCHAR`, `BINARY`, and `VARBINARY`.

### Hash Partitioning
<a name="chap-sql-server-aurora-mysql.storage.mysql.hash"></a>

Hash partitioning is typically used to guarantee even distribution of rows for a desired number of partitions. When using range or list partitioning, or their variants, the boundaries are explicitly defined and associate a row to a partition based on the column value or set of values.

With hash partitioning, Aurora MySQL manages the values and individual partitions. You only need to specify the column or column expression to be hashed and the total number of partitions.

### Subpartitioning
<a name="chap-sql-server-aurora-mysql.storage.mysql.subpartitioning"></a>

With subpartitioning, or composite partitioning, each primary partition is further partitioned to create a two-layer partitioning hierarchy. Subpartitions must use either HASH or KEY partitioning and only range or list partitions may be subpartitioned. SQL Server doesn’t support subpartitions.

### Partition Management
<a name="chap-sql-server-aurora-mysql.storage.mysql.management"></a>

 Aurora MySQL provides several mechanisms for managing partitioned tables including adding, dropping, redefining, merging, and splitting existing partitioned tables. These management operations can use the Aurora MySQL partitioning extensions to the `ALTER TABLE` statement.

### Dropping Partitions
<a name="chap-sql-server-aurora-mysql.storage.mysql.dropping"></a>

For tables using either range or list partitioning, drop a partition using the `ALTER TABLE …​ DROP PARTITION` statement option.

When a partition is dropped from a range partitioned table, all the data in the current partition is deleted and new rows with values that would have fit the partition go to the immediate neighbor partition.

When a partition is dropped from a list partitioned table, data is also deleted but new rows with values that would have fit the partition can’t be INSERTED or UPDATED because they no longer have a logical container.

For hash and key partitions, use the `ALTER TABLE …​ COALESCE PARTITION <Number of Partitions>`. This approach reduces the current total number of partitions by the `<Number of Partitions>` value.

### Adding and Splitting Partitions
<a name="chap-sql-server-aurora-mysql.storage.mysql.adding"></a>

To add a new range boundary, or partition for a new list of values, use the `ALTER TABLE …​ ADD PARTITION` statement option.

For range partitioned tables, you can only add a new range to the end of the list of existing partitions.

If you need to split an existing range partition into two partitions, use the `ALTER TABLE …​ REORGANIZE PARTITION` statement.

### Switching and Exchanging Partitions
<a name="chap-sql-server-aurora-mysql.storage.mysql.switching"></a>

 Aurora MySQL supports the exchange of a table partition, or a subpartition, with another table. Use the `ALTER TABLE <Partitioned Table> EXCHANGE PARTITION <Partition> WITH TABLE <Non Partitioned Table>` statement option.

The non-partitioned table can’t be a temporary table and the schema of both tables must be identical. The non-partitioned table can’t have a foreign key being referenced, or referencing it. It is critical that all rows in the nonpartitioned table are within the partition boundaries, unless the `WITHOUT VALIDATION` option is used.

**Note**  
 `ALTER TABLE …​ EXCHANGE PARTITION` requires the `ALTER`, `INSERT`, `CREATE`, and `DROP` privileges.

Executing the `ALTER TABLE …​ EXCHANGE PARTITION` statement doesn’t trigger the running of triggers on the partitioned table or the exchanged non-partitioned table.

**Note**  
 `AUTO_INCREMENT` columns in the exchanged table are reset when you run the `ALTER TABLE …​ EXCHANGE PARTITION` statement. For more information, see [Identity and Sequences](chap-sql-server-aurora-mysql.tsql.identitysequences.md).

### Syntax
<a name="chap-sql-server-aurora-mysql.storage.mysql.syntax"></a>

Create a partitioned table.

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] <Table Name>
(<Table Definition>) [<Table Options>]
PARTITION BY
{ [LINEAR] HASH(<Expression>)
    | [LINEAR] KEY [ALGORITHM={1|2}] (<Column List>)
    | RANGE{(expr) | COLUMNS(<Column List>)}
    | LIST{(expr) | COLUMNS(<Column List>)} }
[PARTITIONS <Number>]
[SUBPARTITION BY
    { [LINEAR] HASH(<Expression>)
    | [LINEAR] KEY [ALGORITHM={1|2}] (<Column List>) }
[SUBPARTITIONS <Number>]
```

Reorganize or split a partition.

```
ALTER TABLE <Table Name>
REORGANIZE PARTITION <Partition> INTO (
PARTITION <New Partition 1> VALUES LESS THAN (<New Range Boundary>),
PARTITION <New Partition 2> VALUES LESS THAN (<Range Boundary>)
);
```

Exchange a partition.

```
ALTER TABLE <Partitioned Table> EXCHANGE PARTITION <Partition> WITH TABLE <Non Partitioned Table>;
```

Drop a partition.

```
ALTER TABLE <Table Name> DROP PARTITION <Partition>;
```

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.storage.mysql.considerations"></a>

Because Aurora MySQL stores each table in its own file and since file management is performed by AWS and can’t be modified, some of the physical aspects of partitioning in SQL Server don’t apply to Aurora MySQL. For example, the concept of file groups and assigning partitions to file groups.

 Aurora MySQL doesn’t support foreign keys partitioned tables. Neither the referencing table nor referenced table can use partitioning. Partitioned tables can’t have foreign keys referencing other tables or be referenced from other tables. Partitioning keys or expressions in Aurora MySQL must be `INT` data types. They can’t be 1ENUM types. The expression may result in a NULL state. The exceptions to this rule are:
+ Partitioning by range columns or list columns. It is possible to use strings, `DATE`, and `DATETIME` columns.
+ Partitioning by `[LINEAR] KEY`. Allows use of any valid MySQL data type except `TEXT` and `BLOB` for partitioning keys. In Aurora MySQL, key-hashing functions result in the correct data type.

Partitioned tables support neither `FULLTEXT` indexes nor spatial data types such as `POINT` and `GEOMETRY`.

Unlike SQL Server, exchanging partitions in Aurora MySQL is only supported between a partitioned and a nonpartitioned table. In SQL server, `SWITCH PARTITION` can be used to switch any partition between partitions tables because technically all tables are partitioned to one or more partitions.

### Examples
<a name="chap-sql-server-aurora-mysql.storage.mysql.examples"></a>

Create a range partitioned table.

```
CREATE TABLE MyTable (
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
)
PARTITION BY RANGE (Col1)
(
    PARTITION p0 VALUES LESS THAN (100000),
    PARTITION p1 VALUES LESS THAN (200000),
    PARTITION p2 VALUES LESS THAN (300000),
    PARTITION p3 VALUES LESS THAN (400000)
);
```

Create subpartitions.

```
CREATE TABLE MyTable (Col1 INT NOT NULL, DateCol DATE NOT NULL, )
PARTITION BY RANGE(YEAR(DateCol))
SUBPARTITION BY HASH(TO_DAYS(<DateCol>))
SUBPARTITIONS 2 (
    PARTITION p0 VALUES LESS THAN (1990),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);
```

Drop a range partition.

```
ALTER TABLE MyTable DROP PARTITION p2
```

Reduce the number of hash partitions by four.

```
ALTER TABLE <Table Name> COALESCE PARTITION 4;
```

Add range partitions.

```
ALTER TABLE MyTable ADD PARTITION (PARTITION p4 VALUES LESS THAN (50000));
```

## Summary
<a name="chap-sql-server-aurora-mysql.storage.summary"></a>

The following table identifies similarities, differences, and key migration considerations.


| Index feature | SQL Server |  Aurora MySQL  | Comments | 
| --- | --- | --- | --- | 
| Partition types. |  `RANGE` only. |  `RANGE`, `LIST`, `HASH`, `KEY`. |  | 
| Partitioned tables scope. | All tables are partitioned, some have more than one partition. | All tables aren’t partitioned, unless explicitly partitioned. |  | 
| Partition boundary direction. |  `LEFT` or `RIGHT`. |  `RIGHT` only. | Only determines to which partition the boundary value itself will go. | 
| Dynamic range partition. | N/A — literal values must be explicitly set in partition function. |  |  | 
| Exchange partition. | Any partition to any partition. | Partition to table (nonpartitioned table). | Only partition to table, no partition to partition switch. | 
| Partition function. | Abstract function object, independent of individual column. | Defined for each partitioned table. |  | 
| Partition scheme. | Abstract partition storage mapping object. | N/A | In Aurora MySQL, physical storage is managed by Amazon RDS. | 
| Limitations on partitioned tables. | None — all tables are partitioned. | Extensive — no FK, no full text. | For more information, see [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html). | 

For more information, see [Overview of Partitioning in MySQL](https://dev.mysql.com/doc/refman/5.7/en/partitioning-overview.html), [Partition Management](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management.html), and [Partitioning Types](https://dev.mysql.com/doc/refman/5.7/en/partitioning-types.html) in the *MySQL documentation*.