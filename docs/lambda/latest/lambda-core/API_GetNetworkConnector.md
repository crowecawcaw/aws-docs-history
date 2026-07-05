# GetNetworkConnector

Retrieves the current configuration, state, and metadata of a network connector. The `Identifier`
parameter accepts the connector ID, name, or full ARN. Use this operation to poll connector state after creation
or update, or to inspect the current VPC configuration and any failure reasons.

The response includes the full connector configuration, current state, and — if the connector has been updated
— the `LastUpdateStatus` and `LastUpdateStatusReasonCode` fields that indicate whether the
most recent update succeeded or failed.

## Request Syntax

```
GET /2026-04-04/network-connectors/`Identifier` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[Identifier](#API_GetNetworkConnector_RequestSyntax "#API_GetNetworkConnector_RequestSyntax")**

The identifier of the network connector to retrieve. You can specify the connector ID, name, or full ARN.

Length Constraints: Minimum length of 1. Maximum length of 140.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "***string***",
   "Configuration": { ... },
   "Id": "***string***",
   "LastModified": "***string***",
   "LastUpdateStatus": "***string***",
   "LastUpdateStatusReason": "***string***",
   "LastUpdateStatusReasonCode": "***string***",
   "Name": "***string***",
   "OperatorRole": "***string***",
   "State": "***string***",
   "StateReason": "***string***",
   "StateReasonCode": "***string***",
   "Version": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The Amazon Resource Name (ARN) of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)`

**[Configuration](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The network configuration of the connector, including VPC subnets and security groups.

Type: [NetworkConnectorConfiguration](API_NetworkConnectorConfiguration.md "API_NetworkConnectorConfiguration.md") object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

**[Id](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The unique identifier of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

**[LastModified](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The date and time when the connector configuration was last modified.

Type: Timestamp

**[LastUpdateStatus](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The status of the most recent update operation (`Successful`, `Failed`, or
`InProgress`).

Type: String

Valid Values: `Successful | Failed | InProgress`

**[LastUpdateStatusReason](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

A human-readable explanation of the last update status.

Type: String

**[LastUpdateStatusReasonCode](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

A machine-readable code indicating the reason for the last update status. Use this for programmatic error
handling.

Type: String

Valid Values: `DisallowedByVpcEncryptionControl | Ec2RequestLimitExceeded | InsufficientRolePermissions | InternalError | InvalidSecurityGroup | InvalidSubnet | SubnetOutOfIPAddresses`

**[Name](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The name of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}`

**[OperatorRole](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The ARN of the IAM role that Lambda uses to manage the underlying ENI resources for this
connector.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 10000.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

**[State](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The current state of the network connector.

Type: String

Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`

**[StateReason](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

A human-readable explanation of the current state, populated when the state is `FAILED` or
`DELETE_FAILED`.

Type: String

**[StateReasonCode](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

A machine-readable code indicating the reason for the current state. Use this for programmatic error
handling.

Type: String

Valid Values: `DisallowedByVpcEncryptionControl | Ec2RequestLimitExceeded | InsufficientRolePermissions | InternalError | InvalidSecurityGroup | InvalidSubnet | SubnetOutOfIPAddresses`

**[Version](#API_GetNetworkConnector_ResponseSyntax "#API_GetNetworkConnector_ResponseSyntax")**

The version number of the connector configuration, incremented on each update.

Type: Long

Valid Range: Minimum value of 0.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

One of the parameters in the request is not valid. Check the error message for details about which parameter
failed validation.

**Type**

The exception type.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.

**Type**

The exception type.

HTTP Status Code: 404

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

- [AWS Command Line Interface V2](../../../goto/cli2/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/cli2/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/DotNetSDKV4/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForCpp/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForGoV2/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForJavaV2/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForKotlin/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForPHPV3/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for Python](../../../goto/boto3/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/boto3/lambda-core-2026-04-30/GetNetworkConnector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lambda-core-2026-04-30/GetNetworkConnector.md "../../../goto/SdkForRubyV3/lambda-core-2026-04-30/GetNetworkConnector.md")
