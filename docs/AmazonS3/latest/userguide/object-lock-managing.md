

# Object Lock considerations
<a name="object-lock-managing"></a>

Amazon S3 Object Lock can help prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely.

You can use the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API to view or set Object Lock information. For general information about S3 Object Lock capabilities, see [Locking objects with Object Lock](object-lock.md).

**Important**  
After you enable Object Lock on a bucket, you can't disable Object Lock or suspend versioning for that bucket. 
S3 buckets with Object Lock can't be used as destination buckets for server access logs. For more information, see [Logging requests with server access logging](ServerLogs.md).

**Topics**
+ [Permissions for viewing lock information](#object-lock-managing-view)
+ [Bypassing governance mode](#object-lock-managing-bypass)
+ [Using Object Lock with S3 Replication](#object-lock-managing-replication)
+ [Using Object Lock with encryption](#object-lock-managing-encryption)
+ [Using Object Lock with Amazon S3 Inventory](#object-lock-inv-report)
+ [Managing S3 Lifecycle policies with Object Lock](#object-lock-managing-lifecycle)
+ [Managing delete markers with Object Lock](#object-lock-managing-delete-markers)
+ [Using S3 Storage Lens with Object Lock](#object-lock-storage-lens)
+ [Uploading objects to an Object Lock enabled bucket](#object-lock-put-object)
+ [Configuring events and notifications](#object-lock-managing-events)
+ [Setting limits on retention periods with a bucket policy](#object-lock-managing-retention-limits)
+ [Troubleshooting variable retention](#object-lock-managing-variable-retention-troubleshooting)

## Permissions for viewing lock information
<a name="object-lock-managing-view"></a>

You can programmatically view the Object Lock status of an Amazon S3 object version by using the [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) or [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) operations. Both operations return the retention mode, retain until date, and legal hold status for the specified object version. Additionally, you can view the Object Lock status for multiple objects in your S3 bucket using S3 Inventory. 

To view an object version's retention mode and retention period, you must have the `s3:GetObjectRetention` permission. To view an object version's legal hold status, you must have the `s3:GetObjectLegalHold` permission. To view a bucket's default retention configuration, you must have the `s3:GetBucketObjectLockConfiguration` permission. If you make a request for an Object Lock configuration on a bucket that doesn't have S3 Object Lock enabled, Amazon S3 returns an error. For information about setting a bucket default, see [Configuring S3 Object Lock](object-lock-configure.md).

## Bypassing governance mode
<a name="object-lock-managing-bypass"></a>

If you have the `s3:BypassGovernanceRetention` permission, you can perform operations on object versions that are locked in governance mode as if they were unprotected. These operations include deleting an object version, shortening the retention period, or removing the Object Lock retention period by placing a new `PutObjectRetention` request with empty parameters. 

To bypass governance mode, you must explicitly indicate in your request that you want to bypass this mode. To do this, include the `x-amz-bypass-governance-retention:true` header with your `PutObjectRetention` API operation request, or use the equivalent parameter with requests made through the AWS CLI or AWS SDKs. The S3 console automatically applies this header for requests made through the S3 console if you have the `s3:BypassGovernanceRetention` permission.

**Note**  
Bypassing governance mode doesn't affect an object version's legal hold status. If an object version has a legal hold enabled, the legal hold remains and prevents requests to overwrite or delete the object version.

## Using Object Lock with S3 Replication
<a name="object-lock-managing-replication"></a>

You can use Object Lock with S3 Replication to enable automatic, asynchronous copying of locked objects and their retention metadata, across S3 buckets. This means that for replicated objects, Amazon S3 takes the object lock configuration of the source bucket. In other words, if the source bucket has Object Lock enabled, the destination buckets must also have Object Lock enabled. If an object is directly uploaded to the destination bucket (outside of S3 Replication), it takes the Object Lock set on the destination bucket. When you use replication, objects in a *source bucket* are replicated to one or more *destination buckets*. 

To set up replication on a bucket with Object Lock enabled, you can use the S3 console, AWS CLI, Amazon S3 REST API, or AWS SDKs.

**Note**  
To use Object Lock with replication, you must grant two additional permissions on the source S3 bucket in the AWS Identity and Access Management (IAM) role that you use to set up replication. The two additional permissions are `s3:GetObjectRetention` and `s3:GetObjectLegalHold`. If the role has an `s3:Get*` permission statement, that statement satisfies the requirement. For more information, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md).  
For general information about S3 Replication, see [Replicating objects within and across Regions](replication.md).  
For examples of setting up S3 Replication, see [Examples for configuring live replication](replication-example-walkthroughs.md).

Amazon S3 replicates variable retention settings—event hold and event hold duration—along with other Object Lock metadata. Both source and destination buckets must have Object Lock enabled. When an event hold is released on the source, Amazon S3 replicates the release to the destination, and the destination sets its own final retain-until-date based on the configured duration and the time of replication.

## Using Object Lock with encryption
<a name="object-lock-managing-encryption"></a>

Amazon S3 encrypts all new objects by default. You can use Object Lock with your encrypted objects. For more information, see [Protecting data with encryption](UsingEncryption.md).

While Object Lock can help prevent Amazon S3 objects from being deleted or overwritten, it does not protect against losing access to the encryption keys or encryption keys being deleted. For example, if you encrypt your objects with AWS KMS server-side encryption and your AWS KMS key is deleted your objects may become unreadable.

## Using Object Lock with Amazon S3 Inventory
<a name="object-lock-inv-report"></a>

You can configure Amazon S3 Inventory to create lists of the objects in an S3 bucket on a defined schedule. You can configure Amazon S3 Inventory to include the following Object Lock metadata for your objects:
+ The retain until date
+ The retention mode
+ The legal hold status
+ The event hold status
+ The event hold duration

While an event hold is on, the `GetObjectRetention`, `HeadObject`, and `GetObject` operations return the computed retain-until-date. If you specified a retain-until-date, the returned value is not earlier than that date.

For objects with an active event hold, Amazon S3 Inventory reports a dynamic retain-until-date based on when Amazon S3 generates the report. For objects with a released event hold or fixed retention, the retain-until-date is fixed. Inventory reports can take up to 48 hours to generate. Therefore, the retain-until-date reflects the report generation time, not the current time. For the most current value, query the object's retention metadata directly by using `GetObjectRetention`.

For more information, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md).

## Managing S3 Lifecycle policies with Object Lock
<a name="object-lock-managing-lifecycle"></a>

Object lifecycle management configurations continue to function normally on protected objects, including placing delete markers. However, a locked version of an object cannot be deleted by a S3 Lifecycle expiration policy. Object Lock is maintained regardless of which storage class the object resides in and throughout S3 Lifecycle transitions between storage classes.

For more information about managing object lifecycles, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md).

## Managing delete markers with Object Lock
<a name="object-lock-managing-delete-markers"></a>

Although you can't delete a protected object version, you can still create a delete marker for that object. Placing a delete marker on an object doesn't delete the object or its object versions. However, it makes Amazon S3 behave in most ways as though the object has been deleted. For more information, see [Working with delete markers](DeleteMarker.md).

**Note**  
Delete markers are not WORM-protected, regardless of any retention period or legal hold in place on the underlying object.

## Using S3 Storage Lens with Object Lock
<a name="object-lock-storage-lens"></a>

To see metrics for Object Lock-enabled storage bytes and object count, you can use Amazon S3 Storage Lens. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity.

For more information, see [Using S3 Storage Lens to protect your data](storage-lens-data-protection.md).

For a complete list of metrics, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md).

## Uploading objects to an Object Lock enabled bucket
<a name="object-lock-put-object"></a>

The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is required for any request to upload an object with a retention period configured using Object Lock. Theses headers are a way to verify the integrity of your object during upload.

When uploading an object with the Amazon S3 console, S3 automatically adds the `Content-MD5` header. You can optionally specify an additional checksum function and checksum value through the console as the `x-amz-sdk-checksum-algorithm` header. If you use the [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) API you must specify the `Content-MD5` header, the `x-amz-sdk-checksum-algorithm` header, or both to configure the Object Lock retention period.

For more information, see [Checking object integrity in Amazon S3](checking-object-integrity.md).

## Configuring events and notifications
<a name="object-lock-managing-events"></a>

You can use Amazon S3 Event Notifications to track access and changes to your Object Lock configurations and data by using AWS CloudTrail. For information about CloudTrail, see [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) in the *AWS CloudTrail User Guide*.

You can also use Amazon CloudWatch to generate alerts based on this data. For information about CloudWatch, see the [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

Amazon S3 publishes an `s3:ObjectRetention:Put` event notification for explicit `PutObjectRetention` calls. This includes setting fixed or variable retention, releasing an event hold, modifying the duration, and extending a retain-until-date.

## Setting limits on retention periods with a bucket policy
<a name="object-lock-managing-retention-limits"></a>

You can set minimum and maximum allowable retention periods for a bucket by using a bucket policy. The maximum retention period is 100 years.

The following example shows a bucket policy that uses the `s3:object-lock-remaining-retention-days` condition key to set a maximum retention period of 10 days.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "{{SetRetentionLimits}}",
    "Statement": [
        {
            "Sid": "{{SetRetentionPeriod}}",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "s3:PutObjectRetention"
            ],
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket1}}/*",
            "Condition": {
                "NumericGreaterThan": {
                    "s3:object-lock-remaining-retention-days": "10"
                }
            }
        }
    ]
}
```

------

**Note**  
If your bucket is the destination bucket for a replication configuration, you can set up minimum and maximum allowable retention periods for object replicas that are created by using replication. To do so, you must allow the `s3:ReplicateObject` action in your bucket policy. For more information about replication permissions, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md). 

For variable retention, you can control event holds and durations with the following condition keys. Amazon S3 evaluates these keys against the values in a request. They don't apply to an event hold or duration that Amazon S3 applies from a bucket's default retention configuration. For more information, see [Set or modify a default variable retention period on an S3 bucket](object-lock-configure.md#object-lock-configure-set-variable-retention-bucket). To restrict bucket defaults, deny the `s3:PutBucketObjectLockConfiguration` action.
+ <a name="object-lock-managing-condition-event-hold"></a>`s3:object-lock-event-hold` – Restricts who can set or release event holds. Values: `ON`, `OFF`.
+ <a name="object-lock-managing-condition-event-hold-duration-days"></a>`s3:object-lock-event-hold-duration-days` – Lets you enforce a minimum or maximum event hold duration, in days.

The following example denies any `PutObjectRetention` request that sets an event hold duration of less than 90 days:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequireMinimumEventHoldDuration",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObjectRetention",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
            "Condition": {
                "NumericLessThan": {
                    "s3:object-lock-event-hold-duration-days": "90"
                }
            }
        }
    ]
}
```

The following example denies any request that sets an event hold on this bucket:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyEventHolds",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectRetention"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
            "Condition": {
                "StringEquals": {
                    "s3:object-lock-event-hold": "ON"
                }
            }
        }
    ]
}
```

**Note**  
A bucket policy that uses the `s3:object-lock-remaining-retention-days` condition key denies a `PutObjectRetention` request when the retention period that you specify exceeds your limit. While an event hold is active, Amazon S3 recalculates the retain-until-date on the service side. The date can move past a limit that the policy enforces at request time. If you don't want this behavior, also restrict the `s3:object-lock-event-hold` condition key to control who can enable event holds.

For more information about bucket policies, see the following topics:
+ [ Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html) in the *Service Authorization Reference*

  For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md).
+ [Object operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects)
+ [Bucket policy examples using condition keys](amazon-s3-policy-keys.md)

## Troubleshooting variable retention
<a name="object-lock-managing-variable-retention-troubleshooting"></a>

Use the following information to diagnose and resolve common issues with variable retention and event holds.

### Request that sets an event hold is rejected
<a name="object-lock-troubleshooting-request-rejected"></a>

A request that sets or modifies an event hold fails with a `400 Bad Request` response.

Common causes and actions:
+ **No retention mode** – An event hold requires a retention mode. Specify either `GOVERNANCE` or `COMPLIANCE`.
+ **Missing or duplicate duration** – An event hold that is set to `ON` requires exactly one event hold duration. Specify the duration in either days or years, but not both.
+ **Duration specified with an event hold that is set to OFF** – Don't specify an event hold duration when you release an event hold. Amazon S3 computes the final retain-until-date from the duration that is already configured on the object version.
+ **No retain-until-date with an event hold that is set to OFF** – When the event hold is off, the object version must have a retain-until-date. Amazon S3 sets this date in one of two ways. It computes the date when you release an active event hold (a transition from `ON` to `OFF`). Or, you provide an explicit retain-until-date, which is fixed retention. To protect an object with variable retention, create it with the event hold set to `ON` and a duration.
+ **Duration outside the allowed range** – An event hold duration must be a positive integer, up to a maximum of 36,500 days or 100 years.

### Bucket policy doesn't match a duration that is set in years
<a name="object-lock-troubleshooting-years-condition-key"></a>

There is no years-based condition key. When you set a duration in years, Amazon S3 converts it to days for evaluation against the `s3:object-lock-event-hold-duration-days` condition key. Amazon S3 counts 1 year as 365 days and doesn't count leap years. Express the limits in your bucket policy in days, and account for this conversion. For example, Amazon S3 evaluates a duration of 1 year as 365 days.

### Amazon S3 Inventory report shows an outdated retain-until-date
<a name="object-lock-troubleshooting-inventory-stale"></a>

While an event hold is active, Amazon S3 dynamically computes the retain-until-date. Amazon S3 Inventory reports are generated periodically and can be up to 48 hours old. As a result, a report might not show the current computed retain-until-date. For the current value, use `GetObjectRetention` or `HeadObject`.