# Reviewing data sensitivity details

for S3 buckets

As automated sensitive data discovery progresses, you can review detailed results in statistics and other
information that Amazon Macie provides about each of your Amazon Simple Storage Service (Amazon S3) buckets. If you're the
Macie administrator for an organization, this includes buckets that your member accounts own.

The statistics and information include details that provide insight into the security and
privacy of an S3 bucket’s data. They also capture the results of automated sensitive data discovery activities that Macie
has performed thus far for a bucket. For example, you can find a list of objects that Macie has
analyzed in a bucket. You can also find a breakdown of the types and number of occurrences of
sensitive data that Macie has found in a bucket. Note that this data doesn't include the results
of sensitive data discovery jobs that you create and run.

Macie automatically recalculates and updates statistics and details for your S3 buckets
while it performs automated sensitive data discovery. For example:

- If Macie doesn't find sensitive data in an S3 object, Macie decreases the bucket's
  sensitivity score and updates the bucket's sensitivity label as necessary. Macie also adds the
  object to the list of objects that it selected for analysis.
- If Macie finds sensitive data in an S3 object, Macie adds those occurrences to the
  breakdown of sensitive data types that Macie has found in the bucket. Macie also increases the
  bucket's sensitivity score and updates the bucket's sensitivity label as necessary. In addition,
  Macie adds the object to the list of objects that it selected for analysis. These tasks are in
  addition to creating a sensitive data finding for the object.
- If Macie finds sensitive data in an S3 object that's subsequently changed or deleted,
  Macie removes sensitive data occurrences for the object from the bucket's breakdown of
  sensitive data types. Macie also decreases the bucket's sensitivity score and updates the bucket's
  sensitivity label as necessary. In addition, Macie removes the object from the list of objects
  that it selected for analysis.
- If Macie attempts to analyze an S3 object but an issue or error prevents analysis, Macie
  adds the object to the list of objects that it selected for analysis, and indicates that it
  wasn't able to analyze the object.
  If you're the Macie administrator for an organization or you have a standalone Macie account, you
  can optionally use these details to assess and adjust certain automated discovery settings for an S3 bucket.
  For example, you can include or exclude specific types of sensitive data from a bucket's score.
  For more information, see [Adjusting sensitivity scores for S3
  buckets](discovery-asdd-s3bucket-manage.md "discovery-asdd-s3bucket-manage.md").

###### To review data sensitivity details for an S3 bucket

To review data sensitivity and other details for an S3 bucket, you can use the Amazon Macie
console or the Amazon Macie API. On the console, the details panel provides centralized access to
this information. With the API, you can retrieve and process the data programmatically.

Console
Follow these steps to review data sensitivity and other details for an S3 bucket by using
the Amazon Macie console.

###### To review the details for an S3 bucket

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **S3 buckets**. The **S3
   buckets** page displays an interactive map of your bucket inventory. Optionally
   choose table (
   ![The table view button, which is a button that displays three black horizontal lines.](images/btn-s3-table-view.png)
   ) at the top of the page to display your inventory in
   tabular format instead.

By default, the page doesn't display data for buckets that are currently excluded from
automated sensitive data discovery. If you're the Macie administrator for an organization, it also doesn't display data for
accounts that automated sensitive data discovery is currently disabled for. To display this data, choose
**X** in the **Is monitored by automated discovery**
filter token below the filter box. 3. To retrieve the latest bucket metadata from Amazon S3, choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) at the
top of the page. 4. Choose the bucket whose details you want to review. The details panel displays data
sensitivity statistics and other information about the bucket.

The top of the panel shows general information about the bucket: the bucket's name, the
account ID for the AWS account that owns the bucket, and the bucket's current sensitivity score.
If you're a Macie administrator or you have a standalone Macie account, it also provides options for
changing certain automated discovery settings for the bucket. Additional settings and information are
organized into the following tabs:

