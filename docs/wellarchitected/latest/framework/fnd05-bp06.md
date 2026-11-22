

# FND05-BP06 Remediate non-compliant resources

 Verify that all resources in your cloud environment comply with your organization's policies and standards to maintain a secure and efficient infrastructure. When you identify non-compliant resources, remediate them. 

 **Desired outcome:** 
+  You have defined resource configuration standards along with the steps to remediate when resources are detected to be non-compliant. 
+  You have defined remediations programmatically so they can be initiated either manually or through automation where possible. 
+  Your detection systems are in place to identify non-compliant resources and publish alerts into centralized tools that are monitored by your security personnel. 
+  Your tools support running programmatic remediations, either manually or automatically. 
+  Your automatic remediations have appropriate oversight and control mechanisms in place to govern their use. 

 **Common anti-patterns:** 
+  Implementing automation without testing and validating remediation actions, which can result in unintended consequences such as disrupting legitimate business operations or causing system instability. 
+  Automating remediation actions without proper monitoring and mechanisms that permit human intervention and judgment when needed. 
+  Relying solely on remediations rather than having remediations as one part of a broader incident response and recovery program. 

 **Benefits of establishing this best practice:** 
+  Automatic remediations can respond to misconfigurations faster than manual processes, reducing business impact and shrinking the window of opportunity for unintended uses. 
+  Programmatically defined remediations are applied consistently, reducing human error. 
+  Automation handles larger volumes of alerts at the same time, which matters most at scale. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Without a systematic remediation process, misconfigurations persist, which expands the window for unintended access or data exposure. Effective remediation of non-compliant resources combines automated detection with automated and manual response: fast correction for common misconfigurations, human judgment for ambiguous situations. Many violations follow predictable patterns, such as a misconfigured security group, an unencrypted volume, a missing log configuration, or an improperly tagged resource. 

 Manual remediation applies fixes inconsistently and scales poorly. Programmatic remediation codifies your response patterns so automated correction handles well-understood violations and structured manual workflows handle cases where human review adds value. 

 [AWS Config](https://aws.amazon.com/config/) continuously evaluates resource configurations against your defined rules and detects non-compliant resources in near real time. Findings flow into a cloud security posture management (CSPM) solution like [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) so security investigators have a central place to monitor, triage, and act. Security Hub CSPM findings are routed automatically to [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html), which correlates them with signals from [Amazon GuardDuty](https://aws.amazon.com/guardduty/), [Amazon Inspector](https://aws.amazon.com/inspector/), and [Amazon Macie](https://aws.amazon.com/macie/) to generate exposure findings that prioritize the most critical risks. AWS [recommends enabling both Security Hub CSPM and Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) so the two services complement each other. Low-risk, well-tested remediations (such as removing a known-bad security group rule or turning on S3 bucket versioning) can execute automatically and cut exposure time from hours to minutes. Higher-risk actions that could affect production deserve a human review gate. AWS Config supports [automated remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) through Systems Manager Automation, and Security Hub CSPM [custom actions](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-custom-actions.html) publish finding details to [Amazon EventBridge](https://aws.amazon.com/eventbridge/) so EventBridge rules can trigger automatic or manually approved workflows. 

 Treat remediations as executable code. Version control, non-production testing, and detailed execution logging produce the audit trail that a security team can defend: what was changed, when, by which actor, and the outcome. [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/) provides durable storage, and Security Hub CSPM's [finding notes](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html#finding-update-batchupdatefindings-note) capture outcomes in the context of the original finding. A conservative rollout (a small set of well-understood remediations in manual-approval mode) builds confidence before broader automatic execution. [Automated Security Response on AWS](https://docs.aws.amazon.com/solutions/automated-security-response-on-aws/) provides pre-built playbooks for common findings and is a reasonable starting point. 

 Align high-impact automated remediations with existing change management practices to reduce the risk of self-inflicted incidents. These include change advisory board review for enterprise environments, blackout periods during releases or peak business hours, and rollback procedures for problematic changes. Notify resource owners and affected teams before and after remediation actions. 

**Important**  
 Automatic remediation can cause unintended disruption if not tested. Validate remediations in non-production environments before turning on automatic execution in production, and implement emergency stop mechanisms to disable problematic remediations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish centralized detection and alerting for non-compliant resources:** Configure detective controls to send alerts to a central security monitoring solution. Consolidate findings from [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and other security services into a single dashboard. Security Hub CSPM provides [integrations with multiple AWS services](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html), and its findings are routed automatically to [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html), where they're correlated with GuardDuty, Inspector, and Macie findings to generate exposure findings. Configure [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) topics to route alerts to security and operations teams for high-severity findings. 

1.  **Prioritize findings based on risk and impact:** Develop a prioritization framework considering severity, potential business impact, and required effort to remediate. Use [AWS Security Hub CSPM severity labels](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-required-attributes.html#Severity) to categorize findings. Use [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) to organize related compliance rules (such as PCI-DSS or CIS benchmarks) and understand your compliance posture across multiple requirements simultaneously. 

1.  **Define programmatic remediations for common violations:** For each type of non-compliance you encounter repeatedly, document the standard remediation and implement it as code. Use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runbooks. Many [pre-built automation runbooks](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.html) cover common scenarios. For custom remediations, implement them using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions. Store remediation code in version control and treat it with the same rigor as application code: testing, peer review, and deployment pipelines. 

1.  **Connect detection to remediation workflows:** Link your centralized monitoring to your remediation automation. For AWS Config rules, configure [automatic remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) directly in the rule settings. For Security Hub CSPM findings, create [custom actions](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-custom-actions.html) for manual triggers, or configure [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) for automatic invocation. Start with manual approval workflows for new remediations until behavior is validated. 

1.  **Establish rollback and recovery procedures:** For each programmatic remediation, document and test a rollback path before turning it on in production. Capture pre-remediation state with [AWS Backup](https://aws.amazon.com/backup/) for resources where backups are appropriate, or store configuration snapshots in [Amazon S3](https://aws.amazon.com/s3/) so changes can be reversed if remediation causes unintended impact. Use [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html) to suppress automatic remediations during blackout windows, release freezes, and approved maintenance periods. Communicate remediation actions to resource owners and affected teams using [Amazon SNS](https://aws.amazon.com/sns/) or [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) so teams are not surprised by changes to resources they operate. 

1.  **Implement comprehensive logging and audit trails:** Configure every remediation execution to generate detailed logs capturing what was changed, when, who or what initiated it, and the outcome. Send logs to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). Use Security Hub CSPM's [BatchUpdateFindings API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) to add [finding notes](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html#finding-update-batchupdatefindings-note) documenting remediation actions in the context of the original finding. 

1.  **Verify remediation effectiveness and compliance:** After executing remediations, verify that non-compliant resources have been corrected. Configure AWS Config to [re-evaluate rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) after remediation. Monitor [Security Hub CSPM compliance standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-view-manage.html) to track compliance posture over time and identify persistent violations indicating deeper issues requiring architectural changes. 

1.  **Measure program effectiveness and continuously improve:** Track key performance indicators including Mean Time to Remediate (MTTR), remediation success rate, and false positive rate so program effectiveness is measurable. Maintain a knowledge base that documents remediation patterns, challenges encountered during deployment, and refinements made over time. After significant incidents or launching new remediations, conduct structured reviews to identify what worked and what requires improvement. Use these insights to refine playbooks, expand your library of automated responses, and decide which additional remediations to automate. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md) 
+  [FND05-BP07 Implement threat detection mechanisms](fnd05-bp07.md) 
+  [FND05-BP01 Shift compliance checks left with proactive controls](fnd05-bp01.md) 

 **Related documents:** 
+  [AWS Security Incident Response Guide - Detection](https://docs.aws.amazon.com/security-ir/latest/userguide/) 

 **Related examples:** 
+  [Automated Security Response on AWS](https://docs.aws.amazon.com/solutions/automated-security-response-on-aws/) 

 **Related services:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 