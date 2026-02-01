# DescribeJobRun

Represents one run of a DataBrew job.

## Request Syntax

```
GET /jobs/`name`/jobRun/`runId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeJobRun_RequestSyntax "#API_DescribeJobRun_RequestSyntax")**

The name of the job being processed during this run.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

**[runId](#API_DescribeJobRun_RequestSyntax "#API_DescribeJobRun_RequestSyntax")**

The unique identifier of the job run.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Attempt": ***number***,
   "CompletedOn": ***number***,
   "DatabaseOutputs": [
      {
         "DatabaseOptions": {
            "TableName": "***string***",
            "TempDirectory": {
               "Bucket": "***string***",
               "BucketOwner": "***string***",
               "Key": "***string***"
            }
         },
         "DatabaseOutputMode": "***string***",
         "GlueConnectionName": "***string***"
      }
   ],
   "DataCatalogOutputs": [
      {
         "CatalogId": "***string***",
         "DatabaseName": "***string***",
         "DatabaseOptions": {
            "TableName": "***string***",
            "TempDirectory": {
               "Bucket": "***string***",
               "BucketOwner": "***string***",
               "Key": "***string***"
            }
         },
         "Overwrite": ***boolean***,
         "S3Options": {
            "Location": {
               "Bucket": "***string***",
               "BucketOwner": "***string***",
               "Key": "***string***"
            }
         },
         "TableName": "***string***"
      }
   ],
   "DatasetName": "***string***",
   "ErrorMessage": "***string***",
   "ExecutionTime": ***number***,
   "JobName": "***string***",
   "JobSample": {
      "Mode": "***string***",
      "Size": ***number***
   },
   "LogGroupName": "***string***",
   "LogSubscription": "***string***",
   "Outputs": [
      {
         "CompressionFormat": "***string***",
         "Format": "***string***",
         "FormatOptions": {
            "Csv": {
               "Delimiter": "***string***"
            }
         },
         "Location": {
            "Bucket": "***string***",
            "BucketOwner": "***string***",
            "Key": "***string***"
         },
         "MaxOutputFiles": ***number***,
         "Overwrite": ***boolean***,
         "PartitionColumns": [ "***string***" ]
      }
   ],
   "ProfileConfiguration": {
      "ColumnStatisticsConfigurations": [
         {
            "Selectors": [
               {
                  "Name": "***string***",
                  "Regex": "***string***"
               }
            ],
            "Statistics": {
               "IncludedStatistics": [ "***string***" ],
               "Overrides": [
                  {
                     "Parameters": {
                        "***string***" : "***string***"
                     },
                     "Statistic": "***string***"
                  }
               ]
            }
         }
      ],
      "DatasetStatisticsConfiguration": {
         "IncludedStatistics": [ "***string***" ],
         "Overrides": [
            {
               "Parameters": {
                  "***string***" : "***string***"
               },
               "Statistic": "***string***"
            }
         ]
      },
      "EntityDetectorConfiguration": {
         "AllowedStatistics": [
            {
               "Statistics": [ "***string***" ]
            }
         ],
         "EntityTypes": [ "***string***" ]
      },
      "ProfileColumns": [
         {
            "Name": "***string***",
            "Regex": "***string***"
         }
      ]
   },
   "RecipeReference": {
      "Name": "***string***",
      "RecipeVersion": "***string***"
   },
   "RunId": "***string***",
   "StartedBy": "***string***",
   "StartedOn": ***number***,
   "State": "***string***",
   "ValidationConfigurations": [
      {
         "RulesetArn": "***string***",
         "ValidationMode": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[JobName](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The name of the job being processed during this run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 240.

**[Attempt](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The number of times that DataBrew has attempted to run the job.

Type: Integer

**[CompletedOn](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The date and time when the job completed processing.

Type: Timestamp

**[DatabaseOutputs](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

Represents a list of JDBC database output objects which defines the output
destination for a DataBrew recipe job to write into.

Type: Array of [DatabaseOutput](API_DatabaseOutput.md "API_DatabaseOutput.md") objects

Array Members: Minimum number of 1 item.

**[DataCatalogOutputs](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

One or more artifacts that represent the AWS Glue Data Catalog output from running the job.

Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md "API_DataCatalogOutput.md") objects

Array Members: Minimum number of 1 item.

**[DatasetName](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The name of the dataset for the job to process.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[ErrorMessage](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

A message indicating an error (if any) that was encountered when the job ran.

Type: String

**[ExecutionTime](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The amount of time, in seconds, during which the job run consumed resources.

Type: Integer

**[JobSample](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

Sample configuration for profile jobs only. Determines the number of rows on which the
profile job will be executed. If a JobSample value is not provided, the default value
will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the
size parameter.

Type: [JobSample](API_JobSample.md "API_JobSample.md") object

**[LogGroupName](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The name of an Amazon CloudWatch log group, where the job writes diagnostic messages
when it runs.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

**[LogSubscription](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The current status of Amazon CloudWatch logging for the job run.

Type: String

Valid Values: `ENABLE | DISABLE`

**[Outputs](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

One or more output artifacts from a job run.

Type: Array of [Output](API_Output.md "API_Output.md") objects

Array Members: Minimum number of 1 item.

**[ProfileConfiguration](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

Configuration for profile jobs. Used to select columns, do evaluations,
and override default parameters of evaluations. When configuration is null, the
profile job will run with default settings.

Type: [ProfileConfiguration](API_ProfileConfiguration.md "API_ProfileConfiguration.md") object

**[RecipeReference](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

Represents the name and version of a DataBrew recipe.

Type: [RecipeReference](API_RecipeReference.md "API_RecipeReference.md") object

**[RunId](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The unique identifier of the job run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[StartedBy](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The Amazon Resource Name (ARN) of the user who started the job run.

Type: String

**[StartedOn](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The date and time when the job run began.

Type: Timestamp

**[State](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

The current state of the job run entity itself.

Type: String

Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`

**[ValidationConfigurations](#API_DescribeJobRun_ResponseSyntax "#API_DescribeJobRun_ResponseSyntax")**

List of validation configurations that are applied to the profile job.

Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md "API_ValidationConfiguration.md") objects

Array Members: Minimum number of 1 item.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeJobRun.md "../../../goto/cli2/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/DescribeJobRun.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeJobRun.md "../../../goto/boto3/databrew-2017-07-25/DescribeJobRun.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeJobRun.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeJobRun.md")
