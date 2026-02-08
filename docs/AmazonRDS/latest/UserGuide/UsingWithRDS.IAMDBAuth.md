# Enabling and disabling IAM database

authentication

By default, IAM database authentication is disabled on DB
instances.
You can enable or disable IAM database authentication using the AWS Management Console, AWS CLI, or the API.

You can enable IAM database authentication when you perform one of the following actions:

- To create a new DB instance with IAM database authentication enabled,
  see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- To modify a DB instance to enable IAM database authentication,
  see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
- To restore a DB instance from a snapshot with IAM database authentication enabled, see
  [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
- To restore a DB instance to a point in time with IAM database authentication enabled, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").
  Each creation or modification workflow has a **Database authentication**
  section, where you can enable or disable IAM database authentication. In that section, choose
  **Password and IAM database authentication** to enable IAM database authentication.

###### To enable or disable IAM database authentication for an existing DB

instance

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance
   that you want to modify.

###### Note

Make sure that the DB instance is compatible with IAM authentication. Check the compatibility
requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability"). 4. Choose **Modify**. 5. In the **Database authentication** section, choose
**Password and IAM database authentication**
to
enable IAM database authentication. Choose **Password
authentication** or **Password and Kerberos
authentication** to disable IAM authentication. 6. You can also choose to enable publishing IAM DB authentication logs to CloudWatch Logs.
Under **Log exports**, choose the
**iam-db-auth-error log** option. Publishing your logs to CloudWatch Logs consumes storage
and you incur charges for that storage. Be sure to delete any CloudWatch Logs that you no longer need. 7. Choose **Continue**. 8. To apply the changes immediately, choose **Immediately** in the
**Scheduling of modifications** section. 9. Choose **Modify DB instance**
.
To create a new DB instance with IAM authentication by using the AWS CLI, use the [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command. Specify the `--enable-iam-database-authentication` option, as shown in
the following example.

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-instance-class `db.m3.medium` \
    --engine `MySQL` \
    --allocated-storage `20` \
    --master-username `masterawsuser` \
    --manage-master-user-password \
    **--enable-iam-database-authentication**
```

To update an existing DB instance to have or not have IAM
authentication, use the AWS CLI
command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Specify either the `--enable-iam-database-authentication` or
`--no-enable-iam-database-authentication` option, as appropriate.

###### Note

Make sure that the DB instance is compatible with IAM authentication. Check the compatibility
requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability").

By default,
Amazon RDS
performs the modification during the next maintenance window.
If you want to override this and enable IAM DB authentication as soon as possible,
use the `--apply-immediately` parameter.

The following example shows how to immediately enable IAM authentication for an
existing DB instance.

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    **--apply-immediately** \
    **--enable-iam-database-authentication**
```

If you are restoring a DB instance,
use one of the following AWS CLI commands:

- `restore-db-instance-to-point-in-time`
- `restore-db-instance-from-db-snapshot`
  The IAM database authentication setting defaults to that of the source snapshot.
  To change this setting, set the `--enable-iam-database-authentication` or
  `--no-enable-iam-database-authentication` option, as appropriate.

To create a new DB instance with IAM authentication by using the API, use the
API operation [`CreateDBInstance`](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md"). Set the `EnableIAMDatabaseAuthentication` parameter to
`true`.

To update an existing DB instance to have IAM
authentication, use the API operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the
`EnableIAMDatabaseAuthentication` parameter to `true`
to enable IAM authentication, or `false` to disable it.

###### Note

Make sure that the DB instance is compatible with IAM authentication. Check the compatibility
requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability").

If you are restoring a DB instance,
use one of the following API operations:

- [`RestoreDBInstanceFromDBSnapshot`](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md")
- [`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")
  The IAM database authentication setting defaults to that of the source
  snapshot. To change this setting, set the
  `EnableIAMDatabaseAuthentication` parameter to `true`
  to enable IAM authentication, or `false` to disable it.
