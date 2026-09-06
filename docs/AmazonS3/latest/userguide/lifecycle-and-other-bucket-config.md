

# How S3 Lifecycle interacts with other bucket configurations
<a name="lifecycle-and-other-bucket-config"></a>

In addition to S3 Lifecycle configurations, you can associate other configurations with your bucket. This section explains how S3 Lifecycle configuration relates to other bucket configurations.

## S3 Lifecycle and S3 Versioning
<a name="lifecycle-versioning-support-intro"></a>

You can add S3 Lifecycle configurations to unversioned buckets and versioning-enabled buckets. For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md). 

A versioning-enabled bucket maintains one current object version, and zero or more noncurrent object versions. You can define separate lifecycle rules for current and noncurrent object versions.

For more information, see [Lifecycle configuration elements](intro-lifecycle-rules.md).

**Important**  
When you have multiple rules in an S3 Lifecycle configuration, an object can become eligible for multiple S3 Lifecycle actions on the same day. In such cases, Amazon S3 follows these general rules:  
Permanent deletion takes precedence over transition.
Transition takes precedence over creation of [delete markers](DeleteMarker.md).
When an object is eligible for both a S3 Glacier Flexible Retrieval and S3 Standard-IA (or S3 One Zone-IA) transition, Amazon S3 chooses the S3 Glacier Flexible Retrieval transition.
 For examples, see [Examples of overlapping filters and conflicting lifecycle actions](lifecycle-conflicts.md#lifecycle-config-conceptual-ex5). 

## S3 Lifecycle and S3 Replication
<a name="lifecycle-and-replication"></a>

When you have both S3 Replication and S3 Lifecycle enabled on a bucket, S3 Lifecycle blocks expiration and transition actions on objects with `PENDING` or `FAILED` replication status. This ensures that Lifecycle does not act on objects until they have successfully replicated to their destination bucket.

Objects transition to a `FAILED` replication state for issues such as missing replication role permissions, AWS Key Management Service (AWS KMS) permissions, or bucket permissions. For more information, see [Troubleshooting replication](replication-troubleshoot.md).

Objects with `FAILED` replication status will continue to incur storage costs past their Lifecycle expiration or transition eligibility date until the replication issue is resolved. Once you fix the underlying replication configuration or IAM permissions, new objects will replicate automatically. However, objects that already have `FAILED` replication status will not automatically retry—you must use S3 Batch Replication to replicate them, or delete them using S3 Batch Operations with AWS Lambda if no longer needed. After objects successfully replicate (or are deleted), Lifecycle will resume processing them according to your configured rules. To identify objects with `FAILED` replication status, you can use Amazon CloudWatch metrics (`OperationFailedReplication`) to monitor failure counts and trends at the bucket level, or use Amazon S3 Inventory reports, Amazon S3 API (`HeadObject` or `GetObject`), or Amazon S3 Event Notifications for object-level details.

## S3 Lifecycle configuration on MFA-enabled buckets
<a name="lifecycle-general-considerations-mfa-enabled-bucket"></a>

S3 Lifecycle configuration on multi-factor authentication buckets configured for MFA delete isn't supported. For more information, see [Configuring MFA delete](MultiFactorAuthenticationDelete.md).

## S3 Lifecycle and logging
<a name="lifecycle-general-considerations-logging"></a>

Amazon S3 Lifecycle actions aren't captured by AWS CloudTrail object level logging. CloudTrail captures API requests made to external Amazon S3 endpoints, whereas S3 Lifecycle actions are performed by using internal Amazon S3 endpoints. 

You can enable Amazon S3 server access logs in an S3 bucket to capture S3 Lifecycle-related actions, such as object transitions to another storage class and object expirations that result in permanent deletion or logical deletion. For more information, see [Logging requests with server access logging](ServerLogs.md).

If you have logging enabled on your bucket, Amazon S3 server access logs report the results of the following operations.


| Operation log | Description | 
| --- | --- | 
| `S3.EXPIRE.OBJECT` | Amazon S3 permanently deletes the object because of the lifecycle `Expiration` action. | 
| `S3.CREATE.DELETEMARKER` | Amazon S3 logically deletes the current version by adding a delete marker in a versioning-enabled bucket. | 
| `S3.TRANSITION_SIA.OBJECT` | Amazon S3 transitions the object to the S3 Standard-IA storage class. | 
| `S3.TRANSITION_ZIA.OBJECT` | Amazon S3 transitions the object to the S3 One Zone-IA storage class. | 
| `S3.TRANSITION_INT.OBJECT` | Amazon S3 transitions the object to the S3 Intelligent-Tiering storage class. | 
| `S3.TRANSITION_GIR.OBJECT` | Amazon S3 initiates the transition of the object to the S3 Glacier Instant Retrieval storage class. | 
| `S3.TRANSITION.OBJECT` | Amazon S3 initiates the transition of the object to the S3 Glacier Flexible Retrieval storage class. | 
| `S3.TRANSITION_GDA.OBJECT` | Amazon S3 initiates the transition of the object to the S3 Glacier Deep Archive storage class. | 
| `S3.DELETE.UPLOAD` | Amazon S3 aborts an incomplete multipart upload. | 

**Note**  
Amazon S3 server access log records are delivered on a best-effort basis and can't be used for a complete accounting of all Amazon S3 requests. 