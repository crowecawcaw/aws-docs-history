# ListScanJobSummaries

This is a request for a summary of scan jobs created or running within the most recent 30 days.

## Request Syntax

```
GET /audit/scan-job-summaries?AccountId=`AccountId`&AggregationPeriod=`AggregationPeriod`&MalwareScanner=`MalwareScanner`&MaxResults=`MaxResults`&NextToken=`NextToken`&ResourceType=`ResourceType`&ScanResultStatus=`ScanResultStatus`&State=`State` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[AccountId](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

Returns the job count for the specified account.

If the request is sent from a member account or an account not part of AWS Organizations, jobs within requestor's account will be returned.

Root, admin, and delegated administrator accounts can use the value `ANY` to return job counts from every account in the organization.

`AGGREGATE_ALL` aggregates job counts from all accounts within the authenticated organization, then returns the sum.

Pattern: `^[0-9]{12}$`

**[AggregationPeriod](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

The period for the returned results.

- `ONE_DAY`The daily job count for the prior 1 day.
- `SEVEN_DAYS`The daily job count for the prior 7 days.
- `FOURTEEN_DAYS`The daily job count for the prior 14 days.

Valid Values: `ONE_DAY | SEVEN_DAYS | FOURTEEN_DAYS`

**[MalwareScanner](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

Returns only the scan jobs for the specified malware scanner.
Currently the only MalwareScanner is `GUARDDUTY`. But the field also supports `ANY`, and `AGGREGATE_ALL`.

Valid Values: `GUARDDUTY`

**[MaxResults](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

The maximum number of items to be returned.

The value is an integer. Range of accepted values is from 1 to 500.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is made to
return `MaxResults` number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the next token.

**[ResourceType](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

Returns the job count for the specified resource type. Use request
`GetSupportedResourceTypes` to obtain strings for supported resource types.

The the value `ANY` returns count of all resource types.

`AGGREGATE_ALL` aggregates job counts for all resource types and returns the sum.

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[ScanResultStatus](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

Returns only the scan jobs for the specified scan results.

Valid Values: `NO_THREATS_FOUND | THREATS_FOUND`

**[State](#API_ListScanJobSummaries_RequestSyntax "#API_ListScanJobSummaries_RequestSyntax")**

Returns only the scan jobs for the specified scanning job state.

Valid Values: `CREATED | COMPLETED | COMPLETED_WITH_ISSUES | RUNNING | FAILED | CANCELED | AGGREGATE_ALL | ANY`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AggregationPeriod": "***string***",
   "NextToken": "***string***",
   "ScanJobSummaries": [
      {
         "AccountId": "***string***",
         "Count": ***number***,
         "EndTime": ***number***,
         "MalwareScanner": "***string***",
         "Region": "***string***",
         "ResourceType": "***string***",
         "ScanResultStatus": "***string***",
         "StartTime": ***number***,
         "State": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AggregationPeriod](#API_ListScanJobSummaries_ResponseSyntax "#API_ListScanJobSummaries_ResponseSyntax")**

The period for the returned results.

- `ONE_DAY`The daily job count for the prior 1 day.
- `SEVEN_DAYS`The daily job count for the prior 7 days.
- `FOURTEEN_DAYS`The daily job count for the prior 14 days.

Valid Values: `'ONE_DAY'` | `'SEVEN_DAYS'` | `'FOURTEEN_DAYS'`

Type: String

**[NextToken](#API_ListScanJobSummaries_ResponseSyntax "#API_ListScanJobSummaries_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is made to
return `MaxResults` number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the next token.

Type: String

**[ScanJobSummaries](#API_ListScanJobSummaries_ResponseSyntax "#API_ListScanJobSummaries_ResponseSyntax")**

The summary information.

Type: Array of [ScanJobSummary](API_ScanJobSummary.md "API_ScanJobSummary.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/cli2/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForCpp/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/boto3/backup-2018-11-15/ListScanJobSummaries.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListScanJobSummaries.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListScanJobSummaries.md")
