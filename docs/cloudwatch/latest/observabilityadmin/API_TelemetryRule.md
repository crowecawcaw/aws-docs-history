

# TelemetryRule
<a name="API_TelemetryRule"></a>

 Defines how telemetry should be configured for specific AWS resources. 

## Contents
<a name="API_TelemetryRule_Contents"></a>

 ** TelemetryType **   <a name="cwoa-Type-TelemetryRule-TelemetryType"></a>
 The type of telemetry to collect (Logs, Metrics, or Traces).   
Type: String  
Valid Values: `Logs | Metrics | Traces`   
Required: Yes

 ** AllowFieldUpdates **   <a name="cwoa-Type-TelemetryRule-AllowFieldUpdates"></a>
 If set to `true`, Amazon CloudWatch Observability Admin detects and remediates configuration drift in telemetry resources that it manages. For example, if a VPC flow log's format, traffic type, or aggregation interval no longer matches the rule's destination configuration, the flow log is replaced with one that matches. Only Observability Admin-managed resources are updated; customer-created resources are never modified. Currently supported for `AWS::EC2::VPC` resources (VPC flow logs).   
Type: Boolean  
Required: No

 ** AllRegions **   <a name="cwoa-Type-TelemetryRule-AllRegions"></a>
 If set to `true`, the telemetry rule is replicated to all AWS Regions where Amazon CloudWatch Observability Admin is available in the current partition. When new regions become available, the rule automatically replicates to them. Mutually exclusive with `Regions`.   
Type: Boolean  
Required: No

 ** DestinationConfiguration **   <a name="cwoa-Type-TelemetryRule-DestinationConfiguration"></a>
 Configuration specifying where and how the telemetry data should be delivered.   
Type: [TelemetryDestinationConfiguration](API_TelemetryDestinationConfiguration.md) object  
Required: No

 ** Regions **   <a name="cwoa-Type-TelemetryRule-Regions"></a>
 An optional list of AWS Regions where this telemetry rule should be replicated. When specified, the rule is created in the home region and automatically replicated to all listed regions. Mutually exclusive with `AllRegions`.   
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1.  
Required: No

 ** ResourceType **   <a name="cwoa-Type-TelemetryRule-ResourceType"></a>
 The type of AWS resource to configure telemetry for (for example, `AWS::EC2::VPC`, `AWS::EKS::Cluster`, `AWS::ElasticLoadBalancingV2::LoadBalancer`, or `AWS::Bedrock::KnowledgeBase`).   
Type: String  
Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function | AWS::CloudTrail | AWS::EKS::Cluster | AWS::WAFv2::WebACL | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::Route53Resolver::ResolverEndpoint | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Browser | AWS::BedrockAgentCore::CodeInterpreter | AWS::BedrockAgentCore::Gateway | AWS::BedrockAgentCore::Memory | AWS::BedrockAgentCore::WorkloadIdentity | AWS::SecurityHub::Hub | AWS::CloudFront::Distribution | AWS::SecurityHub::HubV2 | AWS::CloudWatch::OTelEnrichment | AWS::MSK::Cluster | AWS::S3::Bucket | AWS::Bedrock::KnowledgeBase`   
Required: No

 ** Scope **   <a name="cwoa-Type-TelemetryRule-Scope"></a>
 The organizational scope to which the rule applies, specified using accounts or organizational units.   
Type: String  
Required: No

 ** SelectionCriteria **   <a name="cwoa-Type-TelemetryRule-SelectionCriteria"></a>
 Criteria for selecting which resources the rule applies to, such as resource tags.   
Type: String  
Required: No

 ** TelemetrySourceTypes **   <a name="cwoa-Type-TelemetryRule-TelemetrySourceTypes"></a>
 The specific telemetry source types to configure for the resource, such as VPC\_FLOW\_LOGS or EKS\_AUDIT\_LOGS. TelemetrySourceTypes must be correlated with the specific resource type.   
Type: Array of strings  
Valid Values: `VPC_FLOW_LOGS | ROUTE53_RESOLVER_QUERY_LOGS | EKS_AUDIT_LOGS | EKS_AUTHENTICATOR_LOGS | EKS_CONTROLLER_MANAGER_LOGS | EKS_SCHEDULER_LOGS | EKS_API_LOGS`   
Required: No

## See Also
<a name="API_TelemetryRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRule) 