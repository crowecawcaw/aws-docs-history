

# TelemetryRuleSummary
<a name="API_TelemetryRuleSummary"></a>

 A summary of a telemetry rule's key properties. 

## Contents
<a name="API_TelemetryRuleSummary_Contents"></a>

 ** CreatedTimeStamp **   <a name="cwoa-Type-TelemetryRuleSummary-CreatedTimeStamp"></a>
 The timestamp when the telemetry rule was created.   
Type: Long  
Required: No

 ** LastUpdateTimeStamp **   <a name="cwoa-Type-TelemetryRuleSummary-LastUpdateTimeStamp"></a>
 The timestamp when the telemetry rule was last modified.   
Type: Long  
Required: No

 ** ResourceType **   <a name="cwoa-Type-TelemetryRuleSummary-ResourceType"></a>
 The type of AWS resource the rule applies to.   
Type: String  
Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function | AWS::CloudTrail | AWS::EKS::Cluster | AWS::WAFv2::WebACL | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::Route53Resolver::ResolverEndpoint | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Browser | AWS::BedrockAgentCore::CodeInterpreter | AWS::BedrockAgentCore::Gateway | AWS::BedrockAgentCore::Memory | AWS::BedrockAgentCore::WorkloadIdentity | AWS::SecurityHub::Hub | AWS::CloudFront::Distribution | AWS::SecurityHub::HubV2 | AWS::CloudWatch::OTelEnrichment | AWS::MSK::Cluster | AWS::S3::Bucket | AWS::Bedrock::KnowledgeBase`   
Required: No

 ** RuleArn **   <a name="cwoa-Type-TelemetryRuleSummary-RuleArn"></a>
 The Amazon Resource Name (ARN) of the telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

 ** RuleName **   <a name="cwoa-Type-TelemetryRuleSummary-RuleName"></a>
 The name of the telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z-_.#/]+`   
Required: No

 ** TelemetrySourceTypes **   <a name="cwoa-Type-TelemetryRuleSummary-TelemetrySourceTypes"></a>
 The types of telemetry sources configured for this rule, such as VPC Flow Logs or EKS audit logs. TelemetrySourceTypes must be correlated with the specific resource type.   
Type: Array of strings  
Valid Values: `VPC_FLOW_LOGS | ROUTE53_RESOLVER_QUERY_LOGS | EKS_AUDIT_LOGS | EKS_AUTHENTICATOR_LOGS | EKS_CONTROLLER_MANAGER_LOGS | EKS_SCHEDULER_LOGS | EKS_API_LOGS`   
Required: No

 ** TelemetryType **   <a name="cwoa-Type-TelemetryRuleSummary-TelemetryType"></a>
 The type of telemetry (Logs, Metrics, or Traces) the rule configures.   
Type: String  
Valid Values: `Logs | Metrics | Traces`   
Required: No

## See Also
<a name="API_TelemetryRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRuleSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRuleSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRuleSummary) 