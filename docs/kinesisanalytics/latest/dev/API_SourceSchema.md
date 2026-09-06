

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# SourceSchema
<a name="API_SourceSchema"></a>

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

## Contents
<a name="API_SourceSchema_Contents"></a>

 ** RecordColumns **   <a name="analytics-Type-SourceSchema-RecordColumns"></a>
A list of `RecordColumn` objects.  
Type: Array of [RecordColumn](API_RecordColumn.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: Yes

 ** RecordFormat **   <a name="analytics-Type-SourceSchema-RecordFormat"></a>
Specifies the format of the records on the streaming source.  
Type: [RecordFormat](API_RecordFormat.md) object  
Required: Yes

 ** RecordEncoding **   <a name="analytics-Type-SourceSchema-RecordEncoding"></a>
Specifies the encoding of the records in the streaming source. For example, UTF-8.  
Type: String  
Pattern: `UTF-8`   
Required: No

## See Also
<a name="API_SourceSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/SourceSchema) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/SourceSchema) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/SourceSchema) 