After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# S3ReferenceDataSource

Identifies the S3 bucket and object that contains the reference data. Also identifies
the IAM role Amazon Kinesis Analytics can assume to read this object on your
behalf.

An Amazon Kinesis Analytics application loads reference data only once. If the data
changes, you call the [UpdateApplication](API_UpdateApplication.md "API_UpdateApplication.md") operation to trigger reloading of data into your
application.

## Contents

**BucketARN**

Amazon Resource Name (ARN) of the S3 bucket.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

**FileKey**

Object key name containing reference data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**ReferenceRoleARN**

ARN of the IAM role that the service can assume to read data on your behalf. This role
must have permission for the `s3:GetObject` action on the object and trust
policy that allows Amazon Kinesis Analytics service principal to assume this
role.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3ReferenceDataSource.md")
