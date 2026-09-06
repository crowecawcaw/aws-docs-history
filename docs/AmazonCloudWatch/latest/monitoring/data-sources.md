

# Supported data sources for CloudWatch
<a name="data-sources"></a>

CloudWatch collects and processes telemetry data from a wide range of sources to provide unified observability and security insights. Data sources fall into four categories: AWS native services, third-party platforms, custom sources, and CloudWatch Metrics (OTel).

You can automate the enablement of AWS data sources using telemetry configuration. For more information, see [Telemetry discovery and enablement](telemetry-config-cloudwatch.md).

## AWS service data sources
<a name="data-sources-aws-services"></a>

CloudWatch provides native integration with 90\+ AWS services for automatic data collection. When an AWS service source is selected, CloudWatch pipelines intercepts logs ingested into CloudWatch Logs for processing. To get started, enable logging for the supported AWS services using the service's console, then select the data source and type in the CloudWatch pipelines creation wizard.

The following table highlights key AWS service data sources. For the complete list of 90\+ supported services, see [Supported AWS services for data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/supported-aws-services-data-sources.html).


| AWS service | Data type | Description | 
| --- | --- | --- | 
| Amazon Amazon VPC | Flow Logs | Network traffic metadata for Amazon VPCs, subnets, and network interfaces | 
| Amazon Amazon EKS | Control Plane Logs | Kubernetes API server, audit, authenticator, controller manager, and scheduler logs | 
| AWS WAF | Web ACL Logs | Web request inspection logs including rule match details and actions taken | 
| Amazon Route 53 | Resolver Query Logs | DNS query logs for Amazon VPC resources routed through Route 53 Resolver | 
| CloudTrail | Management and Data Events | API activity and resource-level operations across AWS services | 
| Amazon Amazon EC2 | Detailed Metrics | Instance-level performance metrics at 1-minute granularity | 
| AWS Security Hub | CSPM Findings | Cloud security posture management findings from AWS and third-party providers | 
| Amazon Bedrock AgentCore | Runtime, Browser, CodeInterpreter, Gateway, Memory | Agent runtime execution, browser interaction, code execution, gateway, and memory operation logs | 
| Amazon CloudFront | Distribution Logs | CDN access logs for content delivery distributions | 
| Network Load Balancer | Access Logs | Network Load Balancer connection and TLS negotiation logs | 
| Amazon RDS | Aurora MySQL and Aurora PostgreSQL Logs | Audit, error, general, slow query, IAM DB authentication error, proxy, and enhanced monitoring logs | 

For more information about CloudWatch Logs data sources, see [Data source discovery and management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-source-discovery-management.html).

## Third-party data sources
<a name="data-sources-third-party"></a>

CloudWatch extends monitoring capabilities beyond AWS with direct integrations for 38 third-party security, identity, and endpoint platforms. These integrations consolidate security events, audit logs, and telemetry data from external sources into CloudWatch Logs for unified analysis.

The following table lists the supported direct third-party integrations:


| Source | Integration pattern | Category | 
| --- | --- | --- | 
| Akamai DataStream 2 | S3 Delivery | CDN and edge security | 
| Check Point NGFW | S3 Delivery | Network security | 
| Cisco Duo | API | Identity and access management | 
| Cisco Meraki | API | Network security | 
| Cisco Umbrella | S3 Delivery | DNS and network security | 
| CrowdStrike Falcon | S3 Delivery | Endpoint security | 
| Drupal Core | API | Content management | 
| Entrust IDaaS | API | Identity and access management | 
| F5 BIG-IP | S3 Delivery | Network security | 
| GitHub | API | Source code and audit logs | 
| GitLab | API | DevSecOps and source code | 
| HashiCorp Vault | S3 Delivery | Secrets management | 
| Jamf Protect | S3 Delivery | Endpoint security | 
| Microsoft Entra ID | API | Identity and access management | 
| Microsoft Office 365 | API | Productivity and audit logs | 
| Microsoft Windows Event Logs | API | Operating system events | 
| Netskope | API | Network security and CASB | 
| Okta Auth0 | API | Identity and access management | 
| Okta SSO | API | Identity and access management | 
| OneLogin Identity | API | Identity and access management | 
| Palo Alto Networks NGFW | API | Network security | 
| Palo Alto Prisma Cloud | API | Cloud security | 
| PingIdentity PingAccess | S3 Delivery | Access management | 
| PingIdentity PingFederate | S3 Delivery | Identity federation | 
| PingIdentity PingOne | API | Identity and access management | 
| Proofpoint TAP | API | Email security | 
| Slack Audit Log | API | Collaboration and audit logs | 
| SentinelOne | S3 Delivery | Endpoint security | 
| ServiceNow CMDB | API | IT service management | 
| Tanium Endpoint Management | S3 Delivery | Endpoint security and management | 
| Tenable Vulnerability Management | API | Vulnerability management | 
| Wazuh Platform | API | Security monitoring and threat detection | 
| Box | API | Content management and file sharing | 
| Jamf Pro | API | Device management (Apple) | 
| Broadcom Carbon Black | S3 Delivery | Endpoint detection and response | 
| Wiz CNAPP | API | Cloud security | 
| Zeek | S3 Delivery | Network security monitoring | 
| Zscaler ZIA/ZPA | S3 Delivery | Network security | 

