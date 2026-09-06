

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# CSVMappingParameters
<a name="API_CSVMappingParameters"></a>

Provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter: 

 `"name1", "address1"` 

 `"name2", "address2"` 

## Contents
<a name="API_CSVMappingParameters_Contents"></a>

 ** RecordColumnDelimiter **   <a name="analytics-Type-CSVMappingParameters-RecordColumnDelimiter"></a>
Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** RecordRowDelimiter **   <a name="analytics-Type-CSVMappingParameters-RecordRowDelimiter"></a>
Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## See Also
<a name="API_CSVMappingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/CSVMappingParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CSVMappingParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CSVMappingParameters) 