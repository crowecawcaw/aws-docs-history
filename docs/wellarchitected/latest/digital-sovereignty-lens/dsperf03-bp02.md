# DSPERF03-BP02 Implement continuous network verification

In highly regulated industries, maintaining integrity of network
infrastructure configurations through comprehensive verification
processes is crucial for security, compliance, and operational
stability.

Customers should implement proactive controls to verify your
networking components meet security standards and maintain
compliance. Compromised or misconfigured networks can lead to data
breaches, regulatory violations, and significant business
disruption.

**Desired outcome:** Network
infrastructure maintains verified security, integrity, and
compliance status throughout its lifecycle with automated detection
of unauthorized configuration changes.

**Common anti-patterns:**

- Relying on manual, infrequent checks instead of automated
  processes for configuration drift and unauthorized changes.
- Using default configurations, overly permissive rules, and
  insufficient network segmentation without zero-trust principles.
- Lacking traffic analysis, anomaly detection, and proper
  integration with SIEM systems.
- Missing network topology documentation, configuration baselines,
  and verification of third-party connections.
- Ignoring firmware and software updates and failing to validate
  encryption for data in transit across network segments.

**Benefits of establishing this best
practice:**

- Continuous validation of network configurations, real-time
  threat detection, and automated auditing to meet regulatory
  standards.
- Early identification and remediation of configuration drift,
  improving incident response capabilities.
- Automated verification processes reduce manual overhead and
  identify unused or misconfigured resources.
- Improved change control, comprehensive network visibility, and
  automated response to security events.
- Consistent application of security policies across hybrid
  environments, enhancing overall security posture.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Develop a comprehensive network infrastructure verification
strategy.

Key implementation elements:

- Establish configuration baselines and automated drift
  detection for network components
- Implement real-time monitoring, logging, and analysis of
  network traffic
- Deploy automated compliance checking and remediation processes
- Configure network segmentation using VPCs, security groups,
  and network access control lists (NACL) with least-privilege
  access
- Enable continuous threat detection and incident response
  capabilities
- Encrypt and validate network traffic

This approach provides continuous verification of network
integrity while adhering to security and regulatory requirements.

### Implementation steps

1. Define network resource rules using
   [AWS Config](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") and enable continuous recording. Consider
   developing your own custom rules using AWS CloudFormation
   guard rules or Lambda functions.
2. Set up AWS Config Rules for automated drift detection and
   send
   [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") alerts.
3. Implement real-time monitoring and traffic analysis by
   enabling
   [Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") for VPCs and subnets, configure
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") for metrics, and use
   [Amazon
   Detective](../../../detective/latest/adminguide/what-is-detective.md "../../../detective/latest/adminguide/what-is-detective.md") for traffic analysis with
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") providing a unified security view.
4. Configure network segmentation and security controls by
   designing proper
   [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") architecture with separate environments,
   implement least-privilege
   [Security
   Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and
   [NACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md"),
   and deploy
   [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md") for stateful inspection.
5. Enable threat detection and incident response by
   implementing
   [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") across each region for threat detection,
   configure
   [AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/what-is-incident-manager.md "../../../incident-manager/latest/userguide/what-is-incident-manager.md") for response
   coordination, and use
   [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") for automated remediation actions.
6. Establish traffic encryption and validation using
   [Site-to-Site VPN](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/") for external connections, implement
   [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") for service connections, configure
   [TLS](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md")
   for applications, and deploy
   [AWS WAF (Web Application Firewall)](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md") for application layer
   protection.
7. Implement continuous auditing and reporting by setting up
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") with integrity validation across regions,
   use
   [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") for log analysis, create dashboards with
   [Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md"), and manage access control through
   [AWS IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and
   [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

## Resources

**Related best practices:**

- [PERF04-BP02
  Evaluate available networking features](../performance-efficiency-pillar/perf_networking_evaluate_networking_features.md "../performance-efficiency-pillar/perf_networking_evaluate_networking_features.md")
- [PERF04-BP07
  Optimize network configuration based on metrics](../performance-efficiency-pillar/perf_networking_optimize_network_configuration_based_on_metrics.md "../performance-efficiency-pillar/perf_networking_optimize_network_configuration_based_on_metrics.md")
- [SEC05-BP04
  Automate network protection](../security-pillar/sec_network_auto_protect.md "../security-pillar/sec_network_auto_protect.md")

**Related documents:**

- [Detect
  drift on individual stack resources](../../../AWSCloudFormation/latest/UserGuide/detect-drift-resource.md "../../../AWSCloudFormation/latest/UserGuide/detect-drift-resource.md")
- [Detect
  drift on an entire CloudFormation stack](../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md "../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md")
- [Set
  up AWS CloudFormation drift detection in a multi-Region,
  multi-account organization](../../../prescriptive-guidance/latest/patterns/set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization.md "../../../prescriptive-guidance/latest/patterns/set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization.md")
- [Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")

**Related videos:**

- [AWS re:Inforce 2025 - Securing AWS networks: Observability meets
  defense-in-depth (NIS306)](https://www.youtube.com/watch?v=J5RwvzaQgvo "https://www.youtube.com/watch?v=J5RwvzaQgvo")
- [AWS re:Invent 2022 Dive deep on AWS networking infrastructure
  (NET402)](https://www.youtube.com/watch?v=HJNR_dX8g8c "https://www.youtube.com/watch?v=HJNR_dX8g8c")

**Related services:**

- [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon
  Detective](https://aws.amazon.com/detective/ "https://aws.amazon.com/detective/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Systems Manager Incident Manager](https://aws.amazon.com/systems-manager/incident-manager/ "https://aws.amazon.com/systems-manager/incident-manager/")
- [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/")
- [Site-to-Site VPN](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/")
