# Working with the Delivery Channel

As AWS Config continually records the changes that occur to your AWS resources, it sends
notifications and updated configuration states through the _delivery
channel_. You can manage the delivery channel to control where AWS Config sends
configuration updates.

###### Topics

- [Considerations](#dc-considerations "#dc-considerations")
- [Terminology](#dc-terminology "#dc-terminology")
- [Components of a Configuration Item](config-item-table.md "config-item-table.md")
- [Viewing the Delivery Channel](dc-view.md "dc-view.md")
- [Updating the Delivery Channel](update-dc-console.md "update-dc-console.md")
- [Renaming the Delivery Channel](update-dc-rename.md "update-dc-rename.md")
- [Delivering Configuration Snapshots](deliver-snapshot-cli.md "deliver-snapshot-cli.md")
- [Verifying Delivery Status](verify-delivery-status.md "verify-delivery-status.md")
- [Viewing Configuration Snapshots](view-configuration-snapshot.md "view-configuration-snapshot.md")
- [Example Configuration Snapshot](example-s3-snapshot.md "example-s3-snapshot.md")
- [Example Notifications](notifications-for-AWS-Config.md "notifications-for-AWS-Config.md")

## Considerations

**One delivery channel per Region per account**

You can have only one delivery channel per AWS Region region per AWS account, and
the delivery channel is required to use AWS Config.

**Oversized configuration item notifications include a brief
summary**

When AWS Config detects a configuration change for a resource and the notification exceeds
the maximum size allowed by Amazon SNS, the notification includes a brief summary of the
configuration item. You can view the complete notification in the Amazon S3 bucket location
specified in the `s3BucketLocation` field. For more information, see [Example Oversized
Configuration Item Change Notification](oversized-notification-example.md "oversized-notification-example.md").

**AWS Config supports AWS KMS encryption for Amazon S3 buckets used by
AWS Config**

You can provide an AWS Key Management Service (AWS KMS) key or alias Amazon Resource Name (ARN) to
encrypt the data delivered to your Amazon Simple Storage Service (Amazon S3) bucket. By default, AWS Config delivers
configuration history and snapshot files to your Amazon S3 bucket and encrypts the data at
rest using S3 AES-256 server-side encryption, SSE-S3. However, if you provide AWS Config with
your KMS key or alias ARN, AWS Config uses that KMS key instead of AES-256
encryption.

AWS Config does not support the delivery channel to an Amazon S3 bucket where object lock is
enabled with default retention enabled. For more information, see [How S3 Object Lock works](../../../AmazonS3/latest/userguide/object-lock-overview.md "../../../AmazonS3/latest/userguide/object-lock-overview.md").

## Terminology

A _configuration item_ represents a point-in-time view of the
various attributes of a supported AWS resource that exists in your account. The
components of a configuration item include metadata, attributes, relationships, current
configuration, and related events. AWS Config creates a configuration item whenever it
detects a change to a resource type that it is recording. For example, if AWS Config is
recording Amazon S3 buckets, AWS Config creates a configuration item whenever a bucket is
created, updated, or deleted. You can also select for AWS Config to create a configuration
item at the recording frequency that you set.

A _configuration history_ is a collection of the configuration
items for a given resource over any time period. A configuration history can help you
answer questions about, for example, when the resource was first created, how the
resource has been configured over the last month, and what configuration changes were
introduced yesterday at 9 AM. The configuration history is available to you in multiple
formats. AWS Config automatically delivers a configuration history file for each resource type
that is being recorded to an Amazon S3 bucket that you specify. You can select a given
resource in the AWS Config console and navigate to all previous configuration items for that
resource using the timeline. Additionally, you can access the historical configuration
items for a resource from the API.

A _configuration snapshot_ is a collection of the configuration
items for the supported resources that exist in your account. This configuration
snapshot is a complete picture of the resources that are being recorded and their
configurations. The configuration snapshot can be a useful tool for validating your
configuration. For example, you may want to examine the configuration snapshot regularly
for resources that are configured incorrectly or that potentially should not exist. The
configuration snapshot is available in multiple formats. You can have the configuration
snapshot delivered to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. Additionally, you can
select a point in time in the AWS Config console and navigate through the snapshot of
configuration items using the relationships between the resources.

A _configuration stream_ is an automatically updated list of all
configuration items for the resources that AWS Config is recording. Every time a resource is
created, modified, or deleted, AWS Config creates a configuration item and adds to the
configuration stream. The configuration stream works by using an Amazon Simple Notification Service (Amazon SNS) topic
of your choice. The configuration stream is helpful for observing configuration changes
as they occur so that you can spot potential problems, generating notifications if
certain resources are changed, or updating external systems that need to reflect the
configuration of your AWS resources.
