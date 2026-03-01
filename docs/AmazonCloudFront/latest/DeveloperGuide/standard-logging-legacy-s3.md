# Configure standard logging (legacy)

###### Notes

- This topic is for the previous version of standard logging. For the latest
  version, see [Configure standard logging (v2)](standard-logging.md "standard-logging.md").
- If you already enabled standard logging (legacy) and you want to enable standard logging (v2) to Amazon S3,
  we recommend that you specify a _different_ Amazon S3 bucket or
  use a _separate path_ in the same bucket (for
  example, use a log prefix or partitioning). This helps you keep track of which
  log files are associated with which distribution and prevents log files from
  overwriting each other.
  To get started with standard logging (legacy), complete the following steps:

1. Choose an Amazon S3 bucket that will receive your logs and add the required
   permissions.
2. Configure standard logging (legacy) from the CloudFront console or the CloudFront API. You can only choose
   an Amazon S3 bucket to receive your logs.
3. View your access logs.

## Choose an Amazon S3 bucket for standard logs

When you enable logging for a distribution, you specify the Amazon S3 bucket that you want
CloudFront to store log files in. If you're using Amazon S3 as your origin, we recommend that you
use a _separate_ bucket for your log files.

Specify the Amazon S3 bucket that you want CloudFront to store access logs in, for example,
`amzn-s3-demo-bucket.s3.amazonaws.com`.

You can store the log files for multiple distributions in the same bucket. When you
enable logging, you can specify an optional prefix for the file names, so you can keep
track of which log files are associated with which distributions.

###### About choosing an S3 bucket

