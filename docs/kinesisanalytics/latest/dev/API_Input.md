After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Input

When you configure the application input, you specify the streaming source, the
in-application stream name that is created, and the mapping between the two. For more
information, see [Configuring Application
Input](how-it-works-input.md "how-it-works-input.md").

## Contents

**InputSchema**

Describes the format of the data in the streaming source, and how each data element
maps to corresponding columns in the in-application stream that is being created.

Also used to describe the format of the reference data source.

Type: [SourceSchema](API_SourceSchema.md "API_SourceSchema.md") object

Required: Yes

**NamePrefix**

Name prefix to use when creating an in-application stream. Suppose that you specify a
prefix "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as
per the `InputParallelism` count you specified) in-application streams with
names "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: Yes

**InputParallelism**

Describes the number of in-application streams to create.

Data from your source is routed to these in-application input streams.

(see [Configuring Application
Input](how-it-works-input.md "how-it-works-input.md").

Type: [InputParallelism](API_InputParallelism.md "API_InputParallelism.md") object

Required: No

**InputProcessingConfiguration**

The [InputProcessingConfiguration](API_InputProcessingConfiguration.md "API_InputProcessingConfiguration.md") for the input. An input processor transforms
records as they are received from the stream, before the application's SQL code
executes. Currently, the only input processing configuration available is [InputLambdaProcessor](API_InputLambdaProcessor.md "API_InputLambdaProcessor.md").

Type: [InputProcessingConfiguration](API_InputProcessingConfiguration.md "API_InputProcessingConfiguration.md") object

Required: No

**KinesisFirehoseInput**

If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the
delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access
the stream on your behalf.

Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is
required.

Type: [KinesisFirehoseInput](API_KinesisFirehoseInput.md "API_KinesisFirehoseInput.md") object

Required: No

**KinesisStreamsInput**

If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon
Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the
stream on your behalf.

Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is
required.

Type: [KinesisStreamsInput](API_KinesisStreamsInput.md "API_KinesisStreamsInput.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/Input.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/Input.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/Input.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/Input.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/Input.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/Input.md")
