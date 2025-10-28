After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# DeleteApplicationInputProcessingConfiguration

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Deletes an [InputProcessingConfiguration](API_InputProcessingConfiguration.md "API_InputProcessingConfiguration.md") from an input.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "CurrentApplicationVersionId": `number`,
   "InputId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax "#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax")**

The Kinesis Analytics application name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CurrentApplicationVersionId](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax "#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax")**

The version ID of the Kinesis Analytics application.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

**[InputId](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax "#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax")**

The ID of the input configuration from which to delete the input processing
configuration. You can get a list of the input IDs for an application by using the
[DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ConcurrentModificationException**

Exception thrown as a result of concurrent modification to an application. For
example, two individuals attempting to edit the same application at the same
time.

**message**

HTTP Status Code: 400

**InvalidArgumentException**

Specified input parameter value is invalid.

**message**

HTTP Status Code: 400

**ResourceInUseException**

Application is not available for this operation.

**message**

HTTP Status Code: 400

**ResourceNotFoundException**

Specified application can't be found.

**message**

HTTP Status Code: 400

**UnsupportedOperationException**

The request was rejected because a specified parameter is not supported or a specified
resource is not valid for this operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/cli2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/boto3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration.md")
