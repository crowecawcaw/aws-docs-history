# TelemetryConfiguration

A model representing the state of a resource within an account according to telemetry
config.

## Contents

**AccountIdentifier**

The account ID which contains the resource managed in telemetry configuration. An example
of a valid account ID is `012345678901`.

Type: String

Length Constraints: Fixed length of 12.

Pattern: `[0-9]{12}`

Required: No

**LastUpdateTimeStamp**

The timestamp of the last change to the telemetry configuration for the resource. For
example, `1728679196318`.

Type: Long

Required: No

**ResourceIdentifier**

The identifier of the resource, for example for Amazon VPC, it would be
`vpc-1a2b3c4d5e6f1a2b3`.

Type: String

Required: No

**ResourceTags**

Tags associated with the resource, for example `{ Name: "ExampleInstance",
 Environment: "Development" }`.

Type: String to string map

Required: No

**ResourceType**

The type of resource, for example `AWS::EC2::Instance`, or
`AWS::EKS::Cluster`, etc.

Type: String

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function | AWS::CloudTrail | AWS::EKS::Cluster | AWS::WAFv2::WebACL | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::Route53Resolver::ResolverEndpoint | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Browser | AWS::BedrockAgentCore::CodeInterpreter | AWS::BedrockAgentCore::Gateway | AWS::BedrockAgentCore::Memory | AWS::BedrockAgentCore::WorkloadIdentity | AWS::SecurityHub::Hub | AWS::CloudFront::Distribution | AWS::SecurityHub::HubV2 | AWS::CloudWatch::OTelEnrichment | AWS::MSK::Cluster | AWS::S3::Bucket | AWS::Bedrock::KnowledgeBase`

Required: No

**TelemetryConfigurationState**

The configuration state for the resource, for example `{ Logs: NotApplicable;
 Metrics: Enabled; Traces: NotApplicable; }`.

Type: String to string map

Valid Keys: `Logs | Metrics | Traces`

Valid Values: `Enabled | Disabled | NotApplicable`

Required: No

**TelemetrySourceType**

Specifies the type of telemetry source for a resource, such as EKS cluster logs.

Type: String

Valid Values: `VPC_FLOW_LOGS | ROUTE53_RESOLVER_QUERY_LOGS | EKS_AUDIT_LOGS | EKS_AUTHENTICATOR_LOGS | EKS_CONTROLLER_MANAGER_LOGS | EKS_SCHEDULER_LOGS | EKS_API_LOGS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
