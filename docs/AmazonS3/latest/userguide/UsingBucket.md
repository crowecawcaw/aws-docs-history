# General purpose buckets overview

To upload your data (photos, videos, documents, etc.) to Amazon S3, you must first create an S3
bucket in one of the AWS Regions.

There are several types of Amazon S3 buckets. Before creating a bucket, make sure that you choose the bucket type that best fits your application and performance requirements. For more information about the various bucket types and the appropriate use cases for each, see [Buckets](Welcome.md#BasicsBucket "Welcome.md#BasicsBucket").

The following sections provide more information about general purpose buckets, including bucket
naming rules, quotas, and bucket configuration details. For a list of restriction and
limitations related to Amazon S3 buckets see, [General purpose bucket quotas, limitations, and restrictions](BucketRestrictions.md "BucketRestrictions.md").

###### Topics

- [General purpose buckets overview](#general-purpose-buckets-overview "#general-purpose-buckets-overview")
- [Common general purpose bucket patterns](#bucket-patterns-overview "#bucket-patterns-overview")
- [Permissions](#about-access-permissions-create-bucket "#about-access-permissions-create-bucket")
- [Managing public access to general purpose buckets](#block-public-access-intro "#block-public-access-intro")
- [Managing public access to general purpose buckets](#bucket-tagging-intro "#bucket-tagging-intro")
- [General purpose buckets configuration options](#bucket-config-options-intro "#bucket-config-options-intro")
- [General purpose buckets operations](#bucket-operations-limits "#bucket-operations-limits")
- [General purpose buckets performance monitoring](#bucket-monitoring-use-cases "#bucket-monitoring-use-cases")

## General purpose buckets overview

Every object is contained in a bucket. For example, if the object named
`photos/puppy.jpg` is stored in the
`amzn-s3-demo-bucket` general purpose bucket in the US West (Oregon)
Region, then it is addressable by using the URL
`https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/photos/puppy.jpg`.
For more information, see [Accessing a
Bucket](access-bucket-intro.md "access-bucket-intro.md").

- General purpose bucket quotas for commercial Regions can only be viewed and managed
  from US East (N. Virginia).
- General purpose bucket quotas for AWS GovCloud (US) can only be viewed and managed from
  AWS GovCloud (US-West).

In terms of implementation, buckets and objects are AWS resources, and Amazon S3 provides
APIs for you to manage them. For example, you can create a bucket and upload objects using
the Amazon S3 API. You can also use the Amazon S3 console to perform these operations. The console
uses the Amazon S3 APIs to send requests to Amazon S3.

This section describes how to work with general purpose buckets. For information about working with
objects, see [Amazon S3 objects overview](UsingObjects.md "UsingObjects.md").

Amazon S3 supports global general purpose buckets, which means that each bucket name must be unique across all
AWS accounts in all the AWS Regions within a partition. A partition is a grouping of
Regions. AWS currently has three partitions: `aws` (Standard Regions),
`aws-cn` (China Regions), and `aws-us-gov` (AWS GovCloud (US)).

After a general purpose bucket is created, the name of that bucket cannot be used by another AWS account
in the same partition until the bucket is deleted. You should not depend on specific bucket
naming conventions for availability or security verification purposes. For bucket naming
guidelines, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

Amazon S3 creates buckets in a Region that you specify. To reduce latency, minimize costs, or
address regulatory requirements, choose any AWS Region that is geographically close to
you. For example, if you reside in Europe, you might find it advantageous to create buckets
in the Europe (Ireland) or Europe (Frankfurt) Regions. For a list of Amazon S3 Regions, see
[Regions and
Endpoints](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _AWS General Reference_.

###### Note

Objects that belong to a bucket that you create in a specific AWS Region never leave
that Region, unless you explicitly transfer them to another Region. For example, objects
that are stored in the Europe (Ireland) Region never leave it.

## Common general purpose bucket patterns

When you build applications on Amazon S3, you can use unique general purpose buckets to separate
different datasets or workloads. Depending on your use case, there are different design
patterns and best practices for using general purpose buckets. For more information, see [Common general purpose bucket patterns for building applications on
Amazon S3](common-bucket-patterns.md "common-bucket-patterns.md").

## Permissions

You can use your AWS account root user credentials to create a general purpose bucket and perform any other Amazon S3
operation. However, we recommend that you do not use the root user credentials of your
AWS account to make requests, such as to create a bucket. Instead, create an AWS Identity and Access Management
(IAM) user, and grant that user full access (users by default have no permissions).

These users are referred to as _administrators_. You
can use the administrator user credentials, instead of the root user credentials of your
account, to interact with AWS and perform tasks, such as create a bucket, create
users, and grant them permissions.

For more information, see [AWS account root user
credentials and IAM user credentials](../../../general/latest/gr/root-vs-iam.md "../../../general/latest/gr/root-vs-iam.md") in the _AWS
General Reference_ and [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

The AWS account that creates a resource owns that resource. For example, if you
create an IAM user in your AWS account and grant the user permission to create a
bucket, the user can create a bucket. But the user does not own the bucket; the
AWS account that the user belongs to owns the bucket. The user needs additional
permission from the resource owner to perform any other bucket operations. For more
information about managing permissions for your Amazon S3 resources, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").

## Managing public access to general purpose buckets

Public access is granted to general purpose buckets and objects through bucket policies, access
control lists (ACLs), or both. To help you manage public access to Amazon S3 resources, Amazon S3
provides settings to block public access. Amazon S3 Block Public Access settings can override
ACLs and bucket policies so that you can enforce uniform limits on public access to
these resources. You can apply Block Public Access settings to individual buckets or to
all buckets in your account.

To ensure that all of your Amazon S3 general purpose buckets and objects have their public access blocked,
all four settings for Block Public Access are enabled by default when you create a new
bucket. We recommend that you turn on all four settings for Block Public Access for your
account too. These settings block all public access for all current and future
buckets.

Before applying these settings, verify that your applications will work correctly
without public access. If you require some level of public access to your buckets or
objects—for example, to host a static website, as described at [Hosting a static website using Amazon S3](WebsiteHosting.md "WebsiteHosting.md")—you can customize
the individual settings to suit your storage use cases. For more information, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

However, we highly recommend keeping Block Public Access enabled. If you want to keep
all four Block Public Access settings enabled and host a static website, you can use
Amazon CloudFront origin access control (OAC). Amazon CloudFront provides the capabilities required to set
up a secure static website. Amazon S3 static websites support only HTTP endpoints. Amazon CloudFront
uses the durable storage of Amazon S3 while providing additional security headers, such as
HTTPS. HTTPS adds security by encrypting a normal HTTP request and protecting against
common cyberattacks.

For more information, see [Getting started with a secure static website](../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md "../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md") in the _Amazon CloudFront Developer Guide_.

###### Note

If you see an `Error` when you list your general purpose buckets and their public
access settings, you might not have the required permissions. Make sure that you
have the following permissions added to your user or role policy:

```
`s3:GetAccountPublicAccessBlock
s3:GetBucketPublicAccessBlock
s3:GetBucketPolicyStatus
s3:GetBucketLocation
s3:GetBucketAcl
s3:ListAccessPoints
s3:ListAllMyBuckets`
```

In some rare cases, requests can also fail because of an AWS Region
outage.

## Managing public access to general purpose buckets

You can add tags to your Amazon S3 buckets to categorize and track your AWS costs or for access control. You can use tags as cost allocation tags to track storage costs in AWS Billing and Cost Management. You can also use tags for attribute-based access control (ABAC), to scale access permissions and grant access to S3 buckets based on their tags.

For more information, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md")

## General purpose buckets configuration options

Amazon S3 supports various options for you to configure your general purpose bucket. For example, you can
configure your bucket for website hosting, add a configuration to manage the lifecycle
of objects in the bucket, and configure the bucket to log all access to the bucket. Amazon S3
supports subresources for you to store and manage the bucket configuration information.
You can use the Amazon S3 API to create and manage these subresources. However, you can also
use the console or the AWS SDKs.

###### Note

There are also object-level configurations. For example, you can configure
object-level permissions by configuring an access control list (ACL) specific to
that object.

These are referred to as subresources because they exist in the context of a specific
bucket or object. The following table lists subresources that enable you to manage
bucket-specific configurations.

| Subresource                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*cors<br>• (cross-origin resource sharing)         | You can configure your bucket to allow cross-origin<br>requests.<br>For more information, see [Using cross-origin resource sharing (CORS)](cors.md "cors.md").                                                                                                                                                                                                                                                                                                                                                                              |
| _event notification_                                | You can enable your bucket to send you notifications of specified<br>bucket events.<br>For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").                                                                                                                                                                                                                                                                                                                                            |
| _lifecycle_                                         | You can define lifecycle rules for objects in your bucket that<br>have a well-defined lifecycle. For example, you can define a rule to<br>archive objects one year after creation, or delete an object 10<br>years after creation.<br>For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md").                                                                                                                                                                                   |
| _location_                                          | When you create a bucket, you specify the AWS Region where you<br>want Amazon S3 to create the bucket. Amazon S3 stores this information in the<br>location subresource and provides an API for you to retrieve this<br>information.                                                                                                                                                                                                                                                                                                        |
| _logging_                                           | Logging enables you to track requests for access to your bucket.<br>Each access log record provides details about a single access<br>request, such as the requester, bucket name, request time, request<br>action, response status, and error code, if any. Access log<br>information can be useful in security and access audits. It can also<br>help you learn about your customer base and understand your Amazon S3<br>bill.<br>For more information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md"). |
| _object locking_                                    | To use S3 Object Lock, you must enable it for a bucket. You can<br>also optionally configure a default retention mode and period that<br>applies to new objects that are placed in the bucket.<br>For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").                                                                                                                                                                                                                                            |
| *policy<br>• and *ACL<br>• (access<br>control list) | All your resources (such as buckets and objects) are private by<br>default. Amazon S3 supports both bucket policy and access control list<br>(ACL) options for you to grant and manage bucket-level permissions.<br>Amazon S3 stores the permission information in the<br>*policy<br>• and *acl\*<br>subresources.<br>For more information, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").                                                                                                          |
| _replication_                                       | Replication is the automatic, asynchronous copying of objects<br>across buckets in different or the same AWS Regions. For more<br>information, see [Replicating objects within and across Regions](replication.md "replication.md").                                                                                                                                                                                                                                                                                                        |
| _requestPayment_                                    | By default, the AWS account that creates the bucket (the bucket<br>owner) pays for downloads from the bucket. Using this subresource,<br>the bucket owner can specify that the person requesting the download<br>will be charged for the download. Amazon S3 provides an API for you to<br>manage this subresource.<br>For more information, see [Using Requester Pays general purpose buckets for storage<br>transfers and usage](RequesterPaysBuckets.md "RequesterPaysBuckets.md").                                                      |
| _tagging_                                           | You can add tags to your Amazon S3 buckets to categorize and track your AWS costs or for access control. You can use tags as cost allocation tags to track storage costs in AWS Billing and Cost Management. You can also use tags for attribute-based access control (ABAC), to scale access permissions and grant access to S3 buckets based on their tags.<br>For more information, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").                                                           |
| _transfer acceleration_                             | Transfer Acceleration enables fast, easy, and secure transfers of files<br>over long distances between your client and an S3 bucket.<br>Transfer Acceleration takes advantage of the globally distributed edge<br>locations of Amazon CloudFront.<br>For more information, see [Configuring fast, secure file transfers using<br>Amazon S3 Transfer Acceleration](transfer-acceleration.md "transfer-acceleration.md").                                                                                                                     |
| _versioning_                                        | Versioning helps you recover accidental overwrites and deletes.<br>We recommend versioning as a best practice to recover objects from<br>being deleted or overwritten by mistake.<br>For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").                                                                                                                                                                                                                                  |
| _website_                                           | You can configure your bucket for static website hosting. Amazon S3<br>stores this configuration by creating a _website_<br>subresource.<br>For more information, see [Hosting a static website using Amazon S3](WebsiteHosting.md "WebsiteHosting.md").                                                                                                                                                                                                                                                                                    |

## General purpose buckets operations

The high availability engineering of Amazon S3 is focused on _get_, _put_, _list_, and _delete_ operations. Because
general purpose bucket operations work against a centralized, global resource space, we recommend that you
don't create, delete, or configure buckets on the high availability code path
of your application. It's better to create, delete, or configure buckets in a separate
initialization or setup routine that you run less often.

## General purpose buckets performance monitoring

When you have critical applications and business processes that rely on AWS
resources, it’s important to monitor and get alerts for your system. [Monitoring your data](monitoring-overview.md "monitoring-overview.md") can help maintain the reliability, availability, and
performance of Amazon S3 and your AWS solutions. There are several AWS services that you
can use to collect and aggregates metrics and logs for your S3 buckets.

Depending on your use case, you can choose which AWS service best suits your
organization’s needs to debug issues, monitor your data, optimize storage costs, or
troubleshoot multi-point issues. For example:

- **To improve the performance of applications that use
  S3:**
  [Set up CloudWatch
  alarms](cloudwatch-monitoring.md "cloudwatch-monitoring.md") to monitor your storage data, replication metrics, or request
  metrics.
- **To plan for storage usage, optimize storage costs, or to
  find out how much storage you have across your entire
  organization:**
  [Use
  Amazon S3 Storage Lens](storage-lens-optimize-storage.md "storage-lens-optimize-storage.md"). Alternatively, you can [use
  S3 Storage Lens to improve your data performance](storage-lens-detailed-status-code.md "storage-lens-detailed-status-code.md") by enabling advanced
  metrics and using the detailed status-code metrics to get counts for successful
  or failed requests.
- **For a unified view of your operational health:**
  [Publish S3 Storage Lens usage and activity metrics](storage_lens_view_metrics_cloudwatch.md "storage_lens_view_metrics_cloudwatch.md") to a [Amazon CloudWatch dashboard](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

###### Note

The Amazon CloudWatch publishing option is available for S3 Storage Lens
dashboards upgraded to **Advanced metrics and recommendations**. You can enable
the CloudWatch publishing option for a new or existing dashboard
configuration in S3 Storage Lens.

- **To obtain a record of actions taken by a user, role, or
  an AWS service:** Set up [AWS CloudTrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md"). You can also use AWS CloudTrail logs to review API calls for Amazon S3 as events.
- **To receive notifications about when a certain event happens in your S3 bucket:**
  [Set up Amazon S3 event notifications](EventNotifications.md "EventNotifications.md").
- **To obtain detailed records for the requests that are
  made to an S3 bucket:** [Set up S3 access
  logs](ServerLogs.md "ServerLogs.md").

For a list of all the different AWS services that you can use to monitor your data,
see [Logging and monitoring in Amazon S3](monitoring-overview.md "monitoring-overview.md").
