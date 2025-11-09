# Scope options for sensitive data discovery

jobs

With sensitive data discovery jobs, you define the scope of the analysis that Amazon Macie performs to detect
and report sensitive data in your Amazon Simple Storage Service (Amazon S3) general purpose buckets. To help you do
this, Macie provides several job-specific options that you can choose when you create and
configure a job.

###### Scope options

- [S3 buckets or bucket criteria](#discovery-jobs-scope-buckets "#discovery-jobs-scope-buckets")
- [Sampling depth](#discovery-jobs-scope-sampling "#discovery-jobs-scope-sampling")
- [Initial run: Include existing S3 objects](#discovery-jobs-scope-objects "#discovery-jobs-scope-objects")
- [S3 object criteria](#discovery-jobs-scope-criteria "#discovery-jobs-scope-criteria")

## S3 buckets or bucket criteria

When you create a sensitive data discovery job, you specify which S3 buckets store objects that you want Macie
to analyze when the job runs. You can do this in two ways: by selecting specific S3
buckets from your bucket inventory, or by specifying custom criteria that derive from
properties of S3 buckets.

**Select specific S3 buckets**

With this option, you explicitly select each S3 bucket to analyze. Then, when the job
runs, Macie analyzes objects only in the buckets that you select. If you
configure a job to run periodically on a daily, weekly, or monthly basis,
Macie analyzes objects in those same buckets each time the job runs.

This configuration is helpful for cases where you want to perform targeted analysis of a
specific set of data. It gives you precise, predictable control over which
buckets a job analyzes.

**Specify S3 bucket criteria**

With this option, you define runtime criteria that determine which S3 buckets to analyze.
The criteria consist of one or more conditions that derive from bucket
properties, such as public access settings and tags. When the job runs,
Macie identifies buckets that match your criteria, and then analyzes objects
in those buckets. If you configure a job to run periodically, Macie does
this each time the job runs. Consequently, Macie might analyze objects in
different buckets each time the job runs, depending on changes to your
bucket inventory and the criteria that you define.

This configuration is helpful for cases where you want the scope of the analysis to
dynamically adapt to changes to your bucket inventory. If you configure a
job to use bucket criteria and run periodically, Macie automatically
identifies new buckets that match the criteria and inspects those buckets
for sensitive data.

The topics in this section provide additional details about each option.

###### Topics

- [Selecting specific
  S3 buckets](#discovery-jobs-scope-buckets-select "#discovery-jobs-scope-buckets-select")
- [Specifying S3 bucket
  criteria](#discovery-jobs-scope-buckets-criteria "#discovery-jobs-scope-buckets-criteria")

### Selecting specific S3

buckets

If you choose to explicitly select each S3 bucket that you want a job to analyze, Macie
provides you with an inventory of your general purpose buckets in the current
AWS Region. You can then review your inventory and select the buckets that you
want. If you're the Macie administrator for an organization, your inventory includes buckets
that your member accounts own. You can select as many as 1,000 of these buckets,
spanning as many as 1,000 accounts.

To help you make your bucket selections, the inventory provides details and statistics for
each bucket. This includes the amount of data that a job can analyze in each
bucket—_classifiable objects_ are
objects that use a [supported Amazon S3
storage class](discovery-supported-storage.md#discovery-supported-s3-classes "discovery-supported-storage.md#discovery-supported-s3-classes") and have a file name extension for a [supported file or storage format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats").
The inventory also indicates whether you configured any existing jobs to analyze
objects in a bucket. These details can help you estimate the breadth of a job and
refine your bucket selections.

In the inventory table:

- **Sensitivity** – Specifies the bucket's current sensitivity score, if
  [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") is enabled.
- **Classifiable objects** – Specifies the total number of objects
  that the job can analyze in the bucket.
- **Classifiable size** – Specifies the total storage size of all
  the objects that the job can analyze in the bucket.

If the bucket stores compressed objects, this value doesn’t reflect the
actual size of those objects after they're decompressed. If versioning is
enabled for the bucket, this value is based on the storage size of the
latest version of each object in the bucket.

- **Monitored by job** – Specifies whether you
  configured any existing jobs to periodically analyze objects in the bucket
  on a daily, weekly, or monthly basis.

If the value for this field is **Yes**, the bucket is
explicitly included in a periodic job or the bucket matched the criteria for
a periodic job within the past 24 hours. In addition, the status of at least
one of those jobs is not _Cancelled_. Macie
updates this data on a daily basis.

- **Latest job run** – If you configured any
  periodic or one-time jobs to analyze objects in the bucket, this field
  specifies the most recent date and time when one of those jobs started to
  run. Otherwise, a dash (–) appears in this field.

If the information icon (
![The information icon, which is a blue circle that has a lowercase letter i in it.](images/icon-info-blue.png)
) appears next to any bucket names, we
recommend that you retrieve the latest bucket metadata from Amazon S3. To do this, choose
refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) above the table. The information icon indicates that a
bucket was created during the past 24 hours, possibly after Macie last retrieved
bucket and object metadata from Amazon S3 as part of the daily refresh cycle. For more
information, see [Data
refreshes](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh").

If the warning icon (
![The warning icon, which is a red triangle that has an exclamation point in it.](images/icon-warning-red.png)
) appears next to a bucket's name, Macie
isn't allowed to access the bucket or the bucket's objects. This means that the job
won't be able to analyze objects in the bucket. To investigate the issue, review the
bucket’s policy and permissions settings in Amazon S3. For example, the bucket might have
a restrictive bucket policy. For more information, see [Allowing Macie to access S3
buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

To customize your view and find specific buckets more easily, you can filter the table by
entering filter criteria in the filter box. The following table provides some
examples.

| To show all buckets that...                                               | Apply this filter...                                                                        |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Are owned by a specific account                                           | \*_Account ID_<br>• = `the<br>12-digit ID for the account`                                  |
| Are publicly accessible                                                   | **Effective permission\*<br>• =<br>**Public\*\*                                             |
| Aren't included in any periodic jobs                                      | **Actively monitored by job\*<br>• =<br>**False\*\*                                         |
| Aren't included in any periodic or one-time jobs                          | **Defined in job\*<br>• =<br>**False\*\*                                                    |
| Have a specific tag key\*                                                 | \*_Tag key_<br>• = `the tag<br>key`                                                         |
| Have a specific tag value\*                                               | \*_Tag value_<br>• = `the tag<br>value`                                                     |
| Store unencrypted objects (or objects that use client-side<br>encryption) | **Object count by encryption\*<br>• is **No<br>encryption*<br>• and \*\*From*<br>• =<br>_1_ |

\* Tag keys and values are case sensitive. Also, you have to specify a complete, valid
value. You can’t specify partial values or use wildcard characters.

To display additional details for a bucket, choose the bucket's name and refer to
the details panel. In the panel, you can also:

- Pivot and drill down on certain fields by choosing a magnifying glass for the field.
  Choose
  ![The zoom in icon, which is a magnifying glass that has a plus sign in it.](images/icon-magnifying-glass-plus-sign.png)
  to show buckets with the same value. Choose

![The zoom out icon, which is a magnifying glass that has a minus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-minus-sign.png)
to show buckets with other values.

- Retrieve the latest metadata for objects in the bucket. This can be
  helpful if you recently created a bucket or made significant changes to the
  bucket's objects during the past 24 hours. To retrieve the data, choose
  refresh (
  ![The refresh button, which is a button that displays an empty, dark gray circle with an arrow.](/images/macie/latest/user/images/btn-refresh-object-data.png)
  ) in the **Object
  statistics** section of the panel. This option is available for
  buckets that store 30,000 or fewer objects.

In certain cases, the panel might not include all the details of a bucket. This can occur
if you store more than 10,000 buckets in Amazon S3. Macie maintains complete inventory
data for only 10,000 buckets for an account—the 10,000 buckets that were most
recently created or changed. You can, however, configure a job to analyze objects in
buckets that exceed this quota. To review additional details for these buckets, use
Amazon S3.

### Specifying S3 bucket

criteria

If you choose to specify bucket criteria for a job, Macie provides options for defining and
testing the criteria. These are runtime criteria that determine which S3 buckets
store objects to analyze. Each time the job runs, Macie identifies general purpose
buckets that match your criteria, and then analyzes objects in the appropriate
buckets. If you're the Macie administrator for an organization, this includes buckets that
your member accounts own.

#### Defining bucket

criteria

Bucket criteria consist of one or more conditions that derive from properties of S3
buckets. Each condition, also referred to as a _criterion_, consists of the following parts:

- A property-based field, such as **Account ID** or **Effective
  permission**.
- An operator, either _equals_ (`eq`) or _not
  equals_ (`neq`).
- One or more values.
- An include or exclude statement that indicates whether to analyze (_include_) or skip (_exclude_) buckets that match the condition.

If you specify more than one value for a field, Macie uses OR logic to join the values. If
you specify more than one condition for the criteria, Macie uses AND logic to
join the conditions. In addition, exclude conditions take precedence over
include conditions. For example, if you include buckets that are publicly
accessible and exclude buckets that have specific tags, the job analyzes objects
in any bucket that's publicly accessible unless the bucket has one of the
specified tags.

You can define conditions that derive from any of the following property-based fields for
S3 buckets.

**Account ID**

The unique identifier (ID) for the AWS account that owns a bucket. To specify multiple
values for this field, enter the ID for each account and separate each entry
with a comma.

Note that Macie doesn't support use of wildcard characters or partial values for this
field.

**Bucket name**

The name of a bucket. This field correlates to the **Name** field, not
the **Amazon Resource Name (ARN)** field, in Amazon S3.
To specify multiple values for this field, enter the name of each
bucket and separate each entry with a comma.

Note that values are case sensitive. In addition, Macie doesn't support use of wildcard
characters or partial values for this field.

**Effective permission**

Specifies whether a bucket is publicly accessible. You can choose one or more of the
following values for this field:

- **Not public** – The general public doesn't have read or write
  access to the bucket.
- **Public** – The general public has read or write access to
  the bucket.
- **Unknown** – Macie wasn't able to evaluate the public access
  settings for the bucket. An issue or quota prevented Macie
  from retrieving and evaluating the requisite data.

To determine whether a bucket is publicly accessible, Macie analyzes a combination of
account- and bucket-level settings for the bucket: the block public
access settings for the account; the block public access settings
for the bucket; the bucket policy for the bucket; and, the access
control list (ACL) for the bucket. For information about these
settings, see [Access
control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") and [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the
_Amazon Simple Storage Service User Guide_.

**Shared access**

Specifies whether a bucket is shared with another AWS account, an Amazon CloudFront origin access identity (OAI),
or a CloudFront origin access control (OAC). You can choose one or more of the following
values for this field:

- **External** – The bucket is shared with one or more of the
  following or any combination of the following: a CloudFront OAI, a
  CloudFront OAC, or an account that's external to (not part of)
  your organization.
- **Internal** – The bucket is shared with one or more accounts
  that are internal to (part of) your organization. It isn't
  shared with a CloudFront OAI or OAC.
- **Not shared** – The bucket isn't shared with another
  account, a CloudFront OAI, or a CloudFront OAC.
- **Unknown** – Macie wasn't able to evaluate the shared access
  settings for the bucket. An issue or quota prevented Macie
  from retrieving and evaluating the requisite data.

To determine whether a bucket is shared with another AWS account, Macie analyzes the
bucket policy and ACL for the bucket. In addition, an _organization_ is defined as a set of
Macie accounts that are centrally managed as a group of related
accounts through AWS Organizations or by Macie invitation. For information
about Amazon S3 options for sharing buckets, see [Access
control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the _Amazon Simple Storage Service User
Guide_.

To determine whether a bucket is shared with a CloudFront OAI or OAC, Macie analyzes the
bucket policy for the bucket. A CloudFront OAI or OAC allows users to
access a bucket's objects through one or more specified CloudFront
distributions. For information about CloudFront OAIs and OACs, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the _Amazon CloudFront Developer Guide_.

**Tags**

The tags that are associated with a bucket. Tags are labels that
you can define and assign to certain types of AWS resources,
including S3 buckets. Each tag consists of a required tag key and an
optional tag value. For information about tagging S3 buckets, see
[Using cost
allocation S3 bucket tags](../../../AmazonS3/latest/userguide/CostAllocTagging.md "../../../AmazonS3/latest/userguide/CostAllocTagging.md") in the _Amazon Simple Storage Service User Guide_.

For a sensitive data discovery job, you can use this type of condition to include or
exclude buckets that have a specific tag key, a specific tag value,
or a specific tag key and tag value (as a pair). For example:

- If you specify `Project` as a tag key
  and don't specify any tag values for a condition, any bucket
  that has the _Project_ tag
  key matches the condition’s criteria, regardless of the tag
  values that are associated with that tag key.
- If you specify `Development` and
  `Test` as tag values and don't
  specify any tag keys for a condition, any bucket that has
  the `Development` or
  `Test` tag value matches the
  condition’s criteria, regardless of the tag keys that are
  associated with those tag values.

Tag keys and values are case sensitive. In addition, Macie doesn't
support use of wildcard characters or partial values in tag
conditions.

To specify multiple tag keys in a condition, enter each tag key in
the **Key** field and separate each entry with a
comma. To specify multiple tag values in a condition, enter each tag
value in the **Value** field and separate each
entry with a comma.

If you store more than 10,000 buckets in Amazon S3, note that Macie
doesn't maintain tag data for all the buckets. Macie maintains
complete inventory data for only 10,000 buckets for an
account—the 10,000 buckets that were most recently created or
changed. For all other buckets, any associated tag keys and values
aren't included in inventory data. This means that the buckets won't
match specific tag keys or values in a condition that uses the
_equals_ (`eq`) operator. If you
specify a _not equals_ (`neq`)
operator for a tag-based condition, this means that the buckets will
match the condition.

#### Testing bucket

criteria

While you define your bucket criteria, you can test and refine the criteria by previewing
the results. To do this, expand the **Preview the criteria
results** section that appears below the criteria on the console.
This section displays a table of up to 25 general purpose buckets that currently
match the criteria.

The table also provides insight into the amount of data that the job can analyze in each
bucket—_classifiable objects_ are
objects that use a [supported Amazon S3
storage class](discovery-supported-storage.md#discovery-supported-s3-classes "discovery-supported-storage.md#discovery-supported-s3-classes") and have a file name extension for a [supported file or storage
format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats"). The table also indicates whether you configured any existing
jobs to periodically analyze objects in a bucket.

In the table:

- **Sensitivity** – Specifies the bucket's current sensitivity score,
  if [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") is enabled.
- **Classifiable objects** – Specifies the total number of objects
  that the job can analyze in the bucket.
- **Classifiable size** – Specifies the total storage size of all
  the objects that the job can analyze in the bucket.

If the bucket stores compressed objects, this value doesn’t reflect the actual size of
those objects after they're decompressed. If versioning is enabled for
the bucket, this value is based on the storage size of the latest
version of each object in the bucket.

- **Monitored by job** – Specifies whether you configured any
  existing jobs to periodically analyze objects in the bucket on a daily,
  weekly, or monthly basis.

If the value for this field is **Yes**, the bucket is
explicitly included in a periodic job or the bucket matched the criteria
for a periodic job within the past 24 hours. In addition, the status of
at least one of those jobs is not _Cancelled_. Macie updates this data on a daily
basis.

If the warning icon (
![The warning icon, which is a red triangle that has an exclamation point in it.](images/icon-warning-red.png)
) appears next to a bucket's name, Macie isn't
allowed to access the bucket or the bucket's objects. This means that the job
won't be able to analyze objects in the bucket. To investigate the issue, review
the bucket’s policy and permissions settings in Amazon S3. For example, the bucket
might have a restrictive bucket policy. For more information, see [Allowing Macie to access S3
buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

To refine the bucket criteria for the job, use the filter options to add, change, or
remove conditions from the criteria. Macie then updates the table to reflect
your changes.

## Sampling depth

With this option, you specify the percentage of eligible S3 objects that you want a
sensitive data discovery job to analyze. Eligible objects are objects that: use a [supported Amazon S3 storage class](discovery-supported-storage.md#discovery-supported-s3-classes "discovery-supported-storage.md#discovery-supported-s3-classes"), have a
file name extension for a [supported file or
storage format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats"), and match other criteria that you specify for the job.

If this value is less than 100%, Macie selects eligible objects to analyze at random, up to
the specified percentage, and analyzes all the data in those objects. For example, if
you configure a job to analyze 10,000 objects and you specify a sampling depth of 20%,
Macie analyzes approximately 2,000 randomly selected, eligible objects when the job
runs.

Reducing the sampling depth of a job can lower the cost and reduce the duration of a job.
It's helpful for cases where the data in objects is highly consistent and you want to
determine whether an S3 bucket, rather than each object, stores sensitive data.

Note that this option controls the percentage of _objects_
that are analyzed, not the percentage of _bytes_ that
are analyzed. If you enter a sampling depth that’s less than 100%, Macie analyzes all
the data in each selected object, not that percentage of the data in each selected
object.

## Initial run: Include existing S3 objects

You can use sensitive data discovery jobs to perform ongoing, incremental analysis of objects in S3
buckets. If you configure a job to run periodically, Macie does this for you
automatically—each run analyzes only those objects that were created or changed
after the preceding run. With the **Include existing objects** option,
you choose the starting point for the first increment:

- To analyze all existing objects immediately after you finish creating the job, select the
  checkbox for this option.
- To wait and analyze only those objects that are created or changed after you create the
  job and before the first run, clear the checkbox for this option.

Clearing this checkbox is helpful for cases where you already analyzed the data and want
to continue to analyze it periodically. For example, if you previously used
another service or application to classify data and you recently started using
Macie, you might use this option to ensure continued discovery and
classification of your data without incurring unnecessary costs or duplicating
classification data.

Each subsequent run of a periodic job automatically analyzes only those objects that are
created or changed after the preceding run.

For both periodic and one-time jobs, you can also configure a job to analyze only those
objects that are created or changed before or after a certain time or during a certain
time range. To do this, add object criteria that use the last modified date for
objects.

## S3 object criteria

To fine tune the scope of a sensitive data discovery job, you can define custom criteria for S3 objects. Macie
uses these criteria to determine which objects to analyze (_include_) or skip (_exclude_) when the
job runs. The criteria consist of one or more conditions that derive from properties of
S3 objects. The conditions apply to objects in all the S3 buckets that are included in
the analysis. If a bucket stores multiple versions of an object, the conditions apply to
the latest version of the object.

If you define multiple conditions as object criteria, Macie uses AND logic to join the
conditions. In addition, exclude conditions take precedence over include conditions. For
example, if you include objects that have the .pdf file name extension and exclude objects
that are larger than 5 MB, the job analyzes any object that has the .pdf file name
extension, unless the object is larger than 5 MB.

You can define conditions that derive from any of the following properties of S3
objects.

**File name extension**

This correlates to the file name extension of an S3 object. You can use
this type of condition to include or exclude objects based on file type. To
do this for multiple types of files, enter the file name extension for each
type and separate each entry with a comma—for example:
`docx,pdf,xlsx`. If you enter multiple file name
extensions as values for a condition, Macie uses OR logic to join the
values.

Note that values are case sensitive. In addition, Macie doesn't support
the use of partial values or wildcard characters in this type of
condition.

For information about the types of files that Macie can analyze, see [Supported file and storage
formats](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats").

**Last modified**

This correlates to the **Last modified** field in Amazon S3.
In Amazon S3, this field stores the date and time when an S3 object was created
or last changed, whichever is latest.

For a sensitive data discovery job, this condition can be a specific date, a specific date and time, or an
exclusive time range:

- To analyze objects that were last modified after a certain date or
  date and time, enter the values in the **From**
  fields.
- To analyze objects that were last modified before a certain date
  or date and time, enter the values in the **To**
  fields.
- To analyze objects that were last modified during a certain time
  range, use the **From** fields to enter the values
  for the first date or date and time in the time range. Use the
  **To** fields to enter the values for the last
  date or date and time in the time range.
- To analyze objects that were last modified at any time during a certain single day,
  enter the date in the **From** date field. Enter
  the date for the next day in the **To** date field.
  Then verify that both time fields are blank. (Macie treats a blank
  time field as `00:00:00`.) For example, to analyze
  objects that changed on August 9, 2023, enter
  `2023/08/09` in the
  **From** date field, enter
  `2023/08/10` in the **To**
  date field, and don't enter a value in either time field.

Enter any time values in Coordinated Universal Time (UTC) and use 24-hour notation.

**Prefix**

This correlates to the **Key** field in Amazon S3. In Amazon S3,
this field stores the name of an S3 object, including the object's prefix. A
_prefix_ is similar to a directory path
within a bucket. It enables you to group similar objects together in a
bucket, much like you might store similar files together in a folder on a
file system. For information about object prefixes and folders in Amazon S3, see
[Organizing objects in
the Amazon S3 console using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the _Amazon Simple Storage Service User Guide_.

You can use this type of condition to include or exclude objects whose
keys (names) begin with a certain value. For example, to exclude all objects
whose key begins with _AWSLogs_, enter
`AWSLogs` as the value for a
**Prefix** condition, and then choose
**Exclude**.

If you enter multiple prefixes as values for a condition, Macie uses OR logic to join the
values. For example, if you enter `AWSLogs1` and
`AWSLogs2` as values for a condition, any object
whose key begins with _AWSLogs1_ or
_AWSLogs2_ matches the condition’s
criteria.

When you enter a value for a **Prefix** condition, keep
the following in mind:

- Values are case sensitive.
- Macie doesn't support the use of wildcard characters in these
  values.
- In Amazon S3, an object’s key doesn’t include the name of the bucket that stores the object.
  For this reason, don’t specify bucket names in these values.
- If a prefix includes a delimiter, include the delimiter in the
  value. For example, enter `AWSLogs/eventlogs`
  to define a condition for all objects whose key begins with
  _AWSLogs/eventlogs_. Macie
  supports the default Amazon S3 delimiter, which is a slash (/), and
  custom delimiters.

Also note that an object matches a condition's criteria only if the object's key exactly
matches the value that you enter, starting with the first character in the
object's key. In addition, Macie applies a condition to the complete
**Key** value for an object, including the object's
file name.

For example, if an object's key is _AWSLogs/eventlogs/testlog.csv_ and you enter any of the
following values for a condition, the object matches the condition's
criteria:

- `AWSLogs`
- `AWSLogs/event`
- `AWSLogs/eventlogs/`
- `AWSLogs/eventlogs/testlog`
- `AWSLogs/eventlogs/testlog.csv`

However, if you enter `eventlogs`, the object doesn't match the
criteria—the condition's value doesn't include the first part of the
key, _AWSLogs/_. Similarly, if you enter
`awslogs`, the object doesn't match the criteria
due to differences in capitalization.

**Storage size**

This correlates to the **Size** field in Amazon S3. In Amazon S3,
this field indicates the total storage size of an S3 object. If an object is
a compressed file, this value doesn't reflect the actual size of the file
after it's decompressed.

You can use this type of condition to include or exclude objects that are
smaller than a certain size, larger than a certain size, or fall within a
certain size range. Macie applies this type of condition to all types of
objects, including compressed or archive files and the files that they
contain. For information about size-based restrictions for each supported
format, see [Quotas for Macie](macie-quotas.md "macie-quotas.md").

**Tags**

The tags that are associated with an S3 object. Tags are labels that you can define and
assign to certain types of AWS resources, including S3 objects. Each tag
consists of a required tag key and an optional tag value. For information about
tagging S3 objects, see [Categorizing your storage
using tags](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md") in the _Amazon Simple Storage Service User
Guide_.

For a sensitive data discovery job, you can use this type of condition to include or exclude objects that
have a specific tag. This can be a specific tag key or a specific tag key
and tag value (as a pair). If you specify multiple tags as values for a
condition, Macie uses OR logic to join the values. For example, if you
specify `Project1` and `Project2`
as tag keys for a condition, any object that has the _Project1_ or _Project2_ tag
key matches the condition’s criteria.

Note that tag keys and values are case sensitive. In addition, Macie doesn't support use
of partial values or wildcard characters in this type of condition.
