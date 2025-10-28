After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputDescription

Describes the application input configuration. For more information, see [Configuring Application Input](how-it-works-input.md "how-it-works-input.md").

## Contents

**InAppStreamNames**

Returns the in-application stream names that are mapped to the stream source.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: No

**InputId**

Input ID associated with the application input. This is the ID that Amazon Kinesis
Analytics assigns to each input configuration you add to your application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**InputParallelism**

Describes the configured parallelism (number of in-application streams mapped to the
streaming source).

Type: [InputParallelism](API_InputParallelism.md "API_InputParallelism.md") object

Required: No

**InputProcessingConfigurationDescription**

The description of the preprocessor that executes on records in this input before the
application's code is run.

Type: [InputProcessingConfigurationDescription](API_InputProcessingConfigurationDescription.md "API_InputProcessingConfigurationDescription.md") object

Required: No

**InputSchema**

Describes the format of the data in the streaming source, and how each data element
maps to corresponding columns in the in-application stream that is being created.

Type: [SourceSchema](API_SourceSchema.md "API_SourceSchema.md") object

Required: No

**InputStartingPositionConfiguration**

Point at which the application is configured to read from the input stream.

Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md "API_InputStartingPositionConfiguration.md") object

Required: No

**KinesisFirehoseInputDescription**

If an Amazon Kinesis Firehose delivery stream is configured as a streaming source,
provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics
to access the stream on your behalf.

Type: [KinesisFirehoseInputDescription](API_KinesisFirehoseInputDescription.md "API_KinesisFirehoseInputDescription.md") object

Required: No

**KinesisStreamsInputDescription**

If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis
stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis
Analytics to access the stream on your behalf.

Type: [KinesisStreamsInputDescription](API_KinesisStreamsInputDescription.md "API_KinesisStreamsInputDescription.md") object

Required: No

**NamePrefix**

In-application name prefix.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputDescription.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputDescription.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputDescription.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputDescription.md")
