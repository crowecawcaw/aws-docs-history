

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# S3ReferenceDataSourceUpdate
<a name="API_S3ReferenceDataSourceUpdate"></a>

Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.

## Contents
<a name="API_S3ReferenceDataSourceUpdate_Contents"></a>

 ** BucketARNUpdate **   <a name="analytics-Type-S3ReferenceDataSourceUpdate-BucketARNUpdate"></a>
Amazon Resource Name (ARN) of the S3 bucket.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:.*`   
Required: No

 ** FileKeyUpdate **   <a name="analytics-Type-S3ReferenceDataSourceUpdate-FileKeyUpdate"></a>
Object key name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** ReferenceRoleARNUpdate **   <a name="analytics-Type-S3ReferenceDataSourceUpdate-ReferenceRoleARNUpdate"></a>
ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:.*`   
Required: No

## See Also
<a name="API_S3ReferenceDataSourceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/S3ReferenceDataSourceUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/S3ReferenceDataSourceUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/S3ReferenceDataSourceUpdate) 