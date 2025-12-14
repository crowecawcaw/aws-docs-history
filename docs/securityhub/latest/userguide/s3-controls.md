# Security Hub CSPM controls for Amazon S3

These AWS Security Hub CSPM controls evaluate the Amazon Simple Storage Service (Amazon S3) service and resources. The controls
might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [S3.1] S3 general purpose buckets should have block public access settings enabled

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.1.4, CIS AWS Foundations Benchmark v3.0.0/2.1.4, CIS AWS Foundations Benchmark v1.4.0/2.1.5, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:**
[s3-account-level-public-access-blocks-periodic](../../../config/latest/developerguide/s3-account-level-public-access-blocks-periodic.md "../../../config/latest/developerguide/s3-account-level-public-access-blocks-periodic.md")

**Schedule type:** Periodic

**Parameters:**

- `ignorePublicAcls`: `true` (not customizable)
- `blockPublicPolicy`: `true` (not customizable)
- `blockPublicAcls`: `true` (not customizable)
- `restrictPublicBuckets`: `true` (not customizable)

This control checks whether the preceding Amazon S3 block public access settings are configured
at the account level for an S3 general purpose bucket. The control fails if one or more of the
block public access settings are set to `false`.

The control fails if any of the settings are set to `false`, or if any of the
settings are not configured.

Amazon S3 public access block is designed to provide controls across an entire AWS account or
at the individual S3 bucket level to ensure that objects never have public access. Public access
is granted to buckets and objects through access control lists (ACLs), bucket policies, or
both.

Unless you intend to have your S3 buckets be publicly accessible, you should configure the
account level Amazon S3 Block Public Access feature.

To learn more, see [Using Amazon S3 Block Public
Access](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_.

### Remediation

To enable Amazon S3 Block Public Access for your AWS account, see [Configuring block public
access settings for your account](../../../AmazonS3/latest/userguide/configuring-block-public-access-account.md "../../../AmazonS3/latest/userguide/configuring-block-public-access-account.md") in the _Amazon Simple Storage Service User Guide_.

## [S3.2] S3 general purpose buckets should block public read

access

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS
v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.6, PCI DSS v3.2.1/7.2.1,
NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4,
NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5
SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network
configuration

**Severity:** Critical

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-public-read-prohibited](../../../config/latest/developerguide/s3-bucket-public-read-prohibited.md "../../../config/latest/developerguide/s3-bucket-public-read-prohibited.md")

**Schedule type:** Periodic and change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket permits public read access.
It evaluates the block public access settings, the bucket policy, and the bucket access
control list (ACL). The control fails if the bucket permits public read access.

###### Note

If an S3 bucket has a bucket policy, this control doesn't evaluate policy
conditions that use wildcard characters or variables. To produce a
`PASSED` finding, conditions in the bucket policy must only use fixed
values, which are values that don't contain wildcard characters or policy variables.
For information about policy variables, see [Variables and
tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _AWS Identity and Access Management User
Guide_.

Some use cases may require that everyone on the internet be able to read from your S3
bucket. However, those situations are rare. To ensure the integrity and security of your
data, your S3 bucket should not be publicly readable.

### Remediation

To block public read access on your Amazon S3 buckets, see [Configuring block public access settings for your S3 buckets](../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md "../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md") in the
_Amazon Simple Storage Service User Guide_.

## [S3.3] S3 general purpose buckets should block public write

access

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS
v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS
v3.2.1/7.2.1, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7),
NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7,
NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20),
NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5
SC-7(9)

**Category:** Protect > Secure network
configuration

**Severity:** Critical

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-public-write-prohibited](../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md "../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md")

**Schedule type:** Periodic and change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket permits public write
access. It evaluates the block public access settings, the bucket policy, and the bucket
access control list (ACL). The control fails if the bucket permits public write
access.

###### Note