[Sensitivity](#discovery-asdd-results-s3-inventory-sensitivity-details "#discovery-asdd-results-s3-inventory-sensitivity-details") | [Bucket details](#discovery-asdd-results-s3-inventory-bucket-details "#discovery-asdd-results-s3-inventory-bucket-details") | [Object samples](#discovery-asdd-results-s3-inventory-sample-details "#discovery-asdd-results-s3-inventory-sample-details") | [Sensitive data
discovery](#discovery-asdd-results-s3-inventory-sdd-details "#discovery-asdd-results-s3-inventory-sdd-details")

Individual settings and information on each tab are as follows.

**Sensitivity**

This tab shows the bucket's current sensitivity score, ranging from _-1_ to _100_. For information about the range
of sensitivity scores that Macie defines, see [Sensitivity scoring for S3 buckets](discovery-scoring-s3.md "discovery-scoring-s3.md").

The tab also provides a breakdown of the types of sensitive data that Macie has found
in the bucket's objects, and the number of occurrences of each type:

- **Sensitive data type** – The unique identifier (ID) for the
  managed data identifier that detected the data, or the name of the custom data identifier
  that detected the data.

A managed data identifier's ID describes the type of sensitive data that it's
designed to detect—for example, **USA_PASSPORT_NUMBER** for US
passport numbers. For details about each managed data identifier, see [Using managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md").

- **Count** – The total number of occurrences of the data that
  the managed or custom data identifier detected.
- **Scoring status** – This field appears if you're a
  Macie administrator or you have a standalone Macie account. It specifies whether occurrences of
  the data are included or excluded from the bucket's sensitivity score.

If Macie calculates the bucket's score, you can adjust the calculation by including
or excluding specific types of sensitive data from the score: select the checkbox for the
identifier that detected the sensitive data to include or exclude, and then choose an
option on the **Actions** menu. For more information, see [Adjusting sensitivity scores for S3
buckets](discovery-asdd-s3bucket-manage.md "discovery-asdd-s3bucket-manage.md").

If Macie hasn't found sensitive data in objects that the bucket currently stores, this
section shows the **No detections found** message.

Note that the **Sensitivity** tab doesn't include data for objects
that were changed or deleted after Macie analyzed them. If objects are changed or deleted
after analysis, Macie automatically recalculates and updates the appropriate statistics and
data to exclude the objects.

**Bucket
details**

This tab provides details about the bucket's settings, including data security and
privacy settings. For example, you can review breakdowns of the bucket’s public access
settings, and determine whether the bucket replicates objects or is shared with other
AWS accounts.

Of special note, the **Last updated** field indicates when Macie most
recently retrieved metadata from Amazon S3 for the bucket or the bucket’s objects. The
**Latest automated discovery run** field indicates when Macie most
recently analyzed objects in the bucket while performing automated sensitive data discovery. If this analysis
hasn't occurred, a dash (–) appears in this field.

The tab also provides object-level statistics that can help you assess how much data
Macie can analyze in the bucket. It also indicates whether you configured any sensitive
data discovery jobs to analyze objects in the bucket. If you have, you can access details
about the job that ran most recently and then optionally display any findings that the job
produced.

In certain cases, this tab might not include all the details of a bucket. This can
occur if you store more than 10,000 buckets in Amazon S3. Macie maintains complete inventory
data for only 10,000 buckets for an account—the 10,000 buckets that were most
recently created or changed. Macie can, however, analyze objects in buckets that exceed
this quota. To review additional details for the buckets, use Amazon S3.

For additional details about the information on this tab, see [Reviewing the details of S3
buckets](monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details "monitoring-s3-inventory-review.md#monitoring-s3-inventory-view-details").

**Object
samples**

This tab lists objects that Macie selected for analysis while performing automated sensitive data discovery
for the bucket. Optionally choose an object's name to open the Amazon S3 console and display the
object's properties.

The list includes data for up to 100 objects. The list is populated based on the value
for the **Object sensitivity** field: **Sensitive**,
followed by **Not Sensitive**, followed by objects that Macie wasn't able
to analyze.

In the list, the **Object sensitivity** field indicates whether Macie
found sensitive data in an object:

- **Sensitive** – Macie found at least one occurrence of
  sensitive data in the object.
- **Not sensitive** – Macie didn't find sensitive data in the
  object.
- **–** (_dash_) –
  Macie wasn't able to complete its analysis of the object due to an issue or error.

The **Classification result** field indicates whether Macie was able
to analyze an object:

- **Complete** – Macie completed its analysis of the
  object.
- **Partial** – Macie analyzed only a subset of data in the
  object due to an issue or error. For example, the object is an archive file that contains
  files in an unsupported format.
- **Skipped** – Macie wasn't able to analyze any data in the
  object due to an issue or error. For example, the object is encrypted with a key that
  Macie isn't allowed to use.

Note that the list doesn't include objects that were changed or deleted after Macie
analyzed or attempted to analyze them. Macie automatically removes an object from the list
if the object is subsequently changed or deleted.

**Sensitive data
discovery**

This tab provides aggregated, automated sensitive data discovery statistics for the bucket:

- **Analyzed bytes** – The total amount of data, in bytes,
  that Macie has analyzed in the bucket.
- **Classifiable bytes** – The total storage size, in bytes,
  of all the objects that Macie can analyze in the bucket. These objects use supported Amazon S3
  storage classes and they have file name extensions for supported file or storage formats.
  For more information, see [Supported storage classes and
  formats](discovery-supported-storage.md "discovery-supported-storage.md").
- **Total detections** – The total number of occurrences of
  sensitive data that Macie has found in the bucket. This includes occurrences that are
  currently suppressed by the sensitivity scoring settings for the bucket.

The **Objects analyzed** chart indicates the total number of objects
that Macie has analyzed in the bucket. It also provides a visual representation of the
number of objects that Macie did or didn't find sensitive data in. The legend below the
chart shows a breakdown of these results:

- **Sensitive objects** (_red_)
  – The total number of objects that Macie found at least one occurrence of
  sensitive data in.
- **Not sensitive objects** (_blue_)
  – The total number of objects that Macie didn't find sensitive data in.
- **Objects skipped** (_dark gray_)
  – The total number of objects that Macie wasn't able to analyze due to an issue or
  error.

The area below the chart's legend provides a breakdown of cases where Macie wasn't
able to analyze objects because certain types of permissions issues or cryptographic errors
occurred:

- **Skipped: Invalid encryption** – The total number of
  objects that are encrypted with customer-provided keys. Macie can't access these
  keys.
- **Skipped: Invalid KMS** – The total number of objects that
  are encrypted with AWS Key Management Service (AWS KMS) keys that are no longer available. These objects are
  encrypted with AWS KMS keys that were disabled, are scheduled for deletion, or were
  deleted. Macie can't use these keys.
- **Skipped: Permission denied** – The total number of objects
  that Macie isn't allowed to access due to the permissions settings for the object, or the
  permissions settings for the key that was used to encrypt the object.

For details about these and other types of issues and errors that can occur, see [Remediating coverage
issues](discovery-coverage-remediate.md "discovery-coverage-remediate.md"). If you remediate the issues and errors, you can increase coverage of the bucket's data
during subsequent analysis cycles.

Statistics on the **Sensitive data discovery** tab don't include data
for objects that were changed or deleted after Macie analyzed or attempted to analyze them.
If objects are changed or deleted after Macie analyzes or attempts to analyze them, Macie
automatically recalculates these statistics to exclude the objects.

API
To retrieve data sensitivity and other details for an S3 bucket programmatically, you
have several options. The appropriate option depends on the details that you want to
retrieve:

- To retrieve a bucket's current sensitivity score and aggregated analysis statistics, use the
  [GetResourceProfile](../APIReference/resource-profiles.md "../APIReference/resource-profiles.md") operation. Or, if you're using the AWS Command Line Interface (AWS CLI), run the
  [get-resource-profile](../../../cli/latest/reference/macie2/get-resource-profile.md "../../../cli/latest/reference/macie2/get-resource-profile.md") command. The statistics include data such as the number of
  objects that Macie has analyzed, and the number of objects that Macie has found sensitive
  data in.
- To retrieve a breakdown of the types and amount of sensitive data that Macie has found
  in a bucket, use the [ListResourceProfileDetections](../APIReference/resource-profiles-detections.md "../APIReference/resource-profiles-detections.md") operation. Or, if you're using the AWS CLI, run the
  [list-resource-profile-detections](../../../cli/latest/reference/macie2/list-resource-profile-detections.md "../../../cli/latest/reference/macie2/list-resource-profile-detections.md") command. The breakdown also provides details
  about the managed or custom data identifier that detected each type of sensitive
  data.
- To retrieve a list of up to 100 objects that Macie selected from a bucket for analysis,
  use the [ListResourceProfileArtifacts](../APIReference/resource-profiles-artifacts.md "../APIReference/resource-profiles-artifacts.md") operation. Or, if you're using the AWS CLI, run the
  [list-resource-profile-artifacts](../../../cli/latest/reference/macie2/list-resource-profile-artifacts.md "../../../cli/latest/reference/macie2/list-resource-profile-artifacts.md") command. For each object, the list specifies: the
  Amazon Resource Name (ARN) of the object, whether Macie completed its analysis of the
  object; and, whether Macie found sensitive data in the object.

In your request, use the `resourceArn` parameter to specify the ARN of the
bucket to retrieve the details for. If you're using the AWS CLI, use the
`resource-arn` parameter to specify the ARN.

For additional details about an S3 bucket, such as the bucket's public access settings,
use the [DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md") operation. If you're using the AWS CLI, run the [describe-buckets](../../../cli/latest/reference/macie2/describe-buckets.md "../../../cli/latest/reference/macie2/describe-buckets.md") command to retrieve these details. In your request, optionally use
filter criteria to specify the name of the bucket. For more information and examples, see
[Filtering your S3 bucket
inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md").

The following examples show how to use the AWS CLI to retrieve data sensitivity details for
an S3 bucket. This first example retrieves the current sensitivity score and aggregated analysis
statistics for a bucket.

```
`$` `aws macie2 get-resource-profile --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket``
```

Where `arn:aws:s3:::amzn-s3-demo-bucket` is the ARN of the
bucket. If the request succeeds, you receive output similar to the following:

```
`{
 "profileUpdatedAt": "2024-11-21T15:44:46+00:00",
 "sensitivityScore": 83,
 "sensitivityScoreOverridden": false,
 "statistics": {
 "totalBytesClassified": 933599,
 "totalDetections": 3641,
 "totalDetectionsSuppressed": 0,
 "totalItemsClassified": 111,
 "totalItemsSensitive": 84,
 "totalItemsSkipped": 1,
 "totalItemsSkippedInvalidEncryption": 0,
 "totalItemsSkippedInvalidKms": 0,
 "totalItemsSkippedPermissionDenied": 0
 }
}`
```

The next example retrieves a breakdown of the types of sensitive data that Macie has
found in an S3 bucket, and the number of occurrences of each type. The breakdown also
specifies which managed data identifier or custom data identifier detected the data. It also
indicates whether the occurrences are currently excluded (`suppressed`) from the
bucket's sensitivity score, if the score is calculated automatically by Macie.

```
`$` `aws macie2 list-resource-profile-detections --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket``
```

Where `arn:aws:s3:::amzn-s3-demo-bucket` is the ARN of the
bucket. If the request succeeds, you receive output similar to the following:

```
`{
 "detections": [
 {
 "count": 8,
 "id": "AWS_CREDENTIALS",
 "name": "AWS_CREDENTIALS",
 "suppressed": false,
 "type": "MANAGED"
 },
 {
 "count": 1194,
 "id": "CREDIT_CARD_NUMBER",
 "name": "CREDIT_CARD_NUMBER",
 "suppressed": false,
 "type": "MANAGED"
 },
 {
 "count": 1194,
 "id": "CREDIT_CARD_SECURITY_CODE",
 "name": "CREDIT_CARD_SECURITY_CODE",
 "suppressed": false,
 "type": "MANAGED"
 },
 {
 "arn": "arn:aws:macie2:us-east-1:123456789012:custom-data-identifier/3293a69d-4a1e-4a07-8715-208ddexample",
 "count": 8,
 "id": "3293a69d-4a1e-4a07-8715-208ddexample",
 "name": "Employee IDs with keyword",
 "suppressed": false,
 "type": "CUSTOM"
 },
 {
 "count": 1237,
 "id": "USA_SOCIAL_SECURITY_NUMBER",
 "name": "USA_SOCIAL_SECURITY_NUMBER",
 "suppressed": false,
 "type": "MANAGED"
 }
 ]
}`
```

This example retrieves a list of objects that Macie selected from an S3 bucket for
analysis. For each object, the list also indicates whether Macie completed its analysis of the
object, and whether Macie found sensitive data in the object.

```
`$` `aws macie2 list-resource-profile-artifacts --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket``
```

Where `arn:aws:s3:::amzn-s3-demo-bucket` is the ARN of the
bucket. If the request succeeds, you receive output similar to the following:

```
`{
 "artifacts": [
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object1.csv",
 "classificationResultStatus": "COMPLETE",
 "sensitive": true
 },
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object2.xlsx",
 "classificationResultStatus": "COMPLETE",
 "sensitive": true
 },
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object3.json",
 "classificationResultStatus": "COMPLETE",
 "sensitive": true
 },
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object4.pdf",
 "classificationResultStatus": "COMPLETE",
 "sensitive": true
 },
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object5.zip",
 "classificationResultStatus": "PARTIAL",
 "sensitive": true
 },
 {
 "arn": "arn:aws:s3:::amzn-s3-demo-bucket/amzn-s3-demo-object6.vssx",
 "classificationResultStatus": "SKIPPED"
 }
 ]
}`
```
