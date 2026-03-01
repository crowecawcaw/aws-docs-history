# Use the CloudTrail console to create an Athena table for CloudTrail logs

You can create a non-partitioned Athena table for querying CloudTrail logs directly from the
CloudTrail console. Creating an Athena table from the CloudTrail console requires that you be logged
in with a role that has sufficient permissions to create tables in Athena.

###### Note

You cannot use the CloudTrail console to create an Athena table for organization trail
logs. Instead, create the table manually using the Athena console so that you can
specify the correct storage location. For information about organization trails, see
[Creating a
trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the
_AWS CloudTrail User Guide_.

- For information about setting up permissions for Athena, see [Set up, administrative, and programmatic access](setting-up.md "setting-up.md").
- For information about creating a table with partitions, see [Create a table for CloudTrail logs in Athena using manual partitioning](create-cloudtrail-table.md "create-cloudtrail-table.md").

###### To create an Athena table for a CloudTrail trail using the CloudTrail console

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**.
3. Choose **Create Athena table**.

![Choose Create Athena table](images/cloudtrail-logs-create-athena-table.png) 4. For **Storage location**, use the down arrow to select the
Amazon S3 bucket where log files are stored for the trail to query.

###### Note

To find the name of the bucket that is associated with a trail, choose
**Trails** in the CloudTrail navigation pane and view the
trail's **S3 bucket** column. To see the Amazon S3 location for
the bucket, choose the link for the bucket in the **S3
bucket** column. This opens the Amazon S3 console to the CloudTrail bucket
location. 5. Choose **Create table**. The table is created with a default
name that includes the name of the Amazon S3 bucket.
