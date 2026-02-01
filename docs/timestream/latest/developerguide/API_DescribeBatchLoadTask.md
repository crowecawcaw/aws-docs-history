For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DescribeBatchLoadTask

Returns information about the batch load task, including configurations, mappings, progress, and other details.
[Service quotas apply](ts-limits.md "ts-limits.md"). See
[code
sample](code-samples.md "code-samples.md") for details.

## Request Syntax

```
{
   "TaskId": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[TaskId](#API_DescribeBatchLoadTask_RequestSyntax "#API_DescribeBatchLoadTask_RequestSyntax")**

The ID of the batch load task.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 32.

Pattern: `[A-Z0-9]+`

Required: Yes

## Response Syntax

```
{
   "BatchLoadTaskDescription": {
      "CreationTime": ***number***,
      "DataModelConfiguration": {
         "DataModel": {
            "DimensionMappings": [
               {
                  "DestinationColumn": "***string***",
                  "SourceColumn": "***string***"
               }
            ],
            "MeasureNameColumn": "***string***",
            "MixedMeasureMappings": [
               {
                  "MeasureName": "***string***",
                  "MeasureValueType": "***string***",
                  "MultiMeasureAttributeMappings": [
                     {
                        "MeasureValueType": "***string***",
                        "SourceColumn": "***string***",
                        "TargetMultiMeasureAttributeName": "***string***"
                     }
                  ],
                  "SourceColumn": "***string***",
                  "TargetMeasureName": "***string***"
               }
            ],
            "MultiMeasureMappings": {
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValueType": "***string***",
                     "SourceColumn": "***string***",
                     "TargetMultiMeasureAttributeName": "***string***"
                  }
               ],
               "TargetMultiMeasureName": "***string***"
            },
            "TimeColumn": "***string***",
            "TimeUnit": "***string***"
         },
         "DataModelS3Configuration": {
            "BucketName": "***string***",
            "ObjectKey": "***string***"
         }
      },
      "DataSourceConfiguration": {
         "CsvConfiguration": {
            "ColumnSeparator": "***string***",
            "EscapeChar": "***string***",
            "NullValue": "***string***",
            "QuoteChar": "***string***",
            "TrimWhiteSpace": ***boolean***
         },
         "DataFormat": "***string***",
         "DataSourceS3Configuration": {
            "BucketName": "***string***",
            "ObjectKeyPrefix": "***string***"
         }
      },
      "ErrorMessage": "***string***",
      "LastUpdatedTime": ***number***,
      "ProgressReport": {
         "BytesMetered": ***number***,
         "FileFailures": ***number***,
         "ParseFailures": ***number***,
         "RecordIngestionFailures": ***number***,
         "RecordsIngested": ***number***,
         "RecordsProcessed": ***number***
      },
      "RecordVersion": ***number***,
      "ReportConfiguration": {
         "ReportS3Configuration": {
            "BucketName": "***string***",
            "EncryptionOption": "***string***",
            "KmsKeyId": "***string***",
            "ObjectKeyPrefix": "***string***"
         }
      },
      "ResumableUntil": ***number***,
      "TargetDatabaseName": "***string***",
      "TargetTableName": "***string***",
      "TaskId": "***string***",
      "TaskStatus": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BatchLoadTaskDescription](#API_DescribeBatchLoadTask_ResponseSyntax "#API_DescribeBatchLoadTask_ResponseSyntax")**

Description of the batch load task.

Type: [BatchLoadTaskDescription](API_BatchLoadTaskDescription.md "API_BatchLoadTaskDescription.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You are not authorized to perform this action.

HTTP Status Code: 400

**InternalServerException**

Timestream was unable to fully process this request because of an internal server error.

HTTP Status Code: 500

**InvalidEndpointException**

The requested endpoint was not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its
status might not be ACTIVE.

HTTP Status Code: 400

**ThrottlingException**

Too many requests were made by a user and they exceeded the service quotas. The request was throttled.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/cli2/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/DotNetSDKV4/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/boto3/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DescribeBatchLoadTask.md")
