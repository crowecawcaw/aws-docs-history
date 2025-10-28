# ListIndexedRecoveryPoints

This operation returns a list of recovery points that have an
associated index, belonging to the specified account.

Optional parameters you can include are: MaxResults;
NextToken; SourceResourceArns; CreatedBefore; CreatedAfter;
and ResourceType.

## Request Syntax

```
GET /indexes/recovery-point/?createdAfter=`CreatedAfter`&createdBefore=`CreatedBefore`&indexStatus=`IndexStatus`&maxResults=`MaxResults`&nextToken=`NextToken`&resourceType=`ResourceType`&sourceResourceArn=`SourceResourceArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[CreatedAfter](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

Returns only indexed recovery points that were created after the
specified date.

**[CreatedBefore](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

Returns only indexed recovery points that were created before the
specified date.

**[IndexStatus](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

Include this parameter to filter the returned list by
the indicated statuses.

Accepted values: `PENDING` | `ACTIVE` | `FAILED` | `DELETING`

A recovery point with an index that has the status of `ACTIVE`
can be included in a search.

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

**[MaxResults](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

The maximum number of resource list items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

The next item following a partial list of returned recovery points.

For example, if a request
is made to return `MaxResults` number of indexed recovery points, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

**[ResourceType](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

Returns a list of indexed recovery points for the specified
resource type(s).

Accepted values include:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[SourceResourceArn](#API_ListIndexedRecoveryPoints_RequestSyntax "#API_ListIndexedRecoveryPoints_RequestSyntax")**

A string of the Amazon Resource Name (ARN) that uniquely identifies
the source resource.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "IndexedRecoveryPoints": [
      {
         "BackupCreationDate": ***number***,
         "BackupVaultArn": "***string***",
         "IamRoleArn": "***string***",
         "IndexCreationDate": ***number***,
         "IndexStatus": "***string***",
         "IndexStatusMessage": "***string***",
         "RecoveryPointArn": "***string***",
         "ResourceType": "***string***",
         "SourceResourceArn": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[IndexedRecoveryPoints](#API_ListIndexedRecoveryPoints_ResponseSyntax "#API_ListIndexedRecoveryPoints_ResponseSyntax")**

This is a list of recovery points that have an
associated index, belonging to the specified account.

Type: Array of [IndexedRecoveryPoint](API_IndexedRecoveryPoint.md "API_IndexedRecoveryPoint.md") objects

**[NextToken](#API_ListIndexedRecoveryPoints_ResponseSyntax "#API_ListIndexedRecoveryPoints_ResponseSyntax")**

The next item following a partial list of returned recovery points.

For example, if a request
is made to return `MaxResults` number of indexed recovery points, `NextToken`
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

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/cli2/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForCpp/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/boto3/backup-2018-11-15/ListIndexedRecoveryPoints.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListIndexedRecoveryPoints.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListIndexedRecoveryPoints.md")
