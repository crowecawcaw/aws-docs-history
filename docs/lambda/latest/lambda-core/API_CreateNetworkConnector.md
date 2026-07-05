# CreateNetworkConnector

Creates a network connector that enables Lambda compute resources to route outbound traffic
through your Amazon VPC. The network connector provisions elastic network interfaces (ENIs) in the subnets you
specify, providing a managed network path to private resources such as databases, caches, and internal APIs.

This operation is asynchronous. The network connector starts in `PENDING` state while ENIs are
provisioned in your VPC (provisioning typically takes up to 10 minutes). Use `GetNetworkConnector` to
poll the connector state until it reaches `ACTIVE`. Once active, you can attach the connector to
Lambda MicroVMs at run time using the `egressNetworkConnectors` parameter on
`RunMicroVm`.

This operation is idempotent when you provide a `ClientToken` — if you retry a request that
completed successfully using the same client token, the operation returns the existing connector without creating
a duplicate.

## Request Syntax

```
POST /2026-04-04/network-connectors HTTP/1.1
Content-type: application/json

{
   "ClientToken": "`string`",
   "Configuration": { ... },
   "Name": "`string`",
   "OperatorRole": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateNetworkConnector_RequestSyntax "#API_CreateNetworkConnector_RequestSyntax")**

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a
request with the same client token, the API returns the existing connector without creating a duplicate.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: No

**[Configuration](#API_CreateNetworkConnector_RequestSyntax "#API_CreateNetworkConnector_RequestSyntax")**

The network configuration for the connector. Specify a `VpcEgressConfiguration` to enable outbound
traffic routing through your VPC.

Type: [NetworkConnectorConfiguration](API_NetworkConnectorConfiguration.md "API_NetworkConnectorConfiguration.md") object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: Yes

**[Name](#API_CreateNetworkConnector_RequestSyntax "#API_CreateNetworkConnector_RequestSyntax")**

A unique name for the network connector within your account and Region. You can use the name to identify the
connector in subsequent API calls.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}`

Required: Yes

**[OperatorRole](#API_CreateNetworkConnector_RequestSyntax "#API_CreateNetworkConnector_RequestSyntax")**

The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This
role must have permissions for `ec2:CreateNetworkInterface`, `ec2:DeleteNetworkInterface`,
and related describe operations.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 10000.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

**[Tags](#API_CreateNetworkConnector_RequestSyntax "#API_CreateNetworkConnector_RequestSyntax")**

A map of key-value pairs to associate with the network connector for organization, cost allocation, or access
control.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Required: No

## Response Syntax

```
HTTP/1.1 202
Content-type: application/json

{
   "Arn": "***string***",
   "Configuration": { ... },
   "Id": "***string***",
   "Name": "***string***",
   "OperatorRole": "***string***",
   "State": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

**[Arn](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The Amazon Resource Name (ARN) of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)`

**[Configuration](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The network configuration of the connector, including VPC subnets and security groups.

Type: [NetworkConnectorConfiguration](API_NetworkConnectorConfiguration.md "API_NetworkConnectorConfiguration.md") object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

**[Id](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The unique identifier of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

**[Name](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The name of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}`

**[OperatorRole](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The ARN of the IAM role that Lambda uses to manage the underlying ENI resources for this
connector.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 10000.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

**[State](#API_CreateNetworkConnector_ResponseSyntax "#API_CreateNetworkConnector_ResponseSyntax")**

The current state of the network connector.

Type: String

Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

One of the parameters in the request is not valid. Check the error message for details about which parameter
failed validation.

**Type**

The exception type.

HTTP Status Code: 400

**NetworkConnectorLimitExceededException**

The account has reached the maximum number of network connectors allowed.

**Type**

The exception type.

HTTP Status Code: 400

**ResourceConflictException**

The request could not be completed due to a conflict with the current state of the resource. For example,
attempting to update a connector that is not in `ACTIVE` state.

**Type**

The exception type.

HTTP Status Code: 409

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

- [AWS Command Line Interface V2](../../../goto/cli2/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/cli2/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/DotNetSDKV4/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForCpp/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForGoV2/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForJavaV2/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForJavaScriptV3/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForKotlin/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForPHPV3/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for Python](../../../goto/boto3/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/boto3/lambda-core-2026-04-30/CreateNetworkConnector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lambda-core-2026-04-30/CreateNetworkConnector.md "../../../goto/SdkForRubyV3/lambda-core-2026-04-30/CreateNetworkConnector.md")
