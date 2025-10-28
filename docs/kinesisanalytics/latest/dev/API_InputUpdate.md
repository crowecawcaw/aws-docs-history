After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputUpdate

Describes updates to a specific input configuration (identified by the
`InputId` of an application).

## Contents

**InputId**

Input ID of the application input to be updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**InputParallelismUpdate**

Describes the parallelism updates (the number in-application streams Amazon Kinesis
Analytics creates for the specific streaming source).

Type: [InputParallelismUpdate](API_InputParallelismUpdate.md "API_InputParallelismUpdate.md") object

Required: No

**InputProcessingConfigurationUpdate**

Describes updates for an input processing configuration.

Type: [InputProcessingConfigurationUpdate](API_InputProcessingConfigurationUpdate.md "API_InputProcessingConfigurationUpdate.md") object

Required: No

**InputSchemaUpdate**

Describes the data format on the streaming source, and how record elements on the
streaming source map to columns of the in-application stream that is created.

Type: [InputSchemaUpdate](API_InputSchemaUpdate.md "API_InputSchemaUpdate.md") object

Required: No

**KinesisFirehoseInputUpdate**

If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated,
provides an updated stream ARN and IAM role ARN.

Type: [KinesisFirehoseInputUpdate](API_KinesisFirehoseInputUpdate.md "API_KinesisFirehoseInputUpdate.md") object

Required: No

**KinesisStreamsInputUpdate**

If an Amazon Kinesis stream is the streaming source to be updated, provides an updated
stream Amazon Resource Name (ARN) and IAM role ARN.

Type: [KinesisStreamsInputUpdate](API_KinesisStreamsInputUpdate.md "API_KinesisStreamsInputUpdate.md") object

Required: No

**NamePrefixUpdate**

Name prefix for in-application streams that Amazon Kinesis Analytics creates for the
specific streaming source.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputUpdate.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputUpdate.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputUpdate.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputUpdate.md")
