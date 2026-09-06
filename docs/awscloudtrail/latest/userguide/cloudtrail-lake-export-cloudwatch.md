

# Exporting data from CloudTrail Lake Event Data Store to CloudWatch
<a name="cloudtrail-lake-export-cloudwatch"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

Making CloudTrail Lake data available to CloudWatch provides several advantages:
+ **Centralized log management** - Combine CloudTrail events with application logs, infrastructure logs, and other data sources in CloudWatch.
+ **Simplified integration** - CloudWatch handles the import process with just a few steps - specify the event data store and data range.
+ **Historical data access** - Import historical CloudTrail Lake data to analyze past events alongside current operational data.
+ **No additional CloudTrail cost** - Simplified import of CloudTrail Lake data is available at no additional CloudTrail cost. However, you will incur CloudWatch cost with Infrequent Access custom logs pricing applied.

This section describes how to export data from an event data store using the CloudTrail console. For information about how to perform this via SDK or AWS CLI, see [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/)

**To export data from an event data store**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store.

1. From **Actions**, choose **Export to CloudWatch**.

1. Choose the time range to export data for the EDS.

1. Use the instructions to either create or provide an IAM role that CloudTrail will use to access your data for export.

1. Choose **Export**.

When making CloudTrail Lake data available for export into CloudWatch, consider the following:
+ **Pricing** - While simplified export of CloudTrail Lake data is available at no additional CloudTrail cost, you incur CloudWatch fees based on custom logs pricing
+ **Data retention** - Ensure that your CloudTrail Lake event data store retention period covers the historical data you want to export
+ **Regional availability** - Check the CloudWatch documentation for supported AWS regions for this feature
+ **Event data store access** - You must have access to the Event Data Store from which data will be exported. 