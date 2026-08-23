# TelemetryDestinationConfiguration

Configuration specifying where and how telemetry data should be delivered for AWS
resources.

## Contents

**CloudtrailParameters**

Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.

Type: [CloudtrailParameters](API_CloudtrailParameters.md "API_CloudtrailParameters.md") object

Required: No

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

**ELBLoadBalancerLoggingParameters**

Configuration parameters specific to ELB load balancer logging when ELB is the resource
type.

Type: [ELBLoadBalancerLoggingParameters](API_ELBLoadBalancerLoggingParameters.md "API_ELBLoadBalancerLoggingParameters.md") object

Required: No

**KmsKeyArn**

The Amazon Resource Name (ARN) of the customer-managed AWS KMS key used to encrypt the
log groups created during telemetry rule remediation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:\d{12}:key/(mrk-)?[a-f0-9-]+`

Required: No

**LogDeliveryParameters**

The configuration parameters for log delivery when the resource type supports configurable
log types, such as Amazon Bedrock Knowledge Bases or Elastic Load Balancing Application Load Balancers.

Type: [LogDeliveryParameters](API_LogDeliveryParameters.md "API_LogDeliveryParameters.md") object

Required: No

**MskMonitoringParameters**

Configuration parameters specific to MSK monitoring when MSK is the resource type.

Type: [MskMonitoringParameters](API_MskMonitoringParameters.md "API_MskMonitoringParameters.md") object

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

**WAFLoggingParameters**

Configuration parameters specific to WAF logging when WAF is the resource type.

Type: [WAFLoggingParameters](API_WAFLoggingParameters.md "API_WAFLoggingParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryDestinationConfiguration.md")
