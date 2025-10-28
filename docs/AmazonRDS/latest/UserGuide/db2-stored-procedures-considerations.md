# Considerations for Amazon RDS for Db2

stored procedures

Before using the Amazon RDS system stored procedures for RDS for Db2 DB instances running the Db2
engine, review the following information:

- Before running the stored procedures, you must first connect to the
  `rdsadmin` database as the master user for your RDS for Db2 DB instance.
  In the following example, replace `master_username` and
  `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

- The stored procedures return the `ERR_MESSAGE` parameter, which
  indicates whether the stored procedure ran successfully or not and why it didn't run
  successfully.

**Examples**

The following example indicates that the stored procedure ran successfully.

```
Parameter Name : ERR_MESSAGE
Parameter Value : -
Return Status = 0
```

The following example indicates that the stored procedure didn't run successfully
because the Amazon S3 bucket name used in the stored procedure wasn't valid.

```
Parameter Name : ERR_MESSAGE
Parameter Value : Invalid S3 bucket name
Return Status = -1006
```

For error messages returned when calling stored procedures, see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").
For information about checking the status of a stored procedure, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").
