# ListSearchResultExportJobs

This operation exports search results of a search job
to a specified destination S3 bucket.

## Request Syntax

```
GET /export-search-jobs?MaxResults=`MaxResults`&NextToken=`NextToken`&SearchJobIdentifier=`SearchJobIdentifier`&Status=`Status` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_BKS_ListSearchResultExportJobs_RequestSyntax "#API_BKS_ListSearchResultExportJobs_RequestSyntax")**

The maximum number of resource list items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_BKS_ListSearchResultExportJobs_RequestSyntax "#API_BKS_ListSearchResultExportJobs_RequestSyntax")**

The next item following a partial list of returned backups
included in a search job.

For example, if a request
is made to return `MaxResults` number of backups, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

**[SearchJobIdentifier](#API_BKS_ListSearchResultExportJobs_RequestSyntax "#API_BKS_ListSearchResultExportJobs_RequestSyntax")**

The unique string that specifies the search job.

**[Status](#API_BKS_ListSearchResultExportJobs_RequestSyntax "#API_BKS_ListSearchResultExportJobs_RequestSyntax")**

The search jobs to be included in the export job
can be filtered by including this parameter.

Valid Values: `RUNNING | FAILED | COMPLETED`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ExportJobs": [
      {
         "CompletionTime": ***number***,
         "CreationTime": ***number***,
         "ExportJobArn": "***string***",
         "ExportJobIdentifier": "***string***",
         "SearchJobArn": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ExportJobs](#API_BKS_ListSearchResultExportJobs_ResponseSyntax "#API_BKS_ListSearchResultExportJobs_ResponseSyntax")**

The operation returns the included export jobs.

Type: Array of [ExportJobSummary](API_BKS_ExportJobSummary.md "API_BKS_ExportJobSummary.md") objects

**[NextToken](#API_BKS_ListSearchResultExportJobs_ResponseSyntax "#API_BKS_ListSearchResultExportJobs_ResponseSyntax")**

The next item following a partial list of returned backups
included in a search job.

For example, if a request
is made to return `MaxResults` number of backups, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**message**

User does not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**

An internal server error occurred. Retry your request.

**message**

Unexpected error during processing of request.

**retryAfterSeconds**

Retry the call after number of seconds.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource was not found for this request.

Confirm the resource information, such as the ARN or type is correct
and exists, then retry the request.

**message**

Request references a resource which does not exist.

**resourceId**

Hypothetical identifier of the resource affected.

**resourceType**

Hypothetical type of the resource affected.

HTTP Status Code: 404

**ServiceQuotaExceededException**

The request denied due to exceeding the quota limits permitted.

**message**

This request was not successful due to a service quota exceeding limits.

**quotaCode**

This is the code specific to the quota type.

**resourceId**

Identifier of the resource.

**resourceType**

Type of resource.

**serviceCode**

This is the code unique to the originating service with the quota.

HTTP Status Code: 402

**ThrottlingException**

The request was denied due to request throttling.

**message**

Request was unsuccessful due to request throttling.

**quotaCode**

This is the code unique to the originating service with the quota.

**retryAfterSeconds**

Retry the call after number of seconds.

**serviceCode**

This is the code unique to the originating service.

HTTP Status Code: 429

**ValidationException**

The input fails to satisfy the constraints specified by a service.

**message**

The input fails to satisfy the constraints specified by an Amazon service.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/cli2/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/DotNetSDKV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForGoV2/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForKotlin/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForPHPV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for Python](../../../goto/boto3/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/boto3/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ListSearchResultExportJobs.md")
