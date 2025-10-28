After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputConfiguration

When you start your application, you provide this configuration, which identifies the
input source and the point in the input source at which you want the application to
start processing records.

## Contents

**Id**

Input source ID. You can get this ID by calling the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**InputStartingPositionConfiguration**

Point at which you want the application to start processing records from the streaming
source.

Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md "API_InputStartingPositionConfiguration.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputConfiguration.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputConfiguration.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputConfiguration.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputConfiguration.md")
