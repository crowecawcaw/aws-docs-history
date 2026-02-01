# ListDatasetImportJobs

Returns a list of dataset import jobs that use the given dataset. When
a dataset is not specified, all the dataset import jobs associated with
the account are listed. The response provides the properties for each
dataset import job, including the Amazon Resource Name (ARN). For more
information on dataset import jobs, see [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md"). For more information on datasets, see
[CreateDataset](API_CreateDataset.md "API_CreateDataset.md").

## Request Syntax

```
{
   "datasetArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetArn](#API_ListDatasetImportJobs_RequestSyntax "#API_ListDatasetImportJobs_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset to list the dataset
import jobs for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListDatasetImportJobs_RequestSyntax "#API_ListDatasetImportJobs_RequestSyntax")**

The maximum number of dataset import jobs to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListDatasetImportJobs_RequestSyntax "#API_ListDatasetImportJobs_RequestSyntax")**

A token returned from the previous call to
`ListDatasetImportJobs` for getting the next set of dataset
import jobs (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "datasetImportJobs": [
      {
         "creationDateTime": ***number***,
         "datasetImportJobArn": "***string***",
         "failureReason": "***string***",
         "importMode": "***string***",
         "jobName": "***string***",
         "lastUpdatedDateTime": ***number***,
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetImportJobs](#API_ListDatasetImportJobs_ResponseSyntax "#API_ListDatasetImportJobs_ResponseSyntax")**

The list of dataset import jobs.

Type: Array of [DatasetImportJobSummary](API_DatasetImportJobSummary.md "API_DatasetImportJobSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListDatasetImportJobs_ResponseSyntax "#API_ListDatasetImportJobs_ResponseSyntax")**

A token for getting the next set of dataset import jobs (if they
exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/cli2/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/boto3/personalize-2018-05-22/ListDatasetImportJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetImportJobs.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetImportJobs.md")