If an S3 bucket has a bucket policy, this control doesn't evaluate policy
conditions that use wildcard characters or variables. To produce a
`PASSED` finding, conditions in the bucket policy must only use fixed
values, which are values that don't contain wildcard characters or policy variables.
For information about policy variables, see [Variables and
tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _AWS Identity and Access Management User
Guide_.

Some use cases require that everyone on the internet be able to write to your S3
bucket. However, those situations are rare. To ensure the integrity and security of your
data, your S3 bucket should not be publicly writable.

### Remediation

To block public write access on your Amazon S3 buckets, see [Configuring block public access settings for your S3 buckets](../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md "../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md") in the
_Amazon Simple Storage Service User Guide_.

## [S3.5] S3 general purpose buckets should require requests to use SSL

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.1.1, CIS AWS Foundations Benchmark v3.0.0/2.1.1, CIS AWS Foundations Benchmark v1.4.0/2.1.2,
NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5
SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3),
NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5
SC-8(2), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.8, NIST.800-171.r2 3.13.15, PCI
DSS v3.2.1/4.1, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-ssl-requests-only](../../../config/latest/developerguide/s3-bucket-ssl-requests-only.md "../../../config/latest/developerguide/s3-bucket-ssl-requests-only.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket has a policy that requires requests to use SSL.
The control fails if the bucket policy doesn't require requests to use SSL.

S3 buckets should have policies that require all requests (`Action: S3:*`) to
only accept transmission of data over HTTPS in the S3 resource policy, indicated by the
condition key `aws:SecureTransport`.

### Remediation

To update an Amazon S3 bucket policy to deny nonsecure transport, see [Adding
a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User Guide_.

Add a policy statement similar to the one in the following policy. Replace
`amzn-s3-demo-bucket` with the name of the bucket you're modifying.

JSON

```
`{
 "Id": "ExamplePolicy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSSLRequestsOnly",
 "Action": "s3:*",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 },
 "Principal": "*"
 }
 ]
}`

```

