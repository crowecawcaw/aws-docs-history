# Monitoring your S3 File Gateway

You can monitor your S3 File Gateway and associated resources in AWS Storage Gateway by
using Amazon CloudWatch metrics and audit logs. You can also use CloudWatch Events to get notified when your file
operations are done.

###### Topics

- [Getting S3 File Gateway health logs
  with CloudWatch log groups](#cw-log-groups "#cw-log-groups")
- [Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics")
- [Getting notified about file operations](#get-notification "#get-notification")
- [Understanding
  gateway metrics](#understanding-file-gateway-metrics "#understanding-file-gateway-metrics")
- [Understanding
  file share metrics](#monitoring-file-gateway-resources "#monitoring-file-gateway-resources")
- [Understanding S3 File Gateway audit
  logs](#audit-logs "#audit-logs")

## Getting S3 File Gateway health logs

with CloudWatch log groups

You can use Amazon CloudWatch Logs to get information about the health of your S3 File Gateway
and related resources. You can use the logs to monitor your gateway for errors that it
encounters. In addition, you can use Amazon CloudWatch subscription filters to automate
processing of the log information in real time. For more information, see [Real-time
Processing of Log Data with Subscriptions](../../../AmazonCloudWatch/latest/logs/Subscriptions.md "../../../AmazonCloudWatch/latest/logs/Subscriptions.md") in the _Amazon CloudWatch User Guide._

For example, you can configure a CloudWatch log group to monitor your
gateway and get notified when your S3 File Gateway fails to upload files to an Amazon S3 bucket. You
can configure the group either when you are activating the gateway or after your gateway
is activated and up and running. For information about how to configure a CloudWatch log group
when activating a gateway, see [Configure your Amazon S3 File Gateway](create-gateway-file.md#configure-gateway-s3-file "create-gateway-file.md#configure-gateway-s3-file"). For general information about CloudWatch log
groups, see [Working
with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch User Guide._

The following is an example of an error reported by an S3 File Gateway.

```
{
    "severity": "ERROR",
    "bucket": "bucket-smb-share2",
    "roleArn": "arn:aws:iam::123456789012:role/amzn-s3-demo-bucket",
    "source": "share-E1A2B34C",
    "type": "InaccessibleStorageClass",
    "operation": "S3Upload",
    "key": "myFolder/myFile.text",
    "gateway": "sgw-B1D123D4",
    "timestamp": "1565740862516"
}
```

This error means that the S3 File Gateway is unable to upload the object
`myFolder/myFile.text` to Amazon S3 because it has transitioned out of the
Amazon S3 Standard storage class to either the S3 Glacier Flexible Retrieval or the
S3 Glacier Deep Archive storage class.

In the preceding gateway health log, these items specify the given
information:

- `source: share-E1A2B34C` indicates the file share that encountered
  this error.
- `"type": "InaccessibleStorageClass"` indicates the type of error
  that occurred. In this case, this error was encountered when the gateway was
  trying to upload the specified object to Amazon S3 or read from Amazon S3. However, in
  this case, the object has transitioned to Amazon Glacier. The value of
  `"type"` can be any error that the S3 File Gateway encounters. For a
  list of possible errors, see [Troubleshooting: File Gateway
  issues](troubleshooting-file-gateway-issues.md "troubleshooting-file-gateway-issues.md").
- `"operation": "S3Upload"` indicates that this error occurred when the
  gateway was trying to upload this object to S3.
- `"key": "myFolder/myFile.text"` indicates the object that caused
  the failure.
- `gateway": "sgw-B1D123D4` indicates the S3 File Gateway that encountered
  this error.
- `"timestamp": "1565740862516"` indicates the time that the error
  occurred.

For information about how to troubleshoot the errors that may be reported by S3 File Gateway, see [Troubleshooting: File Gateway
issues](troubleshooting-file-gateway-issues.md "troubleshooting-file-gateway-issues.md").

### Configuring a CloudWatch log group after your gateway is

activated

The following procedure shows you how to configure a CloudWatch Log Group after your
gateway is activated.

###### To configure a CloudWatch log group to work with your S3 File Gateway

1. Sign in to the AWS Management Console and open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Gateways**, and then
   choose the gateway that you want to configure the CloudWatch log group for.
3. For **Actions**, choose **Edit gateway
   information**.
4. For **Choose how to set up log group**, choose one of the
   following:
   - **Create a new log group** to create a new CloudWatch
     log group.
   - **Use an existing log group** to use a CloudWatch log
     group that already exists.

   Choose a log group from the **Existing log group
   list**.
   - **Deactivate logging** if you don't want to
     monitor your gateway using CloudWatch log groups.

5. Choose **Save changes**.
6. To see the health logs for your gateway, do the following:
   1. In the navigation pane, choose **Gateways**, and
      then choose the gateway that you configured the CloudWatch log group
      for.
   2. Choose the **Details** tab, and under
      **Health logs**, choose **CloudWatch
      Logs**. The **Log group details** page
      opens in the CloudWatch console.

## Using Amazon CloudWatch metrics

You can get monitoring data for your S3 File Gateway by using either
the AWS Management Console or the CloudWatch API. The console displays a series of graphs based on the raw
data from the CloudWatch API. The CloudWatch API can also be used through one of the [AWS SDKs](https://aws.amazon.com/tools "https://aws.amazon.com/tools") or [Amazon CloudWatch API](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch") tools. Depending on your needs, you might
prefer to use either the graphs displayed in the console or retrieved from the
API.

Regardless of which method you use to work with metrics, you must specify the
following information:

- The metric dimension to work with. A _dimension_ is a
  name-value pair that helps you to uniquely identify a metric. The dimensions for
  Storage Gateway are `GatewayId` and `GatewayName`. In the
  CloudWatch console, you can use the `Gateway Metrics` view to select
  gateway-specific dimensions. For more information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the _Amazon CloudWatch User Guide_.
- The metric name, such as `ReadBytes`.

The following table summarizes the types of Storage Gateway metric data that are
available to you.

| Amazon CloudWatch namespace | Dimension                  | Description                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/StorageGateway`        | `GatewayId`, `GatewayName` | These dimensions filter for metric data that describes aspects of<br>the gateway. You can identify a S3 File Gateway to work with by specifying both the<br>`GatewayId` and the<br>`GatewayName` dimensions.<br>Throughput and latency data of a gateway are based on all the file<br>shares in the gateway.<br>Data is available automatically in 5-minute periods at no charge. |

Working with gateway and file metrics is similar to working with other service
metrics. You can find a discussion of some of the most common metrics tasks in the CloudWatch
documentation listed following:

- [Viewing available metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md")
- [Getting statistics for a metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md")
- [Creating
  CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

## Getting notified about file operations

Storage Gateway can initiate the following CloudWatch Events when your file operations are done:

- You can get notified when the gateway finishes the asynchronous uploading of
  your files from the file share to Amazon S3. Use the `NotificationPolicy`
  parameter to request a file upload notification. This sends a notification for
  each completed file upload to Amazon S3. For more information, see [Getting file upload
  notification](#get-file-upload-notification "#get-file-upload-notification").
- You can get notified when the gateway finishes the asynchronous uploading of
  your working file set from the file share to Amazon S3. Use the [NotifyWhenUploaded](../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md "../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md") API operation to request a working file set
  upload notification. This sends a notification when all files in the working
  file set have been uploaded to Amazon S3. For more information, see [Getting working file set
  upload notification](#get-working-file-set-upload-notification "#get-working-file-set-upload-notification").
- You can get notified when the gateway finishes refreshing the cache for your
  S3 bucket. When you invoke the [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") operation through the Storage Gateway console or API,
  subscribe to the notification when the operation is complete. For more
  information, see [Getting refresh cache
  notification](#get-refresh-cache-notification "#get-refresh-cache-notification").

When the file operation you requested is done, Storage Gateway sends you a notification
through CloudWatch Events. You can configure CloudWatch Events to send the notification through event targets
such as Amazon SNS, Amazon SQS, or an AWS Lambda function. For example, you can configure an Amazon SNS
target to send the notification to Amazon SNS consumers such as an email or text message. For
information about CloudWatch Events, see [What is
CloudWatch Events?](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md")

###### To set up CloudWatch Events notification

1. Create a target, such as an Amazon SNS topic or Lambda function, to invoke when the
   event you requested in Storage Gateway occurs.
2. Create a rule in the CloudWatch Events console to invoke targets based on an event in
   Storage Gateway.
3. In the rule, create an event pattern for the event type. The notification sent
   when the event matches this rule pattern.
4. Select the target and configure the settings.

The following example shows a rule that initiates the specified event type in the
specified gateway and in the specified AWS Region. For example, you could specify the
`Storage Gateway File Upload Event` as the event type.

```
{
   "source":[
      "aws.storagegateway"
   ],
   "resources":[
      "arn:aws:storagegateway:`AWS Region`:`account-id`
                 :gateway/`gateway-id`"
   ],
   "detail-type":[
      "`Event type`"
   ]
}
```

For information about how to use CloudWatch Events rules, see
[Creating a
CloudWatch Events rule that triggers on an event](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md") in the
_Amazon CloudWatch Events User Guide_.

### Getting file upload

notification

There are two use cases in which you can use file upload notification:

- For automating in-cloud processing of files that are uploaded, you can
  call the `NotificationPolicy` parameter and get back a
  notification ID. The notification that occurs when the files have been
  uploaded has the same notification ID as the one that was returned by the
  API. If you map this notification ID to track the list of files that you are
  uploading, you can initiate processing of the file that is uploaded in AWS
  when the event with the same ID is generated.
- For content distribution use cases, you can have two S3 File Gateways that map to
  the same Amazon S3 bucket. The file share client for Gateway1 could upload new
  files to Amazon S3, and the files are read by file share clients on Gateway2. The
  files upload to Amazon S3, but they are not visible to Gateway2 because it uses a
  locally cached version of files in Amazon S3. To make the files visible in
  Gateway2, you can use the `NotificationPolicy` parameter to
  request file upload notification from Gateway1 to notify you when the upload
  file is done. You can then use CloudWatch Events to automatically issue a [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") request for the file share on Gateway2. When the
  [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") request is complete, the new file is visible in
  Gateway2.

###### Example—File upload notification

The following example shows a file upload notification that is sent to you
through CloudWatch when the event matches the rule you created. This notification is
in JSON format. You can configure this notification to be delivered to the
target as a text message. The `detail-type` is `Storage Gateway
 Object Upload Event`.

```
{
    "version": "0",
    "id": "2649b160-d59d-c97f-3f64-8aaa9ea6aed3",
    "detail-type": "Storage Gateway Object Upload Event",
    "source": "aws.storagegateway",
    "account": "123456789012",
    "time": "2020-11-05T12:34:56Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:storagegateway:us-east-1:123456789011:share/share-F123D451",
        "arn:aws:storagegateway:us-east-1:123456789011:gateway/sgw-712345DA",
        "arn:aws:s3:::do-not-delete-bucket"
    ],
    "detail": {
        "object-size": 1024,
        "modification-time": "2020-01-05T12:30:00Z",
        "object-key": "my-file.txt",
        "event-type": "object-upload-complete",
        "prefix": "prefix/",
        "bucket-name": "amzn-s3-demo-bucket",
    }
}
```

| Field names       | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| version           | The current version of the IAM policy.                                               |
| id                | The ID that identifies the IAM policy.                                               |
| detail-type       | A description of the event that initiated the notification<br>that was sent.         |
| source            | The AWS service that is the source of the request and<br>notification.               |
| account           | The ID of the AWS account where the request and<br>notification were generated from. |
| time              | When the request to upload files to Amazon S3 was<br>made.                           |
| region            | The AWS Region where the request and notification was<br>sent from.                  |
| resources         | The Storage Gateway resources that the policy applies<br>to.                         |
| object-size       | The size of the object in bytes.                                                     |
| modification-time | The time the client modified the file.                                               |
| object-key        | The path to the file.                                                                |
| event-type        | The CloudWatch Events that initiated the notification.                               |
| prefix            | The prefix name of the S3 bucket.                                                    |
| bucket-name       | The name of the S3 bucket.                                                           |

### Getting working file set

upload notification

There are two use cases in which you can use the working file set upload
notification:

- For automating in-cloud processing of files that are uploaded, you can
  call the `NotifyWhenUploaded` API and get back a notification ID.
  The notification that occurs when the working set of files have been
  uploaded has the same notification ID as the one that was returned by the
  API. If you map this notification ID to track the list of files that you are
  uploading, you can initiate processing of the working set of files that are
  uploaded in AWS when the event with the same ID is generated.
- For content distribution use cases, you can have two S3 File Gateways that map to
  the same Amazon S3 bucket. The file share client for Gateway1 can upload new
  files to Amazon S3, and the files are read by file share clients on Gateway2. The
  files upload to Amazon S3, but they aren't visible to Gateway2 because it uses a
  locally cached version of files in S3. To make the files visible in
  Gateway2, use the [NotifyWhenUploaded](../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md "../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md") API operation to request file upload
  notification from Gateway1, to notify you when the upload of the working set
  of files is done. You can then use the CloudWatch Events to automatically issue a [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") request for the file share on Gateway2. When the
  [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") request is complete, the new files are visible in
  Gateway2. This operation does not import files into the gateway cache
  storage. It only updates the cached inventory to reflect changes in the
  inventory of the objects in the S3 bucket.

###### Example—Working file set upload notification

The following example shows a working file set upload notification that is
sent to you through CloudWatch when the event matches the rule you created. This
notification is in JSON format. You can configure this notification to be
delivered to the target as a text message. The `detail-type` is
`Storage Gateway File Upload Event`.

```
{
    "version": "2012-10-17",
    "id": "2649b160-d59d-c97f-3f64-8aaa9ea6aed3",
    "detail-type": "Storage Gateway File Upload Event",
    "source": "aws.storagegateway",
    "account": "123456789012",
    "time": "2017-11-06T21:34:42Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:storagegateway:us-east-2:123456789011:share/share-F123D451",
        "arn:aws:storagegateway:us-east-2:123456789011:gateway/sgw-712345DA"
    ],
    "detail": {
        "event-type": "upload-complete",
        "notification-id": "11b3106b-a18a-4890-9d47-a1a755ef5e47",
        "request-received": "2018-02-06T21:34:42Z",
        "completed": "2018-02-06T21:34:53Z"
    }
}
```

| Field names      | Description                                                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| version          | The current version of the IAM policy.                                                                                                                                             |
| id               | The ID that identifies the IAM policy.                                                                                                                                             |
| detail-type      | A description of the event that initiated the notification<br>that was sent.                                                                                                       |
| source           | The AWS service that is the source of the request and<br>notification.                                                                                                             |
| account          | The ID of the AWS account where the request and<br>notification were generated from.                                                                                               |
| time             | When the request to upload files to Amazon S3 was<br>made.                                                                                                                         |
| region           | The AWS Region where the request and notification was<br>sent from.                                                                                                                |
| resources        | The Storage Gateway resources that the policy applies<br>to.                                                                                                                       |
| event-type       | The CloudWatch Events that initiated the notification.                                                                                                                             |
| notification-id  | The randomly generated ID of the notification that was<br>sent. This ID is in UUID format. This is the notification ID<br>that is returned when `NotifyWhenUploaded` is<br>called. |
| request-received | When the gateway received the<br>`NotifyWhenUploaded` request.                                                                                                                     |
| completed        | When all the files in the working-set were uploaded to<br>Amazon S3.                                                                                                               |

### Getting refresh cache

notification

For refresh cache notification use case, you can have two S3 File Gateways that map to
the same Amazon S3 bucket and the NFS client for Gateway1 uploads new files to the S3
bucket. The files upload to Amazon S3, but they don't appear in Gateway2 until you
refresh the cache. This is because Gateway2 uses a locally cached version of the
files in Amazon S3. You might want to do something with the files in Gateway2 when the
refresh cache is done. Large files could take a while to show up in Gateway2, so you
might want to be notified when the cache refresh is done. You can request refresh
cache notification from Gateway2 to notify you when all the files are visible in
Gateway2.

###### Example—Refresh cache notification

The following example shows a refresh cache notification that is sent to you
through CloudWatch when the event matches the rule you created. This notification is
in JSON format. You can configure this notification to be delivered to the
target as a text message. The `detail-type` is `Storage Gateway
 Refresh Cache Event`.

```
{
    "version": "2012-10-17",
    "id": "2649b160-d59d-c97f-3f64-8aaa9ea6aed3",
    "detail-type": "Storage Gateway Refresh Cache Event",
    "source": "aws.storagegateway",
    "account": "209870788375",
    "time": "2017-11-06T21:34:42Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:storagegateway:us-east-2:123456789011:share/share-F123D451",
        "arn:aws:storagegateway:us-east-2:123456789011:gateway/sgw-712345DA"
    ],
    "detail": {
        "event-type": "refresh-complete",
        "notification-id": "1c14106b-a18a-4890-9d47-a1a755ef5e47",
        "started": "2018-02-06T21:34:42Z",
        "completed": "2018-02-06T21:34:53Z",
        "folderList": [
            "/"
        ]
    }
}
```

| Field names     | Description                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| version         | The current version of the IAM policy.                                                                                                                                   |
| id              | The ID that identifies the IAM policy.                                                                                                                                   |
| detail-type     | A description of the type of the event that initiated the<br>notification that was sent.                                                                                 |
| source          | The AWS service that is the source of the request and<br>notification.                                                                                                   |
| account         | The ID of the AWS account where the request and notification<br>were generated from.                                                                                     |
| time            | When the request to refresh the files in working-set was<br>made.                                                                                                        |
| region          | The AWS Region where the request and notification was sent<br>from.                                                                                                      |
| resources       | The Storage Gateway resources that the policy applies to.                                                                                                                |
| event-type      | The CloudWatch Events that initiated the notification.                                                                                                                   |
| notification-id | The randomly generated ID of the notification that was sent.<br>This ID is in UUID format. This is the notification ID that is<br>returned when you call `RefreshCache`. |
| started         | when the gateway received the `RefreshCache` request<br>and the refresh was started.                                                                                     |
| completed       | When the refresh of the working-set was<br>completed.                                                                                                                    |
| folderList      | A comma-separated list of the paths of folders that were<br>refreshed in the cache. The default is ["/"].                                                                |

## Understanding

gateway metrics

The following table describes metrics that cover S3 File Gateways. Each
gateway has a set of metrics associated with it. Some gateway-specific metrics have the
same name as certain file-share-specific metrics. These metrics represent the same kinds
of measurements, but are scoped to the gateway rather than the file share.

Always specify whether you want to work with a gateway or a file
share when working with a particular metric. Specifically, when working with gateway
metrics, you must specify the `Gateway Name` for the gateway whose metric
data you want to view. For more information, see [Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

The following table describes the metrics that you can use to get information about
your S3 File Gateways.

| Metric                      | Description                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AuditNotifications`        | This metric reports the number of audit logs emitted.<br>Units: Count                                                                                                                                                                                                                                                                                                                |
| `AvailabilityNotifications` | This metric reports the number of availability-related health notifications that were generated by the gateway in the reporting period.<br>Units: Count                                                                                                                                                                                                                              |
| `CacheFileSize`             | This metric tracks the size of files in the gateway cache.<br>Use this metric with the `Average` statistic to measure the average size of a file in the gateway cache. Use this metric with the `Max` statistic to measure the maximum size of a file in the gateway cache.<br>Units: Bytes                                                                                          |
| `CacheFree`                 | This metric reports the number of available bytes in the gateway cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                              |
| `CacheHitPercent`           | Percent of application read operations from the gateway that are served from cache. The sample is taken at the end of the reporting period.<br>When there are no application read operations from the gateway, this metric reports 100 percent.<br>Units: Percent                                                                                                                    |
| `CachePercentDirty`         | The overall percentage of the gateway cache that has not been persisted to AWS. The sample is taken at the end of the reporting period.<br>Use this metric with the `Sum` statistic.<br>Ideally, this metric should remain low.<br>Units: Percent                                                                                                                                    |
| `CachePercentUsed`          | The percent of the data cache used across the entire gateway. The sample is taken at the end of the reporting period.<br>Units: Percent                                                                                                                                                                                                                                              |
| `CacheUsed`                 | This metric reports the number of used bytes in the gateway cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                                   |
| `CloudBytesDownloaded`      | The total number of bytes that the gateway downloaded from AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure IOPS.<br>Units: Bytes                                                                                                                                                      |
| `CloudBytesUploaded`        | The total number of bytes that the gateway uploaded to AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure input/output operations per second (IOPS).<br>Units: Bytes                                                                                                                     |
| `FilesFailingUpload`        | This metric tracks the number of files which are failing to upload to AWS. These files will generate health notifications which contain more information on the issue.<br>Use this metric with the `Sum` statistic to show the number of files which are currently failing to upload to AWS.<br>Units: Count                                                                         |
| `FileSharesUnavailable`     | This metric provides the number of file shares on this gateways which are in the \*_Unavailable_<br>• state.<br>If this metric reports any file shares are unavailable, then it is likely there is a problem with the gateway which is may cause disruption to your workflow. It is recommended to create an alarm for when this metric reports a non-zero value.<br>Units: Count    |
| `FilesRenamed`              | This metric tracks the number of files renamed in the reporting period.<br>Units: Count                                                                                                                                                                                                                                                                                              |
| `HealthNotifications`       | This metric reports the number of health notifications that were generated by this gateway in the reporting period.<br>Units: Count                                                                                                                                                                                                                                                  |
| `IndexEvictions`            | This metric reports the number of files whose metadata was evicted from the cached index of file metadata to make room for new entries. The gateway maintains this metadata index, which is populated from the AWS Cloud on demand.<br>Units: Count                                                                                                                                  |
| `IndexFetches`              | This metric reports the number of files for which metadata was fetched. The gateway maintains a cached index of file metadata, which is populated from the AWS Cloud on demand.<br>Units: Count                                                                                                                                                                                      |
| `IoWaitPercent`             | This metric reports the percentage of time that the CPU is waiting for a response from the local disk.<br>Units: Percent                                                                                                                                                                                                                                                             |
| `MemTotalBytes`             | This metric reports the total amount of memory on the gateway.<br>Units: Bytes                                                                                                                                                                                                                                                                                                       |
| `MemUsedBytes`              | This metric reports the amount of used memory on the gateway.<br>Units: Bytes                                                                                                                                                                                                                                                                                                        |
| `NfsSessions`               | This metric reports the number of NFS sessions that are active on the gateway.<br>Units: Count                                                                                                                                                                                                                                                                                       |
| `RootDiskFreeBytes`         | This metric reports the number of available bytes on the root disk of the gateway.<br>If this metric reports less than 20 GB are free, you should increase the size of the root disk.<br>To increase the root disk size, you can increase the size of existing root disk on the VM. When the VM is rebooted, gateway recognizes the increased size on the root disk.<br>Units: Bytes |
| `S3GetObjectRequestTime`    | This metric reports the time for the gateway to complete S3 get object requests.<br>Units: Milliseconds                                                                                                                                                                                                                                                                              |
| `S3PutObjectRequestTime`    | This metric reports the time for the gateway to complete S3 put object requests.<br>Units: Milliseconds                                                                                                                                                                                                                                                                              |
| `S3UploadPartRequestTime`   | This metric reports the time for the gateway to complete S3 upload part requests.<br>Units: Milliseconds                                                                                                                                                                                                                                                                             |
| `SmbV1Sessions`             | This metric reports the number of SMBv1 sessions that are active on the gateway.<br>Units: Count                                                                                                                                                                                                                                                                                     |
| `SmbV2Sessions`             | This metric reports the number of SMBv2 sessions that are active on the gateway.<br>Units: Count                                                                                                                                                                                                                                                                                     |
| `SmbV3Sessions`             | This metric reports the number of SMBv3 sessions that are active on the gateway.<br>Units: Count                                                                                                                                                                                                                                                                                     |
| `TotalCacheSize`            | This metric reports the total size of the cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                     |
| `UserCpuPercent`            | This metric reports the percentage of time that is spent on gateway processing.<br>Units: Percent                                                                                                                                                                                                                                                                                    |

## Understanding

file share metrics

You can find information following about the Storage Gateway metrics that
cover file shares. Each file share has a set of metrics associated with it. Some file
share-specific metrics have the same name as certain gateway-specific metrics. These
metrics represent the same kinds of measurements, but are scoped to the file share
instead.

Always specify whether you want to work with either a gateway or a
file share metric before working with a metric. Specifically, when working with file
share metrics, you must specify the `File share ID` that identifies the file
share for which you are interested in viewing metrics. For more information, see [Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

The following table describes the Storage Gateway metrics that you can use to get
information about your file shares.

| Metric                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CacheHitPercent`      | Percent of application read operations from the file shares that<br>are served from cache. The sample is taken at the end of the reporting<br>period.<br>When there are no application read operations from the file share,<br>this metric reports 100 percent.<br>Units: Percent                                                                                                                                                                   |
| `CachePercentDirty`    | The file share's contribution to the overall percentage of the<br>gateway's cache that has not been persisted to AWS. The<br>sample is taken at the end of the reporting period.<br>Use this metric with the `Sum` statistic.<br>Ideally, this metric should remain low.<br>NoteUse the `CachePercentDirty` metric of the gateway<br>to view the overall percentage of the gateway's cache that has<br>not been persisted to AWS.<br>Units: Percent |
| `CachePercentUsed`     | The percent of the data cache used across the entire gateway. The sample is taken at the end of the reporting<br>period. This file share-specific metric reports the same value as the corresponding gateway-specific metric.<br>Units: Percent                                                                                                                                                                                                     |
| `CloudBytesUploaded`   | The total number of bytes that the<br>gateway uploaded to AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                                                |
| `CloudBytesDownloaded` | The total number of bytes that the gateway<br>downloaded from AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure input/output operations per second (IOPS).<br>Units: Bytes                                                                                                                                                                       |
| `FilesFailingUpload`   | This metric tracks the number of files which are failing to upload to AWS. These files will generate health notifications which contain more information on the issue.<br>Use this metric with the `Sum` statistic to show the number of files which are currently failing to upload to AWS.<br>Units: Count                                                                                                                                        |
| `ReadBytes`            | The total number of bytes read from your on-premises<br>applications in the reporting period for a file share.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                            |
| `WriteBytes`           | The total number of bytes written to your on-premises<br>applications in the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                                            |

## Understanding S3 File Gateway audit

logs

Amazon S3 File Gateway (S3 File Gateway) audit logs provide you with details about
user access to files and folders within a file share. You can use them to monitor user
activities and take action if inappropriate activity patterns are identified.

**Operations**

The following table describes the S3 File Gateway audit log file access operations.

| Operation name   | Definition                                                           |
| ---------------- | -------------------------------------------------------------------- |
| Read Data        | Read the contents of a file.                                         |
| Write Data       | Change the contents of a file.                                       |
| Create           | Create a new file or folder.                                         |
| Rename           | Rename an existing file or folder.                                   |
| Delete           | Delete a file or folder.                                             |
| Write Attributes | Update file or folder metadata (ACLs, owner, group,<br>permissions). |

**Attributes**

The following table describes S3 File Gateway audit log file access
attributes.

| Attribute                              | Definition                                                                                                                                   |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `accessMode`                           | The permission setting for the object.                                                                                                       |
| `accountDomain`<br>**(SMB only)**      | The Active Directory (AD) domain that the client’s account belongs<br>to.                                                                    |
| `accountName`<br>**(SMB only)**        | The Active Directory user name of the client.                                                                                                |
| `bucket`                               | The S3 bucket name.                                                                                                                          |
| `clientGid`<br>**(NFS only)**          | The identifier of the group of the user accessing the object.                                                                                |
| `clientUid`<br>**(NFS only)**          | The identifier of the user accessing the object.                                                                                             |
| `ctime`                                | The time that the object’s content or metadata was modified, set by<br>the client.                                                           |
| `groupId`                              | The identifier for group owner of the object.                                                                                                |
| `fileSizeInBytes`                      | The size of the file in bytes, set by the client at file creation<br>time.                                                                   |
| `gateway`                              | The Storage Gateway ID.                                                                                                                      |
| `mtime`                                | This time that the object's content was modified, set by the<br>client.                                                                      |
| `newObjectName`                        | The full path to the new object after it has been renamed.                                                                                   |
| `objectName`                           | The full path to the object.                                                                                                                 |
| `objectType`                           | Defines whether the object is a file or folder.                                                                                              |
| `operation`                            | The name of the object access operation.                                                                                                     |
| `ownerId`                              | The identifier for the owner of the object.                                                                                                  |
| `securityDescriptor`<br>**(SMB only)** | Shows the discretionary access control list (DACL) set on an object,<br>in SDDL format.                                                      |
| `shareName`                            | The name of the share that is being accessed.                                                                                                |
| `source`                               | The ID of the file share being audited.                                                                                                      |
| `sourceAddress`                        | The IP address of file share client machine.                                                                                                 |
| `status`                               | The status of the operation. Only success is logged (failures are<br>logged with the exception of failures arising from permissions denied). |
| `timestamp`                            | The time that the operation occurred based on the OS timestamp of the<br>gateway.                                                            |
| `version`                              | The version of the audit log format.                                                                                                         |

**Attributes logged per operation**

The following table describes the S3 File Gateway audit log attributes
logged in each file access operation.

|                                        | Read data | Write data | Create folder | Create file | Rename file/folder | Delete file/folder | Write attributes (change ACL<br>• **SMB only**) | Write attributes (chown) | Write attributes (chmod) | Write attributes (chgrp) |
| -------------------------------------- | --------- | ---------- | ------------- | ----------- | ------------------ | ------------------ | ----------------------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| `accessMode`                           |           |            | X             | X           |                    |                    |                                                 |                          | X                        |                          |
| `accountDomain`<br>**(SMB only)**      | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `accountName`<br>**(SMB only)**        | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `bucket`                               | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `clientGid`<br>**(NFS only)**          | X         | X          | X             | X           | X                  | X                  |                                                 | X                        | X                        | X                        |
| `clientUid`<br>**(NFS only)**          | X         | X          | X             | X           | X                  | X                  |                                                 | X                        | X                        | X                        |
| `ctime`                                |           |            | X             | X           |                    |                    |                                                 |                          |                          |                          |
| `groupId`                              |           |            | X             | X           |                    |                    |                                                 |                          |                          |                          |
| `fileSizeInBytes`                      |           |            |               | X           |                    |                    |                                                 |                          |                          |                          |
| `gateway`                              | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `mtime`                                |           |            | X             | X           |                    |                    |                                                 |                          |                          |                          |
| `newObjectName`                        |           |            |               |             | X                  |                    |                                                 |                          |                          |                          |
| `objectName`                           | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `objectType`                           | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `operation`                            | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `ownerId`                              |           |            | X             | X           |                    |                    |                                                 | X                        |                          |                          |
| `securityDescriptor`<br>**(SMB only)** |           |            |               |             |                    |                    | X                                               | X                        |                          |                          |
| `shareName`                            | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `source`                               | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `sourceAddress`                        | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `status`                               | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `timestamp`                            | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
| `version`                              | X         | X          | X             | X           | X                  | X                  | X                                               | X                        | X                        | X                        |
