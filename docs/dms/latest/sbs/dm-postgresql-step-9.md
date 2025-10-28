# Step 9: Running and Monitoring a Data Migration

After you create a data migration, you can run it and monitor its status.

**To start a data migration**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page opens.
3. Choose the migration project that you created in [Step 7](dm-postgresql-step-7.md "dm-postgresql-step-7.md").
4. On the **Data migrations** tab, choose the data migration that you created in [Step 7](dm-postgresql-step-7.md "dm-postgresql-step-7.md").
5. For **Actions**, choose **Start**.
   The first launch of a homogeneous data migration requires some setup. AWS DMS creates a serverless environment for your data migration. This process takes up to 15 minutes.

**To monitor a data migration**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page opens.
3. Choose the migration project that you created in [Step 7](dm-postgresql-step-7.md "dm-postgresql-step-7.md").
4. On the **Data migrations** tab, see the **Status** column for your data migration. For more information about values in this column, see [Statuses of homogeneous data migrations](../userguide/dm-migrating-data-statuses.md "../userguide/dm-migrating-data-statuses.md").
5. For a running data migration, the **Migration progress** column displays the percentage of migrated data.
6. Choose your data migration. On the **Details** tab, you can see the progress of your homogeneous data migration.
   After AWS DMS completes the full load process, your data migration starts the replication of ongoing changes.
