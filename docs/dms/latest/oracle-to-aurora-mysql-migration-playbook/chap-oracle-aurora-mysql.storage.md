# Oracle and MySQL table partitioning

With AWS DMS, you can implement table partitioning for Oracle and MySQL databases, which involves dividing a large table into multiple smaller partitions. Table partitioning helps manage and maintain large databases by improving query performance, facilitating data management operations, and reducing storage costs.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                           | Key differences                                                                                                                                                     |
| -------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | Three star automation level        | [Partitioning](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.partitioning "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.partitioning") | Aurora MySQL doesn’t support interval partitioning, partition advisor, preference partitioning, virtual column-based partitioning, and automatic list partitioning. |

## Oracle usage

The purpose of database partitioning is to provide support for very large tables and indexes by splitting them into smaller pieces. Each partition has its own name and definitions. They can be managed separately or collectively as one object. From an application perspective, partitions are transparent. Partitioned tables behave the same as non-partitioned tables allowing your applications access using unmodified SQL statements. Table partitioning provides several benefits:

- **Performance improvements** — Table partitions help improve query performance by accessing a subset of a partition instead of scanning a larger set of data. Additional performance improvements can be achieved when using partitions and parallel query execution for DML and DDL operations.
- **Data management** — Table partitions facilitate easier data management operations (such as data migration), index management (creation, dropping, or rebuilding indexes), and backup/recovery. These operations are also referred to as Information Lifecycle Management (ILM) activities.
- **Maintenance operations** — Table partitions can significantly reduce downtime caused by table maintenance operations.

Oracle 18c introduces the following enhancements to partitioning.

- Online Merging of Partitions and Subpartitions: now it is possible to merge table partitions concurrently with Updates/Deletes and Inserts on a partitioned table.
- Oracle 18c also allows to modify partitioning strategy for the partitioned table: e.g. hash partitioning to range. This can be done both offline and online.

Oracle 19 introduces hybrid partitioned tables: partitions can now be both internal Oracle tables and external tables and sources. It is also possible to integrate both internal and external partitions together in a single partitioned table.

### Hash table partitioning

When a partition key is specified (for example, a table column with a `NUMBER` data type), Oracle applies a hashing algorithm to evenly distribute the data (records) among all defined partitions. The partitions have approximately the same size.

The following example creates a hash partitioned table.

```
CREATE TABLE SYSTEM_LOGS
  (EVENT_NO NUMBER NOT NULL,
  EVENT_DATE DATE NOT NULL,
  EVENT_STR VARCHAR2(500),
  ERROR_CODE VARCHAR2(10))
  PARTITION BY HASH (ERROR_CODE)
  PARTITIONS 3
  STORE IN (TB1, TB2, TB3);
```

### List table partitioning

You can specify a list of discrete values for the table partitioning key in the description of each partition. This type of table partitioning enables control over partition organization using explicit values. For example, partition events by error code values.

The following example creates a list-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
  (EVENT_NO NUMBER NOT NULL,
  EVENT_DATE DATE NOT NULL,
  EVENT_STR VARCHAR2(500),
  ERROR_CODE VARCHAR2(10))
  PARTITION BY LIST (ERROR_CODE)
  (PARTITION warning VALUES ('err1', 'err2', 'err3') TABLESPACE TB1,
  PARTITION critical VALUES ('err4', 'err5', 'err6') TABLESPACE TB2);
```

### Range table partitioning

Partition a table based on a range of values. The Oracle database assigns rows to table partitions based on column values falling within a given range. Range table partitioning is one of the most frequently used type of partitioning, primarily with date values. Range table partitioning can also be implemented with numeric ranges (1-10000, 10001- 20000…).

The following example creates a range-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
  (EVENT_NO NUMBER NOT NULL,
  EVENT_DATE DATE NOT NULL,
  EVENT_STR VARCHAR2(500))
  PARTITION BY RANGE (EVENT_DATE)
  (PARTITION EVENT_DATE VALUES
    LESS THAN (TO_DATE('01/01/2015',
    'DD/MM/YYYY')) TABLESPACE TB1,
  PARTITION EVENT_DATE VALUES
    LESS THAN (TO_DATE('01/01/2016',
    'DD/MM/YYYY')) TABLESPACE TB2,
  PARTITION EVENT_DATE VALUES
    LESS THAN (TO_DATE('01/01/2017',
    'DD/MM/YYYY')) TABLESPACE TB3);
```

