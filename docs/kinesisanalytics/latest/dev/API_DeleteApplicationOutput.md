After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# DeleteApplicationOutput

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Deletes output destination configuration from your application configuration. Amazon
Kinesis Analytics will no longer write data from the corresponding in-application stream
to the external output destination.

This operation requires permissions to perform the
`kinesisanalytics:DeleteApplicationOutput` action.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "CurrentApplicationVersionId": `number`,
   "OutputId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_DeleteApplicationOutput_RequestSyntax "#API_DeleteApplicationOutput_RequestSyntax")**

Amazon Kinesis Analytics application name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CurrentApplicationVersionId](#API_DeleteApplicationOutput_RequestSyntax "#API_DeleteApplicationOutput_RequestSyntax")**

Amazon Kinesis Analytics application version. You can use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get the current application version. If
the version specified is not the current version, the
`ConcurrentModificationException` is returned.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

**[OutputId](#API_DeleteApplicationOutput_RequestSyntax "#API_DeleteApplicationOutput_RequestSyntax")**

The ID of the configuration to delete. Each output configuration that is added to the
application, either when the application is created or later using the [AddApplicationOutput](API_AddApplicationOutput.md "API_AddApplicationOutput.md") operation, has a unique ID. You need to provide the ID
to uniquely identify the output configuration that you want to delete from the
application configuration. You can use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get the specific `OutputId`.

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/cli2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/boto3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DeleteApplicationOutput.md")
