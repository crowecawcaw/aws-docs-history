After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# StartApplication

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Starts the specified Amazon Kinesis Analytics application. After creating an
application, you must exclusively call this operation to start your application.

After the application starts, it begins consuming the input data, processes it, and
writes the output to the configured destination.

The application status must be `READY` for you to start an application.
You can get the application status in the console or using the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation.

After you start the application, you can stop the application from processing the
input by calling the [StopApplication](API_StopApplication.md "API_StopApplication.md")
operation.

This operation requires permissions to perform the
`kinesisanalytics:StartApplication` action.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "InputConfigurations": [
      {
         "Id": "`string`",
         "InputStartingPositionConfiguration": {
            "InputStartingPosition": "`string`"
         }
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_StartApplication_RequestSyntax "#API_StartApplication_RequestSyntax")**

Name of the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[InputConfigurations](#API_StartApplication_RequestSyntax "#API_StartApplication_RequestSyntax")**

Identifies the specific input, by ID, that the application starts consuming. Amazon
Kinesis Analytics starts reading the streaming source associated with the input. You can
also specify where in the streaming source you want Amazon Kinesis Analytics to start
reading.

Type: Array of [InputConfiguration](API_InputConfiguration.md "API_InputConfiguration.md") objects

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidApplicationConfigurationException**

User-provided application configuration is not valid.

**message**

test

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/cli2/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/boto3/kinesisanalytics-2015-08-14/StartApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/StartApplication.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/StartApplication.md")
