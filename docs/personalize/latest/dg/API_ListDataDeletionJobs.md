# ListDataDeletionJobs

Returns a list of data deletion jobs for a dataset group ordered by creation time,
with the most recent first.
When
a dataset group is not specified, all the data deletion jobs associated with
the account are listed. The response provides the properties for each
job, including the Amazon Resource Name (ARN). For more
information on data deletion jobs, see [Deleting users](delete-records.md "delete-records.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_ListDataDeletionJobs_RequestSyntax "#API_ListDataDeletionJobs_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group to list data deletion jobs for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListDataDeletionJobs_RequestSyntax "#API_ListDataDeletionJobs_RequestSyntax")**

The maximum number of data deletion jobs to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListDataDeletionJobs_RequestSyntax "#API_ListDataDeletionJobs_RequestSyntax")**

A token returned from the previous call to
`ListDataDeletionJobs` for getting the next set of jobs (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "dataDeletionJobs": [
      {
         "creationDateTime": ***number***,
         "dataDeletionJobArn": "***string***",
         "datasetGroupArn": "***string***",
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

**[dataDeletionJobs](#API_ListDataDeletionJobs_ResponseSyntax "#API_ListDataDeletionJobs_ResponseSyntax")**

The list of data deletion jobs.

Type: Array of [DataDeletionJobSummary](API_DataDeletionJobSummary.md "API_DataDeletionJobSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListDataDeletionJobs_ResponseSyntax "#API_ListDataDeletionJobs_ResponseSyntax")**

A token for getting the next set of data deletion jobs (if they
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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/cli2/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/boto3/personalize-2018-05-22/ListDataDeletionJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDataDeletionJobs.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDataDeletionJobs.md")
