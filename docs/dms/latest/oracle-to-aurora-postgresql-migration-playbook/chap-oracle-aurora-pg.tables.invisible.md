

# Oracle and PostgreSQL invisible indexes
<a name="chap-oracle-aurora-pg.tables.invisible"></a>

You can create invisible indexes in Oracle Database. An invisible index is a type of index that is not used by the optimizer by default but can still be used if explicitly specified in a query.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-1.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  |  [Indexes](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.indexes)  | PostgreSQL doesn’t support invisible indexes. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.invisible.ora"></a>

In Oracle, the invisible index feature gives database administrators the ability to create indexes, or change existing indexes, that are ignored by the optimizer. They are maintained during DML operations and are kept relevant, but are different from usable indexes.

The most common uses for invisible indexes are:
+ Testing the effect of a dropped index without actually dropping it.
+ Using a specific index for certain operations or modules of an application without affecting the overall application.
+ Adding an index to a set of columns on which an index already exists.

Database administrators can force the optimizer to use invisible indexes by changing the `OPTIMIZER_USE_INVISIBLE_INDEXES` parameter to true. You can use invisible indexes if they are specified as a HINT.

 **Examples** 

Change an index to an invisible index.

```
ALTER INDEX idx_name INVISIBLE;
```

Change an invisible index to a visible index.

```
ALTER INDEX idx_name VISIBLE;
```

Create an invisible index.

```
CREATE INDEX idx_name ON employees(first_name) INVISIBLE;
```

Query all invisible indexes.

```
SELECT TABLE_OWNER, INDEX_NAME FROM DBA_INDEXES
  WHERE VISIBILITY = 'INVISIBLE';
```

For more information, see [Understand When to Use Unusable or Invisible Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html#GUID-3A66938F-73C6-4173-844E-3938A0DBBB54) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.invisible.pg"></a>

Currently, Aurora PostgreSQL doesn’t provide a directly comparable alternative for Oracle invisible indexes.