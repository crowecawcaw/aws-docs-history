# Collecting data from AWS services in Security Lake

Amazon Security Lake can collect logs and events from the following natively-supported
AWS services:

- AWS CloudTrail management and data events (S3, Lambda)
- Amazon Elastic Kubernetes Service (Amazon EKS) Audit Logs
- Amazon Route 53 resolver query logs
- AWS Security Hub findings
- Amazon Virtual Private Cloud (Amazon VPC) Flow Logs
- AWS WAFv2 logs
  Security Lake automatically transforms this data into the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") and Apache Parquet format.

###### Tip

To add one or more of the preceding services as a log source in Security Lake, you
_don't_ need to separately configure logging in these services,
except CloudTrail management events. If you do have logging configured in these services, you
_don't_ need to change your logging configuration to add them as
log sources in Security Lake. Security Lake pulls data directly from these services through an independent
and duplicated stream of events.

## Prerequisite: Verify

permissions

To add an AWS service as a source in Security Lake, you must have the necessary permissions.
Verify that the AWS Identity and Access Management (IAM) policy attached to the role that you use to add a
source has permission to perform the following actions:

- `glue:CreateDatabase`
- `glue:CreateTable`
- `glue:GetDatabase`
- `glue:GetTable`
- `glue:UpdateTable`
- `iam:CreateServiceLinkedRole`
- `s3:GetObject`
- `s3:PutObject`

It is recommended for the role to have the following conditions and resource scope for
the `S3:getObject` and `s3:PutObject` permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdatingSecurityLakeS3Buckets",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::aws-security-data-lake*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

These actions allow you to collect logs and events from the an AWS service and send
them to the correct AWS Glue database and table.

If you use a AWS KMS key for server-side encryption of your data lake, you also need
permission for `kms:DescribeKey`.

## Adding an AWS service as a source

After you add an AWS service as a source, Security Lake automatically starts collecting
security logs and events from it. These instructions tell you how to add a
natively-supported AWS service as a source in Security Lake. For instructions on adding a
custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

Console

###### To add an AWS log source (console)

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Choose **Sources** from the navigation
   pane.
3. Select the AWS service that you want to collect data from, and
   choose **Configure**.
4. In the **Source settings** section, enable the
   source and select the **Version** of data source
   that you want to use for data ingestion. By default, the latest
   version of data source is ingested by Security Lake.

###### Important

