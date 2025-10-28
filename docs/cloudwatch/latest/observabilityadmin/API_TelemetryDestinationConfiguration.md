# TelemetryDestinationConfiguration

Configuration specifying where and how telemetry data should be delivered for AWS
resources.

## Contents

**DestinationPattern**

The pattern used to generate the destination path or name, supporting macros like
<resourceId> and <accountId>.

Type: String

Required: No

**DestinationType**

The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").

Type: String

Valid Values: `cloud-watch-logs`

Required: No

**RetentionInDays**

The number of days to retain the telemetry data in the destination.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 3653.

Required: No

**VPCFlowLogParameters**

Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

Type: [VPCFlowLogParameters](API_VPCFlowLogParameters.md "API_VPCFlowLogParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
