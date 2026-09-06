

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# ReferenceDataSourceDescription
<a name="API_ReferenceDataSourceDescription"></a>

Describes the reference data source configured for an application.

## Contents
<a name="API_ReferenceDataSourceDescription_Contents"></a>

 ** ReferenceId **   <a name="analytics-Type-ReferenceDataSourceDescription-ReferenceId"></a>
ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns when you add the reference data source to your application using the [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html) operation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

 ** S3ReferenceDataSourceDescription **   <a name="analytics-Type-ReferenceDataSourceDescription-S3ReferenceDataSourceDescription"></a>
Provides the S3 bucket name, the object key name that contains the reference data. It also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application reference table.  
Type: [S3ReferenceDataSourceDescription](API_S3ReferenceDataSourceDescription.md) object  
Required: Yes

 ** TableName **   <a name="analytics-Type-ReferenceDataSourceDescription-TableName"></a>
The in-application table name created by the specific reference data source configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Required: Yes

 ** ReferenceSchema **   <a name="analytics-Type-ReferenceDataSourceDescription-ReferenceSchema"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.  
Type: [SourceSchema](API_SourceSchema.md) object  
Required: No

## See Also
<a name="API_ReferenceDataSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/ReferenceDataSourceDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ReferenceDataSourceDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ReferenceDataSourceDescription) 