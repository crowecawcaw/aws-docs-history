# Object Lock considerations

Amazon S3 Object Lock can help prevent objects from being deleted or overwritten for a fixed
 amount of time or indefinitely.

You can use the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API to view or
 set Object Lock information. For general information about S3 Object Lock capabilities,
 see [Locking objects with Object Lock](object-lock.md "object-lock.md").

###### Important


* After you enable Object Lock on a bucket, you can't disable Object Lock or
 suspend versioning for that bucket.
* S3 buckets with Object Lock can't be used as destination buckets for server
 access logs. For more information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").
###### Topics

* [Permissions for viewing lock
 information](#object-lock-managing-view "#object-lock-managing-view")
* [Bypassing governance mode](#object-lock-managing-bypass "#object-lock-managing-bypass")
* [Using Object Lock with
 S3 Replication](#object-lock-managing-replication "#object-lock-managing-replication")
* [Using Object Lock with encryption](#object-lock-managing-encryption "#object-lock-managing-encryption")
* [Using Object Lock with Amazon S3 Inventory](#object-lock-inv-report "#object-lock-inv-report")
* [Managing S3 Lifecycle policies with
 Object Lock](#object-lock-managing-lifecycle "#object-lock-managing-lifecycle")
* [Managing delete markers with Object Lock](#object-lock-managing-delete-markers "#object-lock-managing-delete-markers")
* [Using S3 Storage Lens with Object Lock](#object-lock-storage-lens "#object-lock-storage-lens")
* [Uploading objects to an Object Lock enabled
 bucket](#object-lock-put-object "#object-lock-put-object")
* [Configuring events and
 notifications](#object-lock-managing-events "#object-lock-managing-events")
* [Setting limits on retention
 periods with a bucket policy](#object-lock-managing-retention-limits "#object-lock-managing-retention-limits")

## Permissions for viewing lock
 information


You can programmatically view the Object Lock status of an Amazon S3 object version by
 using the [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") or [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
 operations. Both operations return the retention mode, retain until date, and legal hold
 status for the specified object version. Additionally, you can view the Object Lock
 status for multiple objects in your S3 bucket using S3 Inventory. 


To view an object version's retention mode and retention period, you must have the
 `s3:GetObjectRetention` permission. To view an object version's legal
 hold status, you must have the `s3:GetObjectLegalHold` permission. To view a
 bucket's default retention configuration, you must have the
 `s3:GetBucketObjectLockConfiguration` permission. If you make a request
 for an Object Lock configuration on a bucket that doesn't have S3 Object Lock
 enabled, Amazon S3 returns an error. 


## Bypassing governance mode


If you have the `s3:BypassGovernanceRetention` permission, you can perform
 operations on object versions that are locked in governance mode as if they were
 unprotected. These operations include deleting an object version, shortening the
 retention period, or removing the Object Lock retention period by placing a new
 `PutObjectRetention` request with empty parameters. 


To bypass governance mode, you must explicitly indicate in your request that you want
 to bypass this mode. To do this, include the
 `x-amz-bypass-governance-retention:true` header with your
 `PutObjectRetention` API operation request, or use the equivalent
 parameter with requests made through the AWS CLI or AWS SDKs. The S3 console
 automatically applies this header for requests made through the S3 console if you have
 the `s3:BypassGovernanceRetention` permission.


###### Note

Bypassing governance mode doesn't affect an object version's legal hold status. If
 an object version has a legal hold enabled, the legal hold remains and prevents
 requests to overwrite or delete the object version.


## Using Object Lock with
 S3 Replication


You can use Object Lock with S3 Replication to enable automatic, asynchronous
 copying of locked objects and their retention metadata, across S3 buckets. This means
 that for replicated objects, Amazon S3 takes the object lock configuration of the source
 bucket. In other words, if the source bucket has Object Lock
 enabled, the destination buckets must also have Object Lock enabled. If an object is directly uploaded to the destination bucket (outside of
 S3 Replication), it takes the Object Lock set on the destination bucket. When you use
 replication, objects in a *source bucket* are replicated to one or
 more *destination buckets*. 


To set up replication on a bucket with Object Lock enabled, you can use the S3
 console, AWS CLI, Amazon S3 REST API, or AWS SDKs.


###### Note

To use Object Lock with replication, you must grant two additional permissions on
 the source S3 bucket in the AWS Identity and Access Management (IAM) role that you use to set up
 replication. The two additional permissions are `s3:GetObjectRetention`
 and `s3:GetObjectLegalHold`. If the role has an `s3:Get*`
 permission statement, that statement satisfies the requirement. For more
 information, see [Setting up permissions for live
 replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").

For general information about S3 Replication, see [Replicating objects within and across Regions](replication.md "replication.md").

For examples of setting up S3 Replication, see [Examples for configuring live replication](replication-example-walkthroughs.md "replication-example-walkthroughs.md").


## Using Object Lock with encryption


Amazon S3 encrypts all new objects by default. You can use Object Lock with your encrypted
 objects. For more information, see [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md").


While Object Lock can help prevent Amazon S3 objects from being deleted or
 overwritten, it does not protect against losing access to the encryption keys or
 encryption keys being deleted. For example, if you encrypt your objects with AWS KMS
 server-side encryption and your AWS KMS key is deleted your objects may become
 unreadable.


## Using Object Lock with Amazon S3 Inventory


You can configure Amazon S3 Inventory to create lists of the objects in an S3 bucket on a
 defined schedule. You can configure Amazon S3 Inventory to include the following Object Lock
 metadata for your objects:



* The retain until date
* The retention mode
* The legal hold status

For more information, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md").


## Managing S3 Lifecycle policies with
 Object Lock


Object lifecycle management configurations continue to function normally on protected
 objects, including placing delete markers. However, a locked version of an object cannot
 be deleted by a S3 Lifecycle expiration policy. Object Lock is maintained regardless of
 which storage class the object resides in and throughout S3 Lifecycle transitions between
 storage classes.


For more information about managing object lifecycles, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md").


## Managing delete markers with Object Lock


Although you can't delete a protected object version, you can still create a delete
 marker for that object. Placing a delete marker on an object doesn't delete the object
 or its object versions. However, it makes Amazon S3 behave in most ways as though the object
 has been deleted. For more information, see [Working with delete markers](DeleteMarker.md "DeleteMarker.md").


###### Note

Delete markers are not WORM-protected, regardless of any retention period or legal
 hold in place on the underlying object.


## Using S3 Storage Lens with Object Lock


To see metrics for Object Lock-enabled storage bytes and object count, you can use
 Amazon S3 Storage Lens. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
 visibility into object-storage usage and activity.


For more information, see [Using S3 Storage Lens to protect your data](storage-lens-data-protection.md "storage-lens-data-protection.md").


For a complete list of metrics, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").


## Uploading objects to an Object Lock enabled
 bucket


The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is
 required for any request to upload an object with a retention period configured using
 Object Lock. Theses headers are a way to verify the integrity of your object during
 upload.


When uploading an object with the Amazon S3 console, S3 automatically adds the
 `Content-MD5` header. You can optionally specify an additional checksum
 function and checksum value through the console as the
 `x-amz-sdk-checksum-algorithm` header. If you use the [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
 API you must specify the `Content-MD5` header, the
 `x-amz-sdk-checksum-algorithm` header, or both to configure the
 Object Lock retention period.


For more information, see [Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md").


## Configuring events and
 notifications


You can use Amazon S3 Event Notifications to track access and changes to your Object Lock
 configurations and data by using AWS CloudTrail. For information about CloudTrail, see [What
 is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html") in the *AWS CloudTrail User
 Guide*.


You can also use Amazon CloudWatch to generate alerts based on this data. For information about
 CloudWatch, see the [What
 is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html") in the *Amazon CloudWatch User
 Guide*.


## Setting limits on retention
 periods with a bucket policy


You can set minimum and maximum allowable retention periods for a bucket by using a
 bucket policy. The maximum retention period is 100 years.


The following example shows a bucket policy that uses the
 `s3:object-lock-remaining-retention-days` condition key to set a maximum
 retention period of 10 days.



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "`SetRetentionLimits`",
 "Statement": [
 {
 "Sid": "`SetRetentionPeriod`",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "s3:PutObjectRetention"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
 "Condition": {
 "NumericGreaterThan": {
 "s3:object-lock-remaining-retention-days": "10"
 }
 }
 }
 ]
}`

```





###### Note

If your bucket is the destination bucket for a replication configuration, you can
 set up minimum and maximum allowable retention periods for object replicas that are
 created by using replication. To do so, you must allow the
 `s3:ReplicateObject` action in your bucket policy. For more
 information about replication permissions, see [Setting up permissions for live
 replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md"). 


For more information about bucket policies, see the following topics:



* [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html") in the *Service Authorization 
 Reference*


For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").
* [Object operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects "security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects")
* [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md")
