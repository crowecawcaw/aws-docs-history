

# OPS06-BP03 Define escalation paths

 When an incident exceeds what the first responder can resolve, someone must decide who acts next and with what authority. Escalation paths define when to escalate, who to involve at each level, and which actions are pre-approved, so decisions happen fast and the right people engage. 

 **Desired outcome:** 
+  Your escalation paths move incidents to the right people quickly, with no confusion about who to involve next. 
+  Your on-call responders hold the permissions and tools they need to act the moment they are paged. 
+  You pre-approve high-impact actions for anticipated scenarios, so responders do not wait for sign-off during an incident. 
+  Your stakeholders and customers receive updates in line with their expectations. 

 **Common anti-patterns:** 
+  Teams lack clear recovery procedures, so responders improvise during critical incidents. 
+  No one holds defined permissions or ownership, which delays action when speed matters most. 
+  Stakeholders and customers learn about incidents late, out of step with expectations. 
+  High-impact decisions, such as how to mitigate customer impact, wait on approvals that were never arranged in advance. 

 **Benefits of establishing this best practice:** 
+  Incident response follows a predefined path, which removes hesitation at each hand-off. 
+  Downtime shrinks because pre-approved actions and clear ownership let responders act immediately. 
+  Support levels adjust to incident severity, so resources match the size of the problem. 
+  Stakeholders and customers stay informed throughout the incident. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A first responder handles what they can, but some incidents need deeper expertise, wider authority, or a decision that carries business risk. An escalation path is the pre-agreed structure that moves an incident to the person who can act, at the moment the current responder reaches their limit. Without it, incidents stall while people work out who to call. 

 During an incident, decision authority is the scarce resource. A responder who knows the fix but lacks permission — or must wait for an executive to approve a customer-impacting action — loses minutes. Pre-approving actions for anticipated scenarios removes this bottleneck. You accept a small risk of a pre-authorized action being wrong in exchange for acting fast on foreseeable cases. Set these boundaries with decision-makers before an incident. 

 An escalation path must reach a person who can act. Name a role on the on-call schedule so the path stays valid when the current holder is unavailable. Each contact needs the permissions and access to act the moment they are engaged. Match the schedule depth to incident severity. 

 Many incidents depend on parties outside your team. Vendors, service providers, and other internal teams each have their own response times and contacts. Build those into the path. Document the service-level agreements (SLAs) you rely on, align them with your recovery goals, and keep vendor escalation contacts current and reachable. Stakeholders and customers expect timely updates, so decide who informs them, and how often, before the incident. 

 [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) can [investigate an incident autonomously](https://docs.aws.amazon.com/devopsagent/latest/userguide/) while the escalation proceeds, correlating telemetry, logs, and change history into a root-cause summary with recommended mitigations. The person engaged then starts with context and a proposed course of action. 

 An escalation path that is never exercised tends to break on first use. Rehearse through drills and game days so responders practice the process and gaps surface while the stakes are low. After each real incident, review how the path performed and refine it, because org charts, vendors, and workloads change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up escalation triggers:** Configure [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) to open a tracked work item when a monitored condition breaches its threshold. Create an [OpsItem in AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) so the response is tracked from the outset, and route the alarm to the paging tool your organization uses so the right responder is notified. 

1.  **Create on-call schedules:** Maintain on-call schedules in the paging tool your organization already runs, such as [Opsgenie](https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-amazon-cloudwatch/) or [PagerDuty](https://docs.pagerduty.com/integrations/amazon-cloudwatch-integration-guide). Name a role rather than a single person so the schedule stays valid when a responder is unavailable, and give on-call responders the permissions and tools to act the moment they are engaged. 

1.  **Define escalation procedures:** Set the conditions under which an incident escalates, and capture them in the escalation policies of your paging or IT service management tool, such as [Opsgenie](https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-amazon-cloudwatch/), [PagerDuty](https://docs.pagerduty.com/integrations/amazon-cloudwatch-integration-guide), [ServiceNow](https://www.servicenow.com/docs/r/zurich/integrate-applications/integration-hub/amazon-cloudwatch.html), or [Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/integrate-with-amazon-cloudwatch/). Route each level to a contact or an on-call schedule, and state the roles and responsibilities at each tier. 

1.  **Pre-approve mitigation actions:** Work with decision-makers to pre-approve actions for anticipated scenarios, and attach [Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to the [OpsItem](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html) so responders run those actions quickly during an incident. 

1.  **Assign ownership:** Name an internal owner for each step of the escalation path, so every stage of an incident has a named owner accountable for moving it forward. 

1.  **Plan third-party escalations:** Document the SLAs you depend on and align them with your recovery goals. Set clear protocols for vendor communication, integrate vendor contacts into your incident tooling for direct access, and keep escalation information current and easy to find. Include third-party scenarios in your drills. 

1.  **Train and rehearse escalation plans:** Train your team on the process, and run regular incident response drills or game days so the path works under pressure. 

1.  **Review and improve:** Review the effectiveness of your escalation paths on a regular cadence, and update them based on lessons from post-incident analysis and ongoing feedback. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS06-BP02 Automate responses to events](ops06-bp02.md) 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 

 **Related documents:** 
+  [Create OpsItems from CloudWatch alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) 
+  [Remediate OpsItems using Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html) 
+  [Creating and managing runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [AWS DevOps Agent: Investigating an incident](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 
+  [Atlassian - Escalation policies for effective incident management](https://www.atlassian.com/incident-management/on-call/escalation-policies) 

 **Related services:** 
+  [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 