For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CreateBatchLoadTask

Creates a new Timestream batch load task. A batch load task processes data from a CSV source in an S3
location and writes to a Timestream table. A mapping from source to target is defined in a batch load task.
Errors and events are written to a report at an S3 location. For the report, if the AWS KMS key is not
specified, the report will be encrypted with an S3 managed key when `SSE_S3` is the option. Otherwise an
error is thrown. For more information, see [AWS managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk"). [Service quotas apply](ts-limits.md "ts-limits.md"). For details,
see [code
sample](code-samples.md "code-samples.md").

## Request Syntax

```
{
   "ClientToken": "`string`",
   "DataModelConfiguration": {
      "DataModel": {
         "DimensionMappings": [
            {
               "DestinationColumn": "`string`",
               "SourceColumn": "`string`"
            }
         ],
         "MeasureNameColumn": "`string`",
         "MixedMeasureMappings": [
            {
               "MeasureName": "`string`",
               "MeasureValueType": "`string`",
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValueType": "`string`",
                     "SourceColumn": "`string`",
                     "TargetMultiMeasureAttributeName": "`string`"
                  }
               ],
               "SourceColumn": "`string`",
               "TargetMeasureName": "`string`"
            }
         ],
         "MultiMeasureMappings": {
            "MultiMeasureAttributeMappings": [
               {
                  "MeasureValueType": "`string`",
                  "SourceColumn": "`string`",
                  "TargetMultiMeasureAttributeName": "`string`"
               }
            ],
            "TargetMultiMeasureName": "`string`"
         },
         "TimeColumn": "`string`",
         "TimeUnit": "`string`"
      },
      "DataModelS3Configuration": {
         "BucketName": "`string`",
         "ObjectKey": "`string`"
      }
   },
   "DataSourceConfiguration": {
      "CsvConfiguration": {
         "ColumnSeparator": "`string`",
         "EscapeChar": "`string`",
         "NullValue": "`string`",
         "QuoteChar": "`string`",
         "TrimWhiteSpace": `boolean`
      },
      "DataFormat": "`string`",
      "DataSourceS3Configuration": {
         "BucketName": "`string`",
         "ObjectKeyPrefix": "`string`"
      }
   },
   "RecordVersion": `number`,
   "ReportConfiguration": {
      "ReportS3Configuration": {
         "BucketName": "`string`",
         "EncryptionOption": "`string`",
         "KmsKeyId": "`string`",
         "ObjectKeyPrefix": "`string`"
      }
   },
   "TargetDatabaseName": "`string`",
   "TargetTableName": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: No

**[DataModelConfiguration](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Type: [DataModelConfiguration](API_DataModelConfiguration.md "API_DataModelConfiguration.md") object

Required: No

**[DataSourceConfiguration](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Defines configuration details about the data source for a batch load task.

Type: [DataSourceConfiguration](API_DataSourceConfiguration.md "API_DataSourceConfiguration.md") object

Required: Yes

**[RecordVersion](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Type: Long

Required: No

**[ReportConfiguration](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Report configuration for a batch load task. This contains details about where error reports are stored.

Type: [ReportConfiguration](API_ReportConfiguration.md "API_ReportConfiguration.md") object

Required: Yes

**[TargetDatabaseName](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Target Timestream database for a batch load task.

Type: String

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[TargetTableName](#API_CreateBatchLoadTask_RequestSyntax "#API_CreateBatchLoadTask_RequestSyntax")**

Target Timestream table for a batch load task.

Type: String

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

## Response Syntax

```
{
   "TaskId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TaskId](#API_CreateBatchLoadTask_ResponseSyntax "#API_CreateBatchLoadTask_ResponseSyntax")**

The ID of the batch load task.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 32.

Pattern: `[A-Z0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You are not authorized to perform this action.

HTTP Status Code: 400

**ConflictException**

Timestream was unable to process this request because it contains resource that already exists.

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

**ServiceQuotaExceededException**

The instance quota of resource exceeded for this account.

HTTP Status Code: 400

**ThrottlingException**

Too many requests were made by a user and they exceeded the service quotas. The request was throttled.

HTTP Status Code: 400

**ValidationException**

An invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/cli2/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/DotNetSDKV3/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/boto3/timestream-write-2018-11-01/CreateBatchLoadTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateBatchLoadTask.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateBatchLoadTask.md")
