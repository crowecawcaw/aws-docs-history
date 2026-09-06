

# Oracle unused columns
<a name="chap-oracle-aurora-mysql.tables.alter"></a>

With AWS DMS, you can identify and manage unused columns in Oracle databases during database migration and replication tasks.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![No compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-0.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | MySQL doesn’t support unused columns. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.alter.oracle"></a>

Oracle provides a method to mark columns as *unused*. Unused columns aren’t physically dropped, but are treated as if they were dropped. Unused columns can’t be restored. Select statements don’t retrieve data from columns marked as unused and aren’t displayed when running a `DESCRIBE` table command.

The main advantage of setting a column to `UNUSED` is to reduce possible high database load when dropping a column from a large table. To overcome this issue, a column can be marked as unused and then be physically dropped later.

To set a column as unused, use the `SET UNUSED` clause.

### Examples
<a name="chap-oracle-aurora-mysql.tables.alter.oracle.examples"></a>

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

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.alter.mysql"></a>

Currently, Amazon Aurora MySQL doesn’t provide a comparable alternative for unused columns.