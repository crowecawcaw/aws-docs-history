After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# ReferenceDataSource

Describes the reference data source by providing the source information (S3 bucket
name and object key name), the resulting in-application table name that is created, and
the necessary schema to map the data elements in the Amazon S3 object to the
in-application table.

## Contents

**ReferenceSchema**

Describes the format of the data in the streaming source, and how each data element
maps to corresponding columns created in the in-application stream.

Type: [SourceSchema](API_SourceSchema.md "API_SourceSchema.md") object

Required: Yes

**TableName**

Name of the in-application table to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: Yes

**S3ReferenceDataSource**

Identifies the S3 bucket and object that contains the reference data. Also identifies
the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf. An
Amazon Kinesis Analytics application loads reference data only once. If the data
changes, you call the `UpdateApplication` operation to trigger reloading of
data into your application.

Type: [S3ReferenceDataSource](API_S3ReferenceDataSource.md "API_S3ReferenceDataSource.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSource.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSource.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSource.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSource.md")
