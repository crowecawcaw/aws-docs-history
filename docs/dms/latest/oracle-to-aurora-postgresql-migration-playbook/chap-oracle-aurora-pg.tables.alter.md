

# Oracle unused columns and PostgreSQL ALTER TABLE statement
<a name="chap-oracle-aurora-pg.tables.alter"></a>

With AWS DMS, you can identify and analyze unused columns in Oracle databases and migrate data to PostgreSQL. Oracle unused columns is a feature that scans Oracle database schemas to detect columns that are not being used by applications or queries. You can modify the structure of an existing table in a PostgreSQL database by using the `ALTER TABLE` statement. `ALTER TABLE` lets you add, remove, or modify columns and constraints in a table after it has been created.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  | N/A | PostgreSQL doesn’t support unused columns. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.alter.ora"></a>

Oracle provides a method to mark columns as *unused*. Unused columns aren’t physically dropped, but are treated as if they were dropped. Unused columns can’t be restored. Select statements don’t retrieve data from columns marked as unused and aren’t displayed when running a `DESCRIBE` table command.

The main advantage of setting a column to UNUSED is to reduce possible high database load when dropping a column from a large table. To overcome this issue, a column can be marked as unused and then be physically dropped later.

To set a column as unused, use the `SET UNUSED` clause.

 **Examples** 

```
ALTER TABLE EMPLOYEES SET UNUSED (COMMISSION_PCT);
ALTER TABLE EMPLOYEES SET UNUSED (JOB_ID, COMMISSION_PCT);
```

Display unused columns.

```
SELECT * FROM USER_UNUSED_COL_TABS;

TABLE_NAME  COUNT
EMPLOYEES   3
```

Drop the column permanently (physically drop the column).

```
ALTER TABLE EMPLOYEES DROP UNUSED COLUMNS;
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.alter.pg"></a>

PostgreSQL doesn’t support marking table columns as *unused*. However, when running the `ALTER TABLE… DROP COLUMN` command, the drop column statement doesn’t physically remove the column; it only makes it invisible to SQL operations. As such, dropping a column is a fast action, but doesn’t reduce the ondisk size of your table immediately because the space occupied by the dropped column isn’t reclaimed.

The unused space is reclaimed by new DML actions, as they use the space that once was occupied by the dropped column. To force an immediate reclamation of storage space, use the `VACUUM FULL` command. Alternatively, run an `ALTER TABLE` statement to force a rewrite.

 **Examples** 

PostgreSQL `drop column` statement.

```
ALTER TABLE EMPLOYEES DROP COLUMN COMMISSION_PCT;
```

Verify the operation.

```
SELECT TABLE_NAME, COLUMN_NAME
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_NAME = 'emps1' AND COLUMN_NAME=LOWER('COMMISSION_PCT');

table_name  column_name
(0 rows)
```

Use the `VACUUM FULL` command to reclaim unused space from storage.

```
VACUUM FULL EMPLOYEES;
```

Run the `VACUUM FULL` statement with the `VERBOSE` option to display an activity report of the vacuum process that includes the tables vacuumed and the time taken to perform the vacuum operation.

```
VACUUM FULL VERBOSE EMPLOYEES;
```

For more information, see [ALTER TABLE](https://www.postgresql.org/docs/10/sql-altertable.html) and [VACUUM](https://www.postgresql.org/docs/13/sql-vacuum.html) in the *PostgreSQL documentation*.