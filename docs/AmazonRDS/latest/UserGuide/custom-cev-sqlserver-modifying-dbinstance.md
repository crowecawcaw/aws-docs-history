# Modifying an RDS Custom for SQL Server DB instance to use a new CEV

You can modify an existing RDS Custom for SQL Server DB instance to use a different CEV. The changes that
you can make include:

- Changing the CEV
- Changing the DB instance class
- Changing the backup retention period and backup window
- Changing the maintenance window

###### To modify an RDS Custom for SQL Server DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to modify.
4. Choose **Modify**.
5. Make the following changes as needed:
   1. For **DB engine version**, choose a different CEV.
   2. Change the value for **DB instance class**.
      For supported classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md").
   3. Change the value for **Backup retention
      period**.
   4. For **Backup window**, set values for the
      **Start time** and
      **Duration**.
   5. For **DB instance maintenance window**, set
      values for the **Start day**, **Start
      time**, and **Duration**.

6. Choose **Continue**.
7. Choose **Apply immediately** or **Apply during the next scheduled maintenance window**.
8. Choose **Modify DB instance**.

###### Note

When modifying a DB instance from one CEV to an another CEV, for example,
when upgrading a minor version, the SQL Server system databases, including their
data and configurations, are persisted from the current RDS Custom for SQL Server DB instance.
To modify a DB instance to use a different CEV by using the AWS CLI, run the [modify-db-instance](../../../cli/latest/reference/rds/modify-custom-db-engine-version.md "../../../cli/latest/reference/rds/modify-custom-db-engine-version.md") command.

The following options are required:

- `--db-instance-identifier`
- `--engine-version
 ``cev```, where
 ``cev`` is the name of the
 custom engine version that you want the DB instance to change to.
The following example modifies a DB instance named `my-cev-db-instance` to use a CEV named`15.00.4249.2.my_cevtest_new` and applies the
  change immediately.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier my-cev-db-instance \
    --engine-version `15.00.4249.2.my_cevtest_new` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier my-cev-db-instance ^
    --engine-version `15.00.4249.2.my_cevtest_new` ^
    --apply-immediately
```
