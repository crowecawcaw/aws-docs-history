

# Oracle bitmap indexes
<a name="chap-oracle-aurora-mysql.tables.bitmap"></a>

With AWS DMS, you can optimize query performance for data warehousing and ad-hoc queries by creating Oracle bitmap indexes. You can use bitmap indexes to enhance the speed of complex queries involving conditions, joins, and aggregations on columns with a relatively small number of distinct values. Bitmap indexes can significantly improve query response times, especially for star schema queries common in data warehousing and business intelligence applications.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![No compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-0.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Indexes](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.indexes)  | MySQL doesn’t support BITMAP index. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.bitmap.oracle"></a>

Bitmap indexes are task-specific indexes best suited for providing fast data retrieval for OLAP workloads and are generally very fast for read-mostly scenarios. However, bitmap indexes don’t perform well in heavy DML or OLTP workloads.

Unlike B-tree indexes where an index entry points to a specific table row, a bitmap index stores a bitmap for each index key.

Bitmap indexes are ideal for low-cardinality data filtering where the number of distinct values in a column is relatively small.

### Example
<a name="chap-oracle-aurora-mysql.tables.bitmap.oracle.example"></a>

Create an Oracle bitmap index.

```
CREATE BITMAP INDEX IDX_BITMAP_EMP_GEN ON EMPLOYEES(GENDER);
```

For more information, see [CREATE INDEX](https://docs.oracle.com/database/121/SQLRF/statements_5013.htm#SQLRF01209) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.bitmap.mysql"></a>

Currently, Amazon Aurora MySQL doesn’t provide a comparable alternative for bitmap indexes.