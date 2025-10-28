# ListCopyJobSummaries

This request obtains a list of copy jobs created
or running within the the most recent 30 days. You can
include parameters AccountID, State, ResourceType, MessageCategory,
AggregationPeriod, MaxResults, or NextToken to filter
results.

This request returns a summary that contains
Region, Account, State, RestourceType, MessageCategory,
StartTime, EndTime, and Count of included jobs.

## Request Syntax

```
GET /audit/copy-job-summaries?AccountId=`AccountId`&AggregationPeriod=`AggregationPeriod`&MaxResults=`MaxResults`&MessageCategory=`MessageCategory`&NextToken=`NextToken`&ResourceType=`ResourceType`&State=`State` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[AccountId](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

Returns the job count for the specified account.

If the request is sent from a member account or an account
not part of AWS Organizations, jobs within requestor's account
will be returned.

Root, admin, and delegated administrator accounts can use
the value ANY to return job counts from every account in the
organization.

`AGGREGATE_ALL` aggregates job counts
from all accounts within the authenticated organization,
then returns the sum.

Pattern: `^[0-9]{12}$`

**[AggregationPeriod](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

The period for the returned results.

- `ONE_DAY` - The daily job count for the prior 14 days.
- `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
- `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.

Valid Values: `ONE_DAY | SEVEN_DAYS | FOURTEEN_DAYS`

**[MaxResults](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

This parameter sets the maximum number of items
to be returned.

The value is an integer. Range of accepted values is from
1 to 500.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[MessageCategory](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

This parameter returns the job count for the specified
message category.

Example accepted strings include `AccessDenied`,
`Success`, and `InvalidParameters`. See
[Monitoring](monitoring.md "monitoring.md")
for a list of accepted MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts
for all message categories and returns the sum.

**[NextToken](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

The next item following a partial list of returned resources. For example, if a request
is made to return `MaxResults` number of resources, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

**[ResourceType](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

Returns the job count for the specified resource type.
Use request `GetSupportedResourceTypes` to obtain
strings for supported resource types.

The the value ANY returns count of all resource types.

`AGGREGATE_ALL` aggregates job counts
for all resource types and returns the sum.

The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[State](#API_ListCopyJobSummaries_RequestSyntax "#API_ListCopyJobSummaries_RequestSyntax")**

This parameter returns the job count for jobs
with the specified state.

The the value ANY returns count of all states.

`AGGREGATE_ALL` aggregates job counts
for all states and returns the sum.

Valid Values: `CREATED | RUNNING | ABORTING | ABORTED | COMPLETING | COMPLETED | FAILING | FAILED | PARTIAL | AGGREGATE_ALL | ANY`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AggregationPeriod": "***string***",
   "CopyJobSummaries": [
      {
         "AccountId": "***string***",
         "Count": ***number***,
         "EndTime": ***number***,
         "MessageCategory": "***string***",
         "Region": "***string***",
         "ResourceType": "***string***",
         "StartTime": ***number***,
         "State": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AggregationPeriod](#API_ListCopyJobSummaries_ResponseSyntax "#API_ListCopyJobSummaries_ResponseSyntax")**

The period for the returned results.

- `ONE_DAY` - The daily job count for the prior 14 days.
- `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
- `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.

Type: String

**[CopyJobSummaries](#API_ListCopyJobSummaries_ResponseSyntax "#API_ListCopyJobSummaries_ResponseSyntax")**

This return shows a summary that contains
Region, Account, State, ResourceType, MessageCategory,
StartTime, EndTime, and Count of included jobs.

Type: Array of [CopyJobSummary](API_CopyJobSummary.md "API_CopyJobSummary.md") objects

**[NextToken](#API_ListCopyJobSummaries_ResponseSyntax "#API_ListCopyJobSummaries_ResponseSyntax")**

The next item following a partial list of returned resources. For example, if a request
is made to return `MaxResults` number of resources, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/cli2/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForCpp/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/boto3/backup-2018-11-15/ListCopyJobSummaries.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListCopyJobSummaries.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListCopyJobSummaries.md")
