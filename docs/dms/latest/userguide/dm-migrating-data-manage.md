# Managing data migrations in AWS DMS

After you create a data migration, AWS DMS doesn't automatically start migrating data. You start
a data migration manually when needed.

Before you start a data migration, you can modify all settings of your data migration. After you
start your data migration, you can't change the replication type. To use another replication type,
create a new data migration.

###### To start a data migration

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project. On the **Data migrations** tab, choose your
   data migration. The **Summary** page for your data migration opens.
4. For **Actions**, choose **Start**.

After this, AWS DMS creates a serverless environment for your data migration. This process takes
up to 15 minutes.
After you start a data migration, AWS DMS sets its status to **Starting**. The next
status that AWS DMS uses for your data migration, depends on the type of replication that you choose in
the data migration settings. For more information, see [Migration statuses](dm-migrating-data-statuses.md "dm-migrating-data-statuses.md").

###### To modify a data migration

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project. On the **Data migrations** tab, choose your
   data migration. The **Summary** page for your data migration opens.
4. Choose **Modify**.
5. Configure the settings for your data migration.

###### Important

If you have started a data migration, then you can't change the replication type. 6. To view your data migration logs in Amazon CloudWatch, select the check box for
**Turn on CloudWatch logs**. 7. Choose **Save changes**.
After AWS DMS starts a data migration, you can stop it. To do so, choose your data migration on the
**Data migrations** tab. Next, for **Actions**, choose **Stop**.

After you stop a data migration, AWS DMS sets its status to **Stopping**. Next,
AWS DMS sets the status of this data migration to **Stopped**. After AWS DMS stops a data migration,
you can modify, resume, restart, or delete your data migration.

To continue the data replication, choose the data migration that you stopped on the **Data migrations** tab.
Next, for **Actions**, choose **Resume processing**.

To restart the data load, choose the data migration that you stopped on the **Data migrations** tab.
Next, for **Actions**, choose **Restart**. AWS DMS deletes all data from your target database
and starts the data migration from scratch.

You can delete a data migration that you have stopped or that you haven't started. To delete a data migration,
choose it on the **Data migrations** tab. Next, for **Actions**, choose
**Delete**. To delete your migration project, stop and delete all data migrations.
