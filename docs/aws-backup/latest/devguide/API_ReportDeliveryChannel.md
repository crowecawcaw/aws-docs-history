# ReportDeliveryChannel

Contains information from your report plan about where to deliver your reports,
specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your
reports.

## Contents

**S3BucketName**

The unique name of the S3 bucket that receives your reports.

Type: String

Required: Yes

**Formats**

The format of your reports: `CSV`, `JSON`, or both. If
not specified, the default format is `CSV`.

Type: Array of strings

Required: No

**S3KeyPrefix**

The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path:
s3://your-bucket-name/`prefix`/Backup/us-west-2/year/month/day/report-name.
If not specified, there is no prefix.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ReportDeliveryChannel.md "../../../goto/SdkForCpp/backup-2018-11-15/ReportDeliveryChannel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ReportDeliveryChannel.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ReportDeliveryChannel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ReportDeliveryChannel.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ReportDeliveryChannel.md")
