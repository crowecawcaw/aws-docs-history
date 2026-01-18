# Monitoring your data migrations

After the data migrations starts, you can monitor its status and progress. Data migrations of large data sets take hours to complete.
To maintain the reliability, availability, and high performance of your data migration,
monitor its progress regularly.

###### To check the status and progress of your data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. The **Associated data migrations** section lists your data migrations. Check the
   **Status** column.
4. For running data migrations, the **Migration process** column displays the
   percentage of migrated data.
5. To monitor the process in CloudWatch, use the link in the in **CloudWatch** column.

## Migration statuses

For each data migration that you run, the RDS console
displays the **Status**. The following list includes the statuses:

- `Ready`: The data migration is ready to start.
- `Starting`: RDS is
  creating the serverless environment for your data migration.
- `Load running`: RDS is performing the full load
  migration.
- `Load complete, replication ongoing`: RDS
  completed the full load and now replicates the ongoing changes. This status only applies for full load and CDC type migrations.
- `Replication ongoing`: RDS is
  replicating ongoing changes. This status only applies to CDC type migrations.
- `Stopping`: RDS
  is stopping the data migrations. This status applies when you choose to stop the data migration from the **Actions** menu.
- `Stopped`: RDS has stopped the data migration.
- `Failed`: The data migration has failed. For more information, see the log files.
- `Restarting`: The data migration has restarted an ongoing data replication from a CDC start point.
