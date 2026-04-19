# AWS service data sources

CloudWatch provides native integration with 90+ AWS services for automatic data
collection. When an AWS service source is selected, CloudWatch pipelines intercepts logs ingested
into CloudWatch Logs for processing. To get started, enable logging for the supported AWS
services using the service's console, then select the data source and type in the
CloudWatch pipelines creation wizard.

The following table highlights key AWS service data sources. For the complete
list of 90+ supported services, see [Supported AWS services for data sources](../logs/supported-aws-services-data-sources.md "../logs/supported-aws-services-data-sources.md").

| Key AWS service data sources | AWS service                                        | Data type                                                                                           | Description |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------- |
| Amazon Amazon VPC            | Flow Logs                                          | Network traffic metadata for Amazon VPCs, subnets, and network<br>interfaces                        |
| Amazon Amazon EKS            | Control Plane Logs                                 | Kubernetes API server, audit, authenticator, controller manager,<br>and scheduler logs              |
| AWS WAF                      | Web ACL Logs                                       | Web request inspection logs including rule match details and<br>actions taken                       |
| Amazon Route 53              | Resolver Query Logs                                | DNS query logs for Amazon VPC resources routed through Route 53<br>Resolver                         |
| CloudTrail                   | Management and Data Events                         | API activity and resource-level operations across AWS<br>services                                   |
| Amazon Amazon EC2            | Detailed Metrics                                   | Instance-level performance metrics at 1-minute granularity                                          |
| AWS Security Hub             | CSPM Findings                                      | Cloud security posture management findings from AWS and<br>third-party providers                    |
| Amazon Bedrock AgentCore     | Runtime, Browser, CodeInterpreter, Gateway, Memory | Agent runtime execution, browser interaction, code execution,<br>gateway, and memory operation logs |
| Amazon CloudFront            | Distribution Logs                                  | CDN access logs for content delivery distributions                                                  |
| Network Load Balancer        | Access Logs                                        | Network Load Balancer connection and TLS negotiation logs                                           |

For more information about CloudWatch Logs data sources, see [Data
source discovery and management](../logs/data-source-discovery-management.md "../logs/data-source-discovery-management.md").
