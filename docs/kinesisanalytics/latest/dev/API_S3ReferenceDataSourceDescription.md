After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# S3ReferenceDataSourceDescription

Provides the bucket name and object key name that stores the reference data.

## Contents

**BucketARN**

Amazon Resource Name (ARN) of the S3 bucket.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

**FileKey**

Amazon S3 object key name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**ReferenceRoleARN**

ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3
object on your behalf to populate the in-application reference table.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3ReferenceDataSourceDescription.md")
