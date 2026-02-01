After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# AddApplicationOutput

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Adds an external destination to your Amazon Kinesis Analytics application.

If you want Amazon Kinesis Analytics to deliver data from an in-application stream
within your application to an external destination (such as an Amazon Kinesis stream, an
Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), you
add the relevant configuration to your application using this operation. You can
configure one or more outputs for your application. Each output configuration maps an
in-application stream and an external destination.

You can use one of the output configurations to deliver data from your in-application
error stream to an external destination so that you can analyze the errors. For more
information, see [Understanding Application
Output (Destination)](how-it-works-output.md "how-it-works-output.md").

Any configuration update, including adding a streaming source using this operation,
results in a new version of the application. You can use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to find the current application
version.

For the limits on the number of application inputs and outputs you can configure, see
[Limits](limits.md "limits.md").

This operation requires permissions to perform the
`kinesisanalytics:AddApplicationOutput` action.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "CurrentApplicationVersionId": `number`,
   "Output": {
      "DestinationSchema": {
         "RecordFormatType": "`string`"
      },
      "KinesisFirehoseOutput": {
         "ResourceARN": "`string`",
         "RoleARN": "`string`"
      },
      "KinesisStreamsOutput": {
         "ResourceARN": "`string`",
         "RoleARN": "`string`"
      },
      "LambdaOutput": {
         "ResourceARN": "`string`",
         "RoleARN": "`string`"
      },
      "Name": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_AddApplicationOutput_RequestSyntax "#API_AddApplicationOutput_RequestSyntax")**

Name of the application to which you want to add the output configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CurrentApplicationVersionId](#API_AddApplicationOutput_RequestSyntax "#API_AddApplicationOutput_RequestSyntax")**

Version of the application to which you want to add the output configuration. You can
use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get the current application version. If
the version specified is not the current version, the
`ConcurrentModificationException` is returned.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

**[Output](#API_AddApplicationOutput_RequestSyntax "#API_AddApplicationOutput_RequestSyntax")**

An array of objects, each describing one output configuration. In the output
configuration, you specify the name of an in-application stream, a destination (that is,
an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the
destination.

Type: [Output](API_Output.md "API_Output.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationOutput.md")
