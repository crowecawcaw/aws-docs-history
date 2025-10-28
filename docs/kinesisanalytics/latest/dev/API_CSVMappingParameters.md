After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# CSVMappingParameters

Provides additional mapping information when the record format uses delimiters, such
as CSV. For example, the following sample records use CSV format, where the records use
the _'\n'_ as the row delimiter and a comma (",") as the column
delimiter:

`"name1", "address1"`

`"name2", "address2"`

## Contents

**RecordColumnDelimiter**

Column delimiter. For example, in a CSV format, a comma (",") is the typical column
delimiter.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

**RecordRowDelimiter**

Row delimiter. For example, in a CSV format, _'\n'_ is the typical
row delimiter.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CSVMappingParameters.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CSVMappingParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CSVMappingParameters.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CSVMappingParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CSVMappingParameters.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CSVMappingParameters.md")
