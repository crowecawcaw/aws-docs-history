

# OPS06-BP02 Automate responses to events

 Manual handling of routine operational events is slow, inconsistent, and hard to scale. Automate the response to well-understood events to act immediately, apply the same remediation every time, and free operators for problems that need judgment. 

 **Desired outcome:** 
+  Your workload responds automatically to well-understood events without waiting for an operator. 
+  Your automated responses apply the same remediation every time, removing variation between operators. 
+  Your operators spend their attention on novel problems, not on repetitive, mechanical tasks. 
+  Your automation is version-controlled and tested, so you trust it to run unattended. 

 **Common anti-patterns:** 
+  Teams handle repetitive, well-defined events manually, which delays resolution and introduces mistakes. 
+  Operators run the same manual remediation for a known event many times a week. 
+  Critical but repetitive tasks stay manual, so alert fatigue causes teams to miss real issues. 
+  Automation runs without testing or version control, so a faulty script causes more damage than the event it addresses. 

 **Benefits of establishing this best practice:** 
+  Event responses accelerate, which reduces downtime. 
+  Operations stay reliable because automated handling is consistent and repeatable. 
+  Operators reclaim time for work that requires human judgment. 
+  Configuration drift and compliance gaps close automatically as they appear. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Not every event is a good candidate for automation. Automate events that occur often enough to justify the effort, have a well-understood cause, and have a remediation safe to run unattended. Leave rare events, or events whose response depends on context, to an operator with a runbook. 

 Event-driven automation connects a trigger, such as a metric crossing a threshold or a log entry, to a remediation action. With detection separated from response, one event can drive notification, remediation, and record-keeping. Define the trigger precisely so that it fires on the precise event you want to catch. 

 Unattended automation is risky. A buggy remediation, or one triggered by a mismatched condition, can cause more damage than the original event and spread across many resources before anyone notices. Treat automation as production code: keep it in version control, test it against realistic scenarios, and constrain its impact scope so a single faulty run cannot cascade. Prefer idempotent actions (those that produce the same result whether they run once or many times) over actions that accumulate side effects. 

 Automation pays off for remediation of known failures, capacity and scaling adjustments, deployment and release tasks, security responses, and drift correction. Start where the manual toil is highest and the risk of a mistake is lowest, then expand as your confidence and test coverage grow. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify automation opportunities:** List the repetitive tasks your teams perform, such as issue remediation, ticket enrichment, capacity management, scaling, deployments, and testing. Rank them by how often they occur and how well their remediation is understood, and automate the safest, highest-toil tasks first. 

1.  **Define the triggers:** Set the conditions that initiate each automated response. Use [Amazon CloudWatch alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html#alarms-and-actions) for metric thresholds, [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to match events from AWS services and applications, and [metric filters on log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) for conditions found in logs. 

1.  **Automate remediation and maintenance with runbooks:** Use [AWS Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to run maintenance, deployment, and remediation tasks without manual steps. When a work item opens in [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html), [attach and run automation runbooks against it](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html) so common remediation runs as soon as the item opens and responders start with context. 

1.  **Automate capacity and scaling:** Monitor quotas with the [Quota Monitor for AWS solution](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/solution-overview.html) so you act before you hit a limit, and adjust capacity automatically with [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) to hold availability and performance. 

1.  **Automate delivery and validation:** Automate build and release work with [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), and continually validate endpoints and APIs with [synthetic monitoring canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html). 

1.  **Automate risk mitigation and compliance:** Apply [automated security responses](https://docs.aws.amazon.com/solutions/automated-security-response-on-aws/) to address findings quickly, hold configuration steady with [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html), and [remediate noncompliant resources with AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html). 

1.  **Augment automated response with agentic AI:** For events whose remediation is not fully predetermined, use [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) to [investigate autonomously](https://docs.aws.amazon.com/devopsagent/latest/userguide/), correlate telemetry and deployment history, and recommend or apply targeted remediation, so investigation and recovery keep pace with events that a fixed script alone cannot handle. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS06-BP03 Define escalation paths](ops06-bp03.md) 
+  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 

 **Related documents:** 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [Configure CloudWatch alarms to create OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) 
+  [Remediate OpsItem issues using Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html) 

 **Related examples:** 
+  [Leverage agentic AI for autonomous incident response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US) 

 **Related services:** 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 