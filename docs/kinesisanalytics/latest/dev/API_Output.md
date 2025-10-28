After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Output

Describes application output configuration in which you identify an in-application
stream and a destination where you want the in-application stream data to be written.
The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery
stream.

For limits on how many destinations an application can write and other limitations,
see [Limits](limits.md "limits.md").

## Contents

**DestinationSchema**

Describes the data format when records are written to the destination. For more
information, see [Configuring Application
Output](how-it-works-output.md "how-it-works-output.md").

Type: [DestinationSchema](API_DestinationSchema.md "API_DestinationSchema.md") object

Required: Yes

**Name**

Name of the in-application stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: Yes

**KinesisFirehoseOutput**

Identifies an Amazon Kinesis Firehose delivery stream as the destination.

Type: [KinesisFirehoseOutput](API_KinesisFirehoseOutput.md "API_KinesisFirehoseOutput.md") object

Required: No

**KinesisStreamsOutput**

Identifies an Amazon Kinesis stream as the destination.

Type: [KinesisStreamsOutput](API_KinesisStreamsOutput.md "API_KinesisStreamsOutput.md") object

Required: No

**LambdaOutput**

Identifies an AWS Lambda function as the destination.

Type: [LambdaOutput](API_LambdaOutput.md "API_LambdaOutput.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/Output.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/Output.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/Output.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/Output.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/Output.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/Output.md")
