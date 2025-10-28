After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# OutputUpdate

Describes updates to the output configuration identified by the
`OutputId`.

## Contents

**OutputId**

Identifies the specific output configuration that you want to update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**DestinationSchemaUpdate**

Describes the data format when records are written to the destination. For more
information, see [Configuring Application
Output](how-it-works-output.md "how-it-works-output.md").

Type: [DestinationSchema](API_DestinationSchema.md "API_DestinationSchema.md") object

Required: No

**KinesisFirehoseOutputUpdate**

Describes an Amazon Kinesis Firehose delivery stream as the destination for the
output.

Type: [KinesisFirehoseOutputUpdate](API_KinesisFirehoseOutputUpdate.md "API_KinesisFirehoseOutputUpdate.md") object

Required: No

**KinesisStreamsOutputUpdate**

Describes an Amazon Kinesis stream as the destination for the output.

Type: [KinesisStreamsOutputUpdate](API_KinesisStreamsOutputUpdate.md "API_KinesisStreamsOutputUpdate.md") object

Required: No

**LambdaOutputUpdate**

Describes an AWS Lambda function as the destination for the
output.

Type: [LambdaOutputUpdate](API_LambdaOutputUpdate.md "API_LambdaOutputUpdate.md") object

Required: No

**NameUpdate**

If you want to specify a different in-application stream for this output
configuration, use this field to specify the new in-application stream name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/OutputUpdate.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/OutputUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/OutputUpdate.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/OutputUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/OutputUpdate.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/OutputUpdate.md")
