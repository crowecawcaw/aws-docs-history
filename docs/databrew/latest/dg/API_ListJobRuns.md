# ListJobRuns

Lists all of the previous runs of a particular DataBrew job.

## Request Syntax

```
GET /jobs/`name`/jobRuns?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListJobRuns_RequestSyntax "#API_ListJobRuns_RequestSyntax")**

The maximum number of results to return in this request.

Valid Range: Minimum value of 1. Maximum value of 100.

**[name](#API_ListJobRuns_RequestSyntax "#API_ListJobRuns_RequestSyntax")**

The name of the job.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

**[NextToken](#API_ListJobRuns_RequestSyntax "#API_ListJobRuns_RequestSyntax")**

The token returned by a previous call to retrieve the next set of results.

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "JobRuns": [
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
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[JobRuns](#API_ListJobRuns_ResponseSyntax "#API_ListJobRuns_ResponseSyntax")**

A list of job runs that have occurred for the specified job.

Type: Array of [JobRun](API_JobRun.md "API_JobRun.md") objects

**[NextToken](#API_ListJobRuns_ResponseSyntax "#API_ListJobRuns_ResponseSyntax")**

A token that you can use in a subsequent call to retrieve the next set of
results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListJobRuns.md "../../../goto/cli2/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/ListJobRuns.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListJobRuns.md "../../../goto/boto3/databrew-2017-07-25/ListJobRuns.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListJobRuns.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListJobRuns.md")
