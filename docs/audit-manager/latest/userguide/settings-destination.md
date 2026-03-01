# Configuring your default assessment report destination

When you generate an assessment report, Audit Manager publishes the report to the S3 bucket of
your choice. This S3 bucket is referred to as an [assessment report destination](concepts.md#assessment-report-destination "concepts.md#assessment-report-destination"). You can choose the S3 bucket that
Audit Manager stores your assessment reports in.

## Prerequisites

### Configuration tips for your assessment report destination

To ensure the successful generation of your assessment report, we
recommend that you use the following configurations for your assessment
report destination.

**Same-Region buckets**

We recommend that you use an S3 bucket that's in the same
AWS Region as your assessment. When you use a same-Region bucket
and assessment, your assessment report can include up to 22,000
evidence items. Conversely, when you use a cross-Region bucket and
assessment, only 3,500 evidence items can be included.

**AWS Region**

The AWS Region of your customer managed key (if you provided one) must
match the Region of your assessment and your assessment report
destination S3 bucket. For instructions on how to change the
KMS key, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md"). For a list of supported Audit Manager
Regions, see [AWS Audit Manager endpoints
and quotas](../../../general/latest/gr/audit-manager.md "../../../general/latest/gr/audit-manager.md") in the _Amazon Web Services General
Reference_.

**S3 bucket encryption**

If your assessment report destination has a bucket policy that
requires server-side encryption (SSE) using [SSE-KMS](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#require-sse-kms "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#require-sse-kms"), then the KMS key used in that bucket policy
must match the KMS key that you configured in your Audit Manager data
encryption settings. If you haven't configured a KMS key in your
Audit Manager settings, and your assessment report destination bucket policy
requires SSE, ensure that the bucket policy allows [SSE-S3](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md"). For instructions on how to configure the
KMS key that's used for data encryption, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").

**Cross-account S3 buckets**

Using a cross-account S3 bucket as your assessment report
destination isn’t supported in the Audit Manager console. It’s possible to
specify a cross-account bucket as your assessment report destination
by using the AWS CLI or one of the AWS SDKs, but for simplicity, we
recommend that you not do this.

###### Tip

For optimal security and performance, we recommend using an S3
bucket in the same AWS account and region as your assessment.

If you do choose to use a cross-account S3 bucket as your
assessment report destination, consider the following points.

- By default, S3 objects—such as assessment
  reports—are owned by the AWS account that uploads
  the object. You can use the [S3 Object Ownership](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") setting to change this
  default behavior so that any new objects that are written by
  accounts with the `bucket-owner-full-control`
  canned access control list (ACL) automatically become owned
  by the bucket owner.

Although it’s not a requirement, we recommend that you
make the following changes to your cross-account bucket
settings. Making these changes ensures that the bucket owner
has full control of the assessment reports that you publish
to their bucket.

    + [Set the object ownership of the S3 bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md#enable-object-ownership "../../../AmazonS3/latest/userguide/about-object-ownership.md#enable-object-ownership")
     to *bucket owner
     preferred*, instead of the default
      *object writer*
    + [Add a bucket policy](../../../AmazonS3/latest/userguide/about-object-ownership.md#ensure-object-ownership "../../../AmazonS3/latest/userguide/about-object-ownership.md#ensure-object-ownership") to ensure that
     objects uploaded to that bucket have the
     `bucket-owner-full-control` ACL

- To allow Audit Manager to publish reports in a cross-account S3
  bucket, you must add the following S3 bucket policy to your
  assessment report destination. Replace the
  `placeholder text` with your
  own information. The `Principal` element in this
  policy is the user or role that owns the assessment and
  creates the assessment report. The `Resource`
  specifies the cross-account S3 bucket where the report is
  published.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow cross account assessment report publishing",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`AssessmentOwnerUserName`"
 },
 "Action": [
 "s3:ListBucket",
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetBucketLocation",
 "s3:PutObjectAcl",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`CROSS-ACCOUNT-BUCKET`",
 "arn:aws:s3:::`CROSS-ACCOUNT-BUCKET/*`"
 ]
 }
 ]
}`

```

## Procedure

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the
Audit Manager API.

Audit Manager console

###### To update your default assessment report destination on the Audit Manager console

1. From the **Assessment** settings tab, go to
   the **Assessment report destination**
   section.
2. To use an existing S3 bucket, select a bucket name from the
   dropdown menu.
3. To create a new S3 bucket, choose **Create new
   bucket**.
4. When you’re done, choose **Save**.

AWS CLI

###### To update your default assessment report destination in the AWS CLI

Run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command and use the
`--default-assessment-reports-destination` parameter
to specify an S3 bucket.

In the following example, replace the `placeholder
 text` with your own information:

```
aws auditmanager update-settings --default-assessment-reports-destination destinationType=S3,destination=`s3://amzn-s3-demo-destination-bucket`
```

Audit Manager API

###### To update your default assessment report destination using the API

Call the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") operation and use the [defaultAssessmentReportsDestination](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-defaultAssessmentReportsDestination "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-defaultAssessmentReportsDestination") parameter to
specify an S3 bucket.

## Additional resources

- [Creating a
  bucket](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md")
- [Assessment reports](assessment-reports.md "assessment-reports.md")
