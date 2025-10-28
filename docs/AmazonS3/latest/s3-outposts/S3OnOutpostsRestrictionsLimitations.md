# How is Amazon S3 on Outposts different from

Amazon S3?

Amazon S3 on Outposts delivers object storage to your on-premises AWS Outposts environment. Using
S3 on Outposts helps you to meet local processing, data residency, and demanding performance
needs by keeping data close to on-premises applications. Because it uses Amazon S3 APIs and
features, S3 on Outposts makes it easy to store, secure, tag, report on, and control access to
the data on your Outposts and extend AWS infrastructure to your on-premises facility for a
consistent hybrid experience.

For more information about how S3 on Outposts is unique, see the following topics.

###### Topics

- [S3 on Outposts specifications](#S3OnOutpostsSpecifications "#S3OnOutpostsSpecifications")
- [API operations supported by
  S3 on Outposts](#S3OnOutpostsAPILimitations "#S3OnOutpostsAPILimitations")
- [Amazon S3 AWS CLI commands supported by S3 on Outposts](#S3OnOutpostsCLILimitations "#S3OnOutpostsCLILimitations")
- [Amazon S3 features not supported by
  S3 on Outposts](#S3OnOutpostsFeatureLimitations "#S3OnOutpostsFeatureLimitations")
- [S3 on Outposts network
  requirements](#S3OnOutpostsConnectivityRestrictions "#S3OnOutpostsConnectivityRestrictions")

## S3 on Outposts specifications

- The maximum Outposts bucket size is 50 TB.
- The maximum number of Outposts buckets is 100 per AWS account.
- Outposts buckets can be accessed only by using access points and endpoints.
- The maximum number of access points per Outposts bucket is 10.
- Access point policies are limited to 20 KB in size.
- The Outpost owner can manage access within your organization in AWS Organizations by
  using AWS Resource Access Manager. All accounts that need access to the Outpost must be within the
  same organization as the owner account in AWS Organizations.
- The S3 on Outposts bucket owner account is always the owner of all objects in
  the bucket.
- Only the S3 on Outposts bucket owner account can perform operations on the
  bucket.
- Object size limitations are consistent with Amazon S3.
- All objects stored on S3 on Outposts are stored in the `OUTPOSTS`
  storage class.
- By default, all objects stored in the `OUTPOSTS` storage class are
  stored by using server-side encryption with Amazon S3 managed encryption keys
  (SSE-S3). You can also explicitly choose to store objects by using server-side
  encryption with customer-provided encryption keys (SSE-C).
- If there is not enough space to store an object on your Outpost, the API
  returns an insufficient capacity exception (ICE).

## API operations supported by

S3 on Outposts

For a list of API operations supported by S3 on Outposts, see [Amazon S3 on Outposts API operations](S3OutpostsAPI.md "S3OutpostsAPI.md").

## Amazon S3 AWS CLI commands supported by S3 on Outposts

The following Amazon S3 AWS CLI commands are currently supported by Amazon S3 on Outposts. For
more information, see [Available Commands](../../../cli/latest/reference/s3.md#available-commands "../../../cli/latest/reference/s3.md#available-commands") in the AWS CLI Command Reference.

- `cp`, `mv`, and `sync` within the same
  Outposts bucket, or between a local environment and an
  Outposts bucket.
- `ls`
- `presign`
- `rm`

## Amazon S3 features not supported by

S3 on Outposts

The following Amazon S3 features are currently not supported by Amazon S3 on Outposts. Any
attempts to use them are rejected.

- Conditional requests
- Access control lists (ACLs)
- Cross-origin resource sharing (CORS)
- S3 Batch Operations
- S3 Inventory reports
- Changing the default bucket encryption
- Public buckets
- Multi-factor authentication (MFA) delete
- S3 Lifecycle transitions (aside from object deletion and stopping incomplete
  multipart uploads)
- S3 Object Lock legal hold
- Object Lock retention
- Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
- S3 Replication Time Control (S3 RTC)
- Amazon CloudWatch request metrics
- Metrics configuration
- Transfer Acceleration
- S3 Event Notifications
- Requester Pays buckets
- S3 Select
- AWS Lambda events
- Server access logging
- HTTP POST requests
- SOAP
- Website access

## S3 on Outposts network

requirements

- To route requests to an S3 on Outposts access point, you must create and configure an
  S3 on Outposts endpoint. The following limits apply to endpoints for
  S3 on Outposts:
  - Each virtual private cloud (VPC) on an Outpost can have one associated endpoint, and you can
    have up to 100 endpoints per Outpost.
  - You can map multiple access points to the same endpoint.
  - You can add endpoints only to VPCs with CIDR blocks in the subspaces
    of the following CIDR ranges:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16

- You can create endpoints to an Outpost only from VPCs that have
  non-overlapping CIDR blocks.
- You can create an endpoint only from within its Outposts subnet.
- The subnet that you use to create an endpoint must contain four IP addresses for
  S3 on Outposts to use.
- If you specify the customer-owned IP address pool (CoIP pool), it must contain
  four IP addresses for S3 on Outposts to use.
- You can create only one endpoint per Outpost per VPC.
