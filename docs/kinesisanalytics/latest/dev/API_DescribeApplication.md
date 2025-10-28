After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# DescribeApplication

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Returns information about a specific Amazon Kinesis Analytics application.

If you want to retrieve a list of all applications in your account, use the [ListApplications](API_ListApplications.md "API_ListApplications.md") operation.

This operation requires permissions to perform the
`kinesisanalytics:DescribeApplication` action. You can use
`DescribeApplication` to get the current application versionId, which you
need to call other operations such as `Update`.

## Request Syntax

```
{
   "ApplicationName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_DescribeApplication_RequestSyntax "#API_DescribeApplication_RequestSyntax")**

Name of the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

## Response Syntax

```
{
   "ApplicationDetail": {
      "ApplicationARN": "***string***",
      "ApplicationCode": "***string***",
      "ApplicationDescription": "***string***",
      "ApplicationName": "***string***",
      "ApplicationStatus": "***string***",
      "ApplicationVersionId": ***number***,
      "CloudWatchLoggingOptionDescriptions": [
         {
            "CloudWatchLoggingOptionId": "***string***",
            "LogStreamARN": "***string***",
            "RoleARN": "***string***"
         }
      ],
      "CreateTimestamp": ***number***,
      "InputDescriptions": [
         {
            "InAppStreamNames": [ "***string***" ],
            "InputId": "***string***",
            "InputParallelism": {
               "Count": ***number***
            },
            "InputProcessingConfigurationDescription": {
               "InputLambdaProcessorDescription": {
                  "ResourceARN": "***string***",
                  "RoleARN": "***string***"
               }
            },
            "InputSchema": {
               "RecordColumns": [
                  {
                     "Mapping": "***string***",
                     "Name": "***string***",
                     "SqlType": "***string***"
                  }
               ],
               "RecordEncoding": "***string***",
               "RecordFormat": {
                  "MappingParameters": {
                     "CSVMappingParameters": {
                        "RecordColumnDelimiter": "***string***",
                        "RecordRowDelimiter": "***string***"
                     },
                     "JSONMappingParameters": {
                        "RecordRowPath": "***string***"
                     }
                  },
                  "RecordFormatType": "***string***"
               }
            },
            "InputStartingPositionConfiguration": {
               "InputStartingPosition": "***string***"
            },
            "KinesisFirehoseInputDescription": {
               "ResourceARN": "***string***",
               "RoleARN": "***string***"
            },
            "KinesisStreamsInputDescription": {
               "ResourceARN": "***string***",
               "RoleARN": "***string***"
            },
            "NamePrefix": "***string***"
         }
      ],
      "LastUpdateTimestamp": ***number***,
      "OutputDescriptions": [
         {
            "DestinationSchema": {
               "RecordFormatType": "***string***"
            },
            "KinesisFirehoseOutputDescription": {
               "ResourceARN": "***string***",
               "RoleARN": "***string***"
            },
            "KinesisStreamsOutputDescription": {
               "ResourceARN": "***string***",
               "RoleARN": "***string***"
            },
            "LambdaOutputDescription": {
               "ResourceARN": "***string***",
               "RoleARN": "***string***"
            },
            "Name": "***string***",
            "OutputId": "***string***"
         }
      ],
      "ReferenceDataSourceDescriptions": [
         {
            "ReferenceId": "***string***",
            "ReferenceSchema": {
               "RecordColumns": [
                  {
                     "Mapping": "***string***",
                     "Name": "***string***",
                     "SqlType": "***string***"
                  }
               ],
               "RecordEncoding": "***string***",
               "RecordFormat": {
                  "MappingParameters": {
                     "CSVMappingParameters": {
                        "RecordColumnDelimiter": "***string***",
                        "RecordRowDelimiter": "***string***"
                     },
                     "JSONMappingParameters": {
                        "RecordRowPath": "***string***"
                     }
                  },
                  "RecordFormatType": "***string***"
               }
            },
            "S3ReferenceDataSourceDescription": {
               "BucketARN": "***string***",
               "FileKey": "***string***",
               "ReferenceRoleARN": "***string***"
            },
            "TableName": "***string***"
         }
      ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ApplicationDetail](#API_DescribeApplication_ResponseSyntax "#API_DescribeApplication_ResponseSyntax")**

Provides a description of the application, such as the application Amazon Resource
Name (ARN), status, latest version, and input and output configuration details.

Type: [ApplicationDetail](API_ApplicationDetail.md "API_ApplicationDetail.md") object

## Errors

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/cli2/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/DotNetSDKV3/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/boto3/kinesisanalytics-2015-08-14/DescribeApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DescribeApplication.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DescribeApplication.md")
