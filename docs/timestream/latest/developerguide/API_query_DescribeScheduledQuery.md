For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DescribeScheduledQuery

Provides detailed information about a scheduled query.

## Request Syntax

```
{
   "ScheduledQueryArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ScheduledQueryArn](#API_query_DescribeScheduledQuery_RequestSyntax "#API_query_DescribeScheduledQuery_RequestSyntax")**

The ARN of the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## Response Syntax

```
{
   "ScheduledQuery": {
      "Arn": "***string***",
      "CreationTime": ***number***,
      "ErrorReportConfiguration": {
         "S3Configuration": {
            "BucketName": "***string***",
            "EncryptionOption": "***string***",
            "ObjectKeyPrefix": "***string***"
         }
      },
      "KmsKeyId": "***string***",
      "LastRunSummary": {
         "ErrorReportLocation": {
            "S3ReportLocation": {
               "BucketName": "***string***",
               "ObjectKey": "***string***"
            }
         },
         "ExecutionStats": {
            "BytesMetered": ***number***,
            "CumulativeBytesScanned": ***number***,
            "DataWrites": ***number***,
            "ExecutionTimeInMillis": ***number***,
            "QueryResultRows": ***number***,
            "RecordsIngested": ***number***
         },
         "FailureReason": "***string***",
         "InvocationTime": ***number***,
         "QueryInsightsResponse": {
            "OutputBytes": ***number***,
            "OutputRows": ***number***,
            "QuerySpatialCoverage": {
               "Max": {
                  "PartitionKey": [ "***string***" ],
                  "TableArn": "***string***",
                  "Value": ***number***
               }
            },
            "QueryTableCount": ***number***,
            "QueryTemporalRange": {
               "Max": {
                  "TableArn": "***string***",
                  "Value": ***number***
               }
            }
         },
         "RunStatus": "***string***",
         "TriggerTime": ***number***
      },
      "Name": "***string***",
      "NextInvocationTime": ***number***,
      "NotificationConfiguration": {
         "SnsConfiguration": {
            "TopicArn": "***string***"
         }
      },
      "PreviousInvocationTime": ***number***,
      "QueryString": "***string***",
      "RecentlyFailedRuns": [
         {
            "ErrorReportLocation": {
               "S3ReportLocation": {
                  "BucketName": "***string***",
                  "ObjectKey": "***string***"
               }
            },
            "ExecutionStats": {
               "BytesMetered": ***number***,
               "CumulativeBytesScanned": ***number***,
               "DataWrites": ***number***,
               "ExecutionTimeInMillis": ***number***,
               "QueryResultRows": ***number***,
               "RecordsIngested": ***number***
            },
            "FailureReason": "***string***",
            "InvocationTime": ***number***,
            "QueryInsightsResponse": {
               "OutputBytes": ***number***,
               "OutputRows": ***number***,
               "QuerySpatialCoverage": {
                  "Max": {
                     "PartitionKey": [ "***string***" ],
                     "TableArn": "***string***",
                     "Value": ***number***
                  }
               },
               "QueryTableCount": ***number***,
               "QueryTemporalRange": {
                  "Max": {
                     "TableArn": "***string***",
                     "Value": ***number***
                  }
               }
            },
            "RunStatus": "***string***",
            "TriggerTime": ***number***
         }
      ],
      "ScheduleConfiguration": {
         "ScheduleExpression": "***string***"
      },
      "ScheduledQueryExecutionRoleArn": "***string***",
      "State": "***string***",
      "TargetConfiguration": {
         "TimestreamConfiguration": {
            "DatabaseName": "***string***",
            "DimensionMappings": [
               {
                  "DimensionValueType": "***string***",
                  "Name": "***string***"
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
            "TableName": "***string***",
            "TimeColumn": "***string***"
         }
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ScheduledQuery](#API_query_DescribeScheduledQuery_ResponseSyntax "#API_query_DescribeScheduledQuery_ResponseSyntax")**

The scheduled query.

Type: [ScheduledQueryDescription](API_query_ScheduledQueryDescription.md "API_query_ScheduledQueryDescription.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have the necessary permissions to access the account settings.

HTTP Status Code: 400

**InternalServerException**

An internal server error occurred while processing the request.

HTTP Status Code: 400

**InvalidEndpointException**

The requested endpoint is invalid.

HTTP Status Code: 400

**ResourceNotFoundException**

The requested resource could not be found.

**ScheduledQueryArn**

The ARN of the scheduled query.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/cli2/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/boto3/timestream-query-2018-11-01/DescribeScheduledQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeScheduledQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeScheduledQuery.md")
