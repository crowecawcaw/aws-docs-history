

# Oracle table compression
<a name="chap-oracle-aurora-mysql.special.tablecompression"></a>

With AWS DMS, you can optimize storage utilization and improve query performance for Oracle databases by leveraging table compression. Oracle table compression reduces the disk space footprint of tables and associated indexes, which can lead to significant cost savings, especially for large datasets.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  | N/A | N/A | Syntax and option differences, similar functionality. MySQL doesn’t compress partitions. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.tablecompression.oracle"></a>

Oracle table compression reduces the size of data. It saves disk space, reduces memory usage, and speeds up query execution during reads. However, the cost is increased CPU overhead for data loading and DML.

Table compression is completely transparent to applications. It is most commonly used for OLAP systems where there are significantly more read operations, but it can also be used in OLTP systems.

Tables can be compressed when they are created using the `COMPRESS` clause. Existing tables can be compressed using the `COMPRESS` clause with an `ALTER TABLE` statement.

You can turn on compression for `ALL OPERATIONS` on the table or for `DIRECT_LOAD OPERATIONS` only. When compression is turned on for all operations, compression occurs during all DML statements and when data is inserted with a bulk (direct-path) insert operation.

The compression clause provides four options:
+  `NOCOMPRESS` — Don’t use compression. This is the default option.
+  `COMPRESS` — Turns on compression on the table or partition during direct-path inserts only.
+  `COMPRESS FOR DIRECT_LOAD OPERATIONS` — Turns on compression on the table or partition during direct-path inserts only.
+  `COMPRESS FOR ALL OPERATIONS` — Turns on the compression for all operations including DML statements. This option is mostly used for OLTP systems.

### Examples
<a name="chap-oracle-aurora-mysql.special.tablecompression.oracle.examples"></a>

View the compression status of tables.

```
SELECT OWNER, TABLE_NAME, COMPRESSION,COMPRESS_FOR FROM dba_tables;
```

The following example creates a compressed table.

```
CREATE TABLE comp_tbl
(id NUMBER NOT NULL,
created_date DATE NOT NULL)
COMPRESS FOR ALL OPERATIONS;
```

The following example creates a partitioned table with a compressed partition.

```
CREATE TABLE comp_part_tbl
(id NUMBER NOT NULL,
created_date DATE NOT NULL)
PARTITION BY RANGE (created_date) (
PARTITION comp_part_tbl_q1 VALUES LESS THAN (TO_DATE('01/01/2018', 'DD/MM/YYYY'))
COMPRESS,
PARTITION comp_part_tbl_q2 VALUES LESS THAN (TO_DATE('01/04/2018', 'DD/MM/YYYY'))
COMPRESS FOR DIRECT_LOAD OPERATIONS,
PARTITION comp_part_tbl_q3 VALUES LESS THAN (TO_DATE('01/07/2018', 'DD/MM/YYYY'))
COMPRESS FOR ALL OPERATIONS,
PARTITION comp_part_tbl_q4 VALUES LESS THAN (MAXVALUE) NOCOMPRESS);
```

For more information, see [DBMS\_COMPRESSION](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_COMPRESSION.html) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.tablecompression.mysql"></a>

 Aurora MySQL doesn’t support compressed tables (that is, tables created with `ROW_FORMAT=COMPRESSED`). Make sure that you expand your compressed tables by setting `ROW_FORMAT` to `DEFAULT`, `COMPACT`, `DYNAMIC`, or `REDUNDANT`.

For more information, see [InnoDB Table Compression](https://dev.mysql.com/doc/refman/5.7/en/innodb-table-compression.html) in the *MySQL documentation*.