- Your bucket must have access control list (ACL) enabled. If you choose a
  bucket without ACL enabled from the CloudFront console, an error message will
  appear. See [Permissions](#AccessLogsBucketAndFileOwnership "#AccessLogsBucketAndFileOwnership").
- Don't choose an Amazon S3 bucket with [S3 Object
  Ownership](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") set to **bucket owner
  enforced**. That setting disables ACLs for the bucket and the
  objects in it, which prevents CloudFront from delivering log files to the
  bucket.
- Don't choose an Amazon S3 bucket in the following
  AWS Regions. CloudFront doesn't deliver standard logs to buckets in these Regions:
  - Africa (Cape Town)
  - Asia Pacific (Hong Kong)
  - Asia Pacific (Hyderabad)
  - Asia Pacific (Jakarta)
  - Asia Pacific (Melbourne)
  - Canada West (Calgary)
  - Europe (Milan)
  - Europe (Spain)
  - Europe (Zurich)
  - Israel (Tel Aviv)
  - Middle East (Bahrain)
  - Middle East (UAE)

## Permissions

###### Important

Starting in April 2023, you must enable S3 ACLs for new S3 buckets used for CloudFront
standard logs. You can enable ACLs when you [create a bucket](../../../AmazonS3/latest/userguide/object-ownership-new-bucket.md "../../../AmazonS3/latest/userguide/object-ownership-new-bucket.md"), or enable ACLs for an [existing bucket](../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md "../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md").

For more information about the changes, see [Default settings for new S3 buckets FAQ](../../../AmazonS3/latest/userguide/create-bucket-faq.md "../../../AmazonS3/latest/userguide/create-bucket-faq.md") in the _Amazon Simple Storage Service User Guide_ and [Heads-Up: Amazon S3 Security Changes Are Coming in April of 2023](https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/ "https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/") in the
_AWS News Blog_.

Your AWS account must have the following permissions for the bucket that you specify
for log files:

- The ACL for the bucket must grant you `FULL_CONTROL`. If you're the
  bucket owner, your account has this permission by default. If you're not, the
  bucket owner must update the ACL for the bucket.
- `s3:GetBucketAcl`
- `s3:PutBucketAcl`

**ACL for the bucket**

When you create or update a distribution and enable logging, CloudFront uses
these permissions to update the ACL for the bucket to give the
`awslogsdelivery` account `FULL_CONTROL`
permission. The `awslogsdelivery` account writes log files to the
bucket. If your account doesn't have the required permissions to update the
ACL, creating or updating the distribution will fail.

In some circumstances, if you programmatically submit a request to create
a bucket but a bucket with the specified name already exists, S3 resets
permissions on the bucket to the default value. If you configured CloudFront to
save access logs in an S3 bucket and you stop getting logs in that bucket,
check permissions on the bucket to ensure that CloudFront has the necessary
permissions.

**Restoring the ACL for the bucket**

If you remove permissions for the `awslogsdelivery` account,
CloudFront won't be able to save logs to the S3 bucket. To enable CloudFront to start
saving logs for your distribution again, restore the ACL permission by doing
one of the following:

- Disable logging for your distribution in CloudFront, and then enable it
  again. For more information, see [Standard logging](DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff "DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff").
- Add the ACL permission for `awslogsdelivery` manually
  by navigating to the S3 bucket in the Amazon S3 console and adding
  permission. To add the ACL for `awslogsdelivery`, you
  must provide the canonical ID for the account, which is the
  following:

`c4c1ede66af53448b93c283ce9448c4ba468c9432aa01d700d3878632f77d2d0`

For more information about adding ACLs to S3 buckets, see [Configuring ACLs](../../../AmazonS3/latest/userguide/managing-acls.md "../../../AmazonS3/latest/userguide/managing-acls.md") in the _Amazon Simple Storage Service User Guide_.

**ACL for each log file**

In addition to the ACL on the bucket, there's an ACL on each log file. The
bucket owner has `FULL_CONTROL` permission on each log file, the
distribution owner (if different from the bucket owner) has no permission,
and the `awslogsdelivery` account has read and write permissions.

**Disabling logging**

If you disable logging, CloudFront doesn't delete the ACLs for either the bucket
or the log files. You can delete the ACLs if needed.

### Required key policy for SSE-KMS buckets

If the S3 bucket for your standard logs uses server-side encryption with
AWS KMS keys (SSE-KMS) by using a customer managed key, you must add the following
statement to the key policy for your customer managed key. This allows CloudFront to write log files
to the bucket. You can't use SSE-KMS with the AWS managed key because CloudFront won't
be able to write log files to the bucket.

```
{
    "Sid": "Allow CloudFront to use the key to deliver logs",
    "Effect": "Allow",
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey*",
    "Resource": "*"
}
```

If the S3 bucket for your standard logs uses SSE-KMS with an [S3 Bucket
Key](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md"), you also need to add the `kms:Decrypt` permission to the
policy statement. In that case, the full policy statement looks like the
following.

```
{
    "Sid": "Allow CloudFront to use the key to deliver logs",
    "Effect": "Allow",
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey*",
        "kms:Decrypt"
    ],
    "Resource": "*"
}
```

###### Note

When you enable SSE-KMS for your S3 bucket, specify the complete ARN for the
customer managed key. For more information, see [Specifying
server-side encryption with AWS KMS keys (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the
_Amazon Simple Storage Service User Guide_.

## Enable standard logging (legacy)

To enable standard logs, use the CloudFront console or the CloudFront API.

###### Contents

- [Enable standard logging (legacy) (CloudFront console)](standard-logging-legacy-s3.md#standard-logs-legacy-enable-console "standard-logging-legacy-s3.md#standard-logs-legacy-enable-console")
- [Enable standard logging (legacy) (CloudFront API)](standard-logging-legacy-s3.md#standard-logs-legacy-enable-api "standard-logging-legacy-s3.md#standard-logs-legacy-enable-api")

### Enable standard logging (legacy) (CloudFront console)

###### To enable standard logs for a CloudFront distribution (console)

1. Use the CloudFront console to create a [new distribution](distribution-web-creating-console.md "distribution-web-creating-console.md") or
   [update an existing
   one](HowToUpdateDistribution.md#HowToUpdateDistributionProcedure "HowToUpdateDistribution.md#HowToUpdateDistributionProcedure").
2. For the **Standard logging** section, for **Log
   delivery**, choose **On**.
3. (Optional) For **Cookie logging**, choose
   **On** if you want to include cookies in your logs. For
   more information, see [Cookie logging](DownloadDistValuesGeneral.md#DownloadDistValuesCookieLogging "DownloadDistValuesGeneral.md#DownloadDistValuesCookieLogging").

###### Tip

Cookie logging is a global setting that applies to _all_ standard logs for your distribution.
You can’t override this setting for separate delivery
destinations. 4. For the **Deliver to** section, specify **Amazon S3
(Legacy)**. 5. Specify your Amazon S3 bucket. If you don't have one already, you can choose
**Create** or see the documentation to [create a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). 6. (Optional) For **Log prefix**, specify the string, if
any, that you want CloudFront to prefix to the access log file names for this
distribution, for example, `exampleprefix/`. The trailing slash (
/ ) is optional but recommended to simplify browsing your log files. For
more information, see [Log prefix](DownloadDistValuesGeneral.md#DownloadDistValuesLogPrefix "DownloadDistValuesGeneral.md#DownloadDistValuesLogPrefix"). 7. Complete the steps to update or create your distribution. 8. From the **Logs** page, verify that the standard logs
status is **Enabled** next to the distribution.

For more information about the standard logging delivery and log fields,
see the [Standard logging reference](standard-logs-reference.md "standard-logs-reference.md").

### Enable standard logging (legacy) (CloudFront API)

You can also use the CloudFront API to enable standard logs for your distributions.

###### To enable standard logs for a distribution (CloudFront API)

- Use the [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md") or [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") API operation and configure the [LoggingConfig](../../../cloudfront/latest/APIReference/API_LoggingConfig.md "../../../cloudfront/latest/APIReference/API_LoggingConfig.md") object.

## Edit standard logging settings

You can enable or disable logging, change the Amazon S3 bucket where your logs are stored,
and change the prefix for log files by using the [CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home") or the CloudFront API. Your changes to
logging settings take effect within 12 hours.

For more information, see the following topics:

- To update a distribution using the CloudFront console, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
- To update a distribution using the CloudFront API, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") in the
  _Amazon CloudFront API Reference_.

## Send logs to Amazon S3

When you send your logs to Amazon S3, your logs appear in the following format.

### File name format

The name of each log file that CloudFront saves in your Amazon S3 bucket uses the following
file name format:

``<optional
 prefix>`/`<distribution
 ID>`.`YYYY`-`MM`-`DD`-`HH`.`unique-ID`.gz`

The date and time are in Coordinated Universal Time (UTC).

For example, if you use `example-prefix` as the prefix, and your
distribution ID is `EMLARXS9EXAMPLE`, your file names look similar to
this:

`example-prefix/EMLARXS9EXAMPLE.2019-11-14-20.RT4KCN4SGK9.gz`

When you enable logging for a distribution, you can specify an optional prefix for
the file names, so you can keep track of which log files are associated with which
distributions. If you include a value for the log file prefix and your prefix
doesn't end with a forward slash (`/`), CloudFront appends one automatically.
If your prefix does end with a forward slash, CloudFront doesn't add another one.

The `.gz` at the end of the file name indicates that CloudFront has
compressed the log file using gzip.

## Standard log file format

Each entry in a log file gives details about a single viewer request. The log files
have the following characteristics:

- Use the [W3C extended log
  file format](https://www.w3.org/TR/WD-logfile.html "https://www.w3.org/TR/WD-logfile.html").
- Contain tab-separated values.
- Contain records that are not necessarily in chronological order.
- Contain two header lines: one with the file format version, and another that
  lists the W3C fields included in each record.
- Contain URL-encoded equivalents for spaces and certain other characters in
  field values.

URL-encoded equivalents are used for the following characters:

    + ASCII character codes 0 through 32, inclusive
    + ASCII character codes 127 and higher
    + All characters in the following table

The URL encoding standard is defined in [RFC 1738](https://tools.ietf.org/html/rfc1738.html "https://tools.ietf.org/html/rfc1738.html").

| URL-Encoded value | Character |
| ----------------- | --------- | --- |
| %3C               | <         |
| %3E               | >         |
| %22               | "         |
| %23               | #         |
| %25               | %         |
| %7B               | {         |
| %7D               | }         |
| %7C               |           |     |
| %5C               | \         |
| %5E               | ^         |
| %7E               | ~         |
| %5B               | [         |
| %5D               | ]         |
| %60               | `         |
| %27               | '         |
| %20               | space     |

## Delete log files

CloudFront doesn't automatically delete log files from your Amazon S3 bucket. For information
about deleting log files from an Amazon S3 bucket, see [Deleting objects](../../../AmazonS3/latest/userguide/DeletingObjects.md "../../../AmazonS3/latest/userguide/DeletingObjects.md") in the
_Amazon Simple Storage Service Console User Guide_.

## Pricing

Standard logging is an optional feature of CloudFront. CloudFront doesn’t charge for enabling
standard logs. However, you accrue the usual Amazon S3 charges for storing and accessing the
files on Amazon S3. You can delete them at any time.

For more information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

For more information about CloudFront pricing, see [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").