### Composite table partitioning

With composite partitioning, a table can be partitioned by one data distribution method, and then each partition can be further subdivided into sub-partitions using the same, or different, data distribution method(s). For example:

- Composite list-range partitioning.
- Composite list-list partitioning.
- Composite range-hash partitioning.

### Partitioning extensions

Oracle provides additional partitioning strategies that enhance the capabilities of basic partitioning. These partitioning strategies include:

- Manageability extensions.
  - Interval partitioning.
  - Partition advisor.

- Partitioning key extensions.
  - Reference partitioning.
  - Virtual column-based partitioning.

### Split partitions

You can use the `SPLIT PARTITION` statement to redistribute the contents of one partition, or sub-partition, into multiple partitions or sub-partitions.

```
ALTER TABLE SPLIT PARTITION p0 INTO
  (PARTITION P01 VALUES LESS THAN (100), PARTITION p02);
```

### Exchange partitions

The `EXCHANGE PARTITION` statement is useful to exchange table partitions in or out of a partitioned table.

```
ALTER TABLE orders EXCHANGE
  PARTITION p_ord3 WITH TABLE orders_year_2016;
```

### Subpartitioning tables

You can create subpartitions within partitions to further split the parent partition.

```
PARTITION BY RANGE(department_id)
  SUBPARTITION BY HASH(last_name)
  SUBPARTITION TEMPLATE
    (SUBPARTITION a TABLESPACE ts1,
    SUBPARTITION b TABLESPACE ts2,
    SUBPARTITION c TABLESPACE ts3,
    SUBPARTITION d TABLESPACE ts4)
  (PARTITION p1 VALUES LESS THAN (1000),
  PARTITION p2 VALUES LESS THAN (2000),
  PARTITION p3 VALUES LESS THAN (MAXVALUE)
```

