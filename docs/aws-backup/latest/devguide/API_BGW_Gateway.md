# Gateway

A gateway is an AWS Backup Gateway appliance that runs on the customer's network
to provide seamless connectivity to backup storage in the AWS Cloud.

## Contents

**GatewayArn**

The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation
to return a list of gateways for your account and AWS Region.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 180.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: No

**GatewayDisplayName**

The display name of the gateway.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**GatewayType**

The type of the gateway.

Type: String

Valid Values: `BACKUP_VM`

Required: No

**HypervisorId**

The hypervisor ID of the gateway.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**LastSeenTime**

The last time AWS Backup gateway communicated with the gateway, in Unix format and
UTC time.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/Gateway.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/Gateway.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/Gateway.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/Gateway.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/Gateway.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/Gateway.md")
