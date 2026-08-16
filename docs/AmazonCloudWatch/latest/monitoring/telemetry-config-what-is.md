# What is telemetry discovery and enablement?

CloudWatch telemetry configuration gives you two core capabilities:

- **Discovery and auditing** – Discover AWS
  resources across your account or organization and audit which resources have telemetry
  enabled. The experience shows the configuration status at the resource-type level and at
  more granular telemetry-detail levels.
- **Enablement rules** – Create rules that
  automatically configure telemetry collection for AWS resources that match your criteria.
  Rules help you standardize telemetry collection across your organization or accounts and
  make sure consistent monitoring coverage.
  Telemetry configuration supports the following data sources:

- Amazon Amazon VPC Flow Logs
- Amazon EKS Control Plane Logs
- AWS WAF Logs
- Amazon Route 53 Resolver Query Logs
- NLB Access Logs
- AWS CloudTrail Data Events and Management Events
- Amazon Bedrock AgentCore Logs
- Amazon Amazon EC2 Detailed Metrics
- AWS Security Hub
- Amazon Bedrock Agentcore Gateway
- Amazon Bedrock Agentcore Memory
- Amazon CloudFront Distribution
- Amazon S3 Server Access Logs
- Amazon MSK Cluster Metrics
- OpenTelemetry Enrichment Metrics
- Amazon Bedrock Agentcore Workload Identity
- Elastic Load Balancing Application Load Balancer Logs
- Amazon Bedrock Knowledge Base Logs
  When you enable telemetry configuration, CloudWatch creates AWS Config
  service-linked configuration recorders that discover resources and their associated telemetry
  configuration metadata. For more information, see [Configuration
  Recorder](../../../config/latest/developerguide/config-concepts.md#config-recorder "../../../config/latest/developerguide/config-concepts.md#config-recorder") in the AWS Config Developer Guide.

###### Note

AWS Config periodically takes inventory of, or discovers, all the
resources in your account as an anti-entropy behavior, regardless of the resource types in
scope for your configuration recorders. The inventory includes deleted resources and
resources that AWS Config is not currently recording. This behavior helps
maintain data consistency.

This means that although the service-linked configuration recorder for the CloudWatch
telemetry configuration feature is configured to record specific resource types, you might
see describe calls from `ConfigResourceCompositionSession` and
`AWSConfig-Describe` in AWS CloudTrail. For more information, see [Non-recorded Resources](../../../config/latest/developerguide/select-resources.md#select-resources-non-recorded "../../../config/latest/developerguide/select-resources.md#select-resources-non-recorded") in the AWS Config Developer Guide.

Amazon CloudWatch uses AWS Config Internal service linked recorder.
You are not charged for CIs that CloudWatch uses as part of the Internal Service Linked Recorders.

You can manage telemetry configuration across multiple AWS Regions from a single
Region. When you enable multi-Region support, the current Region becomes your home Region
and telemetry configuration is replicated to the Regions you select. For more information,
see [Setting up telemetry configuration](telemetry-config-turn-on.md "telemetry-config-turn-on.md").
