

# Oracle composite indexes and PostgreSQL multi-column indexes
<a name="chap-oracle-aurora-pg.tables.composite"></a>

With AWS DMS, you can optimize query performance by creating composite indexes or multi-column indexes on your migrated databases. A composite index (Oracle) or multi-column index (PostgreSQL) is a database index created on multiple columns, allowing queries involving those columns to leverage the index for faster data retrieval.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  |  [Indexes](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.indexes)  | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.composite.ora"></a>

An index created on multiple table columns is known as a multi-column, concatenated, or composite index. The main purpose of composite indexes is to improve the performance of data retrieval for `SELECT` statements when filtering on all, or some, of the composite index columns. When using composite indexes, it is beneficial to place the most restrictive columns at the first position of the index to improve query performance. Column placement order is crucial when using composite indexes because the most prevalent columns are accessed first.

 **Examples** 

Create a composite index on the `HR.EMPLOYEES` table.

```
CREATE INDEX IDX_EMP_COMPI ON
  EMPLOYEES (FIRST_NAME, EMAIL, PHONE_NUMBER);
```

Drop a composite index.

```
DROP INDEX IDX_EMP_COMPI;
```

For more information, see [Composite Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-ABE1DE2A-59CC-4ADE-86A5-426B16459464) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.composite.pg"></a>

PostgreSQL multi-column indexes are similar to Oracle composite indexes. Currently, only B-tree, GiST, GIN, and BRIN support multi-column indexes. You can specify up to 32 columns to create a multi-column index.

PostgreSQL uses the same syntax as Oracle to create multi-column indexes.

 **Examples** 

Create a multi-column index on the EMPLOYEES table.

```
CREATE INDEX IDX_EMP_COMPI
  ON EMPLOYEES (FIRST_NAME, EMAIL, PHONE_NUMBER);
```

Drop a multi-column index.

```
DROP INDEX IDX_EMP_COMPI;
```

For more information, see [Multicolumn Indexes](https://www.postgresql.org/docs/13/indexes-multicolumn.html) in the *PostgreSQL documentation*.