After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# ReferenceDataSourceUpdate

When you update a reference data source configuration for an application, this object
provides all the updated values (such as the source bucket name and object key name),
the in-application table name that is created, and updated mapping information that maps
the data in the Amazon S3 object to the in-application reference table that is
created.

## Contents

**ReferenceId**

ID of the reference data source being updated. You can use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get this value.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**ReferenceSchemaUpdate**

Describes the format of the data in the streaming source, and how each data element
maps to corresponding columns created in the in-application stream.

Type: [SourceSchema](API_SourceSchema.md "API_SourceSchema.md") object

Required: No

**S3ReferenceDataSourceUpdate**

Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis
Analytics can assume to read the Amazon S3 object on your behalf and populate the
in-application reference table.

Type: [S3ReferenceDataSourceUpdate](API_S3ReferenceDataSourceUpdate.md "API_S3ReferenceDataSourceUpdate.md") object

Required: No

**TableNameUpdate**

In-application table name that is created by this update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate.md")
