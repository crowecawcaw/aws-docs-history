# Using vended logs to send AWS Elemental MediaTailor logs

You can use vended logs for greater flexibility and control over where to deliver logs
that MediaTailor emits from your playback configuration.

With vended logs, MediaTailor sends all log activity associated with a configuration to
Amazon CloudWatch Logs. CloudWatch Logs then sends the percent of logs that you specify to your chosen destination.
Supported destinations are an Amazon CloudWatch Logs log group, Amazon S3 bucket, or Amazon Data Firehose stream.

Because vended logs are available at volume discount pricing, you could see cost savings
compared to sending logs directly to CloudWatch Logs. For pricing, see _Vended
Logs_ on the **Logs** tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To use vended logs, you must do the following:

1. [Add permissions](#vended-logs-perms "#vended-logs-perms").
2. [Create log delivery destinations](#vended-logs-destinations "#vended-logs-destinations").
3. [Configure log delivery in
   CloudWatch Logs](#vended-logs-delivery "#vended-logs-delivery").
4. [Enable vended logs in MediaTailor](#vended-logs-config "#vended-logs-config").
   For more information about vended logs, see [Enable logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the
   CloudWatch Logs user guide. MediaTailor supports V2 of vended logs.

## Step 1: Add permissions for MediaTailor log delivery

The person who's setting up vended logs must have permissions to create the delivery
destination, configure log delivery, and enable vended logs in MediaTailor. Use the following
policies to ensure that you have the appropriate permissions to set up vended logs.

**Policies for CloudWatch Logs and delivery destinations**
The following sections in the _Amazon CloudWatch Logs User Guide_ provide
the policies that enable you to work with logs in CloudWatch Logs and your delivery
destinations. If you send logs to multiple locations, you can combine the
policy statements into one policy instead of creating multiple policies.

- [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs")
- [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3")
- [Logs sent to Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose")

**Policy for set up from the console**

If you're setting up vended logs delivery through the console instead of
the API or AWS CLI, you must have the following additional permissions in your
policy.

**Policy for vended logs in MediaTailor**
To create, view, or modify vended logs delivery in MediaTailor, you must have the following
permissions in your policy.

For information about adding permissions and working with policies, see [Identity and Access Management for AWS Elemental MediaTailor](security-iam.md "security-iam.md").

## Step 2: Create delivery destinations for MediaTailor logs

Create the resources where your logs will be sent. Record the ARN of the resource for
use in configuring the log delivery in a later step.

**CloudWatch Logs log group delivery destination**
Use one of the following for help creating a log group.

- For the console, see [Create a log group in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group") in the _Amazon CloudWatch Logs User
  Guide_.
- For the API, see [CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md") in the _Amazon CloudWatch Logs API Reference._
- For SDKs and CLI, see [Use `CreateLogGroup` with an AWS SDK or
  AWS CLI](../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogGroup_section.md "../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogGroup_section.md") in the _Amazon CloudWatch Logs User
  Guide_.

**Amazon S3 bucket delivery destination**

Use one of the following for help creating a bucket.

- For the console, SDKs, and CLI, see [Create a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the
  _Amazon Simple Storage Service User Guide_.
- For the API, see [CreateBucket](../../../AmazonS3/latest/API/API_CreateBucket.md "../../../AmazonS3/latest/API/API_CreateBucket.md") in the _Amazon Simple Storage Service API
  Reference_.

**Firehose stream delivery destination**

For help creating a stream, see [Create a Firehose stream from console](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the
_Amazon Data Firehose Developer Guide_.

## Step 3: Enable vended logs for the MediaTailor playback

configuration

Create or update the playback configuration that will be sending logs to the delivery
destination that you created in the previous step. Record the name of the configuration
for use in configuring the log delivery in a later step.

- To enable vended logs through the console, using [Creating a
  configuration](configurations-create.md "configurations-create.md") or [Editing configuration
  settings](configurations-edit.md "configurations-edit.md")
  Editing a configuration to access the **Logging** settings. For
  **Logging strategies**, choose **Vended
  logs**.
- To enable vended logs through the API, you must have an existing
  configuration. Use `ConfigureLogsForPlaybackConfiguration` to add the
  logging strategy `Vended logs`.

If you're using the legacy MediaTailor logging strategy of sending logs directly to CloudWatch Logs
and want to migrate to vended logs, see [Migrating the logging
strategy](vended-logs-migrate.md "vended-logs-migrate.md").

###### Important

If you change the log strategy from Legacy CloudWatch to vended logs, MediaTailor will make
this change as soon as you save the updates. You will stop receiving logs until you
have fully configured vended logging.

## Step 4: Configure log delivery in CloudWatch Logs

In CloudWatch Logs, you must create three elements to represent the pieces of log delivery.
These elements are described in detail in [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") in the _Amazon CloudWatch Logs API Reference_. The
high-level steps to configure the delivery with the CloudWatch Logs API are as follows.

###### To configure log delivery in CloudWatch Logs (API)

1. Use [`PutDeliverySource`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") to add the source of logs.

A `DeliverySource` represents the playback configuration that's
generating the logs. You need the name of the playback configuration to create
the `DeliverySource`. 2. Use [`PutDeliveryDestination`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") to add the destination where logs will
be written.

A `DeliveryDestination` represents the delivery destination. You
need the ARN of the log group, bucket, or stream to create the
`DeliveryDestination`. 3. Use [`PutDeliveryDestinationPolicy`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md") if you are delivering logs
across accounts.

If the delivery destination is in a different account from the playback
configuration, you need a `DeliveryDestinationPolicy`. This policy
allows CloudWatch Logs to deliver logs to the `DeliveryDestination`. 4. Use [`CreateDelivery`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") to link the `DeliverySource` to the
`DeliveryDestination`.

A `Delivery` represents the connection between the
`DeliverySource` and `DeliveryDestination`.
