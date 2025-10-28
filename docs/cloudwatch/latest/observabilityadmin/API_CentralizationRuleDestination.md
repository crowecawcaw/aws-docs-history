# CentralizationRuleDestination

Configuration specifying the primary destination for centralized telemetry data.

## Contents

**Region**

The primary destination region to which telemetry data should be centralized.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

**Account**

The destination account (within the organization) to which the telemetry data should be
centralized.

Type: String

Length Constraints: Fixed length of 12.

Pattern: `[0-9]{12}`

Required: No

**DestinationLogsConfiguration**

Log specific configuration for centralization destination log groups.

Type: [DestinationLogsConfiguration](API_DestinationLogsConfiguration.md "API_DestinationLogsConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleDestination.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleDestination.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleDestination.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleDestination.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleDestination.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleDestination.md")
