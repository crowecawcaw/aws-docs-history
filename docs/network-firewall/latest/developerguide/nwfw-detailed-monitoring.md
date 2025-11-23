# Firewall monitoring in the Network Firewall console

Firewall monitoring provides comprehensive visibility into your firewall's flow logs and alert logs.
After you enable detailed monitoring, you can access these dashboards directly from the **Monitoring**
tab in the firewall details page, without leaving the Network Firewall console.

## Prerequisites

Before you can use firewall monitoring, review the following prerequisites based on your logging configuration:

General prerequisites

- Set up flow or alert log delivery to either Amazon CloudWatch or Amazon S3. For more information, see [Sending AWS Network Firewall logs to Amazon Simple Storage Service](logging-s3.md "logging-s3.md") or [Sending AWS Network Firewall logs to Amazon CloudWatch Logs](logging-cw-logs.md "logging-cw-logs.md").
- Ensure you have the necessary permissions to access monitoring features. For more information, see [(Optional) Permissions to access CloudWatch log metrics in Network Firewall](logging-cw-logs.md#cw-permissions-for-nwfw-dashboard "logging-cw-logs.md#cw-permissions-for-nwfw-dashboard") or [(Optional) Permissions to access Amazon S3 log metrics in Network Firewall using Amazon Athena](logging-s3.md#logging-s3-athena "logging-s3.md#logging-s3-athena").

###### Note

CloudWatch and Amazon S3 logs may incur additional charges. For information, see [Pricing for AWS Network Firewall logging](firewall-logging-pricing.md "firewall-logging-pricing.md").

For best practices on using the firewall monitoring dashboard, see [Working with the firewall monitoring dashboard](nwfw-using-dashboard.md "nwfw-using-dashboard.md").

S3 logging prerequisites
If your firewall sends logs to Amazon S3, ensure the following:

- The Amazon S3 bucket storing the logs is in the same region as the firewall. Amazon Athena requires this for log processing, as it doesn't support cross-region processing.
- If you specify a prefix for your S3 bucket, it doesn't begin with a forward slash (`/`). Prefixes starting with "/" aren't compatible with Amazon Athena processing and prevent the dashboard from functioning correctly. For more information about S3 bucket configuration, see [Sending AWS Network Firewall logs to Amazon Simple Storage Service](logging-s3.md "logging-s3.md").
- Your account has the required permissions to query Amazon Athena APIs. For information, see [(Optional) Permissions to access Amazon S3 log metrics in Network Firewall using Amazon Athena](logging-s3.md#logging-s3-athena "logging-s3.md#logging-s3-athena").

## Enable firewall monitoring

You can enable firewall monitoring in any of the following ways:

- During firewall creation, using the logging configuration widget in the **Configure advanced settings** workflow.
  For more information, see [Creating a firewall in AWS Network Firewall](creating-firewall.md "creating-firewall.md").
- From the **Edit Logging Configuration** page of an existing firewall
  For more information, see [Updating a firewall in AWS Network Firewall](firewall-updating.md "firewall-updating.md").
- Directly from the **Monitoring** tab in the firewall details page

## Considerations for using firewall monitoring

When you modify or move an Amazon S3 bucket or CloudWatch log group that is queried to populate the firewall monitoring dashboard, the metrics populated in the dashboard can become inaccurate.

When you enable detailed monitoring for a firewall that sends logs to Amazon S3:

- Network Firewall creates Amazon Athena tables in your account to process the log data.
- These tables are used exclusively for populating detailed monitoring dashboards and are managed by the Network Firewall console.
- Network Firewall creates Amazon Athena metadata files (including CSV files) in your S3 bucket. These metadata files are downloadable records of the metrics that populate the firewall monitoring dashboard.

For information about how Amazon S3 integrates with Amazon Athena, see [Querying Amazon S3 Inventory with Athena](../../../AmazonS3/latest/userguide/storage-inventory-athena-query.md "../../../AmazonS3/latest/userguide/storage-inventory-athena-query.md").

For best practices on using the firewall monitoring dashboard, see [Working with the firewall monitoring dashboard](nwfw-using-dashboard.md "nwfw-using-dashboard.md").
