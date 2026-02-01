# ListClusters

Returns information about provisioned Amazon DocumentDB elastic clusters.

## Request Syntax

```
GET /clusters?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_elastic_ListClusters_RequestSyntax "#API_elastic_ListClusters_RequestSyntax")**

The maximum number of elastic cluster snapshot results to receive in the response.

Valid Range: Minimum value of 1. Maximum value of 100.

**[nextToken](#API_elastic_ListClusters_RequestSyntax "#API_elastic_ListClusters_RequestSyntax")**

A pagination token provided by a previous request.
If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.

If there is no more data in the responce, the `nextToken` will not be returned.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "clusters": [
      {
         "clusterArn": "***string***",
         "clusterName": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[clusters](#API_elastic_ListClusters_ResponseSyntax "#API_elastic_ListClusters_ResponseSyntax")**

A list of Amazon DocumentDB elastic clusters.

Type: Array of [ClusterInList](API_elastic_ClusterInList.md "API_elastic_ClusterInList.md") objects

**[nextToken](#API_elastic_ListClusters_ResponseSyntax "#API_elastic_ListClusters_ResponseSyntax")**

A pagination token provided by a previous request.
If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.

If there is no more data in the responce, the `nextToken` will not be returned.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/cli2/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/boto3/docdb-elastic-2022-11-28/ListClusters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListClusters.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListClusters.md")
