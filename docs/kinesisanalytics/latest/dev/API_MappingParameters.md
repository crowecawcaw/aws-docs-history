After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# MappingParameters

When configuring application input at the time of creating or updating an application,
provides additional mapping information specific to the record format (such as JSON,
CSV, or record fields delimited by some delimiter) on the streaming source.

## Contents

**CSVMappingParameters**

Provides additional mapping information when the record format uses delimiters (for
example, CSV).

Type: [CSVMappingParameters](API_CSVMappingParameters.md "API_CSVMappingParameters.md") object

Required: No

**JSONMappingParameters**

Provides additional mapping information when JSON is the record format on the
streaming source.

Type: [JSONMappingParameters](API_JSONMappingParameters.md "API_JSONMappingParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/MappingParameters.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/MappingParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/MappingParameters.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/MappingParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/MappingParameters.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/MappingParameters.md")
