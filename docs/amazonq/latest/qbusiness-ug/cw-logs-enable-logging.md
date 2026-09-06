

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Enabling Amazon Q Business user conversation logging
<a name="cw-logs-enable-logging"></a>

You can enable Amazon Q Business user conversation logging within the Amazon Q Business console or using the Amazon CloudWatch Logs API operations.

 When you enable logging, you specify a delivery destination for the logs. If you choose Amazon S3, the prefix of logs delivered to the Amazon S3 bucket is `AWSLogs/account-id/AmazonQBusinessLogs/your-region/application-id/year/month/day/hour/.` The files are compressed and named with `Feedback-20240905T19Z_501fec0f.log.gz ` or `VendedAnalyticsChat-20240905T19Z_d26ccf9e.log.gz` formats.

**Important**  
Logs might include sensitive or personally identifiable data passed in the chats. You can filter out this information from your logs with the Amazon Q Business console. Or you can mask this data on your logs using CloudWatch Logs masking policies. For more information, see [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html). 

**Topics**
+ [Enabling user conversation logging with the Amazon Q Business console](#cws-logs-enable-logging-console)
+ [Enabling user conversation logging with the Amazon CloudWatch Logs API operations](#cws-logs-enable-logging-api)

## Enabling user conversation logging with the Amazon Q Business console
<a name="cws-logs-enable-logging-console"></a>

To enable user conversation logging with the Amazon Q Business console, use the admin controls for your environment to configure log delivery, optionally filter out sensitive information, and then enable logging to start streaming conversation and feedback data.

**To enable logging**

1. Open the Amazon Q Business console at [Amazon Q Business](https://console.aws.amazon.com/amazonq/business/) and sign in to your account.

1. In **Applications**, choose the name of your application environment.

1. In the navigation pane, choose **Enhancements** and choose **Admin Controls and Guardrails**.

1. In **Log delivery**, choose **Add** and choose one of the following options.
   + **Amazon CloudWatch Logs** – Enter the **Destination log group ** where the logs will be stored. To filter out sensitive or personally identifiable information, choose **Additional settings - optional** and specify the fields to be logged, the output format, and field delimiter.

     For more information about log groups, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs* user guide.
   + **Amazon S3** – To add delivery to Amazon S3, choose the **Log type** and specify a **Destination S3 bucket**. To filter out sensitive or personally identifiable information, in **Additional settings - optional** specify the fields to be logged, whether to use hive compatible S3 paths, the output format, and the field delimiter. 
   + **Amazon Data Firehose** – To add delivery to Amazon Data Firehose, choose the **Log type** and specify a **Destination delivery stream**. To filter out sensitive or personally identifiable information, in **Additional settings - optional** specify the fields to be logged, the output format, and the field delimiter. 

      For information about creating a delivery stream, see [Create a Firehose delivery stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateFirehoseStream.html). 
**Note**  
If you want the users' email recorded in your logs, it must be added explicitly as a field in **Additional settings**.

1. Choose **Enable logging** start streaming conversation and feedback data to your logging destination.

## Enabling user conversation logging with the Amazon CloudWatch Logs API operations
<a name="cws-logs-enable-logging-api"></a>

To enable user conversation logging with the Amazon CloudWatch Logs API operations, you call the PutDeliverySource, PutDeliveryDesintation, and CreateDelivery API operations. For information about quotas for these API operations, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html#limits_cloudwatch_events).

**Note**  
To enable conversation logging, you need the Amazon Resource Name (ARN) of your environment. To get this ARN, you can use the Amazon Q Business console or the [GetApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html) API operation. An ARN follows this format: `arn:aws:qbusiness:region:account-id:application/application-id`.

**To enable user conversation logging**

1.  Create a delivery source with the [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) Amazon CloudWatch Logs API operation. Give the delivery source a name and for `resourceArn`, specify the ARN of your application. For `logType`, specify `EVENT_LOGS`. 

   ```
   {
     "logType": "EVENT_LOGS",
     "name": "my-q-business-application-delivery-source",
     "resourceArn": "arn:aws:qbusiness:your-region:your-account-id:application/application-id"
   }
   ```

1.  Configure the log delivery destination with the [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) Amazon CloudWatch Logs API operation. You can choose either Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose as the destination for storing logs. You must specify the Amazon Resource Name of one of the destination options for where your logs will be stored. The `outputFormat` of the logs can be one of the following: json, plain, w3c, raw, or parquet. The following shows how to specify an Amazon S3 bucket as a log delivery destination with an `outputFormat` of `json`. 

   ```
   {
       "deliveryDestinationConfiguration": {
           "destinationResourceArn": "arn:aws:s3:::bucket-name"
       },
       "name": "s3-delivery-destination",
       "outputFormat": "json",
       "tags": {
           "key": "value"
       }
   }
   ```

1.  Enable monitoring with the [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) Amazon CloudWatch Logs API operation. This API operation links the delivery source to the destination you created in the previous steps. 

   ```
   {
     "deliveryDestinationArn": "string",
     "deliverySourceName": "string",
     "tags": {
       "string": "string"
     }
   }
   ```
**Note**  
If you want the users' email recorded in your logs, it must be added explicitly as a field along with the [other fields](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-log-examples.html) that you want in the [`recordFields`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html#CWL-CreateDelivery-request-recordFields) parameter as part of calling the `CreateDelivery` operation .