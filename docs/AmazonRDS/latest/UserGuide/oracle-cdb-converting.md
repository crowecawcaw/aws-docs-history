# Converting an RDS for Oracle non-CDB to a CDB

You can change the architecture of an Oracle database from the non-CDB architecture to the
Oracle multitenant architecture, also called the _CDB architecture_, with
the `modify-db-instance` command. In most cases, this technique is preferable to
creating a new CDB and importing data. The conversion operation incurs downtime.

When you upgrade your database engine version, you can't change the database architecture
in the same operation. Therefore, to upgrade an Oracle Database 19c non-CDB to an Oracle Database 21c CDB, you first
need to convert the non-CDB to a CDB in one step, and then upgrade the 19c CDB to a 21c CDB
in a separate step.

The non-CDB conversion operation has the following requirements:

- You must specify `oracle-ee-cdb` or `oracle-se2-cdb` for the
  DB engine type. These are the only supported values.
- Your DB engine must use Oracle Database 19c with an April 2021 or later release update
  (RU).
  The operation has the following limitations:

- You can't convert a CDB to a non-CDB. You can only convert a non-CDB to a
  CDB.
- You can't convert a non-CDB to the multi-tenant configuration in a single
  `modify-db-instance` call. After you convert a non-CDB to a CDB, your
  CDB is in the single-tenant configuration. To convert the single-tenant
  configuration to the multi-tenant configuration, run `modify-db-instance`
  again. For more information, see [Converting the single-tenant configuration
  to multi-tenant](oracle-single-tenant-converting.md "oracle-single-tenant-converting.md").
- You can't convert a primary or replica database that has Oracle Data Guard
  enabled. To convert a non-CDB that has read replicas, first delete all read
  replicas.
- You can't upgrade the DB engine version and convert a non-CDB to a CDB in the same
  operation.
  Before converting your non-CDB, consider the following:

- The considerations for option and parameter groups are the same as for upgrading
  the DB engine. For more information, see [Considerations for Oracle database
  upgrades](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").
- You can convert existing non-CDB instances that uses managed master passwords to
  single-tenant instances in a single operation. The single-tenant instances inherit
  the managed passwords.
- If your DB instance has the `OEMAGENT` option installed, a best practice is
  to remove this option before you convert your non-CDB. After your non-CDB is
  converted to a CDB, reinstall the option. For more information, see [Oracle Management Agent for Enterprise Manager
  Cloud Control](Oracle.Options.md "Oracle.Options.md").
- During the conversion process, RDS resets the online redo log size to the default
  128M.

###### To convert a non-CDB to a CDB

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region
   where your DB instance resides.
3. In the navigation pane, choose **Databases**, and then
   choose the non-CDB instance that you want to convert to a CDB instance.
4. Choose **Modify**.
5. For **Architecture settings**, select **Oracle
   multitenant architecture**. After conversion, your CDB will be
   in the single-tenant configuration.
6. (Optional) For **DB parameter group**, choose a new
   parameter group for your CDB instance. The same parameter group
   considerations apply when converting a DB instance as when upgrading a DB instance. For
   more information, see [Parameter group
   considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.PG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.PG").
7. (Optional) For **Option group**, choose a new option
   group for your CDB instance. The same option group considerations apply when
   converting a DB instance as when upgrading a DB instance. For more information, see
   [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").
8. (Optional) For **Credentials management**, choose
   **Managed in AWS Secrets Manager** or
   **Self-managed**. For more information, see [Managing the master user password for a DB instance with Secrets Manager](rds-secrets-manager.md#rds-secrets-manager-db-instance "rds-secrets-manager.md#rds-secrets-manager-db-instance").
9. When all the changes are as you want them, choose
   **Continue** and check the summary of modifications.
10. (Optional) Choose **Apply immediately** to apply the
    changes immediately. Choosing this option can cause downtime in some cases.
    For more information, see [Using the schedule modifications
    setting](USER_ModifyInstance.md "USER_ModifyInstance.md").
11. On the confirmation page, review your changes. If they are correct, choose
    **Modify DB instance**.

Or choose **Back** to edit your changes or
**Cancel** to cancel your changes.
To convert the non-CDB on your DB instance to a CDB in the single-tenant configuration,
set `--engine` to `oracle-ee-cdb` or
`oracle-se2-cdb` in the AWS CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). For
more information, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md").

The following example converts the DB instance named
`my-non-cdb` and specifies a custom option group and
parameter group. The command also enables password management with
Secrets Manager.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-non-cdb` \
    --engine oracle-ee-cdb \
    --option-group-name `custom-option-group` \
    --db-parameter-group-name `custom-parameter-group` \
    --manage-master-user-password
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-non-cdb` ^
    --engine oracle-ee-cdb ^
    --option-group-name `custom-option-group` ^
    --db-parameter-group-name `custom-parameter-group` ^
    --manage-master-user-password
```

To convert a non-CDB to a CDB, specify `Engine` in the RDS API
operation [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md").
