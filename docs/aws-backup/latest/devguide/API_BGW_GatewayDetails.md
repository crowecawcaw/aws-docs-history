# GatewayDetails

The details of gateway.

## Contents

**GatewayArn**

The Amazon Resource Name (ARN) of the
gateway. Use the `ListGateways` operation
to return a list of gateways for your account and
AWS Region.

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

The type of the gateway type.

Type: String

Valid Values: `BACKUP_VM`

Required: No

**HypervisorId**

The hypervisor ID of the gateway.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**LastSeenTime**

Details showing the last time AWS Backup gateway communicated
with the cloud, in Unix format and UTC time.

Type: Timestamp

Required: No

**MaintenanceStartTime**

Returns your gateway's weekly maintenance start time including the day and time of the week.
Note that values are in terms of the gateway's time zone. Can be weekly or monthly.

Type: [MaintenanceStartTime](API_BGW_MaintenanceStartTime.md "API_BGW_MaintenanceStartTime.md") object

Required: No

**NextUpdateAvailabilityTime**

Details showing the next update availability time of the
gateway.

Type: Timestamp

Required: No

**VpcEndpoint**

The DNS name for the virtual private cloud (VPC) endpoint the gateway
uses to connect to the cloud for backup gateway.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/GatewayDetails.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/GatewayDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/GatewayDetails.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/GatewayDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/GatewayDetails.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/GatewayDetails.md")
