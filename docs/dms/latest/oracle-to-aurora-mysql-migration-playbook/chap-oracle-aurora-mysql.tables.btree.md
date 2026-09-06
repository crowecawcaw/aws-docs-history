

# Oracle and MySQL B-tree indexes
<a name="chap-oracle-aurora-mysql.tables.btree"></a>

With AWS DMS, you can efficiently migrate data from your Oracle database to Aurora MySQL , while preserving existing B-tree indexes.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-5.png)  |  [Indexes](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.indexes)  | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.btree.oracle"></a>

B-tree indexes (B stands for balanced), are the most common index type in a relational database and are used for a variety of common query performance enhancing tasks. You can define B-tree indexes as an ordered list of values divided into ranges. They provide superior performance by associating a key with a row or range of rows.

B-tree indexes contain two types of blocks: branch blocks for searching and leaf blocks for storing values. The branch blocks also contain the root branch, which points to lower-level index blocks in the B-tree index structure.

B-tree indexes are useful for primary keys and other high-cardinality columns. They provide excellent data access performance for a variety of query patterns such as exact match searches and range searches. B-tree indexes are the default when you create a new index.

### Example
<a name="chap-oracle-aurora-mysql.tables.btree.oracle.example"></a>

Create a B-tree index.

```
CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG(EVENT_ID);
```

For more information, see [CREATE INDEX](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.btree.mysql"></a>

MySQL provides full support for B-tree indexes. Certain constraints created in MySQL such as primary keys or unique keys are stored in a B-tree index format. Similar to Oracle, B-tree indexes are the default for new indexes.

The query optimizer in MySQL can use B-tree indexes when handling equality and range queries on data. The MySQL optimizer considers using B-tree indexes to access data, especially when queries use one or more of the following operators: `>`, `>=`, `<`, `⇐`, `=`.

In addition, query elements such as `IN`, `BETWEEN`, `IS NULL`, or `IS NOT NULL` can also use B-tree indexes for faster data retrieval.

There are two types of indexes: \* **Clustered index** — A reference as primary key. When a primary key is defined on a table, InnoDB uses it as the clustered index. It is highly recommended to specify a primary key for all tables. If there is no primary key, MySQL locates the first `UNIQUE` index where all columns are `NOT NULL` and are used as a clustered index. If there is no primary key or `UNIQUE` index to use, InnoDB internally generates a hidden clustered index named `GEN_CLUST_INDEX`. \* **Secondary index**: All indexes that are not clustered indexes. Each index entry has a reference to the clustered index. If the clustered index is applied on long values, the secondary indexes consume more storage space.

## Example
<a name="chap-oracle-aurora-mysql.tables.btree.mysql.example"></a>

Create a B-tree Index.

```
CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG (EVENT_ID);

or

CREATE INDEX IDX_EVENT_ID ON SYSTEM_LOG (EVENT_ID) USING BTREE;
```

For more information, see [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html) in the *MySQL documentation*.