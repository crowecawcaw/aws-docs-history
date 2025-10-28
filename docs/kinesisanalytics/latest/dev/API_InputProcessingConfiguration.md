After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputProcessingConfiguration

Provides a description of a processor that is used to preprocess the records in the
stream before being processed by your application code. Currently, the only input
processor available is [AWS Lambda](../../../lambda.md "../../../lambda.md").

## Contents

**InputLambdaProcessor**

The [InputLambdaProcessor](API_InputLambdaProcessor.md "API_InputLambdaProcessor.md") that is used to preprocess the records in the stream
before being processed by your application code.

Type: [InputLambdaProcessor](API_InputLambdaProcessor.md "API_InputLambdaProcessor.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputProcessingConfiguration.md")
