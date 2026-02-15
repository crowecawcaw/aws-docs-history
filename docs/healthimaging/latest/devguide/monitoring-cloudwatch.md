# Using Amazon CloudWatch with HealthImaging

You can monitor AWS HealthImaging using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so you can use that
historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

HealthImaging publishes the following types of metrics to CloudWatch, in the `AWS/HealthImaging` namespace:

- **API metrics** - Call counts for HealthImaging API operations
- **HealthImaging metrics** - Data store and account-level resource usage

###### Note

- Metrics are reported for most HealthImaging APIs.
- HealthImaging metrics are only available for data stores created after February 9, 2026, or by filing a
  [support Case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

## AWS HealthImaging API Metrics

The following tables list the metrics and dimensions for HealthImaging. Each is presented as a
frequency count for a user-specified data range.

| Metric      | Metrics                                                                                                                                                                                                         | Description |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `CallCount` | The number of calls to APIs. This can be reported either for the account or a<br>specified data store.<br>Units: Count<br>Valid Statistics: Sum, Count<br>Dimensions: Operation, data store ID, data store type |

You can get metrics for HealthImaging with the AWS Management Console, the AWS CLI, or the CloudWatch API. You can use
the CloudWatch API through one of the Amazon AWS Software Development Kits (SDKs) or the CloudWatch API
tools. The HealthImaging console displays graphs based on the raw data from the CloudWatch API.

You must have the appropriate CloudWatch permissions to monitor HealthImaging with CloudWatch. For more
information, see [Identity and access
management for CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _CloudWatch User Guide_.

## AWS HealthImaging Metrics

The `AWS/HealthImaging` namespace includes the following metrics at the account and data store levels.

### Account-Level Metrics

Account-level metrics provide aggregated visibility across all data stores in your account.

| Account-Level Metrics | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `DataStoreCount`      | The number of data stores with active status.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ImageSetCount`       | The total number of image sets across all data stores.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `StorageBytes`        | The amount of data in bytes stored across all data stores in the following storage tiers:<br>• Frequent Access `(FrequentAccessStorage)`<br>• Archive Instant Access `(ArchiveInstantAccessStorage)`<br>This value is calculated by summing the size of all image sets in all data stores.<br>Valid storage-tier filters (See the [StorageTier](#dimensions-cloudwatch "#dimensions-cloudwatch") dimension):<br>• `FrequentAccessStorage`<br>• `ArchiveInstantAccessStorage`<br>• `AllStorage`<br>Units: Bytes<br>Valid statistics: Sum, Average |

### Data Store-Level Metrics

Data store-level metrics provide detailed visibility into individual data store.

| Data Store-Level Metrics | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `TotalImageSetCount`     | The total number of image sets in the data store.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `PrimaryImageSetCount`   | The number of primary image sets in the datastore.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SmallImageSetCount`     | The number of image sets less than 5MB in the datastore.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `StorageBytes`           | The amount of data in bytes stored across all data stores in the following storage tiers:<br>• Frequent Access `(FrequentAccessStorage)`<br>• Archive Instant Access `(ArchiveInstantAccessStorage)`<br>This value is calculated by summing the size of all image sets in the data store.<br>Valid storage-tier filters (See the [StorageTier](#dimensions-cloudwatch "#dimensions-cloudwatch") dimension):<br>• FrequentAccessStorage<br>• ArchiveInstantAccessStorage<br>• AllStorage<br>Units: Bytes<br>Valid statistics: Sum, Average |
| `DICOMStudyCount`        | The number of DICOM studies in the datastore.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `DICOMSeriesCount`       | The number of DICOM series in the datastore.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `DICOMInstanceCount`     | The number of DICOM instances in the datastore.<br>Units: Count<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `StructuredStorageBytes` | The amount of structured storage in bytes indexed by the data store.<br>Units: Bytes<br>Valid statistics: Sum, Average                                                                                                                                                                                                                                                                                                                                                                                                                    |

## HealthImaging Dimensions in CloudWatch

The following dimensions are used to filter HealthImaging metrics.

| Dimensions    | Dimension                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `AccountId`   | This dimension filters the data for the identified AWS account.                                                                                                                                                                                                                                                                                            |
| `DatastoreId` | This dimension filters the data for the identified data store only.                                                                                                                                                                                                                                                                                        |
| `StorageTier` | This dimension filters the data by the following storage tiers:<br>• `FrequentAccessStorage` – The number of bytes used for image sets in Frequent Access storage.<br>• `ArchiveInstantAccessStorage` – The number of bytes used for image sets in Archive Instant Access storage.<br>• `AllStorage` – The total number of bytes across all storage tiers. |

## Accessing HealthImaging Metrics

You can access HealthImaging metrics using:

- **AWS Management Console** - View metrics in the CloudWatch console
- **AWS CLI** - Use CloudWatch CLI commands
- **CloudWatch API** - Access through AWS SDKs or CloudWatch
  API tools

You must have the appropriate permissions to monitor HealthImaging with CloudWatch. For more
information, see [Identity and access
management for CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _CloudWatch User Guide_.

## Setting Up HealthImaging Metrics

To receive HealthImaging metrics in your CloudWatch account, you need to create a service-linked role
that allows HealthImaging to publish metrics on your behalf. See [Using service-linked
roles for HealthImaging](security-iam-service-linked-roles.md "security-iam-service-linked-roles.md") for details on how to create a service-linked role.

## Viewing HealthImaging Metrics

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Metrics**, choose **All Metrics**, and then
   choose **`AWS/HealthImaging`**.
3. Choose the dimension:
   - **By Account Id** - View account-level metrics
   - **By Datastore Id** - View data store-level metrics

4. Choose a metric name, then choose **Add to graph**.
5. Choose a value for the date range, and the metric count will be displayed.

## Creating an alarm using CloudWatch

A CloudWatch alarm watches a single metric over a specified time period, and performs one or
more actions: sending a notification to an Amazon Simple Notification Service (Amazon SNS) topic or Auto Scaling policy. The
action or actions are based on the value of the metric relative to a given threshold over a
number of time periods that you specify. CloudWatch can also send you an Amazon SNS message when the
alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has persisted for the period
you specify. For more information, see [Using CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").
