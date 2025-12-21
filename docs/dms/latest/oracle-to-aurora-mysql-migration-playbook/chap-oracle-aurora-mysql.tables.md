# Oracle composite indexes and MySQL multiple-column indexes

With AWS DMS, you can optimize database performance by creating composite indexes in Oracle databases and multiple-column indexes in MySQL databases. A composite index (Oracle) or multiple-column index (MySQL) is a database index built from multiple columns in a table, allowing queries to be satisfied by utilizing the index entries alone.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                            | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| Five star feature compatibility | Five star automation level         | [Indexes](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes") | N/A             |

## Oracle usage

An index created on multiple table columns is known as a multi-column, concatenated, or composite index. The main purpose of composite indexes is to improve the performance of data retrieval for `SELECT` statements when filtering on all, or some, of the composite index columns. When using composite indexes, it is beneficial to place the most restrictive columns at the first position of the index to improve query performance. Column placement order is crucial when using composite indexes because the most prevalent columns are accessed first.

### Examples

Create a composite index on the `HR.EMPLOYEES` table.

```
CREATE INDEX IDX_EMP_COMPI ON
  EMPLOYEES (FIRST_NAME, EMAIL, PHONE_NUMBER);
```

Drop a composite index.

```
DROP INDEX IDX_EMP_COMPI;
```

For more information, see [Composite Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-ABE1DE2A-59CC-4ADE-86A5-426B16459464 "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-ABE1DE2A-59CC-4ADE-86A5-426B16459464") in the _Oracle documentation_.

## MySQL usage

MySQL multiple-column indexes are similar to composite indexes in Oracle.

These indexes are beneficial when queries filter on all indexed columns, the first indexed column, the first two indexed columns, the first three indexed columns, and so on. When indexed columns are specified in the optimal order during index creation, a single multiple-column index can improve performance in scenarios where several queries access the same database table.

You can specify up to 16 columns when creating a multiple-column index.

### Examples

Create a multiple-column index on the EMPLOYEES table.

```
CREATE INDEX IDX_EMP_COMPI
  ON EMPLOYEES (FIRST_NAME, EMAIL, PHONE_NUMBER);
```

Drop a multiple-column index.

```
DROP INDEX IDX_EMP_COMPI;
```

For more information, see [Multiple-Column Indexes](https://dev.mysql.com/doc/refman/5.7/en/multiple-column-indexes.html "https://dev.mysql.com/doc/refman/5.7/en/multiple-column-indexes.html") in the _MySQL documentation_.
