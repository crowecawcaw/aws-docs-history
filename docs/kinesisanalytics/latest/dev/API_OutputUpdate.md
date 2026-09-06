

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# OutputUpdate
<a name="API_OutputUpdate"></a>

 Describes updates to the output configuration identified by the `OutputId`. 

## Contents
<a name="API_OutputUpdate_Contents"></a>

 ** OutputId **   <a name="analytics-Type-OutputUpdate-OutputId"></a>
Identifies the specific output configuration that you want to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

 ** DestinationSchemaUpdate **   <a name="analytics-Type-OutputUpdate-DestinationSchemaUpdate"></a>
Describes the data format when records are written to the destination. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html).  
Type: [DestinationSchema](API_DestinationSchema.md) object  
Required: No

 ** KinesisFirehoseOutputUpdate **   <a name="analytics-Type-OutputUpdate-KinesisFirehoseOutputUpdate"></a>
Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.  
Type: [KinesisFirehoseOutputUpdate](API_KinesisFirehoseOutputUpdate.md) object  
Required: No

 ** KinesisStreamsOutputUpdate **   <a name="analytics-Type-OutputUpdate-KinesisStreamsOutputUpdate"></a>
Describes an Amazon Kinesis stream as the destination for the output.  
Type: [KinesisStreamsOutputUpdate](API_KinesisStreamsOutputUpdate.md) object  
Required: No

 ** LambdaOutputUpdate **   <a name="analytics-Type-OutputUpdate-LambdaOutputUpdate"></a>
Describes an AWS Lambda function as the destination for the output.  
Type: [LambdaOutputUpdate](API_LambdaOutputUpdate.md) object  
Required: No

 ** NameUpdate **   <a name="analytics-Type-OutputUpdate-NameUpdate"></a>
If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Required: No

## See Also
<a name="API_OutputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/OutputUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/OutputUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/OutputUpdate) 