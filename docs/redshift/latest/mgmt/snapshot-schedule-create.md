Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a snapshot schedule

Amazon Redshift takes automatic, incremental snapshots of your data periodically and saves them
to Amazon S3. Additionally, you can take manual snapshots of your data whenever you want.

All snapshot tasks in the Amazon Redshift console start from the snapshot list. You can filter
the list by using a time range, the snapshot type, and the cluster associated with the
snapshot. In addition, you can sort the list by date, size, and snapshot type. Depending on
the snapshot type that you select, you might have different options available for working
with the snapshot.

To precisely control when snapshots are taken, you can create a snapshot schedule and
attach it to one or more clusters. You can attach a schedule when you create a cluster or
by modifying the cluster. For more information, see [Automated snapshot schedules](working-with-snapshots.md#automated-snapshot-schedules "working-with-snapshots.md#automated-snapshot-schedules").

###### To create a snapshot schedule

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose the **Snapshot
   schedules** tab. The snapshot schedules are displayed.
3. Choose **Add schedule** to display the page to add a schedule.
4. Enter the properties of the schedule definition, then choose **Add
   schedule**.
5. On the page that appears, you can attach clusters to your new snapshot schedule,
   then choose **OK**.
