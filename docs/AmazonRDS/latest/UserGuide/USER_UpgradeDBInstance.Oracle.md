# Upgrading the version of an

RDS for Oracle DB instance

To manually upgrade the DB engine version of an RDS for Oracle DB instance,use the AWS Management Console, the AWS CLI,
or the RDS API. For general information about database upgrades in RDS, see Upgrading the version of an
RDS for Oracle DB instance. To get valid upgrade targets,
use the AWS CLI [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

###### To upgrade the engine version of an RDS for Oracle DB instance by using the

console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then
   choose the DB instance that you want to upgrade.
3. Choose **Modify**.
4. For **DB engine version**, choose a higher database
   version.
5. Choose **Continue** and check the summary of
   modifications. Make sure that you understand the implications of a database
   version upgrade. You can't convert an upgraded DB instance back to the previous
   version. Make sure you have tested both your database and your application
   with the new version before continuing.
6. Decide when to schedule your DB instance upgrade. To apply the changes
   immediately, choose **Apply immediately**. Choosing this
   option can cause an outage in some cases. For more information, see [Using the schedule modifications
   setting](USER_ModifyInstance.md "USER_ModifyInstance.md").
7. On the confirmation page, review your changes. If they are correct, choose
   **Modify DB instance** to save your changes.

Alternatively, choose **Back** to edit your changes, or
choose **Cancel** to cancel your changes.
To upgrade the engine version of an RDS for Oracle DB instance, you can use the CLI [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
command. Specify the following parameters:

- `--db-instance-identifier` – the name of the RDS for Oracle
  DB instance.
- `--engine-version` – the version number of the database
  engine to upgrade to.

For information about valid engine versions, use the AWS CLI [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

- `--allow-major-version-upgrade` – to upgrade the DB engine
  version.
- `--no-apply-immediately` – to apply changes during the
  next maintenance window. To apply changes immediately, use
  `--apply-immediately`.

###### Example

The following example upgrades a CDB instance named `myorainst`
from its current version of `19.0.0.0.ru-2024-01.rur-2024-01.r1` to
version `21.0.0.0.ru-2024-04.rur-2024-04.r1`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `myorainst` \
    --engine-version `21.0.0.0.ru-2024-04.rur-2024-04.r1` \
    --allow-major-version-upgrade \
    --no-apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `myorainst` ^
    --engine-version `21.0.0.0.ru-2024-04.rur-2024-04.r1` ^
    --allow-major-version-upgrade ^
    --no-apply-immediately
```

To upgrade an RDS for Oracle DB instance, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action.
Specify the following parameters:

- `DBInstanceIdentifier` – the name of the DB instance, for
  example `myorainst`.
- `EngineVersion` – the version number of the database
  engine to upgrade to. For information about valid engine versions, use the
  [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") operation.
- `AllowMajorVersionUpgrade` – whether to allow a major
  version upgrade. To do so, set the value to `true`.
- `ApplyImmediately` – whether to apply changes
  immediately or during the next maintenance window. To apply changes
  immediately, set the value to `true`. To apply changes during the
  next maintenance window, set the value to `false`.