For more information, see [Partitioning Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html#GUID-EA7EF5CB-DD49-43AF-889A-F83AAC0D7D51 "https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html#GUID-EA7EF5CB-DD49-43AF-889A-F83AAC0D7D51") in the _Oracle documentation_.

### Automatic list partitioning

Oracle 12c introduces automatic list partitioning. This enhancement enables automatic creation of new partitions for new values inserted into a list-partitioned table. An automatic list-partitioned table is created with only one partition. The database creates the additional table partitions automatically.

The following example creates an automatic list-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
  (EVENT_NO NUMBER NOT NULL,
  EVENT_DATE DATE NOT NULL,
  EVENT_STR VARCHAR2(500),
  ERROR_CODE VARCHAR2(10))
  PARTITION BY LIST (ERROR_CODE) AUTOMATIC
  (PARTITION warning VALUES ('err1', 'err2', 'err3'))
```

For more information, see [Oracle Partitioning](https://www.oracle.com/technetwork/database/options/partitioning/partitioning-wp-12c-1896137.pdf "https://www.oracle.com/technetwork/database/options/partitioning/partitioning-wp-12c-1896137.pdf") in the _Oracle documentation_.

## MySQL Usage

The table partitioning mechanism in MySQL is similar to Oracle and contains most of the Oracle table partitioning features. The only items not supported in MySQL table partitioning are the automatic features such as interval partitioning and automatic list partitioning. You can implement these features using triggers or procedures. For more information, see [Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning.html") in the _MySQL documentation_.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version 8 support the following partitioning options: `ADD PARTITION`, `DROP PARTITION`, `COALESCE PARTITION`, `REORGANIZE PARTITION`, and `REBUILD PARTITION ALTER TABLE`. You can use them with `ALGORITHM={COPY|INPLACE}` and `LOCK` clauses.

`DROP PARTITION` with `ALGORITHMM=INPLACE` deletes data stored in the partition and drops the partition. However, `DROP PARTITION` with `ALGORITHM=COPY` or `old_alter_table=ON` rebuilds the partitioned table and attempts to move data from the dropped partition to another partition with a compatible `PARTITION …​ VALUES` definition. Data that cannot be moved to another partition is deleted.

### MySQL basic table partitioning methods

#### Hash table partitioning

Partitioning by hash is used mostly to achieve an even distribution of data between the partitions. Make sure that you specify a column value or expression based on a column value to be hashed and the number of partitions into which the partitioned table is to be divided when creating the partitioned table.

Make sure that you use an SQL expression that returns an integer for the hash expression. The only permitted data types beside integer are date types and one of the following functions:

```
ABS, CEILING, DAY, DAYOFMONTH, DAYOFWEEK, DAYOFYEAR, DATEDIFF, EXTRACT, FLOOR, HOUR, MICROSECOND, MINUTE, MOD, MONTH, QUARTER, SECOND, TIME_TO_SEC, TO_DAYS, TO_SECONDS, UNIX_TIMESTAMP (with TIMESTAMP columns), WEEKDAY, YEAR, YEARWEEK
```

For other column types you can use `KEY` partitioning, which takes any column used as part or all of the table’s primary key.

**Examples**

The following example creates a hash-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500),
    ERROR_CODE INT)
    PARTITION BY HASH (ERROR_CODE)
    PARTITIONS 3;
```

The following example creates a key-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500),
    ERROR_CODE VARCHAR(10) PRIMARY KEY)
    PARTITION BY KEY()
    PARTITIONS 3;
```

For more information, see [HASH Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-hash.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-hash.html") and [KEY Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-key.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-key.html") in the _MySQL documentation_.

#### List table partitioning

As with the hash partition, make sure that this partitioned column in `INT`. To use `LIST` on `varchar`, use `LIST COLUMNS`.

**Examples**

The following example creates a list-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500),
    ERROR_CODE INT)
    PARTITION BY LIST (ERROR_CODE)
    (PARTITION warning VALUES IN (3345, 5423,3332),
    PARTITION critical VALUES IN (9786, 9231, 6321));
```

The following example creates a list-columns-partition table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500),
    ERROR_CODE VARCHAR(500))
    PARTITION BY LIST COLUMNS (ERROR_CODE)
    (PARTITION warning VALUES IN ('err1', 'err2', 'err3'),
    PARTITION critical VALUES IN ('err4', 'err5', 'err6'));
```

For more information, see [LIST Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-list.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-list.html") in the _MySQL documentation_.

#### Range table partitioning

Similar to a list partition, you can use a range partition on integer values or `RANGE COLUMNS` for `DATE` or `DATETIME`.

**Examples**

The following example creates a range-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500))
    PARTITION BY RANGE (YEAR(EVENT_DATE))
    (PARTITION p0 VALUES LESS THAN (2015),
    PARTITION p1 VALUES LESS THAN (2016),
    PARTITION p2 VALUES LESS THAN (2017));
```

The following example creates a range columns-partitioned table.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500))
    PARTITION BY RANGE COLUMNS (EVENT_DATE)
    (PARTITION p0 VALUES LESS THAN ('2015-01-01'),
    PARTITION p1 VALUES LESS THAN ('2016-01-01'),
    PARTITION p2 VALUES LESS THAN ('2017-01-01'));
