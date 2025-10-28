# Collecting data from custom sources in Security Lake

Amazon Security Lake can collect logs and events from third-party custom sources. A Security Lake custom source is a third-party service that sends security logs and events to Amazon Security Lake. Before sending the data, the custom source must convert the logs and events to the Open Cybersecurity Schema Framework (OCSF) and meet the source requirements for Security Lake including partitioning, parquet file format and object size and rate requirements.

For each custom source, Security Lake handles the following:

- Provides a unique prefix for the source in your Amazon S3 bucket.
- Creates a role in AWS Identity and Access Management (IAM) that permits a custom source to write data to
  the data lake. The permissions boundary for this role is set by an AWS managed
  policy called [AmazonSecurityLakePermissionsBoundary](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary").
- Creates an AWS Lake Formation table to organize objects that the source writes to
  Security Lake.
- Sets up an AWS Glue crawler to partition your source data. The crawler populates
  the AWS Glue Data Catalog with the table. It also automatically discovers new source data and
  extracts schema definitions.

###### Note

You can add up to a maximum of 50 custom log sources in an account.

To add a custom source to Security Lake, it must meet the following requirements. Failure to meet these requirements could have performance impacts, and may impact analytics use cases such as querying.

- **Destination** – The custom source must be
  able to write data to Security Lake as a set of S3 objects underneath the prefix
  assigned to the source. For sources that contain multiple categories of data, you
  should deliver each unique [Open Cybersecurity Schema Framework (OCSF) event class](https://schema.ocsf.io/classes?extensions= "https://schema.ocsf.io/classes?extensions=") as a separate
  source. Security Lake creates an IAM role that permits the custom source to write to
  the specified location in your S3 bucket.
- **Format** – Each S3 object that's collected from the custom source should be formatted as an Apache Parquet file.
- **Schema** – The same OCSF event class should apply to each record within a Parquet-formatted object. Security Lake supports versions 1.x and 2.x of Parquet. Data page size should be limited to 1 MB (uncompressed). Row group size should be no larger than 256 MB (compressed). For compression within the Parquet object, zstandard is preferred.
- **Partitioning** – Objects must be partitioned by region, AWS account, eventDay. Objects should be prefixed with ``source location`/region=`region`/accountId=`accountID`/eventDay=`yyyyMMdd`/`.
- **Object size and rate** – Files sent to Security Lake should be sent in increments between 5 minutes and 1 event day. Customers may send files more often than 5 minutes if files are larger than 256MB in size. The object and size requirement is to optimize Security Lake for Query Performance. Not following the custom source requirements may have an impact on your Security Lake performance.
- **Sorting** – Within each Parquet-formatted object, records should be ordered by time to reduce the cost of querying data.

###### Note

Use the [OCSF
Validation tool](https://github.com/aws-samples/amazon-security-lake-ocsf-validation "https://github.com/aws-samples/amazon-security-lake-ocsf-validation") to verify if the custom source is compatible with the `OCSF Schema`.
For custom sources, Security Lake supports OCSF version 1.3 and earlier.

## Partitioning requirements for ingesting custom

sources in Security Lake

To facilitate efficient data processing and querying, we require meeting the partitioning and object and size requirements when adding a custom source to Security Lake:

**Partitioning**

Objects should be partitioned by source location, AWS Region,
AWS account, and date.

- The partition data path is formatted as

`/ext/`custom-source-name`/region=`region`/accountId=`accountID`/eventDay=`YYYYMMDD``.

A sample partition with example bucket name is
`aws-security-data-lake-`us-west-2-lake-uid`/ext/`custom-source-name`/region=`us-west-2`/accountId=`123456789012`/eventDay=`20230428`/`.

The following list describes the parameters used in the S3 path partition:

- The name of the Amazon S3 bucket in which Security Lake stores your custom source data.
- `source-location` – Prefix for the custom source
  in your S3 bucket. Security Lake stores all S3 objects for a given
  source under this prefix, and the prefix is unique to the given
  source.
- `region` – AWS Region to which the data is
  uploaded. For example, you must use `US East (N. Virginia)` to upload data into your Security Lake bucket in the US East (N. Virginia) region.
- `accountId` – AWS account ID that the records
  in the source partition pertain to. For records pertaining to
  accounts outside of AWS, we recommend using a string such as
  `external` or
  `external_externalAccountId`. By adopting this naming
  convection, you can avoid ambiguity in naming external account IDs
  so that they do not conflict with AWS account IDs or external
  account IDs maintained by other identity management systems.
- `eventDay` – UTC timestamp of the record, truncated to hour
  formatted as an eight character string
  (`YYYYMMDD`). If records specify a different timezone in the event timestamp, you must convert the timestamp into UTC for this partition key.

## Prerequisites to adding a custom

source in Security Lake

When adding a custom source, Security Lake creates an IAM role that permits the source
to write data to the correct location in the data lake. The name of the role follows the
format `AmazonSecurityLake-Provider-{name of the custom source}-{region}`,
where `region` is the AWS Region in which you're adding the custom source.
Security Lake attaches a policy to the role that permits access to the data lake. If you've
encrypted the data lake with a customer managed AWS KMS key, Security Lake also attaches a
policy with `kms:Decrypt` and `kms:GenerateDataKey` permissions to
the role. The permissions boundary for this role is set by an AWS managed policy
called [AmazonSecurityLakePermissionsBoundary](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary").

###### Topics

- [Verify permissions](#add-custom-sources-permissions "#add-custom-sources-permissions")
- [Create IAM role to permit write access
  to Security Lake bucket location (API and AWS CLI-only step)](#iam-roles-glue-crawler "#iam-roles-glue-crawler")

### Verify permissions

Before adding a custom source, verify that you have the permissions to perform the
following actions.

To verify your permissions, use IAM to review the IAM policies that are
attached to your IAM identity. Then, compare the information in those policies to
the following list of actions that you must be allowed to perform to add a custom
source.

- `glue:CreateCrawler`
- `glue:CreateDatabase`
- `glue:CreateTable`
- `glue:StopCrawlerSchedule`
- `iam:GetRole`
- `iam:PutRolePolicy`
- `iam:DeleteRolePolicy`
- `iam:PassRole`
- `lakeformation:RegisterResource`
- `lakeformation:GrantPermissions`
- `s3:ListBucket`
- `s3:PutObject`

These actions allow you to collect logs and events from a custom source, send them
to the correct AWS Glue database and table, and store them in Amazon S3.

If you use an AWS KMS key for server-side encryption of your data lake, you also
need permission for `kms:CreateGrant`, `kms:DescribeKey`, and
`kms:GenerateDataKey`.

###### Important

If you plan to use the Security Lake console to add a custom source, you can
skip the next step and proceed to [Adding a custom source in Security Lake](adding-custom-sources.md "adding-custom-sources.md"). The Security Lake console offers a
streamlined process for getting started, and creates all necessary IAM roles or uses
existing roles on your behalf.

If you plan to use Security Lake API or AWS CLI to add a custom source, continue with
the next step to create an IAM role to permit write access to Security Lake bucket location.

### Create IAM role to permit write access

to Security Lake bucket location (API and AWS CLI-only step)

If you're using Security Lake API or AWS CLI to add a custom source, add this IAM role to
grant AWS Glue permission to crawl your custom source data and
identify partitions in the data. These partitions are necessary to organize your
data and create and update tables in the Data Catalog.

After creating this IAM role, you will need the Amazon Resource Name (ARN) of
the role in order to add a custom source.

You must attach the
`arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole` AWS
managed policy.

To grant the necessary permissions, you must also create and embed the following
inline policy in your role to permit AWS Glue crawler to read data files from the
custom source and create/update the tables in AWS Glue Data Catalog.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3WriteRead",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

Attach the following trust policy to permit an AWS account by using which, it
can assume the role based on the external ID:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

[Show moreShow less](# "#")
If the S3 bucket in the Region where you're adding the custom source is encrypted
with a customer-managed AWS KMS key, you must also attach the following policy to
the role and to your KMS key policy:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey"
        "kms:Decrypt"
    ],
    "Condition": {
        "StringLike": {
            "kms:EncryptionContext:aws:s3:arn": [
                "arn:aws:s3:::{{`name of S3 bucket created by Security Lake`}"
            ]
        }
    },
    "Resource": [
        "{{ARN of customer managed key}}"
    ]
}
```

[Show moreShow less](# "#")
