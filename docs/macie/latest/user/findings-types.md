# Types of Macie findings

Amazon Macie generates two categories of findings: _policy
findings_ and _sensitive data findings_. A _policy finding_ is a detailed report of a potential policy violation or
issue with the security or privacy of an Amazon Simple Storage Service (Amazon S3) general purpose bucket. Macie generates
policy findings as part of its ongoing activities to evaluate and monitor your general purpose
buckets for security and access control. A _sensitive data
finding_ is a detailed report of sensitive data that Macie detected in an S3 object.
Macie generates sensitive data findings as part of the activities that it performs when you run
sensitive data discovery jobs or it performs automated sensitive data discovery.

Within each category, there are specific types. A finding's type provides insight into the
nature of the issue or sensitive data that Macie found. A finding's details provide a [severity rating](findings-severity.md "findings-severity.md"), information about the affected resource, and
additional information, such as when and how Macie found the issue or sensitive data. The severity
and details of each finding vary depending on the type and nature of the finding.

###### Topics

- [Types of policy findings](#findings-policy-types "#findings-policy-types")
- [Types of sensitive data findings](#findings-sensitive-data-types "#findings-sensitive-data-types")

###### Tip

To explore and learn about the different categories and types of findings that Macie can
generate, [create sample findings](findings-samples.md "findings-samples.md"). Sample findings use
example data and placeholder values to demonstrate the kinds of information that each type of
finding might contain.

## Types of policy findings

Amazon Macie generates a policy finding when the policies or settings for an S3 general purpose
bucket are changed in a way that reduces the security or privacy of the bucket and the bucket's
objects. For information about how Macie detects and evaluates these changes, see [How Macie monitors Amazon S3 data
security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md").

Note that Macie generates a policy finding only if the change occurs after you enable Macie
for your AWS account. For example, if block public access settings are disabled for an S3
bucket after you enable Macie, Macie generates a
**Policy:IAMUser/S3BlockPublicAccessDisabled** finding for the bucket. If block
public access settings were disabled for a bucket when you enabled Macie and they continue to be
disabled, Macie doesn't generate a
**Policy:IAMUser/S3BlockPublicAccessDisabled** finding for the bucket.

If Macie detects a subsequent occurrence of an existing policy finding, Macie updates the
existing finding by adding details about the subsequent occurrence and incrementing the count of
occurrences. Macie stores policy findings for 90 days.

Macie can generate the following types of policy findings for an S3 general purpose
bucket.

**Policy:IAMUser/S3BlockPublicAccessDisabled**

All bucket-level block public access settings were disabled for the bucket. Public access
to the bucket is controlled by the block public access settings for the account, access
control lists (ACLs), the bucket policy for the bucket, and other settings and policies that
apply to the bucket.

To investigate the finding, start by [reviewing the bucket’s details](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details") in Macie. The details include a breakdown of the
bucket's public access settings. For detailed information about the settings, see [Access
control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") and [Blocking public
access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon Simple Storage Service User
Guide_.

**Policy:IAMUser/S3BucketEncryptionDisabled**

Default encryption settings for the bucket were reset to default Amazon S3 encryption
behavior, which is to encrypt new objects automatically with an Amazon S3 managed key.

Starting January 5, 2023, Amazon S3 automatically applies server-side encryption with Amazon S3
managed keys (SSE-S3) as the base level of encryption for objects that are added to buckets. You can optionally configure a
bucket's default encryption settings to instead use server-side encryption with an AWS KMS key (SSE-KMS) or dual-layer server-side
encryption with an AWS KMS key (DSSE-KMS). If Macie generated this type of finding prior to January 5, 2023, the
finding indicates that default encryption settings were disabled for the affected bucket. This
meant that the bucket’s settings didn’t specify default server-side encryption behavior for
new objects. The ability to disable default encryption settings for a bucket is no longer
supported by Amazon S3.

To learn about default encryption settings and options for S3 buckets, see [Setting default
server-side encryption behavior for S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the _Amazon Simple Storage Service User Guide_.

**Policy:IAMUser/S3BucketPublic**

An ACL or bucket policy for the bucket was changed to allow access by anonymous users or
all authenticated AWS Identity and Access Management (IAM) identities.

To investigate the finding, start by [reviewing the bucket’s details](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details") in Macie. The details include a breakdown of the
bucket's public access settings. For detailed information about ACLs, bucket policies, and
access settings for S3 buckets, see [Access control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the
_Amazon Simple Storage Service User Guide_.

**Policy:IAMUser/S3BucketReplicatedExternally**

Replication was enabled and configured to replicate objects from the bucket to a bucket
for an AWS account that's external to (not part of) your organization. An _organization_ is a set of Macie accounts that are centrally managed
as a group of related accounts through AWS Organizations or by Macie invitation.

Under certain conditions, Macie might generate this type of finding for a bucket that
isn’t configured to replicate objects to a bucket for an external AWS account. This can
occur if the destination bucket was created in a different AWS Region during the preceding
24 hours, after Macie retrieved bucket and object metadata from Amazon S3 as part of the [daily refresh cycle](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh").

To investigate the finding, start by refreshing your inventory data in Macie. Then [review the bucket’s details](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details"). The
details indicate whether the bucket is configured to replicate objects to other buckets. If
the bucket is configured to do this, the details include the account ID for each account that
owns a destination bucket. For detailed information about replication settings for S3 buckets,
see [Replicating
objects](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") in the _Amazon Simple Storage Service User Guide_.

**Policy:IAMUser/S3BucketSharedExternally**

An ACL or bucket policy for the bucket was changed to allow the bucket to be shared with
an AWS account that's external to (not part of) your organization. An _organization_ is a set of Macie accounts that are centrally managed
as a group of related accounts through AWS Organizations or by Macie invitation.

In certain cases, Macie might generate this type of finding for a bucket that isn’t
shared with an external AWS account. This can occur if Macie isn’t able to fully evaluate
the relationship between the `Principal` element in the bucket’s policy and certain
[AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") or [Amazon S3
condition keys](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys") in the `Condition` element of the policy. This can be the
case for the following condition keys: `aws:PrincipalAccount`,
`aws:PrincipalArn`, `aws:PrincipalOrgID`,
`aws:PrincipalOrgPaths`, `aws:PrincipalTag`,
`aws:PrincipalType`, `aws:SourceAccount`, `aws:SourceArn`,
`aws:SourceIp`, `aws:SourceOrgID`, `aws:SourceOrgPaths`,
`aws:SourceVpc`, `aws:SourceVpce`, `aws:userid`,
`s3:DataAccessPointAccount`, and `s3:DataAccessPointArn`. We recommend
that you review the bucket’s policy to determine whether this access is intended and
safe.

To learn about ACLs and bucket policies for S3 buckets, see [Access control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the
_Amazon Simple Storage Service User Guide_.

**Policy:IAMUser/S3BucketSharedWithCloudFront**

The bucket policy for the bucket was changed to allow the bucket to be shared with an
Amazon CloudFront origin access identity (OAI), a CloudFront origin access control (OAC), or both a CloudFront OAI and a CloudFront OAC. A CloudFront OAI or OAC
allows users to access a bucket's objects through one or more specified CloudFront
distributions.

To learn about CloudFront OAIs and OACs, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the _Amazon CloudFront
Developer Guide_.

###### Note

In certain cases, Macie generates a
**Policy:IAMUser/S3BucketSharedExternally** finding instead of a
**Policy:IAMUser/S3BucketSharedWithCloudFront** finding for a bucket. These
cases are:

- The bucket is shared with an AWS account that's external to your organization, in
  addition to a CloudFront OAI or OAC.
- The bucket's policy specifies a canonical user ID, instead of the Amazon Resource Name
  (ARN), of a CloudFront OAI.
  This produces a higher severity policy finding for the bucket.

## Types of sensitive data findings

Amazon Macie generates a sensitive data finding when it detects sensitive data in an S3 object
that it analyzes to discover sensitive data. This includes analysis that Macie performs when you
run a sensitive data discovery job or it performs automated sensitive data discovery.

For example, if you create and run a sensitive data discovery job and Macie detects bank account numbers in an
S3 object, Macie generates a **SensitiveData:S3Object/Financial** finding for
the object. Similarly, if Macie detects bank account numbers in an S3 object that it analyzes
during an automated sensitive data discovery cycle, Macie generates a
**SensitiveData:S3Object/Financial** finding for the object.

If Macie detects sensitive data in the same S3 object during a subsequent job run or
automated sensitive data discovery cycle, Macie generates a new sensitive data finding for the object. Unlike policy
findings, all sensitive data findings are treated as new (unique). Macie stores sensitive data
findings for 90 days.

Macie can generate the following types of sensitive data findings for an S3 object.

**SensitiveData:S3Object/Credentials**

The object contains sensitive credentials data, such as AWS secret access keys or
private keys.

**SensitiveData:S3Object/CustomIdentifier**

The object contains text that matches the detection criteria of one or more custom data
identifiers. The object might contain more than one type of sensitive data.

**SensitiveData:S3Object/Financial**

The object contains sensitive financial information, such as bank account numbers or
credit card numbers.

**SensitiveData:S3Object/Multiple**

The object contains more than one category of sensitive data—any combination of
credentials data, financial information, personal information, or text that matches the
detection criteria of one or more custom data identifiers.

**SensitiveData:S3Object/Personal**

The object contains sensitive personal information—personally identifiable
information (PII) such as passport numbers or driver's license identification numbers,
personal health information (PHI) such as health insurance or medical identification numbers,
or a combination of PII and PHI.

For information about the types of sensitive data that Macie can detect using built-in
criteria and techniques, see [Using managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md"). For information about the types of S3 objects
that Macie can analyze, see [Supported storage classes and
formats](discovery-supported-storage.md "discovery-supported-storage.md").
