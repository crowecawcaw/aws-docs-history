

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# ReferenceDataSourceUpdate
<a name="API_ReferenceDataSourceUpdate"></a>

When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

## Contents
<a name="API_ReferenceDataSourceUpdate_Contents"></a>

 ** ReferenceId **   <a name="analytics-Type-ReferenceDataSourceUpdate-ReferenceId"></a>
ID of the reference data source being updated. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to get this value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

 ** ReferenceSchemaUpdate **   <a name="analytics-Type-ReferenceDataSourceUpdate-ReferenceSchemaUpdate"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.   
Type: [SourceSchema](API_SourceSchema.md) object  
Required: No

 ** S3ReferenceDataSourceUpdate **   <a name="analytics-Type-ReferenceDataSourceUpdate-S3ReferenceDataSourceUpdate"></a>
Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.  
Type: [S3ReferenceDataSourceUpdate](API_S3ReferenceDataSourceUpdate.md) object  
Required: No

 ** TableNameUpdate **   <a name="analytics-Type-ReferenceDataSourceUpdate-TableNameUpdate"></a>
In-application table name that is created by this update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Required: No

## See Also
<a name="API_ReferenceDataSourceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSourceUpdate) 