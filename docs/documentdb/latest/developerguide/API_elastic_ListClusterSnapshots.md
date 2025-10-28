# ListClusterSnapshots

Returns information about snapshots for a specified elastic cluster.

## Request Syntax

```
GET /cluster-snapshots?clusterArn=`clusterArn`&maxResults=`maxResults`&nextToken=`nextToken`&snapshotType=`snapshotType` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[clusterArn](#API_elastic_ListClusterSnapshots_RequestSyntax "#API_elastic_ListClusterSnapshots_RequestSyntax")**

The ARN identifier of the elastic cluster.

**[maxResults](#API_elastic_ListClusterSnapshots_RequestSyntax "#API_elastic_ListClusterSnapshots_RequestSyntax")**

The maximum number of elastic cluster snapshot results to receive in the response.

Valid Range: Minimum value of 20. Maximum value of 100.

**[nextToken](#API_elastic_ListClusterSnapshots_RequestSyntax "#API_elastic_ListClusterSnapshots_RequestSyntax")**

A pagination token provided by a previous request.
If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.

If there is no more data in the responce, the `nextToken` will not be returned.

**[snapshotType](#API_elastic_ListClusterSnapshots_RequestSyntax "#API_elastic_ListClusterSnapshots_RequestSyntax")**

The type of cluster snapshots to be returned. You can specify one of the following values:

- `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
- `manual` - Return all cluster snapshots that you have manually created for your AWS account.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "***string***",
   "snapshots": [
      {
         "clusterArn": "***string***",
         "snapshotArn": "***string***",
         "snapshotCreationTime": "***string***",
         "snapshotName": "***string***",
         "status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_elastic_ListClusterSnapshots_ResponseSyntax "#API_elastic_ListClusterSnapshots_ResponseSyntax")**

A pagination token provided by a previous request.
If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.

If there is no more data in the responce, the `nextToken` will not be returned.

Type: String

**[snapshots](#API_elastic_ListClusterSnapshots_ResponseSyntax "#API_elastic_ListClusterSnapshots_ResponseSyntax")**

A list of snapshots for a specified elastic cluster.

Type: Array of [ClusterSnapshotInList](API_elastic_ClusterSnapshotInList.md "API_elastic_ClusterSnapshotInList.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

An exception that occurs when there are not sufficient permissions to perform an action.

**message**

An error message explaining why access was denied.

HTTP Status Code: 403

**InternalServerException**

There was an internal server error.

HTTP Status Code: 500

**ThrottlingException**

ThrottlingException will be thrown when request was denied due to request throttling.

**retryAfterSeconds**

The number of seconds to wait before retrying the operation.

HTTP Status Code: 429

**ValidationException**

A structure defining a validation exception.

**fieldList**

A list of the fields in which the validation exception occurred.

**message**

An error message describing the validation exception.

**reason**

The reason why the validation exception occurred (one of `unknownOperation`,
`cannotParse`, `fieldValidationFailed`, or `other`).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/cli2/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/boto3/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListClusterSnapshots.md")
