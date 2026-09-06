

# Using vended logs to send AWS Elemental MediaTailor logs
<a name="vended-logs"></a>

You can use vended logs for greater flexibility and control over where to deliver logs that MediaTailor emits from your playback configuration. 

With vended logs, MediaTailor sends all log activity associated with a configuration to Amazon CloudWatch Logs. CloudWatch Logs then sends the percent of logs that you specify to your chosen destination. Supported destinations are an Amazon CloudWatch Logs log group, Amazon S3 bucket, or Amazon Data Firehose stream. 

Because vended logs are available at volume discount pricing, you could see cost savings compared to sending logs directly to CloudWatch Logs. For pricing, see *Vended Logs* on the **Logs** tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

To use vended logs, you must do the following:

1. [Add permissions](#vended-logs-perms).

1. [Create log delivery destinations](#vended-logs-destinations).

1. [Configure log delivery in CloudWatch Logs](#vended-logs-delivery).

1. [Enable vended logs in MediaTailor](#vended-logs-config).

For more information about vended logs, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the CloudWatch Logs user guide. MediaTailor supports V2 of vended logs. 

## Step 1: Add permissions for MediaTailor log delivery
<a name="vended-logs-perms"></a>

The person who's setting up vended logs must have permissions to create the delivery destination, configure log delivery, and enable vended logs in MediaTailor. Use the following policies to ensure that you have the appropriate permissions to set up vended logs. 

**Policies for CloudWatch Logs and delivery destinations**  
The following sections in the *Amazon CloudWatch Logs User Guide* provide the policies that enable you to work with logs in CloudWatch Logs and your delivery destinations. If you send logs to multiple locations, you can combine the policy statements into one policy instead of creating multiple policies.   
+ [Logs sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-CloudWatchLogs)
+ [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-S3)
+ [Logs sent to Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-Firehose)

**Policy for set up from the console**  
If you're setting up vended logs delivery through the console instead of the API or AWS CLI, you must have the following additional permissions in your policy.

**Policy for vended logs in MediaTailor**  
To create, view, or modify vended logs delivery in MediaTailor, you must have the following permissions in your policy.

For information about adding permissions and working with policies, see [Identity and Access Management for AWS Elemental MediaTailor](security-iam.md).

## Step 2: Create delivery destinations for MediaTailor logs
<a name="vended-logs-destinations"></a>

Create the resources where your logs will be sent. Record the ARN of the resource for use in configuring the log delivery in a later step.

**CloudWatch Logs log group delivery destination**  
Use one of the following for help creating a log group.  
+ For the console, see [Create a log group in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch Logs User Guide*.
+ For the API, see [CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html) in the *Amazon CloudWatch Logs API Reference.* 
+ For SDKs and CLI, see [Use `CreateLogGroup` with an AWS SDK or AWS CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogGroup_section.html) in the *Amazon CloudWatch Logs User Guide*. 

**Amazon S3 bucket delivery destination**  
Use one of the following for help creating a bucket.  
+ For the console, SDKs, and CLI, see [Create a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon Simple Storage Service User Guide*.
+ For the API, see [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) in the *Amazon Simple Storage Service API Reference*. 

**Firehose stream delivery destination**  
For help creating a stream, see [Create a Firehose stream from console](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*.

## Step 3: Enable vended logs for the MediaTailor playback configuration
<a name="vended-logs-config"></a>

Create or update the playback configuration that will be sending logs to the delivery destination that you created in the previous step. Record the name of the configuration for use in configuring the log delivery in a later step. 
+ To enable vended logs through the console, using [Creating a configuration](configurations-create.md) or [Editing configuration settings](configurations-edit.md) Editing a configuration to access the **Logging** settings. For **Logging strategies**, choose **Vended logs**.
+ To enable vended logs through the API, you must have an existing configuration. Use `ConfigureLogsForPlaybackConfiguration` to add the logging strategy `Vended logs`.

If you're using the legacy MediaTailor logging strategy of sending logs directly to CloudWatch Logs and want to migrate to vended logs, see [Migrating the logging strategy](vended-logs-migrate.md).

**Important**  
 If you change the log strategy from Legacy CloudWatch to vended logs, MediaTailor will make this change as soon as you save the updates. You will stop receiving logs until you have fully configured vended logging.

## Step 4: Configure log delivery in CloudWatch Logs
<a name="vended-logs-delivery"></a>

In CloudWatch Logs, you must create three elements to represent the pieces of log delivery. These elements are described in detail in [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) in the *Amazon CloudWatch Logs API Reference*. The high-level steps to configure the delivery with the CloudWatch Logs API are as follows. 

**To configure log delivery in CloudWatch Logs (API)**

1. Use [`PutDeliverySource`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) to add the source of logs.

   A `DeliverySource` represents the playback configuration that's generating the logs. You need the name of the playback configuration to create the `DeliverySource`. 

1. Use [`PutDeliveryDestination`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) to add the destination where logs will be written.

   A `DeliveryDestination` represents the delivery destination. You need the ARN of the log group, bucket, or stream to create the `DeliveryDestination`.

1. Use [`PutDeliveryDestinationPolicy`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) if you are delivering logs across accounts. 

   If the delivery destination is in a different account from the playback configuration, you need a `DeliveryDestinationPolicy`. This policy allows CloudWatch Logs to deliver logs to the `DeliveryDestination`.

1. Use [`CreateDelivery`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) to link the `DeliverySource` to the `DeliveryDestination`.

   A `Delivery` represents the connection between the `DeliverySource` and `DeliveryDestination`.