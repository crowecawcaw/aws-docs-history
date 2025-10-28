After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# CreateApplication

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Creates an Amazon Kinesis Analytics application. You can configure each application
with one streaming source as input, application code to process the input, and up to
three destinations where you want Amazon Kinesis Analytics to write the output data from
your application. For an overview, see [How it Works](how-it-works.md "how-it-works.md").

In the input configuration, you map the streaming source to an in-application stream,
which you can think of as a constantly updating table. In the mapping, you must provide
a schema for the in-application stream and map each data column in the in-application
stream to a data element in the streaming source.

Your application code is one or more SQL statements that read input data, transform
it, and generate output. Your application code can create one or more SQL artifacts like
SQL streams or pumps.

In the output configuration, you can configure the application to write data from
in-application streams created in your applications to up to three destinations.

To read data from your source stream or write data to destination streams, Amazon
Kinesis Analytics needs your permissions. You grant these permissions by creating IAM
roles. This operation requires permissions to perform the
`kinesisanalytics:CreateApplication` action.

For introductory exercises to create an Amazon Kinesis Analytics application, see
[Getting Started](getting-started.md "getting-started.md").

## Request Syntax

```
{
   "ApplicationCode": "`string`",
   "ApplicationDescription": "`string`",
   "ApplicationName": "`string`",
   "CloudWatchLoggingOptions": [
      {
         "LogStreamARN": "`string`",
         "RoleARN": "`string`"
      }
   ],
   "Inputs": [
      {
         "InputParallelism": {
            "Count": `number`
         },
         "InputProcessingConfiguration": {
            "InputLambdaProcessor": {
               "ResourceARN": "`string`",
               "RoleARN": "`string`"
            }
         },
         "InputSchema": {
            "RecordColumns": [
               {
                  "Mapping": "`string`",
                  "Name": "`string`",
                  "SqlType": "`string`"
               }
            ],
            "RecordEncoding": "`string`",
            "RecordFormat": {
               "MappingParameters": {
                  "CSVMappingParameters": {
                     "RecordColumnDelimiter": "`string`",
                     "RecordRowDelimiter": "`string`"
                  },
                  "JSONMappingParameters": {
                     "RecordRowPath": "`string`"
                  }
               },
               "RecordFormatType": "`string`"
            }
         },
         "KinesisFirehoseInput": {
            "ResourceARN": "`string`",
            "RoleARN": "`string`"
         },
         "KinesisStreamsInput": {
            "ResourceARN": "`string`",
            "RoleARN": "`string`"
         },
         "NamePrefix": "`string`"
      }
   ],
   "Outputs": [
      {
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
   ],
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationCode](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

One or more SQL statements that read input data, transform it, and generate output.
For example, you can write a SQL statement that reads data from one in-application
stream, generates a running average of the number of advertisement clicks by vendor, and
insert resulting rows in another in-application stream using pumps. For more information
about the typical pattern, see [Application
Code](how-it-works-app-code.md "how-it-works-app-code.md").

You can provide such series of SQL statements, where output of one statement can be
used as the input for the next statement. You store intermediate results by creating
in-application streams and pumps.

Note that the application code must create the streams with names specified in the
`Outputs`. For example, if your `Outputs` defines output
streams named `ExampleOutputStream1` and `ExampleOutputStream2`,
then your application code must create these streams.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 102400.

Required: No

**[ApplicationDescription](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

Summary description of the application.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No

**[ApplicationName](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

Name of your Amazon Kinesis Analytics application (for example,
`sample-app`).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CloudWatchLoggingOptions](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

Use this parameter to configure a CloudWatch log stream to monitor application
configuration errors. For more information, see [Working with Amazon
CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

Type: Array of [CloudWatchLoggingOption](API_CloudWatchLoggingOption.md "API_CloudWatchLoggingOption.md") objects

Required: No

**[Inputs](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

Use this parameter to configure the application input.

You can configure your application to receive input from a single streaming source. In
this configuration, you map this streaming source to an in-application stream that is
created. Your application code can then query the in-application stream like a table
(you can think of it as a constantly updating table).

For the streaming source, you provide its Amazon Resource Name (ARN) and format of
data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role
that Amazon Kinesis Analytics can assume to read this stream on your behalf.

To create the in-application stream, you need to specify a schema to transform your
data into a schematized version used in SQL. In the schema, you provide the necessary
mapping of the data elements in the streaming source to record columns in the in-app
stream.

Type: Array of [Input](API_Input.md "API_Input.md") objects

Required: No

**[Outputs](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

You can configure application output to write data from any of the in-application
streams to up to three destinations.

These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery
streams, AWS Lambda destinations, or any combination of the three.

In the configuration, you specify the in-application stream name, the destination
stream or Lambda function Amazon Resource Name (ARN), and the format to use when writing
data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to
write to the destination stream or Lambda function on your behalf.

In the output configuration, you also provide the output stream or Lambda function
ARN. For stream destinations, you provide the format of data in the stream (for example,
JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume
to write to the stream or Lambda function on your behalf.

Type: Array of [Output](API_Output.md "API_Output.md") objects

Required: No

**[Tags](#API_CreateApplication_RequestSyntax "#API_CreateApplication_RequestSyntax")**

A list of one or more tags to assign to the application. A tag is a key-value pair
that identifies an application. Note that the maximum number of application tags
includes system tags. The maximum number of user-defined application tags is 50. For
more information, see [Using Tagging](how-tagging.md "how-tagging.md").

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 1 item. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "ApplicationSummary": {
      "ApplicationARN": "***string***",
      "ApplicationName": "***string***",
      "ApplicationStatus": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ApplicationSummary](#API_CreateApplication_ResponseSyntax "#API_CreateApplication_ResponseSyntax")**

In response to your `CreateApplication` request, Amazon Kinesis Analytics
returns a response with a summary of the application it created, including the
application Amazon Resource Name (ARN), name, and status.

Type: [ApplicationSummary](API_ApplicationSummary.md "API_ApplicationSummary.md") object

## Errors

**CodeValidationException**

User-provided application code (query) is invalid. This can be a simple syntax
error.

**message**

Test

HTTP Status Code: 400

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

**LimitExceededException**

Exceeded the number of applications allowed.

**message**

HTTP Status Code: 400

**ResourceInUseException**

Application is not available for this operation.

**message**

HTTP Status Code: 400

**TooManyTagsException**

Application created with too many tags, or too many tags added to an application. Note
that the maximum number of application tags includes system tags. The maximum number of
user-defined application tags is 50.

HTTP Status Code: 400

**UnsupportedOperationException**

The request was rejected because a specified parameter is not supported or a specified
resource is not valid for this operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/cli2/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/boto3/kinesisanalytics-2015-08-14/CreateApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CreateApplication.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CreateApplication.md")
