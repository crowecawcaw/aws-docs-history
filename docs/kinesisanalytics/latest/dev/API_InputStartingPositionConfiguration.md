After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputStartingPositionConfiguration

Describes the point at which the application reads from the streaming source.

## Contents

**InputStartingPosition**

The starting position on the stream.

- `NOW` - Start reading just after the most recent record in the
  stream, start at the request time stamp that the customer issued.
- `TRIM_HORIZON` - Start reading at the last untrimmed record in the
  stream, which is the oldest record available in the stream. This option is not
  available for an Amazon Kinesis Firehose delivery stream.
- `LAST_STOPPED_POINT` - Resume reading from where the application last
  stopped reading.

Type: String

Valid Values: `NOW | TRIM_HORIZON | LAST_STOPPED_POINT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputStartingPositionConfiguration.md")
