After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# S3Configuration

Provides a description of an Amazon S3 data source, including the Amazon Resource Name
(ARN) of the S3 bucket, the ARN of the IAM role that is used to access the bucket, and
the name of the Amazon S3 object that contains the data.

## Contents

**BucketARN**

ARN of the S3 bucket that contains the data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

**FileKey**

The name of the object that contains the data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**RoleARN**

IAM ARN of the role used to access the data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3Configuration.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3Configuration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3Configuration.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3Configuration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3Configuration.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3Configuration.md")
