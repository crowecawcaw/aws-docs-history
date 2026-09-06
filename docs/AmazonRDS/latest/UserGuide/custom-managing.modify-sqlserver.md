

# Modifying an RDS Custom for SQL Server DB instance
<a name="custom-managing.modify-sqlserver"></a>

Modifying an RDS Custom for SQL Server DB instance is similar to doing this for Amazon RDS, but the changes that you can make are limited to the following:
+ Changing the DB instance class
+ Changing the backup retention period and backup window
+ Changing the maintenance window
+ Upgrading the DB engine version when a new version becomes available
+ Changing the allocated storage, provisioned IOPS, and storage type
+ Allowing and removing Multi-AZ deployments

The following limitations apply to modifying an RDS Custom for SQL Server DB instance:
+ Custom DB option and parameter groups aren't supported.
+ Any storage volumes that you attach manually to your RDS Custom DB instance are outside the support perimeter.

  For more information, see [RDS Custom support perimeter](custom-concept.md#custom-troubleshooting.support-perimeter).

## Console
<a name="custom-managing.modify-sqlserver.CON"></a>

**To modify an RDS Custom for SQL Server DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the DB instance that you want to modify.

1. Choose **Modify**.

1. Make the following changes as needed:

   1. For **DB engine version**, choose the new version.

   1. Change the value for **DB instance class**. For supported classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.instancesMS.md)

   1. Change the value for **Backup retention period**.

   1. For **Backup window**, set values for the **Start time** and **Duration**.

   1. For **DB instance maintenance window**, set values for the **Start day**, **Start time**, and **Duration**.

1. Choose **Continue**.

1. Choose **Apply immediately** or **Apply during the next scheduled maintenance window**.

1. Choose **Modify DB instance**.

## AWS CLI
<a name="custom-managing.modify-sqlserver.CLI"></a>

To modify an RDS Custom for SQL Server DB instance, use the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) AWS CLI command. Set the following parameters as needed:
+ `--db-instance-class` – For supported classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.instancesMS.md)
+ `--engine-version` – The version number of the database engine to which you're upgrading.
+ `--backup-retention-period` – How long to retain automated backups, from 0–35 days.
+ `--preferred-backup-window` – The daily time range during which automated backups are created.
+ `--preferred-maintenance-window` – The weekly time range (in UTC) during which system maintenance can occur.
+ `--apply-immediately` – Use `--apply-immediately` to apply the storage changes immediately.

  Or use `--no-apply-immediately` (the default) to apply the changes during the next maintenance window.