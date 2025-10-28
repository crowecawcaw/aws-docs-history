After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputSchemaUpdate

Describes updates for the application's input schema.

## Contents

**RecordColumnUpdates**

A list of `RecordColumn` objects. Each object describes the mapping of the
streaming source element to the corresponding column in the in-application stream.

Type: Array of [RecordColumn](API_RecordColumn.md "API_RecordColumn.md") objects

Array Members: Minimum number of 1 item. Maximum number of 1000 items.

Required: No

**RecordEncodingUpdate**

Specifies the encoding of the records in the streaming source. For example,
UTF-8.

Type: String

Pattern: `UTF-8`

Required: No

**RecordFormatUpdate**

Specifies the format of the records on the streaming source.

Type: [RecordFormat](API_RecordFormat.md "API_RecordFormat.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputSchemaUpdate.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputSchemaUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputSchemaUpdate.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputSchemaUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputSchemaUpdate.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputSchemaUpdate.md")
