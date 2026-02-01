# ListDatasetExportJobs

Returns a list of dataset export jobs that use the given dataset. When
a dataset is not specified, all the dataset export jobs associated with
the account are listed. The response provides the properties for each
dataset export job, including the Amazon Resource Name (ARN). For more
information on dataset export jobs, see [CreateDatasetExportJob](API_CreateDatasetExportJob.md "API_CreateDatasetExportJob.md"). For more information on datasets, see
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

**[datasetArn](#API_ListDatasetExportJobs_RequestSyntax "#API_ListDatasetExportJobs_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset to list the dataset
export jobs for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListDatasetExportJobs_RequestSyntax "#API_ListDatasetExportJobs_RequestSyntax")**

The maximum number of dataset export jobs to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListDatasetExportJobs_RequestSyntax "#API_ListDatasetExportJobs_RequestSyntax")**

A token returned from the previous call to
`ListDatasetExportJobs` for getting the next set of dataset
export jobs (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "datasetExportJobs": [
      {
         "creationDateTime": ***number***,
         "datasetExportJobArn": "***string***",
         "failureReason": "***string***",
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

**[datasetExportJobs](#API_ListDatasetExportJobs_ResponseSyntax "#API_ListDatasetExportJobs_ResponseSyntax")**

The list of dataset export jobs.

Type: Array of [DatasetExportJobSummary](API_DatasetExportJobSummary.md "API_DatasetExportJobSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListDatasetExportJobs_ResponseSyntax "#API_ListDatasetExportJobs_ResponseSyntax")**

A token for getting the next set of dataset export jobs (if they
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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/cli2/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/boto3/personalize-2018-05-22/ListDatasetExportJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetExportJobs.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetExportJobs.md")
