

# FND05-BP07 Implement threat detection mechanisms

 As security risks continue to evolve, establish detection mechanisms that identify security issues, misconfigurations, and unexpected activity in your environment so you can respond quickly. 

 **Desired outcome:** 
+  You have implemented full threat detection capabilities that combine both behavioral and rule-based detection methods. 
+  You can monitor your environment across your cloud resources, workloads, and services. 
+  You have established mechanisms to correlate security events from multiple sources to provide context and reduce alert fatigue. 
+  You generate useful, prioritized alerts based on severity and business impact, so your security teams can respond to threats. 

 **Common anti-patterns:** 
+  Relying solely on basic logging without correlation or analysis. 
+  Using only rule-based detection without behavioral analysis. 
+  Implementing detection tools without proper alert prioritization. 
+  Not considering context when evaluating security alerts. 
+  Deploying detection services without understanding the alerts they produce or assigning owners for response. 

 **Benefits of establishing this best practice:** 
+  Detection mechanisms identify unauthorized access and identity misuse, and verify that security-relevant activities are monitored consistently. 
+  Multi-layered detection mechanisms protect across different security boundaries and provide important components of security telemetry. 
+  Behavioral and rule-based detection together provide broad security visibility and help identify anomalous resource behavior. 
+  Automated detection provides consistent security monitoring and simplifies security operations. 
+  Detection mechanisms help identify potential unintended data disclosure and are fundamental components of effective incident response capabilities. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Before cloud computing, organizations struggled with limited visibility across their infrastructure and siloed security tools. Cloud services now provide integrated security capabilities and the ability to centralize threat detection across the environment. 

 Threat detection combines behavioral analysis and rule-based detection. Behavioral detection uses machine learning and statistical analysis to identify anomalies. Anomalous activity deviates from normal patterns and might indicate a novel attack or insider threat. Rule-based detection identifies known-bad patterns based on signatures, compliance rules, or threat intelligence. Behavioral detection can miss attacks that appear normal, and rule-based detection cannot catch unknown threats. 

 AWS provides services for threat detection: 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) delivers behavioral threat detection using machine learning. 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) runs continual checks against AWS-recommended and industry security standards and consolidates findings from across your AWS accounts and third-party products. 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) is a unified cloud security solution that correlates and enriches signals from Security Hub CSPM, GuardDuty, Inspector, and Macie to generate exposure findings that prioritize the most critical risks. 
