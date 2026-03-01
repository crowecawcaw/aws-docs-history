# Requirements and considerations for replication

Amazon S3 replication requires the following:

- The source bucket owner must have the source and destination AWS Regions enabled for
  their account. The destination bucket owner must have the destination Region enabled for
  their account.

For more information about enabling or disabling an AWS Region, see [Specify
which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management Reference Guide_.

- Both source and destination buckets must have versioning enabled. For more information
  about versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").
- Amazon S3 must have permissions to replicate objects from the source bucket to the
  destination bucket or buckets on your behalf. For more information about these
  permissions, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").
- If the owner of the source bucket doesn't own the object in the bucket, the object
  owner must grant the bucket owner `READ` and `READ_ACP` permissions
  with the object access control list (ACL). For more information, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").
- If the source bucket has S3 Object Lock enabled, the destination buckets must also
  have S3 Object Lock enabled.

To enable replication on a bucket that has Object Lock enabled, you must use the
AWS Command Line Interface, REST API, or AWS SDKs. For more general information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").

###### Note

You must grant two new permissions on the source S3 bucket in the AWS Identity and Access Management (IAM)
role that you use to set up replication. The two new permissions are
`s3:GetObjectRetention` and `s3:GetObjectLegalHold`. If the role
has an `s3:Get*` permission, it satisfies the requirement. For more
information, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").
For more information, see [Setting up live replication overview](replication-how-setup.md "replication-how-setup.md").

If you are setting the replication configuration in a _cross-account
scenario_, where the source and destination buckets are owned by different
AWS accounts, the following additional requirement applies:

- The owner of the destination buckets must grant the owner of the source bucket
  permissions to replicate objects with a bucket policy. For more information, see [(Optional) Step 3: Granting permissions when the source and destination buckets are owned by different AWS accounts](setting-repl-config-perm-overview.md#setting-repl-config-crossacct "setting-repl-config-perm-overview.md#setting-repl-config-crossacct").
- The destination buckets cannot be configured as Requester Pays buckets. For more
  information, see [Using Requester Pays general purpose buckets for storage transfers and usage](RequesterPaysBuckets.md "RequesterPaysBuckets.md").

## Considerations for replication

Before you create a replication configuration, be aware of the following considerations.

###### Topics

- [Lifecycle configuration and object replicas](#replica-and-lifecycle "#replica-and-lifecycle")
- [Versioning configuration and replication configuration](#replication-and-versioning "#replication-and-versioning")
- [Using S3 Replication with S3 Intelligent-Tiering](#replication-and-intelligent-tiering "#replication-and-intelligent-tiering")
- [Logging configuration and replication configuration](#replication-and-logging "#replication-and-logging")
- [CRR and the destination Region](#replication-and-dest-region "#replication-and-dest-region")
- [S3 Batch Replication](#considerations-batch-replication "#considerations-batch-replication")
- [S3 Replication Time Control](#considerations-RTC "#considerations-RTC")

### Lifecycle configuration and object replicas

The time it takes for Amazon S3 to replicate an object depends on the size of the object.
For large objects, it can take several hours. Although it might take a while before a
replica is available in the destination, it takes the same amount of time to create the
replica as it took to create the corresponding object in the source bucket. If a lifecycle
configuration is enabled on a destination bucket, the lifecycle rules honor the original
creation time of the object, not when the replica became available in the destination
bucket.

Replication configuration requires the bucket to be versioning-enabled. When you
enable versioning on a bucket, keep the following in mind:

- If you have an object Expiration lifecycle configuration, after you enable
  versioning, add a `NonCurrentVersionExpiration` policy to maintain the same
  permanent delete behavior as before you enabled versioning.
- If you have a Transition lifecycle configuration, after you enable versioning,
  consider adding a `NonCurrentVersionTransition` policy.

### Versioning configuration and replication configuration

Both the source and destination buckets must be versioning-enabled when you configure
replication on a bucket. After you enable versioning on both the source and destination
buckets and configure replication on the source bucket, you will encounter the following
issues:

- If you attempt to disable versioning on the source bucket, Amazon S3 returns an error.
  You must remove the replication configuration before you can disable versioning on the
  source bucket.
- If you disable versioning on the destination bucket, replication fails. The source
  object has the replication status `FAILED`.

### Using S3 Replication with S3 Intelligent-Tiering

S3 Intelligent-Tiering is a storage class that is designed to optimize storage costs by
automatically moving data to the most cost-effective access tier. For a small monthly
object monitoring and automation charge, S3 Intelligent-Tiering monitors access patterns
and automatically moves objects that have not been accessed to lower-cost access
tiers.

Replicating objects stored in S3 Intelligent-Tiering with S3 Batch Replication or
invoking [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") or [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
constitutes access. In these cases, the source objects of the copy or replication
operations are tiered up.

For more information about S3 Intelligent-Tiering see, [Managing storage costs with Amazon S3 Intelligent-Tiering](intelligent-tiering.md "intelligent-tiering.md").

### Logging configuration and replication configuration

If Amazon S3 delivers logs to a bucket that has replication enabled, it replicates the log
objects.

If [server access logs](ServerLogs.md "ServerLogs.md") or
[AWS CloudTrail logs](cloudtrail-logging.md "cloudtrail-logging.md")
are enabled on your source or destination bucket, Amazon S3 includes replication-related
requests in the logs. For example, Amazon S3 logs each object that it replicates.

### CRR and the destination Region

Amazon S3 Cross-Region Replication (CRR) is used to copy objects across S3 buckets in
different AWS Regions. You might choose the Region for your destination bucket based on
either your business needs or cost considerations. For example, inter-Region data transfer
charges vary depending on the Regions that you choose.

Suppose that you chose US East (N. Virginia) (`us-east-1`) as the Region for
your source bucket. If you choose US West (Oregon) (`us-west-2`) as the
Region for your destination buckets, you pay more than if you choose the
US East (Ohio) (`us-east-2`) Region. For pricing information, see "Data
Transfer Pricing" in [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

There are no data transfer charges associated with Same-Region Replication
(SRR).

### S3 Batch Replication

For information about considerations for Batch Replication, see [S3 Batch Replication considerations](s3-batch-replication-batch.md#batch-replication-considerations "s3-batch-replication-batch.md#batch-replication-considerations").

### S3 Replication Time Control

For information about best practices and considerations for S3 Replication Time Control (S3 RTC), see [Best practices and guidelines for S3 RTC](replication-time-control.md#rtc-best-practices "replication-time-control.md#rtc-best-practices").
