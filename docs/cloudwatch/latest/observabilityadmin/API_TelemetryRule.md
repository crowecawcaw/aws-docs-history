# TelemetryRule

Defines how telemetry should be configured for specific AWS resources.

## Contents

**TelemetryType**

The type of telemetry to collect (Logs, Metrics, or Traces).

Type: String

Valid Values: `Logs | Metrics | Traces`

Required: Yes

**DestinationConfiguration**

Configuration specifying where and how the telemetry data should be delivered.

Type: [TelemetryDestinationConfiguration](API_TelemetryDestinationConfiguration.md "API_TelemetryDestinationConfiguration.md") object

Required: No

**ResourceType**

The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC",
"AWS::EKS::Cluster", "AWS::WAFv2::WebACL").

Type: String

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function | AWS::CloudTrail | AWS::EKS::Cluster | AWS::WAFv2::WebACL | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::Route53Resolver::ResolverEndpoint | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Browser | AWS::BedrockAgentCore::CodeInterpreter`

Required: No

**Scope**

The organizational scope to which the rule applies, specified using accounts or
organizational units.

Type: String

Required: No

**SelectionCriteria**

Criteria for selecting which resources the rule applies to, such as resource tags.

Type: String

Required: No

**TelemetrySourceTypes**

The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS
or EKS_AUDIT_LOGS. TelemetrySourceTypes must be correlated with the specific resource type.

Type: Array of strings

Valid Values: `VPC_FLOW_LOGS | ROUTE53_RESOLVER_QUERY_LOGS | EKS_AUDIT_LOGS | EKS_AUTHENTICATOR_LOGS | EKS_CONTROLLER_MANAGER_LOGS | EKS_SCHEDULER_LOGS | EKS_API_LOGS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRule.md")
