# Viewing the properties for an S3 general purpose bucket

You can view properties for any Amazon S3 bucket you own. These settings include the following:


* **Bucket Versioning** – Keep multiple versions of an object
 in one general purpose bucket by using versioning. By default, versioning is disabled for a new bucket.
 For information about enabling versioning, see [Enabling versioning on buckets](manage-versioning-examples.md "manage-versioning-examples.md").
* **Tags** – With AWS cost allocation, you can use bucket tags to
 annotate billing for your use of a general purpose bucket. A tag is a key-value pair that represents a label
 that you assign to a bucket. For more information, see [Using cost allocation S3 bucket tags](CostAllocTagging.md "CostAllocTagging.md").
* **Default encryption** – Enabling default encryption provides
 you with automatic server-side encryption. Amazon S3 encrypts an object before saving it to a
 disk and decrypts the object when you download it. For more information, see [Setting default server-side encryption behavior for Amazon S3
 buckets](bucket-encryption.md "bucket-encryption.md").
* **Server access logging** – Get detailed records for the
 requests that are made to your general purpose bucket with server access logging. By default, Amazon S3
 doesn't collect server access logs. For information about enabling server access
 logging, see [Enabling Amazon S3 server access logging](enable-server-access-logging.md "enable-server-access-logging.md").
* **AWS CloudTrail data events** – Use CloudTrail to log data events. By
 default, trails don't log data events. Additional charges apply for data events. For
 more information, see [Logging
 Data Events for Trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html") in the *AWS CloudTrail User Guide*.
* **Event notifications** – Enable certain Amazon S3 general purpose bucket events to
 send notification messages to a destination whenever the events occur. For more information,
 see [Enabling and configuring event notifications using the Amazon S3 console](enable-event-notifications.md "enable-event-notifications.md").
* **Transfer acceleration** – Enable fast, easy, and secure
 transfers of files over long distances between your client and an S3 bucket. For
 information about enabling transfer acceleration, see [Enabling and using S3 Transfer Acceleration](transfer-acceleration-examples.md "transfer-acceleration-examples.md").
* **Object Lock** – Use S3 Object Lock to prevent an object
 from being deleted or overwritten for a fixed amount of time or indefinitely. For more
 information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
* **Requester Pays** – Enable Requester Pays if you want the
 requester (instead of the general purpose bucket owner) to pay for requests and data transfers. For more
 information, see [Using Requester Pays general purpose buckets for storage
 transfers and usage](RequesterPaysBuckets.md "RequesterPaysBuckets.md").
* **Static website hosting** – You can host a static website on
 Amazon S3. For more information, see [Hosting a static website using Amazon S3](WebsiteHosting.md "WebsiteHosting.md").
You can view bucket properties using the AWS Management Console, AWS CLI, or AWS SDKs

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you want to
 view the properties for.
4. Choose the **Properties** tab.
5. On the **Properties** page, you can configure the above properties
 for the bucket.

###### View bucket properties with the AWS CLI


The following commands show how you can use the AWS CLI to list different general purpose bucket
 properties.
 


The following returns the tag set associated with the bucket `amzn-s3-demo-bucket1`. For more
 information about bucket tags see, [Using cost allocation S3 bucket tags](CostAllocTagging.md "CostAllocTagging.md").


```
aws s3api get-bucket-tagging --bucket `amzn-s3-demo-bucket1`
```
For more information and examples, see [get-bucket-tagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html") in the
 *AWS CLI Command Reference*.

The following returns the versioning state of the bucket `amzn-s3-demo-bucket1`. For
 information about the bucket versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").


```
aws s3api get-bucket-versioning --bucket `amzn-s3-demo-bucket1`
```
For more information and examples, see [get-bucket-versioning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-versioning.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-versioning.html") in the
 *AWS CLI Command Reference*.

The following returns the default encryption configuration for the bucket
 `amzn-s3-demo-bucket1`. By default, all buckets have a default encryption configuration that
 uses server-side encryption with Amazon S3 managed keys (SSE-S3). For information about the
 bucket default encryption, see [Setting default server-side encryption behavior for Amazon S3
 buckets](bucket-encryption.md "bucket-encryption.md").


```
aws s3api get-bucket-encryption --bucket `amzn-s3-demo-bucket1`
```
For more information and examples, see [get-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html") in the
 *AWS CLI Command Reference*.

The following returns the notification configuration of the bucket `amzn-s3-demo-bucket1`.
 For information about the bucket event notifications, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").


```
aws s3api get-bucket-notification-configuration --bucket `amzn-s3-demo-bucket1`
```
For more information and examples, see [get-bucket-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification-configuration.html") in the
 *AWS CLI Command Reference*.

The following returns the logging status for the bucket `amzn-s3-demo-bucket1`. For
 information about the bucket logging, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").


```
aws s3api get-bucket-logging --bucket `amzn-s3-demo-bucket1`
```
For more information and examples, see [get-bucket-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html") in the
 *AWS CLI Command Reference*.

For examples of how to return general purpose bucket properties with the AWS SDKs, such as versioning,
 tags, and more, see [Code examples](../API/s3_example_s3_ListBuckets_section.md "../API/s3_example_s3_ListBuckets_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.