If you don't have the required role permissions to enable the
new version of the AWS log source in the specified Region,
contact your Security Lake administrator. For more information, see
[Update role permissions](internal-sources.md#update-role-permissions "internal-sources.md#update-role-permissions").

For your subscribers to ingest the selected version of the data
source, you must also update your subscriber settings. For the
details on how to edit a subscriber, see [Subscriber management in Amazon Security Lake](subscriber-management.md "subscriber-management.md").

Optionally, you can choose to ingest the latest version only and
disable all previous source versions used for data ingestion. 5. In the **Regions** section, select the Regions in
which you want to collect data for the source. Security Lake will collect
data from the source from _all_ accounts in the
selected Regions. 6. Choose **Enable**.

API
**To add an AWS log source (API)**

To add an AWS service as a source programmatically, use the [CreateAwsLogSource](../APIReference/API_CreateAwsLogSource.md "../APIReference/API_CreateAwsLogSource.md") operation of the Security Lake API. If you're using
the AWS Command Line Interface (AWS CLI), run the [create-aws-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-aws-log-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-aws-log-source.html") command. The `sourceName` and
`regions` parameters are required. Optionally, you can
limit the scope of the source to specific `accounts` or a
specific `sourceVersion`.

###### Important

When you don't provide a parameter in your command, Security Lake assumes that
the missing parameter refers to the entire set. For example, if you
don't provide the `accounts` parameter , the command
applies to the entire set of accounts in your organization.

The following example adds VPC Flow Logs as a source in the designated
accounts and Regions. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

###### Note

If you apply this request to a Region in which you haven't enabled
Security Lake, you'll receive an error. You can resolve the error by enabling
Security Lake in that Region or by using the `regions` parameter
to specify only those Regions in which you've enabled Security Lake.

```
`$` aws securitylake create-aws-log-source \
--sources sourceName=`VPC_FLOW`,accounts=`'["123456789012", "111122223333"]'`,regions=`["us-east-2"]`,sourceVersion=`"2.0"`
```

## Getting the status of source

collection

Choose your access method, and follow the steps to get a snapshot of the accounts and
sources for which log collection is enabled in the current Region.

Console

###### To get the status of log collection in the current Region

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. On the navigation pane, choose
   **Accounts**.
3. Hover the cursor over the number in the
   **Sources** column to see which logs are
   enabled for the selected account.

API
To get the status of log collection in the current Region, use the [GetDataLakeSources](../APIReference/API_GetDataLakeSources.md "../APIReference/API_GetDataLakeSources.md") operation of the Security Lake API. If you're using
the AWS CLI, run the [get-data-lake-sources](../../../cli/latest/reference/securitylake/get-data-lake-sources.md "../../../cli/latest/reference/securitylake/get-data-lake-sources.md") command. For the `accounts`
parameter, you can specify one or more AWS account IDs as a list. If your
request succeeds, Security Lake returns a snapshot for those accounts in the current
Region, including which AWS sources Security Lake is collecting data from and the
status of each source. If you don't include the `accounts`
parameter, the response includes the status of log collection for all
accounts in which Security Lake is configured in the current Region.

For example, the following AWS CLI command retrieves log collection status
for the specified accounts in the current Region. This example is formatted
for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws securitylake get-data-lake-sources \
--accounts "`123456789012`" "`111122223333`"`
```

## Removing an AWS service as a source

Choose your access method, and follow these steps to remove a natively-supported
AWS service as a Security Lake source. You can remove a source for one or more Regions. When
you remove the source, Security Lake stops collecting data from that source in the specified
Regions and accounts, and subscribers can no longer consume new data from the source.
However, subscribers can still consume data that Security Lake collected from the source before
removal. You can only use these instructions to remove a natively-supported
AWS service as a source. For information about removing a custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Choose **Sources** from the navigation
   pane.
3. Select a source, and choose **Disable**.
4. Select a Region or Regions in which you want to stop collecting
   data from this source. Security Lake will stop collecting data from the
   source from _all_ accounts in the selected
   Regions.

API
To remove an AWS service as a source programmatically, use the [DeleteAwsLogSource](../APIReference/API_DeleteAwsLogSource.md "../APIReference/API_DeleteAwsLogSource.md") operation of the Security Lake API. If you're using
the AWS Command Line Interface (AWS CLI), run the [delete-aws-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html") command. The
`sourceName` and `regions` parameters
are required. Optionally, you can limit the scope of the removal to specific
`accounts` or a specific
`sourceVersion`.

###### Important

When you don't provide a parameter in your command, Security Lake assumes that
the missing parameter refers to the entire set. For example, if you
don't provide the `accounts` parameter , the command
applies to the entire set of accounts in your organization.

The following example removes VPC Flow Logs as a source in the designated
accounts and Regions.

```
`$` `aws securitylake delete-aws-log-source \
--sources sourceName=`VPC_FLOW`,accounts=`'["123456789012", "111122223333"]'`,regions=`'["us-east-1", "us-east-2"]'`,sourceVersion=`"2.0"``
```

The following example removes Route 53 as a source in the designated
account and Regions.

```
`$` `aws securitylake delete-aws-log-source \
--sources sourceName=`ROUTE53`,accounts=`'["123456789012"]'`,regions=`'["us-east-1", "us-east-2"]'`,sourceVersion=`"2.0"``
```

The preceding examples are formatted for Linux, macOS, or Unix, and they
use the backslash (\) line-continuation character to improve
readability.
