# NetworkConnectorSummary

Summary information about a network connector returned by `ListNetworkConnectors`. Contains
identifying fields and current state. To retrieve full configuration details, use
`GetNetworkConnector`.

## Contents

**Arn**

The ARN of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)`

Required: Yes

**Id**

The unique identifier of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Required: Yes

**Name**

The name of the network connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}`

Required: Yes

**Type**

The type of the network connector (`VPC_EGRESS`).

Type: String

Valid Values: `VPC_EGRESS`

Required: Yes

**LastModified**

The date and time when the connector was last modified.

Type: Timestamp

Required: No

**State**

The current state of the network connector.

Type: String

Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorSummary.md "../../../goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorSummary.md "../../../goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorSummary.md "../../../goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorSummary.md")