For more information, see [What S3 bucket policy
should I use to comply with the AWS Config rule s3-bucket-ssl-requests-only?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/") in the _AWS Official Knowledge Center_.

## [S3.6] S3 general purpose bucket policies should restrict access to other AWS accounts

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5
CM-2, NIST.800-171.r2 3.13.4

**Category:** Protect > Secure access management > Sensitive
API operations actions restricted

**Severity:** High

**Resource type:**
`AWS::S3::Bucket`

**AWS Config** rule: [s3-bucket-blacklisted-actions-prohibited](../../../config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.md "../../../config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.md")

**Schedule type:** Change triggered

**Parameters:**

- `blacklistedactionpatterns`: `s3:DeleteBucketPolicy, s3:PutBucketAcl,
s3:PutBucketPolicy, s3:PutEncryptionConfiguration, s3:PutObjectAcl` (not customizable)

This control checks whether an Amazon S3 general purpose bucket policy prevents principals from other AWS accounts
from performing denied actions on resources in the S3 bucket. The control fails if the
bucket policy allows one or more of the preceding actions for a principal in another AWS account.

Implementing least privilege access is fundamental to reducing security risk and the impact
of errors or malicious intent. If an S3 bucket policy allows access from external accounts, it
could result in data exfiltration by an insider threat or an attacker.

The `blacklistedactionpatterns` parameter allows for successful evaluation of
the rule for S3 buckets. The parameter grants access to external accounts for action patterns
that are not included in the `blacklistedactionpatterns` list.

### Remediation

To update an Amazon S3 bucket policy to remove permissions, see.[Adding
a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User Guide_.

On the **Edit bucket policy** page, in the policy editing text box, take one of the
following actions:

- Remove the statements that grant other
  AWS accounts access to denied actions.
- Remove the permitted denied actions from the statements.

## [S3.7] S3 general purpose buckets should use cross-Region replication

**Related requirements:** PCI DSS v3.2.1/2.2, NIST.800-53.r5 AU-9(2), NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-36(2), NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-cross-region-replication-enabled](../../../config/latest/developerguide/s3-bucket-cross-region-replication-enabled.md "../../../config/latest/developerguide/s3-bucket-cross-region-replication-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket has cross-Region replication enabled. The control fails if the
bucket doesn't have cross-Region replication enabled.

Replication is the automatic, asynchronous copying of objects across buckets in the same or different AWS Regions.
Replication copies newly created objects and object updates from a source bucket to a destination bucket or buckets.
AWS best practices recommend replication for source and destination buckets that are owned by the same AWS account.
In addition to availability, you should consider other systems hardening settings.

This control produces a `FAILED` finding for a replication destination bucket if it doesn't have cross-region
replication enabled. If there's a legitimate reason that the destination bucket doesn't need cross-region replication to be
enabled, you can suppress findings for this bucket.

### Remediation

To enable Cross-Region Replication on an S3 bucket, see [Configuring replication for source and destination buckets owned by the same account](../../../AmazonS3/latest/userguide/replication-walkthrough1.md "../../../AmazonS3/latest/userguide/replication-walkthrough1.md") in the _Amazon Simple Storage Service User Guide_.
For **Source bucket**, choose **Apply to all objects in the bucket**.

## [S3.8] S3 general purpose buckets should block public access

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.1.4, CIS AWS Foundations Benchmark v3.0.02.1.4, CIS AWS Foundations Benchmark v1.4.0/2.1.5, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure access management > Access
control

**Severity:** High

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-level-public-access-prohibited](../../../config/latest/developerguide/s3-bucket-level-public-access-prohibited.md "../../../config/latest/developerguide/s3-bucket-level-public-access-prohibited.md")

**Schedule type:** Change triggered

**Parameters:**

- `excludedPublicBuckets` (not customizable) – A comma-separated list of known
  allowed public S3 bucket names

This control checks whether an Amazon S3 general purpose bucket blocks public access at the bucket level. The
control fails if any of the following settings are set to `false`:

- `ignorePublicAcls`
- `blockPublicPolicy`
- `blockPublicAcls`
- `restrictPublicBuckets`

Block Public Access at the S3 bucket level provides controls to ensure that objects never
have public access. Public access is granted to buckets and objects through access control lists
(ACLs), bucket policies, or both.

Unless you intend to have your S3 buckets publicly accessible, you should configure the
bucket level Amazon S3 Block Public Access feature.

### Remediation

For information on how to remove public access at a bucket level, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md") in the _Amazon S3 User Guide_.

## [S3.9] S3 general purpose buckets should have server access logging enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5
AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5
AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.3.8,
PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-logging-enabled](../../../config/latest/developerguide/s3-bucket-logging-enabled.md "../../../config/latest/developerguide/s3-bucket-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether server access logging is enabled for an Amazon S3 general purpose bucket. The control fails if server
access logging isn't enabled. When logging is enabled, Amazon S3 delivers access logs for a source bucket to a chosen target bucket. The
target bucket must be in the same AWS Region as the source bucket and must not have a default retention period configured. The
target logging bucket does not need to have server access logging enabled, and you should suppress findings for this bucket.

Server access logging provides detailed records of requests made to a bucket. Server access logs can assist in security and access audits. For more information, see [Security Best Practices for Amazon S3: Enable Amazon S3 server access logging](../../../AmazonS3/latest/dev/security-best-practices.md "../../../AmazonS3/latest/dev/security-best-practices.md").

### Remediation

To enable Amazon S3 server access logging, see [Enabling Amazon S3 server access logging](../../../AmazonS3/latest/userguide/enable-server-access-logging.md "../../../AmazonS3/latest/userguide/enable-server-access-logging.md") in the _Amazon S3 User Guide_.

## [S3.10] S3 general purpose buckets with versioning enabled should have Lifecycle configurations

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-version-lifecycle-policy-check](../../../config/latest/developerguide/s3-version-lifecycle-policy-check.md "../../../config/latest/developerguide/s3-version-lifecycle-policy-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose versioned bucket has a Lifecycle configuration. The control fails
if the bucket doesn't have a Lifecycle configuration.

We recommended creating a Lifecycle configuration for your S3 bucket to help you define actions that you want Amazon S3 to take during
an object's lifetime.

### Remediation

For more information on configuring lifecycle on an Amazon S3 bucket, see [Setting lifecycle configuration on a bucket](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md") and [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").

## [S3.11] S3 general purpose buckets should have event notifications enabled

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5
SI-3(8), NIST.800-53.r5 SI-4, NIST.800-53.r5 SI-4(4), NIST.800-171.r2 3.3.8

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-event-notifications-enabled](../../../config/latest/developerguide/s3-event-notifications-enabled.md "../../../config/latest/developerguide/s3-event-notifications-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter    | Description                      | Type                           | Allowed custom values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Security Hub CSPM default value |
| ------------ | -------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `eventTypes` | List of preferred S3 event types | EnumList (maximum of 28 items) | `s3:IntelligentTiering, s3:LifecycleExpiration:*, s3:LifecycleExpiration:Delete, s3:LifecycleExpiration:DeleteMarkerCreated, s3:LifecycleTransition, s3:ObjectAcl:Put, s3:ObjectCreated:*, s3:ObjectCreated:CompleteMultipartUpload, s3:ObjectCreated:Copy, s3:ObjectCreated:Post, s3:ObjectCreated:Put, s3:ObjectRemoved:*, s3:ObjectRemoved:Delete, s3:ObjectRemoved:DeleteMarkerCreated, s3:ObjectRestore:*, s3:ObjectRestore:Completed, s3:ObjectRestore:Delete, s3:ObjectRestore:Post, s3:ObjectTagging:*, s3:ObjectTagging:Delete, s3:ObjectTagging:Put, s3:ReducedRedundancyLostObject, s3:Replication:*, s3:Replication:OperationFailedReplication, s3:Replication:OperationMissedThreshold, s3:Replication:OperationNotTracked, s3:Replication:OperationReplicatedAfterThreshold, s3:TestEvent` | No default value                |

This control checks whether S3 Event Notifications are enabled on an Amazon S3 general purpose bucket.
The control fails if S3 Event Notifications are not enabled on the bucket. If you provide custom values for
the `eventTypes` parameter, the control passes only if event notifications are enabled for the specified
types of events.

When you enable S3 Event Notifications, you receive alerts when specific
events occur that impact your S3 buckets. For example, you can be notified of object creation, object removal, and object
restoration. These notifications can alert relevant teams to
accidental or intentional modifications that may lead to unauthorized data access.

### Remediation

For information about detecting changes to S3 buckets and objects, see [Amazon S3 Event Notifications](../../../AmazonS3/latest/userguide/NotificationHowTo.md "../../../AmazonS3/latest/userguide/NotificationHowTo.md") in the _Amazon S3 User Guide_.

## [S3.12] ACLs should not be used to manage user access to S3 general purpose buckets

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-acl-prohibited](../../../config/latest/developerguide/s3-bucket-acl-prohibited.md "../../../config/latest/developerguide/s3-bucket-acl-prohibited.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket provides user permissions with an access control list (ACL).
The control fails if an ACL is configured for managing user access on the bucket.

ACLs are legacy access control mechanisms that predate IAM. Instead of ACLs,
we recommend using S3 bucket policies or AWS Identity and Access Management (IAM) policies to manage access to your S3 buckets.

### Remediation

To pass this control, you should disable ACLs for your S3 buckets. For instructions, see [Controlling ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the _Amazon Simple Storage Service User Guide_.

To create an S3 bucket policy, see [Adding a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md").
To create an IAM user policy on an S3 bucket, see [Controlling access to a bucket with user policies](../../../AmazonS3/latest/userguide/walkthrough1.md#walkthrough-grant-user1-permissions "../../../AmazonS3/latest/userguide/walkthrough1.md#walkthrough-grant-user1-permissions").

## [S3.13] S3 general purpose buckets should have Lifecycle configurations

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Protect > Data protection

**Severity:** Low

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-lifecycle-policy-check](../../../config/latest/developerguide/s3-lifecycle-policy-check.md "../../../config/latest/developerguide/s3-lifecycle-policy-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                      | Description                                                                                     | Type    | Allowed custom values                                                                            | Security Hub CSPM default value |
| ------------------------------ | ----------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------ | ------------------------------- |
| `targetTransitionDays`         | Number of days after object creation when objects are transitioned to a specified storage class | Integer | `1` to `36500`                                                                                   | No default value                |
| `targetExpirationDays`         | Number of days after object creation when objects are deleted                                   | Integer | `1` to `36500`                                                                                   | No default value                |
| `targetTransitionStorageClass` | Destination S3 storage class type                                                               | Enum    | `STANDARD_IA,<br>INTELLIGENT_TIERING,<br>ONEZONE_IA,<br>GLACIER,<br>GLACIER_IR,<br>DEEP_ARCHIVE` | No default value                |

This control checks whether an Amazon S3 general purpose bucket has a Lifecycle configuration. The control fails if the
bucket doesn't have a Lifecycle configuration. If you provide custom values for one or more of the preceding parameters, the
control passes only if the policy includes the specified storage class, deletion time, or transition time.

Creating a Lifecycle configuration for your S3 bucket defines actions that you want Amazon S3 to take during an object's
lifetime. For example, you can transition objects to another storage class, archive them, or delete them after a specified period of time.

### Remediation

For information about configuring lifecycle policies on an Amazon S3 bucket, see [Setting lifecycle configuration on a bucket](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md") and
see [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the _Amazon S3 User Guide_.

## [S3.14] S3 general purpose buckets should have versioning enabled

**Category:** Protect > Data protection > Data deletion protection

**Related requirements:** NIST.800-53.r5 AU-9(2),
NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5
CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12,
NIST.800-53.r5 SI-13(5), NIST.800-171.r2 3.3.8

**Severity:** Low

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-versioning-enabled](../../../config/latest/developerguide/s3-bucket-versioning-enabled.md "../../../config/latest/developerguide/s3-bucket-versioning-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket has versioning enabled. The control fails if versioning is
suspended for the bucket.

Versioning keeps multiple variants of an object in the same S3 bucket. You can use
versioning to preserve, retrieve, and restore earlier versions of an object stored in your S3
bucket. Versioning helps you recover from both unintended user actions and application
failures.

###### Tip

As the number of objects increases in a bucket because of versioning, you can set up a Lifecycle configuration to
automatically archive or delete versioned objects based on rules. For more information, see
[Amazon S3 Lifecycle Management for Versioned Objects](https://aws.amazon.com/blogs/aws/amazon-s3-lifecycle-management-update/ "https://aws.amazon.com/blogs/aws/amazon-s3-lifecycle-management-update/").

### Remediation

To use versioning on an S3 bucket, see [Enabling versioning on buckets](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md") in the _Amazon S3 User Guide_.

## [S3.15] S3 general purpose buckets should have Object Lock enabled

**Category:** Protect > Data protection > Data deletion protection

**Related requirements:** NIST.800-53.r5 CP-6(2), PCI DSS v4.0.1/10.5.1

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-default-lock-enabled](../../../config/latest/developerguide/s3-bucket-default-lock-enabled.md "../../../config/latest/developerguide/s3-bucket-default-lock-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter | Description                   | Type | Allowed custom values      | Security Hub CSPM default value |
| --------- | ----------------------------- | ---- | -------------------------- | ------------------------------- |
| `mode`    | S3 Object Lock retention mode | Enum | `GOVERNANCE`, `COMPLIANCE` | No default value                |

This control checks whether an Amazon S3 general purpose bucket has Object Lock enabled. The control fails if Object Lock
isn't enabled for the bucket. If you provide a custom value for the `mode` parameter, the control passes only if
S3 Object Lock uses the specified retention mode.

You can use S3 Object Lock to store objects using a write-once-read-many (WORM) model. Object Lock can help prevent
objects in S3 buckets from being deleted or overwritten for a fixed amount of time or indefinitely. You can use S3 Object
Lock to meet regulatory requirements that require WORM storage, or add an extra layer of protection against object changes
and deletion.

### Remediation

To configure Object Lock for new and existing S3 buckets, see [Configuring S3 Object Lock](../../../AmazonS3/latest/userguide/object-lock-configure.md "../../../AmazonS3/latest/userguide/object-lock-configure.md") in the _Amazon S3 User Guide_.

## [S3.17] S3 general purpose buckets should be encrypted at rest with AWS KMS keys

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Related requirements:** NIST.800-53.r5 SC-12(2),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 SI-7(6),
NIST.800-53.r5 AU-9, NIST.800-171.r2 3.8.9, NIST.800-171.r2 3.13.11, NIST.800-171.r2
3.13.16, PCI DSS v4.0.1/3.5.1

**Severity:** Medium

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-default-encryption-kms](../../../config/latest/developerguide/s3-default-encryption-kms.md "../../../config/latest/developerguide/s3-default-encryption-kms.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 general purpose bucket is encrypted with an AWS KMS key (SSE-KMS or DSSE-KMS).
The control fails if the bucket is encrypted with default encryption (SSE-S3).

Server-side encryption (SSE) is the encryption of data at its destination by the application or service that
receives it. Unless you specify otherwise, S3 buckets use Amazon S3 managed keys (SSE-S3) by default for server-side encryption. However, for
added control, you can choose to configure buckets to use server-side encryption with AWS KMS keys (SSE-KMS or DSSE-KMS) instead.
Amazon S3 encrypts your data at the object level as it writes it to disks in AWS data centers and decrypts it for you
when you access it.

### Remediation

To encrypt an S3 bucket using SSE-KMS, see [Specifying server-side encryption with AWS KMS (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the _Amazon S3 User Guide_.
To encrypt an S3 bucket using DSSE-KMS, see [Specifying dual-layer server-side encryption with AWS KMS keys (DSSE-KMS)](../../../AmazonS3/latest/userguide/specifying-dsse-encryption.md "../../../AmazonS3/latest/userguide/specifying-dsse-encryption.md")
in the _Amazon S3 User Guide_.

## [S3.19] S3 access points should have block public access settings enabled

**Related requirements:** NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3,
NIST.800-53.r5 AC-3(7),
NIST.800-53.r5 AC-4,
NIST.800-53.r5 AC-4(21),
NIST.800-53.r5 AC-6,
NIST.800-53.r5 SC-7,
NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16),
NIST.800-53.r5 SC-7(20),
NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3),
NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::S3::AccessPoint`

**AWS Config rule:**
[s3-access-point-public-access-blocks](../../../config/latest/developerguide/s3-access-point-public-access-blocks.md "../../../config/latest/developerguide/s3-access-point-public-access-blocks.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 access point has block public access settings enabled. The control fails if block
public access settings aren't enabled for the access point.

The Amazon S3 Block Public Access feature helps you manage access to your S3 resources at three levels: the account, bucket,
and access point levels. The settings at each level can be configured independently, allowing you to have different
levels of public access restrictions for your data. The access point settings can't individually override the more
restrictive settings at higher levels (account level or bucket assigned to the access point). Instead, the settings at
the access point level are additive, meaning they complement and work alongside the settings at the other levels.
Unless you intend an S3 access point to be publicly accessible, you should enable block public access settings.

### Remediation

Amazon S3 currently doesn't support changing an access point's block public access settings after the access point has
been created. All block public access settings are enabled by default when you create a new access point. We recommend that you
keep all settings enabled unless you know that you have a specific need to disable any of them. For more information, see
[Managing public access to access points](../../../AmazonS3/latest/userguide/access-points-bpa-settings.md "../../../AmazonS3/latest/userguide/access-points-bpa-settings.md")
in the _Amazon Simple Storage Service User Guide_.

## [S3.20] S3 general purpose buckets should have MFA delete enabled

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.1.2, CIS AWS Foundations Benchmark v3.0.0/2.1.2, CIS AWS Foundations Benchmark v1.4.0/2.1.3, NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2,
NIST.800-53.r5 CM-2(2),
NIST.800-53.r5 CM-3,
NIST.800-53.r5 SC-5(2)

**Category:** Protect > Data protection > Data deletion protection

**Severity:** Low

**Resource type:**
`AWS::S3::Bucket`

**AWS Config rule:**
[s3-bucket-mfa-delete-enabled](../../../config/latest/developerguide/s3-bucket-mfa-delete-enabled.md "../../../config/latest/developerguide/s3-bucket-mfa-delete-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether multi-factor authentication (MFA) delete is enabled for an
Amazon S3 general purpose bucket. The control fails if MFA delete is not enabled for the
bucket. The control doesn't produce findings for buckets that have a lifecycle
configuration.

If you enable versioning for an S3 general purpose bucket, you can optionally add
another layer of security by configuring MFA delete for the bucket. If you do this, the
bucket owner must include two forms of authentication in any request to delete a version
of an object in the bucket or change the versioning state of the bucket. MFA delete
provides added security if, for example, the bucket owner’s security credentials are
compromised. MFA delete can also help prevent accidental bucket deletions by requiring
the user who initiates the delete action to prove physical possession of an MFA device
with an MFA code, which adds an extra layer of friction and security to the delete
action.

###### Note

This control produces a `PASSED` finding only if MFA delete is enabled for the
S3 general purpose bucket. To enable MFA delete for a bucket, versioning must also
be enabled for the bucket. Bucket versioning is a method of storing multiple
variations of an S3 object in the same bucket. In addition, only the bucket owner
who is logged in as a root user can enable MFA delete and perform delete actions on
the bucket. You cannot use MFA delete with a bucket that has a lifecycle
configuration.

### Remediation

For information about enabling versioning and configuring MFA delete for an S3
bucket, see [Configuring
MFA delete](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md") in the _Amazon Simple Storage Service User Guide_.

## [S3.22] S3 general purpose buckets should log object-level write events

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/3.8, CIS AWS Foundations Benchmark v3.0.0/3.8, PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::::Account`

**AWS Config rule:**
[cloudtrail-all-write-s3-data-event-check](../../../config/latest/developerguide/cloudtrail-all-write-s3-data-event-check.md "../../../config/latest/developerguide/cloudtrail-all-write-s3-data-event-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an AWS account has at least one AWS CloudTrail multi-Region trail that logs all write data
events for Amazon S3 buckets. The control fails if the account doesn't have a multi-Region trail that logs write data events for S3
buckets.

S3 object-level operations, such as `GetObject`, `DeleteObject`, and `PutObject`,
are called data events. By default, CloudTrail doesn't log data events, but you can configure trails to log data events for S3 buckets.
When you enable object-level logging for write data events, you can log each individual object (file) access within an S3 bucket.
Enabling object-level logging can help you meet data compliance requirements, perform comprehensive security analysis, monitor
specific patterns of user behavior in your AWS account, and take action on object-level API activity within your S3 buckets by
using Amazon CloudWatch Events. This control produces a `PASSED` finding if you configure a multi-Region trail that logs write-only or
all types of data events for all S3 buckets.

### Remediation

To enable object-level logging for S3 buckets, see
[Enabling CloudTrail event logging for S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md")
in the _Amazon Simple Storage Service User Guide_.

## [S3.23] S3 general purpose buckets should log object-level read events

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/3.9, CIS AWS Foundations Benchmark v3.0.0/3.9, PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::::Account`

**AWS Config rule:**
[cloudtrail-all-read-s3-data-event-check](../../../config/latest/developerguide/cloudtrail-all-read-s3-data-event-check.md "../../../config/latest/developerguide/cloudtrail-all-read-s3-data-event-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an AWS account has at least one AWS CloudTrail multi-Region trail that logs all read data
events for Amazon S3 buckets. The control fails if the account doesn't have a multi-Region trail that logs read data events for S3
buckets.

S3 object-level operations, such as `GetObject`, `DeleteObject`, and `PutObject`,
are called data events. By default, CloudTrail doesn't log data events, but you can configure trails to log data events for S3 buckets.
When you enable object-level logging for read data events, you can log each individual object (file) access within an S3 bucket.
Enabling object-level logging can help you meet data compliance requirements, perform comprehensive security analysis, monitor
specific patterns of user behavior in your AWS account, and take action on object-level API activity within your S3 buckets by
using Amazon CloudWatch Events. This control produces a `PASSED` finding if you configure a multi-Region trail that logs read-only or
all types of data events for all S3 buckets.

### Remediation

To enable object-level logging for S3 buckets, see
[Enabling CloudTrail event logging for S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md")
in the _Amazon Simple Storage Service User Guide_.

## [S3.24] S3 Multi-Region Access Points should have block public access settings enabled

**Related requirements:** PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:**
`AWS::S3::MultiRegionAccessPoint`

**AWS Config rule:**
`s3-mrap-public-access-blocked` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon S3 Multi-Region Access Point has block public access settings enabled. The control
fails when the Multi-Region Access Point doesn't have block public access settings enabled.

Publicly accessible resources can be lead to unauthorized access, data breaches, or exploitation of vulnerabilities.
Restricting access through authentication and authorization measures helps to safeguard sensitive information and maintain the
integrity of your resources.

### Remediation

By default, all Block Public Access settings are enabled for an S3 Multi-Region Access Point. For more
information , see [Blocking public access with Amazon S3 Multi-Region Access Points](../../../AmazonS3/latest/userguide/multi-region-access-point-block-public-access.md "../../../AmazonS3/latest/userguide/multi-region-access-point-block-public-access.md") in the _Amazon Simple Storage Service User Guide_. You
can't change the Block Public Access settings for a Multi-Region Access Point after it has been created.

## [S3.25] S3 directory buckets should have lifecycle

configurations

**Category:** Protect > Data Protection

**Severity:** Low

**Resource type:**
`AWS::S3Express::DirectoryBucket`

**AWS Config rule:** [s3express-dir-bucket-lifecycle-rules-check](../../../config/latest/developerguide/s3express-dir-bucket-lifecycle-rules-check.md "../../../config/latest/developerguide/s3express-dir-bucket-lifecycle-rules-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter              | Description                                                               | Type    | Allowed custom values | Security Hub CSPM default value |
| ---------------------- | ------------------------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `targetExpirationDays` | The number of days, after object creation, when objects should<br>expire. | Integer | `1` to `2147483647`   | No default value                |

This control checks whether lifecycle rules are configured for an S3 directory bucket.
The control fails if lifecycle rules aren't configured for the directory bucket, or a
lifecycle rule for the bucket specifies expiration settings that don't match the
parameter value that you optionally specify.

In Amazon S3, a lifecycle configuration is a set of rules that define actions for Amazon S3 to
apply to a group of objects in a bucket. For an S3 directory bucket, you can create a
lifecycle rule that specifies when objects expire based on age (in days). You can also
create a lifecycle rule that deletes incomplete multipart uploads. Unlike other types of
S3 buckets, such as general purpose buckets, directory buckets do not support other
types of actions for lifecycle rules, such as transitioning objects between storage
classes.

### Remediation

To define a lifecycle configuration for an S3 directory bucket, create a lifecycle
rule for the bucket. For more information, see [Creating and
managing a lifecycle configuration for your directory bucket](../../../AmazonS3/latest/userguide/directory-bucket-create-lc.md "../../../AmazonS3/latest/userguide/directory-bucket-create-lc.md") in the
_Amazon Simple Storage Service User Guide_.
