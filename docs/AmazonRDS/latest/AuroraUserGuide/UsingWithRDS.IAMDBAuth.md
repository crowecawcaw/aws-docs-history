# Enabling and disabling IAM database

authentication

By default, IAM database authentication is disabled on DB
clusters.
You can enable or disable IAM database authentication using the AWS Management Console, AWS CLI, or the API.

You can enable IAM database authentication when you perform one of the following actions:

- To create a new DB cluster with IAM database authentication enabled,
  see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
- To modify a DB cluster to enable IAM database authentication,
  see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
- To restore a DB cluster from a snapshot with IAM database authentication enabled, see
  [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").
- To restore a DB cluster to a point in time with IAM database authentication enabled, see [Restoring a DB cluster to a specified time](aurora-pitr.md "aurora-pitr.md").
  Each creation or modification workflow has a **Database authentication**
  section, where you can enable or disable IAM database authentication. In that section, choose
  **Password and IAM database authentication** to enable IAM database authentication.

###### To enable or disable IAM database authentication for an existing DB

cluster

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB cluster
   that you want to modify.

###### Note

You can only enable IAM authentication if all DB instances in the DB cluster are
compatible with IAM. Check the compatibility requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability"). 4. Choose **Modify**. 5. In the **Database authentication** section, choose

**IAM database authentication** to
enable IAM database authentication. Choose **Password
authentication** or **Password and Kerberos
authentication** to disable IAM authentication. 6. You can also choose to enable publishing IAM DB authentication logs to CloudWatch Logs.
Under **Log exports**, choose the
**iam-db-auth-error log** option. Publishing your logs to CloudWatch Logs consumes storage
and you incur charges for that storage. Be sure to delete any CloudWatch Logs that you no longer need. 7. Choose **Continue**. 8. To apply the changes immediately, choose **Immediately** in the
**Scheduling of modifications** section. 9. Choose
**Modify cluster**.
To create a new DB cluster with IAM authentication by using the AWS CLI, use the [`create-db-cluster`](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") command. Specify the `--enable-iam-database-authentication` option.

To update an existing DB cluster to have or not have IAM
authentication, use the AWS CLI
command [`modify-db-cluster`](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md"). Specify either the `--enable-iam-database-authentication` or
`--no-enable-iam-database-authentication` option, as appropriate.

###### Note

You can only enable IAM authentication if all DB instances in the DB cluster are
compatible with IAM. Check the compatibility requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability").

By default,
Aurora
performs the modification during the next maintenance window.
If you want to override this and enable IAM DB authentication as soon as possible,
use the `--apply-immediately` parameter.

If you are restoring a DB cluster,
use one of the following AWS CLI commands:

- `restore-db-cluster-to-point-in-time`
- `restore-db-cluster-from-db-snapshot`
  The IAM database authentication setting defaults to that of the source snapshot.
  To change this setting, set the `--enable-iam-database-authentication` or
  `--no-enable-iam-database-authentication` option, as appropriate.

To create a new DB instance with IAM authentication by
using the API, use the API operation [`CreateDBCluster`](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md"). Set the `EnableIAMDatabaseAuthentication` parameter to
`true`.

To update an existing DB cluster to have IAM
authentication, use the API operation [`ModifyDBCluster`](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md"). Set the
`EnableIAMDatabaseAuthentication` parameter to `true`
to enable IAM authentication, or `false` to disable it.

###### Note

You can only enable IAM authentication if all DB instances in the DB cluster are
compatible with IAM. Check the compatibility requirements in
[Region and version availability](UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability "UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Availability").

If you are restoring a DB cluster,
use one of the following API operations:

- [`RestoreDBClusterFromSnapshot`](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md")
- [`RestoreDBClusterToPointInTime`](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md")
  The IAM database authentication setting defaults to that of the source
  snapshot. To change this setting, set the
  `EnableIAMDatabaseAuthentication` parameter to `true`
  to enable IAM authentication, or `false` to disable it.
