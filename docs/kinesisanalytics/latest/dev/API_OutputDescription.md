

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# OutputDescription
<a name="API_OutputDescription"></a>

Describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream. 

## Contents
<a name="API_OutputDescription_Contents"></a>

 ** DestinationSchema **   <a name="analytics-Type-OutputDescription-DestinationSchema"></a>
Data format used for writing data to the destination.  
Type: [DestinationSchema](API_DestinationSchema.md) object  
Required: No

 ** KinesisFirehoseOutputDescription **   <a name="analytics-Type-OutputDescription-KinesisFirehoseOutputDescription"></a>
Describes the Amazon Kinesis Firehose delivery stream configured as the destination where output is written.  
Type: [KinesisFirehoseOutputDescription](API_KinesisFirehoseOutputDescription.md) object  
Required: No

 ** KinesisStreamsOutputDescription **   <a name="analytics-Type-OutputDescription-KinesisStreamsOutputDescription"></a>
Describes Amazon Kinesis stream configured as the destination where output is written.  
Type: [KinesisStreamsOutputDescription](API_KinesisStreamsOutputDescription.md) object  
Required: No

 ** LambdaOutputDescription **   <a name="analytics-Type-OutputDescription-LambdaOutputDescription"></a>
Describes the AWS Lambda function configured as the destination where output is written.  
Type: [LambdaOutputDescription](API_LambdaOutputDescription.md) object  
Required: No

 ** Name **   <a name="analytics-Type-OutputDescription-Name"></a>
Name of the in-application stream configured as output.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Required: No

 ** OutputId **   <a name="analytics-Type-OutputDescription-OutputId"></a>
A unique identifier for the output configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: No

## See Also
<a name="API_OutputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/OutputDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/OutputDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/OutputDescription) 