

# Oracle bitmap indexes and PostgreSQL bitmap
<a name="chap-oracle-aurora-pg.tables.bitmap"></a>

With AWS DMS, you can efficiently migrate databases utilizing Oracle bitmap indexes for optimized query performance. Oracle bitmap indexes are data structures that improve the efficiency of data filtering operations on tables with low cardinality columns.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  |  [Indexes](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.indexes)  | PostgreSQL doesn’t support BITMAP index. You can use BRIN index in some cases. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.bitmap.ora"></a>

Bitmap indexes are task-specific indexes best suited for providing fast data retrieval for OLAP workloads and are generally very fast for read-mostly scenarios. However, bitmap indexes don’t perform well in heavy DML or OLTP workloads.

Unlike B-tree indexes where an index entry points to a specific table row, a bitmap index stores a bitmap for each index key.

Bitmap indexes are ideal for low-cardinality data filtering where the number of distinct values in a column is relatively small.

 **Examples** 

Create an Oracle bitmap index.

```
CREATE BITMAP INDEX IDX_BITMAP_EMP_GEN ON EMPLOYEES(GENDER);
```

For more information, see [CREATE INDEX](https://docs.oracle.com/database/121/SQLRF/statements_5013.htm#SQLRF01209) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.bitmap.pg"></a>

 Amazon Aurora PostgreSQL doesn’t currently provide a directly comparable alternative for Oracle bitmap indexes.