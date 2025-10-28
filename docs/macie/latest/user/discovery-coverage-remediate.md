# Remediating coverage issues for automated sensitive data discovery

As automated sensitive data discovery progresses each day, Amazon Macie provides statistics and details to help you
assess and monitor its coverage of your Amazon Simple Storage Service (Amazon S3) data estate. By [reviewing coverage data](discovery-coverage-review.md "discovery-coverage-review.md"), you can check the status of
automated sensitive data discovery for your data estate overall and individual S3 buckets within it. You can also
identify issues that prevented Macie from analyzing objects in specific buckets. If you remediate
the issues, you can increase coverage of your Amazon S3 data during subsequent analysis cycles.

Macie reports several types of issues that reduce coverage of your Amazon S3 data by automated sensitive data discovery.
This includes bucket-level issues that prevent Macie from analyzing any objects in an S3 bucket.
It also includes object-level issues. These issues, referred to as _classification errors_, prevented Macie from analyzing specific objects in a bucket.
The following information can help you investigate and remediate the issues.

###### Issue types and details

- [Access denied](#discovery-issues-access-denied "#discovery-issues-access-denied")
- [Classification error: Invalid content](#discovery-issues-invalid-content "#discovery-issues-invalid-content")
- [Classification error:
  Invalid encryption](#discovery-issues-classification-error-invalid-encryption "#discovery-issues-classification-error-invalid-encryption")
- [Classification error:
  Invalid KMS key](#discovery-issues-classification-error-invalid-key "#discovery-issues-classification-error-invalid-key")
- [Classification error:
  Permission denied](#discovery-issues-classification-error-permission-denied "#discovery-issues-classification-error-permission-denied")
- [Unclassifiable](#discovery-issues-unclassifiable "#discovery-issues-unclassifiable")

###### Tip

To investigate object-level classification errors for an S3 bucket, start by reviewing the
list of object samples for the bucket. This list indicates which objects Macie analyzed or
attempted to analyze in the bucket, for up to 100 objects.

To review the list on the Amazon Macie console, choose the bucket on the **S3
buckets** page, and then choose the **Object samples** tab in the
details panel. To review the list programmatically, use the [ListResourceProfileArtifacts](../APIReference/resource-profiles-artifacts.md "../APIReference/resource-profiles-artifacts.md") operation of the Amazon Macie API. If the status of the
analysis for an object is **Skipped** (`SKIPPED`), the object might
have caused the error.

## Access denied

This issue indicates that an S3 bucket's permissions settings prevent Macie from accessing
the bucket and the bucket’s objects. Macie can't retrieve and analyze any objects in the
bucket.

Details

The most common cause for this type of issue is a restrictive bucket policy. A _bucket policy_ is a resource-based AWS Identity and Access Management (IAM) policy that
specifies which actions a principal (user, account, service, or other entity) can perform on
an S3 bucket, and the conditions under which a principal can perform those actions. A
_restrictive bucket policy_ uses explicit
`Allow` or `Deny` statements that grant or restrict access to a
bucket's data based on specific conditions. For example, a bucket policy might contain an
`Allow` or `Deny` statement that denies access to a bucket unless
specific source IP addresses are used to access the bucket.

If the bucket policy for an S3 bucket contains an explicit `Deny` statement
with one or more conditions, Macie might not be allowed to retrieve and analyze the bucket’s
objects to detect sensitive data. Macie can only provide a subset of information about the
bucket, such as the bucket's name and creation date.

Remediation guidance

To remediate this issue, update the bucket policy for the S3 bucket. Ensure that the
policy allows Macie to access the bucket and the bucket’s objects. To allow this access, add
a condition for the Macie service-linked role (`AWSServiceRoleForAmazonMacie`) to
the policy. The condition should exclude the Macie service-linked role from matching the
`Deny` restriction in the policy. It can do this by using the
`aws:PrincipalArn` global condition context key and the Amazon Resource Name
(ARN) of the Macie service-linked role for your account.

If you update the bucket policy and Macie gains access to the S3 bucket, Macie will
detect the change. When this happens, Macie will update statistics, inventory data, and other
information that it provides about your Amazon S3 data. In addition, the bucket's objects will be
a higher priority for analysis during a subsequent analysis cycle.

Additional reference

For more information about updating an S3 bucket policy to allow Macie to access a
bucket, see [Allowing Macie to access S3 buckets and
objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md"). For information about using bucket
policies to control access to buckets, see [Bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") and [How Amazon S3 authorizes a request](../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md "../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md") in the _Amazon Simple Storage Service User
Guide_.

## Classification error: Invalid content

This type of classification error occurs if Macie attempts to analyze an object in an S3
bucket and the object is malformed or the object contains content that exceeds a sensitive data
discovery quota. Macie can't analyze the object.

Details

This error typically occurs because an S3 object is a malformed or corrupted file.
Consequently, Macie can't parse and analyze all the data in the file.

This error can also occur if analysis of an S3 object would exceed a sensitive data
discovery quota for an individual file. For example, the storage size of the object exceeds
the size quota for that type of file.

For either case, Macie can't complete its analysis of the S3 object and the status of
the analysis for the object is **Skipped** (`SKIPPED`).

Remediation guidance

To investigate this error, download the S3 object and check the formatting and contents
of the file. Also assess the contents of the file against Macie quotas for sensitive data
discovery.

If you don't remediate this error, Macie will try to analyze other objects in the S3
bucket. If Macie analyzes another object successfully, Macie will update coverage data and
other information that it provides about the bucket.

Additional reference

For a list of sensitive data discovery quotas, including the quotas for certain types of
files, see [Quotas for Macie](macie-quotas.md "macie-quotas.md"). For information about
how Macie updates sensitivity scores and other information that it provides about S3 buckets,
see [How automated sensitive data discovery works](discovery-asdd-how-it-works.md "discovery-asdd-how-it-works.md").

## Classification error:

Invalid encryption

This type of classification error occurs if Macie attempts to analyze an object in an S3
bucket and the object is encrypted with a customer-provided key. The object uses SSE-C
encryption, which means that Macie can't retrieve and analyze the object.

Details

Amazon S3 supports multiple encryption options for S3 objects. For most of these options,
Macie can decrypt an object by using the Macie service-linked role for your account. However,
this depends on the type of encryption that was used.

For Macie to decrypt an S3 object, the object must be encrypted with a key that Macie
can access and is allowed to use. If an object is encrypted with a customer-provided key,
Macie can't provide the requisite key material to retrieve the object from Amazon S3.
Consequently, Macie can't analyze the object and the status of the analysis for the object is
**Skipped** (`SKIPPED`).

Remediation guidance

To remediate this error, encrypt S3 objects with Amazon S3 managed keys or AWS Key Management Service (AWS KMS)
keys. If you prefer to use AWS KMS keys, the keys can be AWS managed KMS keys, or customer
managed KMS keys that Macie is allowed to use.

To encrypt existing S3 objects with keys that Macie can access and use, you can change
the encryption settings for the objects. To encrypt new objects with keys that Macie can
access and use, change the default encryption settings for the S3 bucket. Also ensure that
the bucket's policy doesn't require new objects to be encrypted with a customer-provided
key.

If you don't remediate this error, Macie will try to analyze other objects in the S3
bucket. If Macie analyzes another object successfully, Macie will update coverage data and
other information that it provides about the bucket.

Additional reference

For information about requirements and options for using Macie to analyze encrypted S3
objects, see [Analyzing encrypted Amazon S3 objects](discovery-supported-encryption-types.md "discovery-supported-encryption-types.md"). For information about encryption
options and settings for S3 buckets, see [Protecting data with encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md")
and [Setting default server-side encryption behavior for S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the _Amazon Simple Storage Service User Guide_.

## Classification error:

Invalid KMS key

This type of classification error occurs if Macie attempts to analyze an object in an S3
bucket and the object is encrypted with an AWS Key Management Service (AWS KMS) key that's no longer available.
Macie can't retrieve and analyze the object.

Details

AWS KMS provides options for disabling and deleting customer managed AWS KMS keys. If
an S3 object is encrypted with a KMS key that is disabled, is scheduled for deletion, or
was deleted, Macie can't retrieve and decrypt the object. Consequently, Macie can't analyze
the object and the status of the analysis for the object is **Skipped**
(`SKIPPED`). For Macie to analyze an encrypted object, the object must be
encrypted with a key that Macie can access and is allowed to use.

Remediation guidance

To remediate this error, re-enable the applicable AWS KMS key or cancel the scheduled
deletion of the key, depending on the current status of the key. If the applicable key was
already deleted, this error cannot be remediated.

To determine which AWS KMS key was used to encrypt an S3 object, you can start by
using Macie to review the server-side encryption settings for the S3 bucket. If the default
encryption settings for the bucket are configured to use a KMS key, the bucket's details
indicate which key is used. You can then check the status of that key. Alternatively, you can
use Amazon S3 to review the encryption settings for the bucket and individual objects in the
bucket.

If you don't remediate this error, Macie will try to analyze other objects in the S3
bucket. If Macie analyzes another object successfully, Macie will update coverage data and
other information that it provides about the bucket.

Additional reference

For information about using Macie to review the server-side encryption settings for an
S3 bucket, see [Reviewing the details of S3
buckets](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details"). For information about re-enabling an
AWS KMS key or canceling the scheduled deletion of a key, see [Enabling and disabling keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") and
[Deleting
keys](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md") in the _AWS Key Management Service Developer Guide_.

## Classification error:

Permission denied

This type of classification error occurs if Macie attempts to analyze an object in an S3
bucket and Macie can't retrieve or decrypt the object due to the permissions settings for the
object or the permissions settings for the key that was used to encrypt the object. Macie can't
retrieve and analyze the object.

Details

This error typically occurs because an S3 object is encrypted with a customer managed
AWS Key Management Service (AWS KMS) key that Macie isn’t allowed to use. If an object is encrypted with a
customer managed AWS KMS key, the key's policy must allow Macie to decrypt data by using
the key.

This error can also occur if Amazon S3 permissions settings prevent Macie from retrieving an
S3 object. The bucket policy for the S3 bucket might restrict access to specific bucket
objects or allow only certain principals (users, accounts, services, or other entities) to
access the objects. Or the access control list (ACL) for an object might restrict access to
the object. Consequently, Macie might not be allowed to access the object.

For any of the preceding cases, Macie can't retrieve and analyze the object, and the
status of the analysis for the object is **Skipped**
(`SKIPPED`).

Remediation guidance

To remediate this error, determine whether the S3 object is encrypted with a customer
managed AWS KMS key. If it is, ensure that the key's policy allows the Macie
service-linked role (`AWSServiceRoleForAmazonMacie`) to decrypt data with the key.
How you allow this access depends on whether the account that owns the AWS KMS key also
owns the S3 bucket that stores the object. If the same account owns the KMS key and the
bucket, a user of the account has to update the key's policy. If one account owns the
KMS key and a different account owns the bucket, a user of the account that owns the key
has to allow cross-account access to the key.

###### Tip

You can automatically generate a list of all the customer managed AWS KMS keys that
Macie needs to access to analyze objects in the S3 buckets for your account. To do this, run
the AWS KMS Permission Analyzer script, which is available from the [Amazon Macie Scripts](https://github.com/aws-samples/amazon-macie-scripts "https://github.com/aws-samples/amazon-macie-scripts")
repository on GitHub. The script can also generate an additional script of AWS Command Line Interface (AWS CLI)
commands. You can optionally run those commands to update the requisite configuration
settings and policies for KMS keys that you specify.

If Macie is already allowed to use the applicable AWS KMS key or the S3 object isn't
encrypted with a customer managed KMS key, ensure that the bucket's policy allows Macie to
access the object. Also verify that the object's ACL allows Macie to read the object's data
and metadata.

For the bucket policy, you can allow this access by adding a condition for the Macie
service-linked role to the policy. The condition should exclude the Macie service-linked role
from matching the `Deny` restriction in the policy. It can do this by using the
`aws:PrincipalArn` global condition context key and the Amazon Resource Name
(ARN) of the Macie service-linked role for your account.

For the object ACL, you can allow this access by working with the object owner to add
your AWS account as a grantee with `READ` permissions for the object. Macie can
then use the service-linked role for your account to retrieve and analyze the object. Also
consider changing the Object Ownership settings for the bucket. You can use these settings to
disable ACLs for all the objects in the bucket and grant ownership permissions to the account
that owns the bucket.

If you don't remediate this error, Macie will try to analyze other objects in the S3
bucket. If Macie analyzes another object successfully, Macie will update coverage data and
other information that it provides about the bucket.

Additional reference

For more information about allowing Macie to decrypt data with a customer managed
AWS KMS key, see [Allowing Macie to use a
customer managed AWS KMS key](discovery-supported-encryption-types.md#discovery-supported-encryption-cmk-configuration "discovery-supported-encryption-types.md#discovery-supported-encryption-cmk-configuration"). For information about
updating an S3 bucket policy to allow Macie to access a bucket, see [Allowing Macie to access S3 buckets and
objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

For information about updating a key policy, see [Changing a key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in
the _AWS Key Management Service Developer Guide_. For information about using customer
managed AWS KMS keys to encrypt S3 objects, see [Using server-side encryption with
AWS KMS keys](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the _Amazon Simple Storage Service User Guide_.

For information about using bucket policies to control access to S3 buckets, see [Access
control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") and [How Amazon S3 authorizes a
request](../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md "../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md") in the _Amazon Simple Storage Service User Guide_. For information about using
ACLs or Object Ownership settings to control access to S3 objects, see [Managing access with
ACLs](../../../AmazonS3/latest/userguide/acls.md "../../../AmazonS3/latest/userguide/acls.md") and [Controlling ownership of objects
and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the _Amazon Simple Storage Service User
Guide_.

## Unclassifiable

This issue indicates that all the objects in an S3 bucket are stored using unsupported Amazon S3
storage classes or unsupported file or storage formats. Macie can't analyze any objects in the
bucket.

Details

To be eligible for selection and analysis, an S3 object must use an Amazon S3 storage class
that Macie supports. The object must also have a file name extension for a file or storage
format that Macie supports. If an object doesn't meet these criteria, the object is treated
as an _unclassifiable object_. Macie doesn't attempt to
retrieve or analyze data in unclassifiable objects.

If all the objects in an S3 bucket are unclassifiable objects, the overall bucket is an
_unclassifiable bucket_. Macie can't perform automated sensitive data discovery for
the bucket.

Remediation guidance

To address this issue, review lifecycle configuration rules and other settings that
determine which storage classes are used to store objects in the S3 bucket. Consider
adjusting those settings to use storage classes that Macie supports. You can also change the
storage class of existing objects in the bucket.

Also assess the file and storage formats of existing objects in the S3 bucket. To
analyze the objects, consider porting the data, either temporarily or permanently, to new
objects that use a supported format.

If objects are added to the S3 bucket and they use a supported storage class and format,
Macie will detect the objects the next time it evaluates your bucket inventory. When this
happens, Macie will stop reporting that the bucket is _unclassifiable_ in statistics, coverage data, and other information that it
provides about your Amazon S3 data. In addition, the new objects will be a higher priority for
analysis during a subsequent analysis cycle.

Additional reference

For information about the Amazon S3 storage classes and the file and storage formats that
Macie supports, see [Supported storage classes and formats](discovery-supported-storage.md "discovery-supported-storage.md"). For information about lifecycle configuration
rules and the storage class options that Amazon S3 provides, see [Managing your storage
lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") and [Using Amazon S3 storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md")
in the _Amazon Simple Storage Service User Guide_.