```

For more information, see [RANGE Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-range.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-range.html") in the _MySQL documentation_.

#### Composite table partitioning

With composite partitioning, a table can be partitioned by one data distribution method, and then each partition can be further subdivided into sub-partitions using the same, or different, data distribution methods.

In MySQL 5.7, you can subpartition tables that are partitioned by range or list. Subpartitions may use either hash or key partitioning.

You can use the following approaches:

- Specify only the number of subpartitions for each partition.
- Explicitly define subpartitions in any partition individually, this option is useful if you want to pick the names for your subpartitions.

###### Note

Make sure that all partitions have the same number of subpartitions.

**Examples**

The following example creates a range-key subpartition. All partitions have two subpartitions.

```
CREATE TABLE EMPLOYESS
    (DEPARTMENT_ID INT NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    FIRST_NAME VARCHAR(50),
    PRIMARY KEY (DEPARTMENT_ID, LAST_NAME))
    PARTITION BY RANGE(DEPARTMENT_ID)
    SUBPARTITION BY KEY (last_name)
    SUBPARTITIONS 2
        (PARTITION p1 VALUES LESS THAN (10),
        PARTITION p2 VALUES LESS THAN (20),
        PARTITION p3 VALUES LESS THAN (MAXVALUE));
```

For more information, see [Subpartitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-subpartitions.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-subpartitions.html") in the _MySQL documentation_.

#### Split partitions

In Oracle, `SPLIT PARTITION STATEMENT` translates to `REORGANIZE PARTITION` in MySQL. Create a list partition and then split one of the partitions.

You can split range partitions at the last partition only.

```
CREATE TABLE SYSTEM_LOGS
    (EVENT_NO INT NOT NULL,
    EVENT_DATE DATE NOT NULL,
    EVENT_STR VARCHAR(500),
    ERROR_CODE VARCHAR(500))
    PARTITION BY LIST COLUMNS (ERROR_CODE)
    (PARTITION warning VALUES IN ('err1', 'err2', 'err3'),
    PARTITION critical VALUES IN ('err4', 'err5', 'err6'));

ALTER TABLE SYSTEM_LOGS REORGANIZE PARTITION warning INTO
    (PARTITION warning0 VALUES IN ('err2.5', 'err3.5'),
    PARTITION warning1 VALUES IN ('err2.8', 'err3.8'));
```

For more information, see [Management of RANGE and LIST Partitions](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-range-list.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-range-list.html") in the _MySQL documentation_.

#### Exchange partitions

Similar to Oracle, you can exchange tables with partitions.

```
ALTER TABLE orders
    EXCHANGE PARTITION p_ord3 WITH TABLE orders_year_2016;
```

For more information, see [Exchanging Partitions and Subpartitions with Tables](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-exchange.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-exchange.html") in the _MySQL documentation_.

## Summary

| Oracle table partition type                    | Built-in MySQL support | Example                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List                                           | Yes                    | [LIST Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-list.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-list.html")                                                                                                                                                                                                                                                                       |
| Range                                          | Yes                    | [RANGE Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-range.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-range.html")                                                                                                                                                                                                                                                                    |
| Hash                                           | Yes                    | [HASH Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-hash.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-hash.html")                                                                                                                                                                                                                                                                       |
| Composite or subpartitioning                   | Yes                    | [Subpartitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-subpartitions.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-subpartitions.html")                                                                                                                                                                                                                                                       |
| Interval                                       | No                     | [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html")                                                                                                                                                                                                                              |
| Partition advisor                              | No                     | [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html")                                                                                                                                                                                                                              |
| Preference                                     | No                     | [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html")                                                                                                                                                                                                                              |
| Virtual column-based                           | No                     | [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html")                                                                                                                                                                                                                              |
| MySQL partitioning automatic list partitioning | No                     | [Restrictions and Limitations on Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html")                                                                                                                                                                                                                              |
| Split and exchange                             | Yes                    | [ALTER TABLE Partition Operations](https://dev.mysql.com/doc/refman/8.0/en/alter-table-partition-operations.html "https://dev.mysql.com/doc/refman/8.0/en/alter-table-partition-operations.html") and [Exchanging Partitions and Subpartitions with Tables](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-exchange.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-exchange.html") |
