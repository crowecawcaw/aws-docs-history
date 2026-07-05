# ListNetworkConnectors

Returns a paginated list of network connectors in your account for the current Region. You can optionally
filter results by connector state. Use the `Marker` parameter from a previous response to retrieve the
next page of results.

Each item in the response includes the connector ARN, name, ID, type, current state, and last modified
timestamp. To retrieve full configuration details for a specific connector, use
`GetNetworkConnector`.

## Request Syntax

```
GET /2026-04-04/network-connectors?Marker=`Marker`&MaxItems=`MaxItems`&State=`State` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[Marker](#API_ListNetworkConnectors_RequestSyntax "#API_ListNetworkConnectors_RequestSyntax")**

The pagination token from a previous `ListNetworkConnectors` response. Use this value to retrieve
the next page of results.

**[MaxItems](#API_ListNetworkConnectors_RequestSyntax "#API_ListNetworkConnectors_RequestSyntax")**

The maximum number of connectors to return per page. Valid range: 1 to 100.

Valid Range: Minimum value of 1. Maximum value of 100.

**[State](#API_ListNetworkConnectors_RequestSyntax "#API_ListNetworkConnectors_RequestSyntax")**

Optional filter to return only connectors in the specified state (for example, `ACTIVE` or
`FAILED`).

Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NetworkConnectors": [
      {
         "Arn": "***string***",
         "Id": "***string***",
         "LastModified": "***string***",
         "Name": "***string***",
         "State": "***string***",
         "Type": "***string***"
      }
   ],
   "NextMarker": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NetworkConnectors](#API_ListNetworkConnectors_ResponseSyntax "#API_ListNetworkConnectors_ResponseSyntax")**

A list of network connector summaries for the current page of results.

Type: Array of [NetworkConnectorSummary](API_NetworkConnectorSummary.md "API_NetworkConnectorSummary.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

**[NextMarker](#API_ListNetworkConnectors_ResponseSyntax "#API_ListNetworkConnectors_ResponseSyntax")**

The pagination token to include in a subsequent request to retrieve the next page. This value is null when
there are no more results.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

One of the parameters in the request is not valid. Check the error message for details about which parameter
failed validation.

**Type**

The exception type.

HTTP Status Code: 400

**ServiceException**

An internal service error occurred. Retry the request with exponential backoff.

**Type**

The exception type.

HTTP Status Code: 500

**TooManyRequestsException**

The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait
using exponential backoff.

**Reason**

The reason for the throttling.

**retryAfterSeconds**

The number of seconds to wait before retrying the request.

**Type**

The exception type.

HTTP Status Code: 429

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/cli2/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/DotNetSDKV4/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForCpp/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForGoV2/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForJavaV2/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForKotlin/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForPHPV3/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for Python](../../../goto/boto3/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/boto3/lambda-core-2026-04-30/ListNetworkConnectors.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lambda-core-2026-04-30/ListNetworkConnectors.md "../../../goto/SdkForRubyV3/lambda-core-2026-04-30/ListNetworkConnectors.md")
