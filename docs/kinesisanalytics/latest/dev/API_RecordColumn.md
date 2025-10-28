After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# RecordColumn

Describes the mapping of each data element in the streaming source to the
corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

## Contents

**Name**

Name of the column created in the in-application input stream or reference
table.

Type: String

Required: Yes

**SqlType**

Type of column created in the in-application input stream or reference table.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

**Mapping**

Reference to the data element in the streaming input or the reference data source.
This element is required if the [RecordFormatType](API_RecordFormat.md#analytics-Type-RecordFormat-RecordFormatTypel "API_RecordFormat.md#analytics-Type-RecordFormat-RecordFormatTypel") is `JSON`.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/RecordColumn.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/RecordColumn.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/RecordColumn.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/RecordColumn.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/RecordColumn.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/RecordColumn.md")
