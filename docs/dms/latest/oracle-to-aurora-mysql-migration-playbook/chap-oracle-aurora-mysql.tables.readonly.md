

# Oracle Read-only tables and partitions and Amazon Aurora MySQL replicas
<a name="chap-oracle-aurora-mysql.tables.readonly"></a>

With AWS DMS, you can migrate data from Oracle databases to Aurora MySQL databases while maintaining read-only access to the Oracle source database during the migration process. This capability utilizes Oracle read-only tables and partitions, which create a consistent view of the data during replication. Additionally, you can replicate data from an on-premises or EC2 instance database to an Aurora MySQL database using the AWS DMS replication instance, creating an Aurora MySQL replica.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | MySQL doesn’t support the `READ ONLY`, you can use a workaround. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.readonly.oracle"></a>

Beginning with Oracle 11g, tables can be marked as read-only to prevent DML operations from altering table data.

Prior to Oracle 11g, the only way to set a table to read-only mode was by limiting table privileges to `SELECT`. The table owner was still able to perform read and write operations. Starting from Oracle 11g, users can run an `ALTER TABLE` statement and change the table mode to either `READ ONLY` or `READ WRITE`.

Oracle 12c Release 2 introduces greater granularity for read-only objects and supports read-only table partitions. Any attempt to perform a DML operation on a partition, or sub-partition, set to `READ ONLY` results in an error.

 `SELECT FOR UPDATE` statements aren’t allowed.

DDL operations are permitted if they don’t modify table data.

Operations on indexes are allowed on tables set to `READ ONLY` mode.

 **Examples** 

```
CREATE TABLE EMP_READ_ONLY (
EMP_ID NUMBER PRIMARY KEY,
EMP_FULL_NAME VARCHAR2(60) NOT NULL);

INSERT INTO EMP_READ_ONLY VALUES(1, 'John Smith');

1 row created

ALTER TABLE EMP_READ_ONLY READ ONLY;

INSERT INTO EMP_READ_ONLY VALUES(2, 'Steven King');

ORA-12081: update operation not allowed on table "SCT"."TBL_READ_ONLY"

ALTER TABLE EMP_READ_ONLY READ WRITE;

INSERT INTO EMP_READ_ONLY VALUES(2, 'Steven King');

1 row created

COMMIT;

SELECT * FROM EMP_READ_ONLY;

EMP_ID  EMP_FULL_NAME
1       John Smith
2       Steven King
```

For more information, see [ALTER TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-TABLE.html) and [Changes in This Release for Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/release-changes.html#GUID-C7A9BAD4-E4C9-4765-88C5-51AC7E97BAF1) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.readonly.mysql"></a>

MySQL doesn’t provide a built-in feature for read only tables, but the same functionality can be achieved using Aurora Replicas. The main disadvantage of this approach is that you must use two separated instances.

It is important to note that there is a granularity difference between this workaround and options with Oracle. you cannot mimic a single read-only table, this workaround creates a read-only copy of the database.

### Example
<a name="chap-oracle-aurora-mysql.tables.readonly.mysql.example"></a>

The following walkthrough demonstrates how to create an Aurora replica:

1. Sign in to the AWS Management Console and choose **RDS**.

1. Choose **Instance actions** and choose **Create Aurora replica**.

1. Enter all required details and choose **Create**.

1. View the new record on the instances page. Make sure that the **Status** changes to **available** and the **Replication role** changes to **reader**.

For more information, see [Create an Amazon Aurora Read Replica from an RDS MySQL DB Instance](https://aws.amazon.com/blogs/aws/new-create-an-amazon-aurora-read-replica-from-a-mysql-db-instance) in the *Amazon Web Services News Blog*.