+  [Amazon Detective](https://aws.amazon.com/detective/) provides investigation capabilities that correlate data from multiple sources. 
+  [Amazon Macie](https://aws.amazon.com/macie/) identifies sensitive data exposure. 

 AWS [recommends enabling both Security Hub CSPM and Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html). Security Hub CSPM produces standards-based posture findings, and Security Hub CSPM correlates them with other detection signals into prioritized exposure findings. Using these services helps you establish a defense-in-depth detection strategy. 

 Alert correlation is critical for avoiding alarm fatigue and overwhelm. AWS Security Hub CSPM correlates findings across AWS security services automatically and produces exposure findings that identify the most critical risks. Tools like [Amazon Detective](https://aws.amazon.com/detective/), SIEM solutions integrated with [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/), or [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) extend correlation across a broader set of log sources. Prioritize by both severity and context. A critical finding in a production workload with sensitive data is more urgent than the same finding in a sandbox. Your organization's maturity should determine how you accomplish this: 
+  Early-stage organizations get the most value from enabling the core services ([GuardDuty](https://aws.amazon.com/guardduty/) and [Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) with their default detections), which provide immediate signal with minimal configuration. 
+  Maturing organizations enable [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) alongside Security Hub CSPM to correlate CSPM findings with Inspector, Macie, and GuardDuty signals into exposure findings. They expand into sensitive-data discovery with [Amazon Macie](https://aws.amazon.com/macie/), container runtime protection, and custom rules tuned to their threat model. 
+  Advanced organizations integrate cloud-based detection with existing SIEM tools to correlate cloud events with on-premises signals across hybrid environments. Whichever stage you are at, decide who receives alerts, who investigates them, and what the response SLAs are before you scale up signal volume. Detection capabilities are most effective when paired with dedicated investigation tooling and workflows. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy comprehensive monitoring across the environment:** Implement logging and monitoring to capture security-relevant events across your entire cloud environment. Configure [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) for API activity logging, [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) for network traffic monitoring, and [AWS Config](https://aws.amazon.com/config/) for resource configuration tracking. Centralize logs in a dedicated security account using [Amazon S3](https://aws.amazon.com/s3/) and bring them into [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/), the destination for operational, security, and compliance telemetry, using [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html). 

1.  **Combine behavioral with rule-based detection methods:** Enable [Amazon GuardDuty](https://aws.amazon.com/guardduty/) for behavioral threat detection using machine learning. See [Getting started with Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html). Complement with rule-based detection using [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) and [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) security standards. Enable [Amazon Macie](https://aws.amazon.com/macie/) to discover and classify sensitive data. For more detail, see [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html). 

1.  **Set up alert correlation capabilities:** Implement alert correlation to reduce false positives and provide context. Enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) so findings from Security Hub CSPM, GuardDuty, Inspector, and Macie are automatically correlated into exposure findings that prioritize the most critical risks. Use [Amazon Detective](https://aws.amazon.com/detective/) for graph-based investigation of log data from multiple sources. For more detail, see [Getting started with Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/). For cross-domain correlation that includes on-premises or third-party signals, integrate a SIEM solution with [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) or [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/). 

1.  **Define an alert prioritization framework:** Establish a framework for prioritizing security alerts based on severity, business impact, and asset criticality, and encode that framework in tooling rather than leaving it in documentation. Use [AWS Security Hub CSPM severity labels](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-required-attributes.html#Severity) to standardize finding severity across services, apply workload criticality tags so the prioritization engine can weight findings against the resources they affect, and configure [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules to route high-priority alerts to on-call systems and lower-priority findings to standard queues. See [Automated response and remediation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html). Document the routing as part of your incident response runbooks and test it regularly so routing failures do not surface during an incident. 

1.  **Enable automated security services:** Enable [Amazon GuardDuty](https://aws.amazon.com/guardduty/) across all accounts and Regions, including optional features like [S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html), [EKS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html), and [RDS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html). Enable [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) to run continual checks against security standards and consolidate findings from GuardDuty, [Amazon Inspector](https://aws.amazon.com/inspector/), [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/), and other services. For more detail, see [Enabling Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html). AWS [recommends enabling both Security Hub CSPM and Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html), so enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) as well. Security Hub CSPM findings are routed to Security Hub CSPM automatically, where they're correlated with findings from Inspector, Macie, and GuardDuty to generate exposure findings. Integrate with third-party security tools using [Security Hub CSPM integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md) 
+  [FND05-BP09 Establish security tooling for investigating incidents](fnd05-bp09.md) 
+  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md) 
+  [SEC01-BP07 Evaluate and implement new security services and features regularly](sec01-bp07.md) 
+  [SEC05-BP03 Implement inspection-based protection](sec05-bp03.md) 

 **Related documents:** 
+  [Security OU - Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) 
+  [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/) 
+  [Navigating Amazon GuardDuty protection plans and Extended Threat Detection](https://aws.amazon.com/blogs/security/navigating-amazon-guardduty-protection-plans-and-extended-threat-detection/) 
+  [What are Security Hub CSPM and Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) 
+  [Introduction to AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [Introduction to AWS Security Hub CSPM (unified experience)](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Threat detection and incident response with AWS security services (SEC326)](https://www.youtube.com/watch?v=K3fB8bpmVUU) 

 **Related examples:** 
+  [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) 
+  [Security Analytics for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-analytics.html) 
+  [Automate incident response and forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html) 
+  [Use Amazon GuardDuty to detect anomalous behavior](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/) 
+  [Automatically block suspicious traffic with AWS Network Firewall and Amazon GuardDuty](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/) 

 **Related workshops:** 
+  [AWS Security Hub CSPM Workshop](https://catalog.workshops.aws/security-hub/en-US) 

 **Related services:** 
+  [Detection and Response on AWS](https://aws.amazon.com/products/security/detection-and-response/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) 
+  [Amazon Detective](https://aws.amazon.com/detective/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 
+  [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) 