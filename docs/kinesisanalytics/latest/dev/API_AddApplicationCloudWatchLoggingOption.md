After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# AddApplicationCloudWatchLoggingOption

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Adds a CloudWatch log stream to monitor application configuration errors. For more
information about using CloudWatch log streams with Amazon Kinesis Analytics
applications, see [Working with Amazon
CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "CloudWatchLoggingOption": {
      "LogStreamARN": "`string`",
      "RoleARN": "`string`"
   },
   "CurrentApplicationVersionId": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax "#API_AddApplicationCloudWatchLoggingOption_RequestSyntax")**

The Kinesis Analytics application name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CloudWatchLoggingOption](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax "#API_AddApplicationCloudWatchLoggingOption_RequestSyntax")**

Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN.
Note: To write application messages to CloudWatch, the IAM role that is used must have
the `PutLogEvents` policy action enabled.

Type: [CloudWatchLoggingOption](API_CloudWatchLoggingOption.md "API_CloudWatchLoggingOption.md") object

Required: Yes

**[CurrentApplicationVersionId](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax "#API_AddApplicationCloudWatchLoggingOption_RequestSyntax")**

The version ID of the Kinesis Analytics application.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption.md")
