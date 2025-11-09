# Monitoring data migrations in AWS DMS

After you start your homogeneous data migration, you can monitor its status and progress. Data migrations of large
data sets such as hundreds of gigabytes take hours to complete. To maintain the reliability, availability, and
high performance of your data migration, monitor its progress regularly.

###### To check the status and progress of your data migration

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project and navigate to the **Data migrations** tab.
4. For your data migration, see the **Status** column. For more information about
   values in this column, see [Migration statuses](dm-migrating-data-statuses.md "dm-migrating-data-statuses.md").
5. For a running data migration, the **Migration progress** column displays the
   percentage of migrated data.

###### To check the details of your data migration

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project. On the **Data migrations** tab, choose your data
   migration.
4. On the **Details** tab, you can see the migration progress. Particularly, you
   can see the following metrics.
   - **Public IP address** – The public IP address of your
     data migration. You need this value to configure a network. For more information, see
     [Setting up a network](dm-network.md "dm-network.md").
   - **Tables loaded** – The number of successfully loaded
     tables.
   - **Tables loading** – The number of tables currently
     loading.
   - **Tables queued** – The number of tables currently
     waiting to be loaded.
   - **Tables errored** – The number of tables that failed
     to load.
   - **Elapsed time** – The amount of time that passed after
     the start of your data migration.
   - **CDC latency** – The average time that passes between
     when a change occurs on a source table and when AWS DMS applies this change to the target table.
   - **Migration started** – The time when you started this
     data migration.
   - **Migration stopped** – The time when you stopped this
     data migration.

5. To view the log files for your data migration, choose **View CloudWatch logs**
   under **Homogeneous data migration settings**. You can **Turn on CloudWatch logs**
   when you create or modify a data migration. For more information, see
   [Creating a data migration](dm-migrating-data-create.md "dm-migrating-data-create.md") and
   [Managing data migrations](dm-migrating-data-manage.md "dm-migrating-data-manage.md").
   You can use Amazon CloudWatch alarms or events to closely track your data migration. For more information,
   see [What are Amazon CloudWatch, Amazon CloudWatch Events, and Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.
   Note that there is a charge for using Amazon CloudWatch.

For homogeneous data migrations, AWS DMS includes the following metrics in Amazon CloudWatch.

| Metric             | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OverallCDCLatency  | The overall latency during the CDC phase.<br>For MySQL databases, this metric shows the number of seconds that passes between the change<br>in the source binary log and the replication of this change.<br>For PostgreSQL databases, this metric shows the number of seconds that passes between<br>`last_msg_receipt_time` and `last_msg_send_time` from<br>the `pg_stat_subscription` view.<br>Units: Seconds |
| StorageConsumption | The storage that your data migration consumes.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                   |
