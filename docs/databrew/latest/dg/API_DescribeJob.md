# DescribeJob

Returns the definition of a specific DataBrew job.

## Request Syntax

```
GET /jobs/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeJob_RequestSyntax "#API_DescribeJob_RequestSyntax")**

The name of the job to be described.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": ***number***,
   "CreatedBy": "***string***",
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
   "EncryptionKeyArn": "***string***",
   "EncryptionMode": "***string***",
   "JobSample": {
      "Mode": "***string***",
      "Size": ***number***
   },
   "LastModifiedBy": "***string***",
   "LastModifiedDate": ***number***,
   "LogSubscription": "***string***",
   "MaxCapacity": ***number***,
   "MaxRetries": ***number***,
   "Name": "***string***",
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
   "ProjectName": "***string***",
   "RecipeReference": {
      "Name": "***string***",
      "RecipeVersion": "***string***"
   },
   "ResourceArn": "***string***",
   "RoleArn": "***string***",
   "Tags": {
      "***string***" : "***string***"
   },
   "Timeout": ***number***,
   "Type": "***string***",
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

**[Name](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The name of the job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 240.

**[CreateDate](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The date and time that the job was created.

Type: Timestamp

**[CreatedBy](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The identifier (user name) of the user associated with the creation of the job.

Type: String

**[DatabaseOutputs](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Represents a list of JDBC database output objects which defines the output
destination for a DataBrew recipe job to write into.

Type: Array of [DatabaseOutput](API_DatabaseOutput.md "API_DatabaseOutput.md") objects

Array Members: Minimum number of 1 item.

**[DataCatalogOutputs](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

One or more artifacts that represent the AWS Glue Data Catalog output from running the job.

Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md "API_DataCatalogOutput.md") objects

Array Members: Minimum number of 1 item.

**[DatasetName](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The dataset that the job acts upon.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[EncryptionKeyArn](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of an encryption key that is used to protect the
job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[EncryptionMode](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The encryption mode for the job, which can be one of the following:

- `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
- `SSE-S3` - Server-side encryption with keys managed by Amazon
  S3.

Type: String

Valid Values: `SSE-KMS | SSE-S3`

**[JobSample](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Sample configuration for profile jobs only. Determines the number of rows on which the
profile job will be executed.

Type: [JobSample](API_JobSample.md "API_JobSample.md") object

**[LastModifiedBy](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The identifier (user name) of the user who last modified the job.

Type: String

**[LastModifiedDate](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The date and time that the job was last modified.

Type: Timestamp

**[LogSubscription](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Indicates whether Amazon CloudWatch logging is enabled for this job.

Type: String

Valid Values: `ENABLE | DISABLE`

**[MaxCapacity](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The maximum number of compute nodes that DataBrew can consume when the job processes
data.

Type: Integer

**[MaxRetries](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The maximum number of times to retry the job after a job run fails.

Type: Integer

Valid Range: Minimum value of 0.

**[Outputs](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

One or more artifacts that represent the output from running the job.

Type: Array of [Output](API_Output.md "API_Output.md") objects

Array Members: Minimum number of 1 item.

**[ProfileConfiguration](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Configuration for profile jobs. Used to select columns, do evaluations,
and override default parameters of evaluations. When configuration is null, the
profile job will run with default settings.

Type: [ProfileConfiguration](API_ProfileConfiguration.md "API_ProfileConfiguration.md") object

**[ProjectName](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The DataBrew project associated with this job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[RecipeReference](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Represents the name and version of a DataBrew recipe.

Type: [RecipeReference](API_RecipeReference.md "API_RecipeReference.md") object

**[ResourceArn](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[RoleArn](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The ARN of the AWS Identity and Access Management (IAM) role to be assumed when
DataBrew runs the job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[Tags](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

Metadata tags associated with this job.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

**[Timeout](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The job's timeout in minutes. A job that attempts to run longer than this timeout
period ends with a status of `TIMEOUT`.

Type: Integer

Valid Range: Minimum value of 0.

**[Type](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

The job type, which must be one of the following:

- `PROFILE` - The job analyzes the dataset to determine its size,
  data types, data distribution, and more.
- `RECIPE` - The job applies one or more transformations to a
  dataset.

Type: String

Valid Values: `PROFILE | RECIPE`

**[ValidationConfigurations](#API_DescribeJob_ResponseSyntax "#API_DescribeJob_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeJob.md "../../../goto/cli2/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeJob.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeJob.md "../../../goto/boto3/databrew-2017-07-25/DescribeJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeJob.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeJob.md")
