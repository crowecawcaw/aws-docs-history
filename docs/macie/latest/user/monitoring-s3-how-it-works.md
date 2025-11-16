# How Macie monitors Amazon S3 data security

When you enable Amazon Macie for your AWS account, Macie creates an AWS Identity and Access Management (IAM) [service-linked role](service-linked-roles.md "service-linked-roles.md") for your account in the
current AWS Region. The permissions policy for this role allows Macie to call other
AWS services and monitor AWS resources on your behalf. By using this role, Macie
generates and maintains an inventory of your Amazon Simple Storage Service (Amazon S3) general purpose buckets in the
Region. Macie also monitors and evaluates the buckets for security and access
control.

If you're the Macie administrator for an organization, the inventory includes statistical and other
data about S3 buckets for your account and member accounts in your organization. With this
data, you can use Macie to monitor and evaluate your organization’s security posture across
your Amazon S3 data estate. For more information, see [Managing multiple accounts](macie-accounts.md "macie-accounts.md").

###### Topics

- [Key
  components](#monitoring-s3-how-it-works-components "#monitoring-s3-how-it-works-components")
- [Data
  refreshes](#monitoring-s3-how-it-works-data-refresh "#monitoring-s3-how-it-works-data-refresh")
- [Considerations](#monitoring-s3-how-it-works-considerations "#monitoring-s3-how-it-works-considerations")

## Key components

Amazon Macie uses a combination of features and techniques to provide and maintain inventory
data for your S3 general purpose buckets, and to monitor and evaluate the buckets for
security and access control.

Gathering metadata and calculating
statistics

To generate and maintain metadata and statistics for your bucket inventory, Macie
retrieves bucket and object metadata directly from Amazon S3. For each bucket,
the metadata includes:

- General information about the bucket, such as the bucket’s name, Amazon Resource Name
  (ARN), creation date, encryption settings, tags, and the account ID
  for the AWS account that owns the bucket.
- Account-level permissions settings that apply to the bucket, such as the block public
  access settings for the account.
- Bucket-level permissions settings for the bucket, such as the block public access
  settings for the bucket and settings that derive from a bucket policy or
  access control list (ACL).
- Shared access and replication settings for the bucket, including whether
  bucket data is replicated to or shared with AWS accounts that aren’t part
  of your organization.
- Object counts and settings for objects in the bucket, such as the number
  of objects in the bucket and breakdowns of object counts by encryption type,
  file type, and storage class.

Macie provides this information to you directly. Macie also uses the information to
calculate statistics and provide assessments of the security and privacy of
your bucket inventory overall and individual buckets in your inventory. For
example, you can find the total storage size and number of buckets in your
inventory, the total storage size and number of objects in those buckets,
and the total storage size and number of objects that Macie can analyze to
detect sensitive data in the buckets.

By default, metadata and statistics include data for any object parts that exist due to
incomplete multipart uploads. If you manually refresh object metadata for a
specific bucket, Macie recalculates statistics for the bucket and your
bucket inventory overall, and excludes data for object parts from the
recalculated values. The next time Macie retrieves bucket and object
metadata from Amazon S3 as part of the daily refresh cycle, Macie updates your
inventory data and includes data for the object parts again. For information
about when Macie retrieves bucket and object metadata, see [Data refreshes](#monitoring-s3-how-it-works-data-refresh "#monitoring-s3-how-it-works-data-refresh").

It's important to note that Macie can’t analyze object parts to detect sensitive data.
Amazon S3 must first finish assembling the parts into one or more objects for
Macie to analyze. For information about multipart uploads and object
parts, including how to delete parts automatically with lifecycle rules,
see [Uploading and
copying objects using multipart upload](../../../AmazonS3/latest/userguide/mpuoverview.md "../../../AmazonS3/latest/userguide/mpuoverview.md") in the _Amazon Simple Storage Service User Guide_. To identify buckets
that contain object parts, you can refer to _incomplete multipart upload_ metrics in Amazon S3 Storage
Lens. For more information, see [Assessing your
storage activity and usage](../../../AmazonS3/latest/userguide/storage_lens.md "../../../AmazonS3/latest/userguide/storage_lens.md") in the _Amazon Simple Storage Service User Guide_.

Monitoring bucket security and privacy

To help ensure the accuracy of bucket-level data in your inventory, Macie
monitors and analyzes certain [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") events that can occur for Amazon S3 data. If a relevant
event occurs, Macie updates the appropriate inventory data.

For example, if you enable block public access settings for a bucket,
Macie updates all data about the bucket’s public access settings. Similarly,
if you add or update the bucket policy for a bucket, Macie analyzes the
policy and updates the appropriate data in your inventory.

If Macie determines that an event reduces the security
or privacy of a bucket, Macie also creates a [policy finding](findings-types.md#findings-policy-types "findings-types.md#findings-policy-types") for you to review
and remediate as necessary.

Macie monitors and analyzes data for the following CloudTrail events:

- **Account-level events** –
  DeletePublicAccessBlock and PutPublicAccessBlock
- **Bucket-level events** –
  CreateBucket, DeleteAccountPublicAccessBlock, DeleteBucket,
  DeleteBucketEncryption, DeleteBucketPolicy,
  DeleteBucketPublicAccessBlock, DeleteBucketReplication,
  DeleteBucketTagging, PutAccountPublicAccessBlock, PutBucketAcl,
  PutBucketEncryption, PutBucketPolicy, PutBucketPublicAccessBlock,
  PutBucketReplication, PutBucketTagging, and
  PutBucketVersioning

You can't enable monitoring for additional CloudTrail events or disable
monitoring for any of the preceding events. For detailed information about
corresponding operations for the preceding events, see the [Amazon Simple Storage Service API Reference](../../../AmazonS3/latest/API/API_Operations_Amazon_Simple_Storage_Service.md "../../../AmazonS3/latest/API/API_Operations_Amazon_Simple_Storage_Service.md").

###### Tip

To monitor object-level events, we recommend that you use the Amazon S3
protection feature of Amazon GuardDuty. This feature monitors object-level,
Amazon S3 data events and analyzes them for malicious and suspicious
activity. For more information, see [GuardDuty S3
Protection](../../../guardduty/latest/ug/s3-protection.md "../../../guardduty/latest/ug/s3-protection.md") in the _Amazon GuardDuty User
Guide_.

Evaluating bucket security and access
control

To evaluate bucket-level security and access control, Macie uses
automated, logic-based reasoning to analyze resource-based policies that
apply to a bucket. Macie also analyzes the account- and bucket-level
permissions settings that apply to a bucket. This analysis factors bucket
policies, bucket-level ACLs, and block public access settings for the
account and the bucket.

For resource-based policies, Macie uses [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/"). Zelkova is an automated reasoning engine that
translates AWS Identity and Access Management (IAM) policies into logical statements and runs a
suite of general-purpose and specialized logical solvers (_satisfiability modulo theories_) against the
decision problem. To learn more about the nature of the solvers that Zelkova
uses, see [Satisfiability Modulo Theories](https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf "https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf").

Macie applies Zelkova repeatedly to a resource-based policy, using
increasingly specific queries to characterize the classes of behaviors that
the policy allows. The analysis is designed to identify potential security
risks for your Amazon S3 data and minimize false negatives. It doesn’t include
AWS Organizations authorization policies that define the maximum available
permissions for your organization’s resources, such as service control
policies (SCPs) or resource control policies (RCPs). It also doesn’t include
key policies for associated AWS KMS keys. For example, if a bucket policy
uses the [s3:x-amz-server-side-encryption-aws-kms-key-id](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys") condition key to
restrict write access to the bucket, Macie doesn't analyze the key policy
for the specified key. This means that Macie might report that the bucket is
publicly accessible, depending on other components of the bucket policy and
Amazon S3 permissions settings that apply to the bucket.

In addition, when Macie assesses the security and privacy of a bucket, it
doesn’t examine access logs or analyze users, roles, and other relevant
configurations for accounts. Instead, Macie analyzes and reports data for
key settings that indicate _potential_
security risks. For example, if a policy finding indicates that a bucket is
publicly accessible, it doesn’t necessarily mean that an external entity
accessed the bucket. Similarly, if a policy finding indicates that a bucket
is shared with an AWS account outside your organization, Macie doesn’t
attempt to determine whether this access is intended and safe. Instead,
these findings indicate that an external entity can potentially access the
bucket's data, which may be an unintended security risk.

If Macie reports that an external entity can potentially access an S3
bucket, we recommend that you review the bucket’s policy and settings to
determine whether this access is intended and safe. If applicable, also
review policies and settings for associated resources, such as
AWS KMS keys, and AWS Organizations authorization policies for your
organization.

###### Important

To perform the preceding tasks for a bucket, the bucket must be an S3 general
purpose bucket. Macie doesn't monitor or analyze S3 directory buckets.

In addition, Macie must be allowed to access the bucket. If a bucket's permissions
settings prevent Macie from retrieving metadata for the bucket or the bucket's
objects, Macie can only provide a subset of information about the bucket, such as
the bucket's name and creation date. Macie can't perform any additional tasks for
the bucket. For more information, see [Allowing Macie to access S3
buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

Macie can perform the preceding tasks for up to 10,000 buckets for an account. If you store
more than 10,000 buckets in Amazon S3, Macie performs these tasks only for the 10,000
buckets that were most recently created or changed. For all other buckets, Macie
doesn't maintain complete inventory data, evaluate or monitor the security and
privacy of the buckets' data, or generate policy findings. Instead, Macie only
provides a subset of information about the buckets.

## Data refreshes

When you enable Amazon Macie for your AWS account, Macie retrieves metadata for your S3
general purpose buckets and objects directly from Amazon S3. Thereafter, Macie automatically
retrieves bucket and object metadata directly from Amazon S3 on a daily basis as part of a
daily refresh cycle.

Macie also retrieves bucket metadata directly from Amazon S3 when any of the following
occurs:

- Macie detects a relevant AWS CloudTrail event.
- You refresh your inventory data by choosing refresh (
  ![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
  ) on the Amazon Macie
  console. Depending on the size of your data estate, you can refresh the data as
  frequently as every five minutes.
- You submit a [DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md")
  request to the Amazon Macie API programmatically and Macie has finished processing
  any preceding **DescribeBuckets** requests.

Macie can also retrieve the latest object metadata for a specific bucket if you choose to
manually refresh that data. This can be helpful if you recently created a bucket or made
significant changes to a bucket's objects during the past 24 hours. To manually refresh
object metadata for a bucket, choose refresh (
![The refresh button, which is a button that displays an empty, dark gray circle with an arrow.](/images/macie/latest/user/images/btn-refresh-object-data.png)
) in the
**Object statistics** section of the [bucket details panel](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details") on the
**S3 buckets** page of the console. This feature is available for
buckets that store 30,000 or fewer objects.

To determine when Macie most recently retrieved bucket or object metadata for your
account, you can refer to the **Last updated** field on the console.
This field appears on the **Summary** dashboard, on the **S3
buckets** page, and in the [bucket details panel](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details") on the
**S3 buckets** page. If you use the Amazon Macie API to query
inventory data, the `lastUpdated` field provides this information. If you're
the Macie administrator for an organization, the field indicates the earliest date and time when
Macie retrieved the data for an account in your organization.

Each time Macie retrieves bucket or object metadata, Macie automatically updates the
appropriate data in your inventory. If Macie detects differences that affect the
security or privacy of a bucket, Macie immediately begins evaluating and analyzing the
changes. When the analysis is complete, Macie updates the appropriate data in your
inventory. If any differences reduce the security or privacy of a bucket, Macie also
creates the appropriate [policy findings](findings-types.md#findings-policy-types "findings-types.md#findings-policy-types") for
you to review and remediate as necessary. Macie does this for as many as 10,000 buckets
for your account. If you have more than 10,000 buckets, Macie does this for the 10,000
buckets that were most recently created or changed. If you're the Macie administrator for an
organization, this quota applies to each account in your organization, not your
organization overall.

On rare occasions under certain conditions, latency and other issues might prevent Macie
from retrieving bucket and object metadata. They might also delay notifications that Macie
receives about changes to your bucket inventory or the permissions settings and policies
for individual buckets. For example, delivery issues with CloudTrail events might cause delays.
If this happens, Macie analyzes new and updated data the next time it performs the daily
refresh, which is within 24 hours.

## Considerations

As you use Amazon Macie to monitor and assess the security posture of your Amazon S3 data,
keep the following in mind:

- Inventory data applies only to S3 general purpose buckets in the current
  AWS Region. To access the data for additional Regions, enable and use Macie in
  each additional Region.
- If you're the Macie administrator for an organization, you can access inventory data
  for a member account only if Macie is enabled for that account in the current
  Region.
- Macie can provide complete inventory data for no more than 10,000 buckets for
  an account. In addition, Macie can evaluate and monitor the security and privacy
  of no more than 10,000 buckets for an account. If your account exceeds this
  quota, Macie evaluates, monitors, and provides detailed information about the
  10,000 buckets that were most recently created or changed. For all other
  buckets, Macie only provides a subset of information about the buckets.

If your account approaches this quota, we notify you by creating an
AWS Health event for your account. We also send email to the address that’s
associated with your account. We notify you again if your account exceeds the
quota. If you're a Macie administrator, this quota applies to each account in your
organization, not your organization overall.

- If a bucket's permissions settings prevent Macie from retrieving information
  about the bucket or the bucket’s objects, Macie can't evaluate and monitor the
  security and privacy of the bucket's data or provide detailed information about
  the bucket. To help you identify a bucket where this is the case, Macie does the
  following:

      + In your bucket inventory on the console, Macie displays a warning icon
       (
      ![The warning icon, which is a red triangle that has an exclamation point in it.](images/icon-warning-red.png)
      ) for the bucket.
      + For the bucket's details, Macie provides data for only a subset of
       fields: the account ID for the AWS account that owns the bucket; the
       bucket's name, Amazon Resource Name (ARN), creation date, and Region;
       and, the date and time when Macie most recently retrieved both bucket
       and object metadata for the bucket as part of the daily refresh cycle.
       If you query inventory data programmatically with the Amazon Macie API,
       Macie also provides an error code and message for the bucket.
      + In the **Summary** dashboard on the console, the
       bucket has a value of **Unknown** for **Public
       access**, **Encryption**, and
       **Sharing** statistics. In addition, Macie excludes
       the bucket when it calculates data for **Storage** and
       **Objects** statistics.
      + If you query aggregated statistics programmatically by using the
       [GetBucketStatistics](../APIReference/datasources-s3-statistics.md "../APIReference/datasources-s3-statistics.md") operation, the bucket has a value of
       `unknown` for many statistics and Macie excludes the
       bucket when it calculates object counts and storage size values.

  To investigate the issue, review the bucket’s policy and permissions settings
  in Amazon S3. For example, the bucket might have a restrictive bucket policy. For
  more information, see [Allowing Macie to access S3
  buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

- Data about access and permissions is limited to account- and bucket-level
  settings. It doesn’t reflect object-level settings that determine access to
  specific objects in a bucket. For example, if public access is enabled for a
  specific object in a bucket, Macie doesn’t report that the bucket or the
  bucket’s objects are publicly accessible.

To monitor object-level operations and identify potential security risks, we
recommend that you use the Amazon S3 protection feature of Amazon GuardDuty. This feature
monitors object-level, Amazon S3 data events and analyzes them for malicious and
suspicious activity. For more information, see [GuardDuty S3 Protection](../../../guardduty/latest/ug/s3-protection.md "../../../guardduty/latest/ug/s3-protection.md") in
the _Amazon GuardDuty User Guide_.

- If you manually refresh object metadata for a specific bucket:
  - Macie temporarily reports _Unknown_ for encryption
    statistics that apply to the objects. The next time Macie performs the
    daily data refresh (within 24 hours), Macie re-evaluates the encryption
    metadata for the objects and reports quantitative data for the
    statistics again.
  - Macie temporarily excludes data for any object parts that the bucket
    contains due to incomplete multipart uploads. The next time Macie
    performs the daily data refresh (within 24 hours), Macie recalculates
    counts and storage size values for the bucket’s objects and includes
    data for the parts in those calculations.

- In certain cases, Macie might not be able to determine whether a bucket is
  publicly accessible or shared, or requires server-side encryption of new
  objects. For example, a quota or temporary issue might prevent Macie from
  retrieving and analyzing the requisite data. Or Macie might not be able to fully
  determine whether one or more policy statements grant access to an external
  entity. In these cases, Macie reports _Unknown_
  for the relevant statistics and fields in your bucket inventory. To investigate
  these cases, review the bucket’s policy and permissions settings in Amazon S3.

Also note that Macie generates policy findings only if the security or privacy of a
bucket is reduced after you enable Macie for your account. For example, if you disable
block public access settings for a bucket after you enable Macie, Macie generates a
**Policy:IAMUser/S3BlockPublicAccessDisabled** finding for the
bucket. However, if block public access settings were disabled for a bucket when you
enabled Macie and they continue to be disabled, Macie doesn't generate a
**Policy:IAMUser/S3BlockPublicAccessDisabled** finding for the
bucket.
