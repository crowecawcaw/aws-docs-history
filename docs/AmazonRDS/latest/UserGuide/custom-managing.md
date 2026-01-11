# Modifying an RDS Custom for SQL Server DB instance

Modifying an RDS Custom for SQL Server DB instance is similar to doing this for Amazon RDS, but the changes that you can make are limited to the
following:

- Changing the DB instance class
- Changing the backup retention period and backup window
- Changing the maintenance window
- Upgrading the DB engine version when a new version becomes available
- Changing the allocated storage, provisioned IOPS, and storage type
- Allowing and removing Multi-AZ deployments
  The following limitations apply to modifying an RDS Custom for SQL Server DB instance:

- Custom DB option and parameter groups aren't supported.
- Any storage volumes that you attach manually to your RDS Custom DB instance are outside the support perimeter.

For more information, see [RDS Custom support
perimeter](custom-concept.md#custom-troubleshooting.support-perimeter "custom-concept.md#custom-troubleshooting.support-perimeter").

###### To modify an RDS Custom for SQL Server DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to modify.
4. Choose **Modify**.
5. Make the following changes as needed:
   1. For **DB engine version**, choose the new version.
   2. Change the value for **DB instance class**.
      For supported classes, see

   [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md") 3. Change the value for **Backup retention
   period**. 4. For **Backup window**, set values for the
   **Start time** and
   **Duration**. 5. For **DB instance maintenance window**, set
   values for the **Start day**, **Start
   time**, and **Duration**.

6. Choose **Continue**.
7. Choose **Apply immediately** or **Apply during the next scheduled maintenance
   window**.
8. Choose **Modify DB instance**.
   To modify an RDS Custom for SQL Server DB instance, use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") AWS CLI command. Set the following parameters as needed:

- `--db-instance-class` – For supported classes, see

[DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md")

- `--engine-version` – The version number of the database engine to which you're
  upgrading.
- `--backup-retention-period` – How long to retain automated backups, from 0–35
  days.
- `--preferred-backup-window` – The daily time range during which automated backups are
  created.
- `--preferred-maintenance-window` – The weekly time range (in UTC) during which system
  maintenance can occur.
- `--apply-immediately` – Use `--apply-immediately` to apply the storage changes
  immediately.

Or use `--no-apply-immediately` (the default) to apply the changes during the next maintenance
window.