For detailed setup procedures, prerequisites, and configuration steps for each integration, see [Third-party data sources integration](third-party-integration-setup.md).

**Additional third-party sources through Security Hub CSPM**  
Beyond the 34 direct integrations, 49\+ additional third-party sources are available through AWS Security Hub CSPM integration. Security Hub CSPM partner providers that send findings to Security Hub are automatically available as data sources. For the full list of supported partners, see the [Security Hub CSPM partner providers](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) documentation.

**Additional third-party sources through Security Hub**  
AWS Security Hub (distinct from Security Hub CSPM) provides its own set of third-party integrations. These integrations that send findings to Security Hub are automatically available as data sources. For the full list of supported integrations, see the [Security Hub third-party integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-integrations.html) documentation.

## Custom data sources
<a name="data-sources-custom"></a>

For logs that are not covered by AWS service or third-party integrations, CloudWatch pipelines can process custom logs stored in CloudWatch Logs or Amazon S3 buckets. Custom sources accommodate unique organizational requirements:
+ **Application-specific logs** – Custom application telemetry from Amazon EC2 instances with specialized logging formats
+ **File-based ingestion** – Amazon S3-based log files from legacy systems or batch processing workflows
+ **Serverless integration** – Lambda function logs and custom serverless application telemetry

For more details, see [Custom log data from CloudWatch Logs or an Amazon S3 bucket](ingestion-custom-data-sources.md).

## CloudWatch Metrics (OTel) source
<a name="data-sources-metrics-otel"></a>

The CloudWatch Metrics (OTel) source processes OpenTelemetry (OTel) metrics on the OTLP ingestion path based on selection criteria. This source enables you to transform metrics data through CloudWatch pipelines before the metrics are persisted in CloudWatch Metrics.

The following metric types are supported:
+ **Custom OTel metrics** – Metrics that your applications emit through OpenTelemetry instrumentation and send to the OTLP endpoint
+ **AWS vended OTel metrics** – Metrics that AWS services emit through OTLP

**Note**  
The CloudWatch Metrics (OTel) source only supports metrics ingested through the OTLP endpoint. Metrics sent through other ingestion paths, such as the `PutMetricData` API, are not processed by this source.

You define which metrics to process by configuring metrics pipeline selection criteria. Selection criteria let you target specific metrics based on OTel attributes such as resource attributes, metric name, and datapoint attributes. For more information, see [CloudWatch Metrics (OTel)](metrics-pipeline-selection-criteria.md).

For information about sending OTel metrics to CloudWatch, see [Using OpenTelemetry with CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html).

**Topics**
+ [AWS service data sources](#data-sources-aws-services)
+ [Third-party data sources](#data-sources-third-party)
+ [Custom data sources](#data-sources-custom)
+ [CloudWatch Metrics (OTel) source](#data-sources-metrics-otel)
+ [CloudWatch Metrics (OTel)](metrics-pipeline-selection-criteria.md)
+ [Third-party data sources integration](third-party-integration-setup.md)
+ [Custom log data from CloudWatch Logs or an Amazon S3 bucket](ingestion-custom-data-sources.md)
+ [AWS service logs from CloudWatch Logs](aws-service-logs-from-cwl.md)