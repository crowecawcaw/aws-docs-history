

# Security best practices for Managed Service for Apache Flink

Amazon Managed Service for Apache Flink provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 

## Implement least privilege access
<a name="security-best-practices-privileges"></a>

When granting permissions, you decide who is getting what permissions to which Managed Service for Apache Flink resources. You enable specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact that could result from errors or malicious intent. 

For enhanced snapshots, follow these least privilege practices:
+ Grant `kinesisanalytics:RestoreFromSnapshot`, `kinesisanalytics:DeleteSnapshot`, and `kinesisanalytics:ExportSnapshot` only on the snapshot ARNs that each caller needs. Use a snapshot name prefix with a wildcard, or an `aws:ResourceTag` condition.
+ Grant `kinesisanalytics:CreateSnapshot` and `kinesisanalytics:CreateSystemSnapshot` only on the application ARNs that each caller manages.
+ Allow `iam:PassRole` only on the IAM roles that Managed Service for Apache Flink assumes to import and export enhanced snapshots. Set the condition `iam:PassedToService` to `kinesisanalytics.amazonaws.com`.
+ Limit `aws:SourceArn` to your snapshot ARNs and `aws:SourceAccount` to your account in the trust policy of each snapshot import or export role.

For example policies, see [Identity-based policy examples for enhanced snapshots](security-iam-snapshots.md#security-iam-snapshots-examples). For the import and export role policies, see [IAM role for import and export](security-iam-snapshots.md#security-iam-snapshots-transfer-role).

## Use IAM roles to access other Amazon services
<a name="security-best-practices-roles"></a>

Your Managed Service for Apache Flink application must have valid credentials to access resources in other services, such as Kinesis data streams, Firehose streams, or Amazon S3 buckets. You should not store AWS credentials directly in the application or in an Amazon S3 bucket. These are long-term credentials that are not automatically rotated and could have a significant business impact if they are compromised. 

Instead, you should use an IAM role to manage temporary credentials for your application to access other resources. When you use a role, you don't have to use long-term credentials to access other resources.

For more information, see the following topics in the *IAM User Guide*:
+ [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+ [Common Scenarios for Roles: Users, Applications, and Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

## Implement server-side encryption in dependent resources
<a name="security-best-practices-sse"></a>

Data at rest and data in transit is encrypted in Managed Service for Apache Flink, and this encryption cannot be disabled. You should implement server-side encryption in your dependent resources, such as Kinesis data streams, Firehose streams, and Amazon S3 buckets. For more information on implementing server-side encryption in dependent resources, see [Data protection ](data-protection.md).

Use server-side encryption on the Amazon S3 bucket that receives exported enhanced snapshots. In the [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) request, set `DestinationEncryptionConfiguration` to use a customer managed AWS KMS key. Or set default encryption on the bucket. If you set the key type in `DestinationEncryptionConfiguration` to `AWS_OWNED_KEY`, Amazon S3 encrypts the exported objects with the default encryption of the bucket. For more information about encryption for exported enhanced snapshots, see [Encryption for imported and exported snapshots](snapshots-import-export.md#snapshots-import-export-encryption-for-imported-and-exported-snapshots).

## Use CloudTrail to monitor API calls
<a name="security-best-practices-cloudtrail"></a>

Managed Service for Apache Flink is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an Amazon service in Managed Service for Apache Flink.

Using the information collected by CloudTrail, you can determine the request that was made to Managed Service for Apache Flink, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information, see [Log Managed Service for Apache Flink API calls with AWS CloudTrail](logging-using-cloudtrail.md).