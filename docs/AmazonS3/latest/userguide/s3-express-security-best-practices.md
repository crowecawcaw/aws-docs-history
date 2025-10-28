# Security best practices for

directory buckets

There are a number of security features to consider when working with directory buckets.
The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful recommendations rather
than prescriptions.

## Default Block Public

Access and Object Ownership settings

Directory buckets support S3 Block Public Access and S3 Object Ownership. These S3 features are
used to audit and manage access to your buckets and objects.

By default, all Block Public Access settings for directory buckets are enabled. In
addition, Object Ownership is set to bucket owner enforced, which means that access
control lists (ACLs) are disabled. These settings can't be modified. For more
information about these features, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md") and [Controlling ownership of objects and disabling ACLs
for your bucket](about-object-ownership.md "about-object-ownership.md").

###### Note

You can't grant access to objects stored in directory buckets. You can grant
access only to your directory buckets. The authorization model for S3 Express One Zone is
different than the authorization model for Amazon S3. For more information, see [Authorizing Zonal endpoint API operations with
CreateSession](s3-express-create-session.md "s3-express-create-session.md").

## Authentication and

authorization

The authentication and authorization mechanisms for directory buckets differ, depending on
whether you are making requests to Zonal endpoint API operations or Regional endpoint
API operations. Zonal API operations are object-level (data plane) operations. Regional
API operations are bucket-level (control plane) operations.

You authenticate and authorize requests to Zonal endpoint API
operations through a new session-based mechanism that is optimized to provide the
lowest latency. With session-based authentication, the AWS SDKs use the
`CreateSession` API operation to request temporary credentials
that provide low-latency access to your directory bucket. These temporary credentials
are scoped to a specific directory bucket and expire after 5 minutes. You can use these
temporary credentials to sign Zonal (object level) API calls. For more information, see
[Authorizing Zonal endpoint API operations with
CreateSession](s3-express-create-session.md "s3-express-create-session.md").

###### Signing requests with credentials for directory bucket management

You use your credentials to sign Zonal endpoint (object level) API
requests with AWS Signature Version 4, with `s3express` as the service
name. When you sign your requests, use the secret key that's returned from
`CreateSession` and also provide the session token with the
`x-amzn-s3session-token header`. For more information, see [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md").

The [supported AWS
SDKs](s3-express-SDKs.md#s3-express-getting-started-accessing-sdks "s3-express-SDKs.md#s3-express-getting-started-accessing-sdks") manage credentials and signing on your behalf. We
recommend using the AWS SDKs to refresh credentials and sign requests
for you.

###### Signing requests with IAM credentials

All Regional (bucket-level) API calls must be authenticated and signed by
AWS Identity and Access Management (IAM) credentials instead of temporary session credentials. IAM
credentials consist of the access key ID and secret access key for the IAM
identities. All `CopyObject` and `HeadBucket` requests must
also be authenticated and signed by using IAM credentials.

To achieve the lowest latency for your Zonal (object-level) operation calls, we
recommend using credentials obtained from calling `CreateSession`
to sign your requests, except for requests to `CopyObject` and
`HeadBucket`.

## Use AWS CloudTrail

AWS CloudTrail provides a record of the actions taken by a user, a role, or an AWS service
in Amazon S3. You can use information collected by CloudTrail to determine the following:

- The request that was made to Amazon S3
- The IP address from which the request was made
- Who made the request
- When the request was made
- Additional details about the request

When you set up your AWS account, CloudTrail management events are enabled by default. The
following Regional endpoint API operations (bucket-level, or control plane, API
operations) are logged to CloudTrail.

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
- [DeleteBucket](../API/API_DeleteBucket.md "../API/API_DeleteBucket.md")
- [DeleteBucketPolicy](../API/API_DeleteBucketPolicy.md "../API/API_DeleteBucketPolicy.md")
- [PutBucketPolicy](../API/API_PutBucketPolicy.md "../API/API_PutBucketPolicy.md")
- [GetBucketPolicy](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")
- [ListDirectoryBuckets](../API/API_ListDirectoryBuckets.md "../API/API_ListDirectoryBuckets.md")
- [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")
- [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md")
- [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md")
- [DeleteBucketEncryption](../API/API_DeleteBucketEncryption.md "../API/API_DeleteBucketEncryption.md")

###### Note

`ListMultipartUploads` is a Zonal endpoint API operation. However, it is logged to CloudTrail as a management event. For more information, see [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md") in the _Amazon Simple Storage Service API Reference_.

By default, CloudTrail trails don't log data events, but you can configure trails to log
data events for directory buckets that you specify, or to log data events for all the
directory buckets in your AWS account. The following Zonal endpoint API operations
(object-level, or data plane, API operations) are logged to CloudTrail.

- [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")
- [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")
- [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
- [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")
- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
- [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")

For more information on using AWS CloudTrail with directory buckets , see [Logging with AWS CloudTrail for directory buckets](s3-express-one-zone-cloudtrail-logging.md "s3-express-one-zone-cloudtrail-logging.md").

### Implement monitoring

by using AWS monitoring tools

Monitoring is an important part of maintaining the reliability, security,
availability, and performance of Amazon S3 and your AWS solutions. AWS provides
several tools and services to help you monitor Amazon S3 and your other AWS services.
For example, you can monitor Amazon CloudWatch metrics for Amazon S3, particularly the
`BucketSizeBytes` and `NumberOfObjects` storage
metrics.

Objects stored in the directory buckets won't be reflected in the
`BucketSizeBytes` and `NumberOfObjects` storage metrics
for Amazon S3. However, the `BucketSizeBytes` and
`NumberOfObjects` storage metrics are supported for directory buckets. To
see the metrics of your choice, you can differentiate between the Amazon S3 storage
classes by specifying a `StorageType`
dimension. For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md") and [Logging and monitoring in Amazon S3](monitoring-overview.md "monitoring-overview.md").
