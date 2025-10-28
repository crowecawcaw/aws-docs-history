# Statuses of homogeneous data migrations in AWS DMS

For each data migration that you run, AWS DMS displays the **Status**
in the AWS DMS console. The following list includes the available statuses.

- `Creating` – AWS DMS is creating the data migration.
- `Ready` – The data migration is ready to start.
- `Starting` – AWS DMS is creating the serverless environment for your
  data migration. This process takes up to 15 minutes.
- `Load running` – AWS DMS is performing the full load migration.
- `Load complete, replication ongoing` – AWS DMS completed the full
  load and now replicates ongoing changes. AWS DMS uses this status only for data migrations
  of the full load and change data capture (CDC) type.
- `Replication ongoing` – AWS DMS is replicating ongoing changes.
  AWS DMS uses this status only for migrations of the change data capture (CDC) type.
- `Reloading target` – AWS DMS is restarting a data migration and performs
  the specified migration type.
- `Stopping` – AWS DMS is stopping the data migration. AWS DMS sets this status
  after you choose to stop the data migration on the **Actions** menu.
- `Stopped` – AWS DMS has stopped the data migration.
- `Failed` – The data migration has failed. For more information,
  see the log files.

To view the log files, choose your data migration on the
**Data migrations** tab. Next, choose **View CloudWatch logs**
under **Homogeneous data migration settings**.

###### Important

You can view log files if you select the check box for **Turn on CloudWatch logs**
when you create your data migration.

- `Deleting` – AWS DMS is deleting the data migration. AWS DMS sets this status
  after you choose to delete the data migration on the **Actions** menu.
- `Maintenance` – AWS DMS puts a task in maintenance mode status
  when new image is deployed on the underlying serverless container associated
  with your data migration task.
