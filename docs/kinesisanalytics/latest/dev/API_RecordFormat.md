

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# RecordFormat
<a name="API_RecordFormat"></a>

 Describes the record format and relevant mapping information that should be applied to schematize the records on the stream. 

## Contents
<a name="API_RecordFormat_Contents"></a>

 ** RecordFormatType **   <a name="analytics-Type-RecordFormat-RecordFormatType"></a>
The type of record format.  
Type: String  
Valid Values: `JSON | CSV`   
Required: Yes

 ** MappingParameters **   <a name="analytics-Type-RecordFormat-MappingParameters"></a>
When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.  
Type: [MappingParameters](API_MappingParameters.md) object  
Required: No

## See Also
<a name="API_RecordFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/RecordFormat) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/RecordFormat) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/RecordFormat) 