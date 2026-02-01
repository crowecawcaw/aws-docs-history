After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# UpdateApplication

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Updates an existing Amazon Kinesis Analytics application. Using this API, you can
update application code, input configuration, and output configuration.

Note that Amazon Kinesis Analytics updates the
`CurrentApplicationVersionId` each time you update your application.

This operation requires permission for the
`kinesisanalytics:UpdateApplication` action.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "ApplicationUpdate": {
      "ApplicationCodeUpdate": "`string`",
      "CloudWatchLoggingOptionUpdates": [
         {
            "CloudWatchLoggingOptionId": "`string`",
            "LogStreamARNUpdate": "`string`",
            "RoleARNUpdate": "`string`"
         }
      ],
      "InputUpdates": [
         {
            "InputId": "`string`",
            "InputParallelismUpdate": {
               "CountUpdate": `number`
            },
            "InputProcessingConfigurationUpdate": {
               "InputLambdaProcessorUpdate": {
                  "ResourceARNUpdate": "`string`",
                  "RoleARNUpdate": "`string`"
               }
            },
            "InputSchemaUpdate": {
               "RecordColumnUpdates": [
                  {
                     "Mapping": "`string`",
                     "Name": "`string`",
                     "SqlType": "`string`"
                  }
               ],
               "RecordEncodingUpdate": "`string`",
               "RecordFormatUpdate": {
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
            "KinesisFirehoseInputUpdate": {
               "ResourceARNUpdate": "`string`",
               "RoleARNUpdate": "`string`"
            },
            "KinesisStreamsInputUpdate": {
               "ResourceARNUpdate": "`string`",
               "RoleARNUpdate": "`string`"
            },
            "NamePrefixUpdate": "`string`"
         }
      ],
      "OutputUpdates": [
         {
            "DestinationSchemaUpdate": {
               "RecordFormatType": "`string`"
            },
            "KinesisFirehoseOutputUpdate": {
               "ResourceARNUpdate": "`string`",
               "RoleARNUpdate": "`string`"
            },
            "KinesisStreamsOutputUpdate": {
               "ResourceARNUpdate": "`string`",
               "RoleARNUpdate": "`string`"
            },
            "LambdaOutputUpdate": {
               "ResourceARNUpdate": "`string`",
               "RoleARNUpdate": "`string`"
            },
            "NameUpdate": "`string`",
            "OutputId": "`string`"
         }
      ],
      "ReferenceDataSourceUpdates": [
         {
            "ReferenceId": "`string`",
            "ReferenceSchemaUpdate": {
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
            "S3ReferenceDataSourceUpdate": {
               "BucketARNUpdate": "`string`",
               "FileKeyUpdate": "`string`",
               "ReferenceRoleARNUpdate": "`string`"
            },
            "TableNameUpdate": "`string`"
         }
      ]
   },
   "CurrentApplicationVersionId": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_UpdateApplication_RequestSyntax "#API_UpdateApplication_RequestSyntax")**

Name of the Amazon Kinesis Analytics application to update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[ApplicationUpdate](#API_UpdateApplication_RequestSyntax "#API_UpdateApplication_RequestSyntax")**

Describes application updates.

Type: [ApplicationUpdate](API_ApplicationUpdate.md "API_ApplicationUpdate.md") object

Required: Yes

**[CurrentApplicationVersionId](#API_UpdateApplication_RequestSyntax "#API_UpdateApplication_RequestSyntax")**

The current application version ID. You can use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get this value.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/cli2/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/boto3/kinesisanalytics-2015-08-14/UpdateApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/UpdateApplication.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/UpdateApplication.md")
