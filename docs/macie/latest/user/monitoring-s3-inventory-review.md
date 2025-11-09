# Reviewing your S3 bucket inventory in

Macie

On the Amazon Macie console, the **S3 buckets** page provides detailed insight
into the security and privacy of your Amazon Simple Storage Service (Amazon S3) data in the current AWS Region. With
this page, you can review and analyze an inventory of your S3 general purpose buckets in the
Region, and review detailed information and statistics for individual buckets. For
information about how Macie generates and maintains this inventory, see [How Macie monitors Amazon S3 data security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md"). If
you're the Macie administrator for an organization, your inventory includes details and statistics
for S3 buckets that your member accounts own.

The **S3 buckets** page also indicates when Macie most recently retrieved
bucket or object metadata from Amazon S3 for your account. You can find this information in the
**Last updated** field at the top of the page. If you're the
Macie administrator for an organization, this field indicates the earliest date and time when Macie
retrieved the data for an account in your organization. For more information, see [Data
refreshes](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh").

Note that inventory data and statistics don't include data about S3 directory buckets, only
general purpose buckets. Macie doesn't monitor or analyze directory buckets. In addition,
Macie maintains complete inventory data for no more than 10,000 general purpose buckets for
an account. If your account exceeds this quota, Macie provides complete inventory data for
the 10,000 buckets that were most recently created or changed. For all other buckets, Macie
provides only a subset of information about each bucket. If you're the Macie administrator for an
organization, this quota applies to each account in your organization, not your organization
overall.

Also note that most inventory data is limited to buckets that Macie is allowed to access
for your account. If a bucket's permissions settings prevent Macie from retrieving
information about the bucket or the bucket's objects, Macie can only provide a subset of
information about the bucket. If this is the case for a particular bucket, Macie displays a
warning icon (
![The warning icon, which is a red triangle that has an exclamation point in it.](images/icon-warning-red.png)
) and message for the bucket in your bucket inventory. For
the bucket's details, Macie provides data for only a subset of fields: the account ID for
the AWS account that owns the bucket; the bucket's name, Amazon Resource Name (ARN),
creation date, and Region; and, when Macie most recently retrieved both bucket and object
metadata for the bucket as part of the daily refresh cycle. To investigate the issue, review
the bucket’s policy and permissions settings in Amazon S3. For example, the bucket might have a
restrictive bucket policy. For more information, see [Allowing Macie to access S3
buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

If you prefer to access and query your inventory data programmatically, you can use the
[DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md") operation of the Amazon Macie API.

###### Topics

- [Reviewing your S3 bucket
  inventory](#monitoring-s3-inventory-view "#monitoring-s3-inventory-view")
- [Reviewing the details of S3
  buckets](#monitoring-s3-inventory-view-details "#monitoring-s3-inventory-view-details")

## Reviewing your S3 bucket

inventory

The **S3 buckets** page on the Amazon Macie console provides information
about your S3 general purpose buckets in the current AWS Region. On this page, a table
displays summary information for each bucket in your inventory. To customize your view,
you can sort and filter the table. If you choose a bucket in the table, the details
panel displays additional information about the bucket. This includes details and
statistics for settings and metrics that provide insight into the security and privacy
of the bucket’s data. You can optionally export data from the table to a comma-separated
values (CSV) file.

If automated sensitive data discovery is enabled, you also have the option of reviewing your inventory by
using an interactive heat map. The map provides a visual representation of data
sensitivity across your Amazon S3 data estate. It captures the results of automated sensitive data discovery
activities that Macie has performed thus far. To learn about this map, see [Visualizing data sensitivity with the
S3 buckets map](discovery-asdd-results-s3-inventory-map.md "discovery-asdd-results-s3-inventory-map.md").

###### To review your S3 bucket inventory

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **S3 buckets**. The
   **S3 buckets** page displays your bucket inventory. If the
   page displays an interactive map of your inventory, choose table
   (
   ![The table view button, which is a button that displays three black horizontal lines.](images/btn-s3-table-view.png)
   ) at the top of the page. Macie then displays the number of
   buckets in your inventory and a table of the buckets.

If automated sensitive data discovery is enabled, the default view doesn't display data for buckets
that are currently excluded from automated discovery. To display this data, choose
**X** in the **Is monitored by automated
discovery** filter token below the filter box. 3. At the top of the page, optionally choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) to retrieve
the latest bucket metadata from Amazon S3.

If the information icon (
![The information icon, which is a blue circle that has a lowercase letter i in it.](images/icon-info-blue.png)
) appears next to any bucket names,
we recommend that you do this. This icon indicates that a bucket was created
during the past 24 hours, possibly after Macie last retrieved bucket and object
metadata from Amazon S3 as part of the [daily refresh
cycle](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh"). 4. In the **S3 buckets** table, review a subset of information
about each bucket in your inventory:

    * **Sensitivity** – The bucket's current
     sensitivity score, if automated sensitive data discovery is enabled. For information about the range
     of sensitivity scores that Macie defines, see [Sensitivity scoring for S3
     buckets](discovery-scoring-s3.md "discovery-scoring-s3.md").
    * **Bucket** – The name of the bucket.
    * **Account** – The account ID for the
     AWS account that owns the bucket.
    * **Classifiable objects** – The total number of
     objects that Macie can analyze to detect sensitive data in the
     bucket.
    * **Classifiable size** – The total storage size
     of all the objects that Macie can analyze to detect sensitive data in
     the bucket.


    Note that this value doesn’t reflect the actual size of any compressed
     objects after they're decompressed. Also, if versioning is enabled for
     the bucket, this value is based on the storage size of the latest
     version of each object in the bucket.
    * **Monitored by job** – Whether you configured
     any sensitive data discovery jobs to periodically analyze objects in the
     bucket on a daily, weekly, or monthly basis.


    If the value for this field is *Yes*,
     the bucket is explicitly included in a periodic job or the bucket
     matched the criteria for a periodic job within the past 24 hours. In
     addition, the status of at least one of those jobs is not *Cancelled*. Macie updates this data on a
     daily basis.
    * **Latest job run** – If you configured any
     periodic or one-time sensitive data discovery jobs to analyze objects in
     the bucket, this field indicates the most recent date and time when one
     of those jobs started to run. Otherwise, a dash (–) appears in
     this field.

In the preceding data, objects are _classifiable_ if they use a supported Amazon S3 storage class and they
have a file name extension for a supported file or storage format. You can
detect sensitive data in the objects by using Macie. For more information, see
[Supported storage classes and
formats](discovery-supported-storage.md "discovery-supported-storage.md"). 5. To analyze your inventory by using the table, do any of the following:

    * To sort the table by a specific field, choose the column heading for
     the field. To change the sort order, choose the column heading
     again.
    * To filter the table and display only those buckets that have a
     specific value for a field, place your cursor in the filter box, and
     then add a filter condition for the field. To further refine the
     results, add filter conditions for additional fields. For more
     information, see [Filtering your S3 bucket
     inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md").

6. To review details and statistics for a particular bucket, choose the bucket's
   name in the table, and then refer to the details panel.

###### Tip

You can pivot and drill down on many of the fields in the bucket details
panel. To show buckets that have the same value for a field, choose

![The zoom in icon, which is a magnifying glass that has a plus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-plus-sign.png)
in the field. To show buckets that have other values
for a field, choose
![The zoom out icon, which is a magnifying glass that has a minus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-minus-sign.png)
in the field. 7. To export data from the table to a CSV file, select the checkbox for each row that you
want to export, or select the checkbox in the selection column heading to select
all rows. Then choose **Export to CSV** at the top of the page.
You can export up to 50,000 rows from the table.

## Reviewing the details of S3

buckets

To review details and statistics for an S3 general purpose bucket, you can use the details
panel on the **S3 buckets** page of the Amazon Macie console. The panel
displays details and statistics that provide insight into the security and privacy of a
bucket’s data.

For example, you can review breakdowns of an S3 bucket’s public access settings, and
determine whether a bucket is configured to replicate objects or is shared with other
AWS accounts. You can also determine whether you configured any sensitive data
discovery jobs to inspect the bucket for sensitive data. If you have, you can access
details about the job that ran most recently, and optionally display any findings that
the job produced.

If automated sensitive data discovery is enabled, you can also use the details panel to review sensitive data discovery statistics
and other information about individual S3 buckets. The panel captures the results of
automated sensitive data discovery activities that Macie has performed thus far for a bucket. To learn about
these details, see [Reviewing data sensitivity details
for S3 buckets](discovery-asdd-results-s3-inventory-details.md "discovery-asdd-results-s3-inventory-details.md").

###### To review the details of an S3 bucket

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **S3 buckets**. The
   **S3 buckets** page displays your bucket inventory.

If automated sensitive data discovery is enabled, the default view doesn't display data for buckets
that are currently excluded from automated discovery. To display this data, choose
**X** in the **Is monitored by automated
discovery** filter token below the filter box. 3. At the top of the page, optionally choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) to retrieve
the latest bucket metadata from Amazon S3. 4. Choose the bucket whose details you want to review. The details panel displays
statistics and other information about the bucket.

In the details panel, statistics and information are organized into the following
primary sections:

[Overview](#monitoring-s3-inventory-view-details-general "#monitoring-s3-inventory-view-details-general") | [Object
statistics](#monitoring-s3-inventory-view-details-objects "#monitoring-s3-inventory-view-details-objects") | [Server-side
encryption](#monitoring-s3-inventory-view-details-sse "#monitoring-s3-inventory-view-details-sse") | [Sensitive data
discovery](#monitoring-s3-inventory-view-details-discovery "#monitoring-s3-inventory-view-details-discovery") | [Public
access](#monitoring-s3-inventory-view-details-public-access "#monitoring-s3-inventory-view-details-public-access") | [Replication](#monitoring-s3-inventory-view-details-replication "#monitoring-s3-inventory-view-details-replication") | [Tags](#monitoring-s3-inventory-view-details-tags "#monitoring-s3-inventory-view-details-tags")

As you review the information in each section, you can optionally pivot and drill down
on certain fields. To show buckets that have the same value for a field, choose

![The zoom in icon, which is a magnifying glass that has a plus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-plus-sign.png)
in the field. To show buckets that have other values for a field,
choose
![The zoom out icon, which is a magnifying glass that has a minus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-minus-sign.png)
in the field.

### Overview

This section provides general information about the bucket, such as the bucket’s
name, when the bucket was created, and the account ID for the AWS account that
owns the bucket. Of special note, the **Last updated** field
indicates when Macie most recently retrieved metadata from Amazon S3 for the bucket or
the bucket’s objects.

The **Shared access** field indicates whether the bucket is
shared with another AWS account, an Amazon CloudFront origin access identity (OAI), or a CloudFront origin access control (OAC):

- **External** – The bucket is shared with one or
  more of the following or any combination of the following: a CloudFront OAI, a
  CloudFront OAC, or an account that's external to (not part of) your
  organization.
- **Internal** – The bucket is shared with one or
  more accounts that are internal to (part of) your organization. It isn't
  shared with a CloudFront OAI or OAC.
- **Not shared** – The bucket isn't shared with
  another account, a CloudFront OAI, or a CloudFront OAC.
- **Unknown** – Macie wasn't able to evaluate the
  shared access settings for the bucket. For example, a quota or temporary
  issue prevented Macie from retrieving and evaluating the requisite
  data.

To determine whether a bucket is shared with another AWS account, Macie analyzes the
bucket policy and access control list (ACL) for the bucket. The analysis is limited
to bucket-level settings. It doesn’t reflect any object-level settings for sharing
specific objects in the bucket. In addition, an _organization_ is defined as a set of Macie accounts that are
centrally managed as a group of related accounts through AWS Organizations or by Macie
invitation. To learn about Amazon S3 options for sharing buckets, see [Access control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the _Amazon Simple Storage Service User
Guide_.

###### Note

In certain cases, Macie might incorrectly indicate that a bucket is shared
with an AWS account that's external to (not part of) your organization. This
can occur if Macie isn’t able to fully evaluate the relationship between the
`Principal` element in the bucket’s policy and certain [AWS
global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") or [Amazon S3 condition keys](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys") in the `Condition` element of the
policy. This can be the case for the following condition keys:
`aws:PrincipalAccount`, `aws:PrincipalArn`,
`aws:PrincipalOrgID`, `aws:PrincipalOrgPaths`,
`aws:PrincipalTag`, `aws:PrincipalType`,
`aws:SourceAccount`, `aws:SourceArn`,
`aws:SourceIp`, `aws:SourceOrgID`,
`aws:SourceOrgPaths`, `aws:SourceVpc`,
`aws:SourceVpce`, `aws:userid`,
`s3:DataAccessPointAccount`, and
`s3:DataAccessPointArn`.

We recommend that you review the bucket’s policy to determine whether this
access is intended and safe.

To determine whether a bucket is shared with a CloudFront OAI or OAC, Macie analyzes the
bucket policy for the bucket. A CloudFront OAI or OAC allows users to access a bucket's
objects through one or more specified CloudFront distributions. To learn about CloudFront OAIs
and OACs, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the _Amazon CloudFront Developer Guide_.

The **Overview** section also includes the **Latest
automated discovery run** field. This field indicates when Macie most
recently analyzed objects in the bucket while performing automated sensitive data discovery. If this
analysis hasn't occurred, a dash (–) appears in this field.

### Object

statistics

This section provides information about the objects in the bucket, starting with
the total number of objects in the bucket (**Total count**), the
total storage size of all those objects (**Total storage size**),
and the total storage size of all the objects that are compressed (.gz, .gzip, or
.zip) files (**Total compressed size**). Additional statistics in
this section can help you assess how much data Macie can analyze to detect sensitive
data in the bucket.

If you recently created the bucket or made significant changes to the bucket's
objects during the past 24 hours, optionally choose refresh
(
![The refresh button, which is a button that displays an empty, dark gray circle with an arrow.](images/btn-refresh-object-data.png)
) to retrieve the latest metadata for the bucket's objects.
Macie displays the information icon (
![The information icon, which is a blue circle that has a lowercase letter i in it.](images/icon-info-blue.png)
) to help you determine whether
this might be the case. The refresh option is available if a bucket stores 30,000 or
fewer objects.

As you review the statistics in this section, keep the following in mind:

- If versioning is enabled for the bucket, size values are based on the
  storage size of the latest version of each object in the bucket.
- If the bucket stores compressed objects, size values don't reflect the
  actual size of those objects after they're decompressed.
- If you refresh object metadata for a bucket, Macie temporarily reports
  _Unknown_ for encryption statistics
  that apply to the objects. Macie will re-evaluate and update the data for
  these statistics when it performs the next [daily refresh](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh")
  of bucket and object metadata, which is within 24 hours.
- By default, object counts and size values include data for any object
  parts that the bucket contains as a result of incomplete multipart uploads.
  If you refresh object metadata for a bucket, Macie excludes data for object
  parts from the recalculated values. When Macie performs the next daily
  refresh of bucket and object metadata (within 24 hours), Macie recalculates
  and updates the values for these statistics and includes data for object
  parts in the values again.

Note that Macie can't analyze object parts to detect sensitive data. Amazon S3
must first finish assembling the parts into one or more objects for Macie to
analyze. For information about multipart uploads and object parts, including
how to delete parts automatically with lifecycle rules, see [Uploading and copying objects using multipart upload](../../../AmazonS3/latest/userguide/mpuoverview.md "../../../AmazonS3/latest/userguide/mpuoverview.md") in the
_Amazon Simple Storage Service User Guide_. To identify
buckets that contain object parts, you can refer to _incomplete multipart upload_ metrics in Amazon S3 Storage Lens.
For more information, see [Assessing your storage
activity and usage](../../../AmazonS3/latest/userguide/storage_lens.md "../../../AmazonS3/latest/userguide/storage_lens.md") in the _Amazon Simple Storage Service User
Guide_.

Object statistics are organized as follows.

**Classifiable objects**

This section indicates the total number of objects that Macie can
analyze to detect sensitive data and the total storage size of those
objects. These objects use a supported Amazon S3 storage class and have a
file name extension for a supported file or storage format. You can
detect sensitive data in the objects by using Macie. For more
information, see [Supported storage classes and
formats](discovery-supported-storage.md "discovery-supported-storage.md").

**Unclassifiable objects**

This section indicates the total number of objects that Macie can’t
analyze to detect sensitive data and the total storage size of those
objects. These objects don’t use a supported Amazon S3 storage class or they
don’t have a file name extension for a supported file or storage
format.

**Unclassifiable objects: Storage class**

This section provides a breakdown of the number and storage size of
the objects that Macie can’t analyze because the objects don’t use a
supported Amazon S3 storage class.

**Unclassifiable objects: File type**

This section provides a breakdown of the number and storage size of
the objects that Macie can’t analyze because the objects don’t have a
file name extension for a supported file or storage format.

**Objects by encryption type**

This section provides a breakdown of the number of objects that use
each type of encryption that Amazon S3 supports:

- **Customer provided** – The number of
  objects that are encrypted with a customer-provided key. These
  objects use SSE-C encryption.
- **AWS KMS managed** – The number of
  objects that are encrypted with an AWS KMS key, either an
  AWS managed key or a customer managed key. These objects use DSSE-KMS or
  SSE-KMS encryption.
- **Amazon S3 managed** – The number of
  objects that are encrypted with an Amazon S3 managed key. These
  objects use SSE-S3 encryption.
- **No encryption** – The number of
  objects that aren’t encrypted or use client-side encryption. (If
  an object is encrypted using client-side encryption, Macie can't
  access and report encryption data for the object.)
- **Unknown** – The number of objects
  that Macie doesn't have current encryption metadata for. This
  typically occurs if you recently chose to manually refresh the
  metadata for the bucket's objects. Macie will update the
  encryption statistics when it performs the next daily refresh of
  bucket and object metadata, which is within 24 hours.

For information about each supported encryption type, see [Protecting data
with encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User
Guide_.

### Server-side

encryption

This section provides insight into the server-side encryption settings for the
bucket.

The **Encryption required by bucket policy** field indicates
whether the bucket's policy requires server-side encryption of objects when objects
are added to the bucket:

- **No** – The bucket doesn't have a bucket policy
  or the bucket's policy doesn't require server-side encryption of new
  objects. If a bucket policy exists, it doesn't require [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") requests to include a valid server-side encryption
  header.
- **Yes** – The bucket's policy requires server-side
  encryption of new objects. **PutObject** requests for the
  bucket must include a valid server-side encryption header. Otherwise, Amazon S3
  denies the request.
- **Unknown** – Macie wasn't able to evaluate the
  bucket's policy to determine whether it requires server-side encryption of
  new objects. For example, a quota or issue prevented Macie from retrieving
  and evaluating the policy.

For this assessment, valid server-side encryption headers are:
`x-amz-server-side-encryption` with a value of `AES256` or
`aws:kms`, and
`x-amz-server-side-encryption-customer-algorithm` with a value of
`AES256`. For information about using bucket policies to require
server-side encryption of new objects, see [Protecting data with
server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon Simple Storage Service User
Guide_.

The **Default encryption** field indicates which server-side
encryption algorithm the bucket is configured to apply by default to objects that
are added to the bucket:

- **AES256** – The bucket's default encryption
  settings are configured to encrypt new objects with an Amazon S3 managed key. New
  objects are encrypted automatically using SSE-S3 encryption.
- **aws:kms** – The bucket's default encryption
  settings are configured to encrypt new objects with an AWS KMS key,
  either an AWS managed key or a customer managed key. New objects are encrypted
  automatically using SSE-KMS encryption. The
  **AWS KMS key** field shows the Amazon Resource Name
  (ARN) or unique identifier (key ID) for the key that's used.
- **aws:kms:dsse** – The bucket's default encryption
  settings are configured to encrypt new objects with an AWS KMS key,
  either an AWS managed key or a customer managed key. New objects are encrypted
  automatically using DSSE-KMS encryption. The
  **AWS KMS key** field shows the ARN or key ID for
  the key that's used.
- **None** – The bucket's default encryption
  settings don't specify server-side encryption behavior for new
  objects.

Starting January 5, 2023, Amazon S3 automatically applies server-side encryption with Amazon S3
managed keys (SSE-S3) as the base level of encryption for objects that are added to buckets. You can optionally configure a
bucket's default encryption settings to instead use server-side encryption with an AWS KMS key (SSE-KMS) or dual-layer server-side
encryption with an AWS KMS key (DSSE-KMS). For information about default encryption settings and options,
see [Setting default
server-side encryption behavior for S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the _Amazon Simple Storage Service User Guide_.

### Sensitive data

discovery

This section indicates whether you configured any sensitive data discovery jobs to
periodically analyze objects in the bucket on a daily, weekly, or monthly basis. If
the value for the **Actively monitored by job** field is _Yes_, the bucket is explicitly included in a periodic
job or the bucket matched the criteria for a periodic job within the past 24 hours.
In addition, the status of at least one of those jobs is not _Cancelled_. Macie updates this data on a daily basis.

If you configured any type of sensitive data discovery job (either a periodic job
or a one-time job) to analyze objects in the bucket, the **Latest
job** field provides the unique identifier for the job that most
recently started to run. The **Latest job run** field indicates
when that job started to run.

###### Tip

To display all the sensitive data findings that the job produced, choose the
link in the **Latest job** field. In the job details panel that
appears, choose **Show results** at the top of the panel, and
then choose **Show findings**.

### Public

access

This section indicates whether the bucket is publicly accessible. It also provides
a breakdown of the various account- and bucket-level settings that determine whether
this is the case. The **Effective permission** field indicates the
cumulative result of these settings:

- **Not public** – The bucket isn’t publicly
  accessible.
- **Public** – The bucket is publicly
  accessible.
- **Unknown** – Macie wasn’t able to evaluate all
  the public access settings for the bucket. For example, a quota or temporary
  issue prevented Macie from retrieving and evaluating the requisite
  data.

For this evaluation, Macie analyzes a combination of account- and bucket-level settings for
each bucket: the block public access settings for the account; the block public
access settings for the bucket; the bucket policy for the bucket; and, the access
control list (ACL) for the bucket. Note that the evaluation doesn’t include
object-level settings that enable public access to specific objects in a
bucket.

To learn about Amazon S3 settings for managing public access to buckets and bucket data, see
[Access control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md")
and [Blocking
public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_.

### Replication

In this section, the **Replicated** field indicates whether the
bucket is configured to replicate objects to other buckets. If the value for this
field is _Yes_, one or more replication rules are
configured and enabled for the bucket. This section then also lists the account ID
for each AWS account that owns a destination bucket.

The **Replicated externally** field indicates whether the bucket
is configured to replicate objects to buckets for AWS accounts that are external
to (not part of) your organization. An _organization_ is a set of Macie accounts that are centrally managed
as a group of related accounts through AWS Organizations or by Macie invitation. If the value
for this field is _Yes_, a replication rule is
configured and enabled for the bucket, and the rule is configured to replicate
objects to a bucket that's owned by an external AWS account.

###### Note

Under certain conditions, Macie might incorrectly indicate that a bucket is configured to
replicate objects to a bucket that's owned by an external AWS account. This
can occur if the destination bucket was created in a different AWS Region
during the preceding 24 hours, after Macie retrieved bucket and object metadata
from Amazon S3 as part of the [daily refresh cycle](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh"). To investigate the issue by using Macie, choose
refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) to retrieve the latest bucket metadata from Amazon S3. Then
review the list of account IDs in this section. For deeper investigation, use
Amazon S3 to review the replication rules for the bucket.

To learn about Amazon S3 options and settings for replicating bucket objects, see
[Replicating objects](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") in the _Amazon Simple Storage Service User
Guide_.

### Tags

If tags are associated with the bucket, this section appears in the panel and
lists those tags. Tags are labels that you can define and assign to certain types of
AWS resources, including S3 buckets. Each tag consists of a required tag key and
an optional tag value.

To learn about tagging buckets, see [Using cost allocation S3
bucket tags](../../../AmazonS3/latest/userguide/CostAllocTagging.md "../../../AmazonS3/latest/userguide/CostAllocTagging.md") in the _Amazon Simple Storage Service User
Guide_.
