

# OPS05-BP02 Develop and test playbooks to respond to incidents

 A playbook is a step-by-step guide for investigating an incident from symptoms to root cause. You use playbooks to scope impact and diagnose problems consistently, whether a deployment failed or a service is degraded. Without them, investigation depends on individual recall and trial and error, which slows response and produces uneven results. 

 **Desired outcome:** 
+  Your team has playbooks for the incidents that occur most often, each guiding an investigator from symptoms to a likely root cause. 
+  Each of your playbooks records the tools and elevated permissions an investigation needs, along with a plan for keeping stakeholders informed. 
+  Each of your playbooks has an escalation path for cases where the root cause cannot be found, and points to a runbook when a known cause has a fix. 
+  Your playbooks live in a central location, stay current, and are linked from the alerts that trigger them. 
+  You use agentic tools to autonomously investigate incidents and provide root cause analysis and mitigation steps. 

 **Common anti-patterns:** 
+  Teams investigate incidents differently every time, with no agreed starting point. 
+  Engineers rely on memory or institutional knowledge to troubleshoot a failed deployment. 
+  New team members learn to investigate issues only through trial and error. 
+  Effective investigation techniques stay with individuals and are not shared across teams. 

 **Benefits of establishing this best practice:** 
+  Investigators reach a root cause faster because the diagnostic path is written down. 
+  Different people investigating the same incident reach consistent conclusions. 
+  Known root causes gain companion runbooks, which shortens recovery time. 
+  New team members contribute to incident response sooner. 
+  Teams scale incident response because playbooks are repeatable. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Incidents start as symptoms, such as a climbing error rate, a failed deployment, or a slow service. You have to reason from those symptoms to the root cause of the issue. A playbook encodes that reasoning as a repeatable diagnostic path. Build the playbook outside-in: begin from what a responder observes first, then work inward toward the systems that could produce those symptoms. 

 During an incident, stakeholders need to know what is understood and what is not. A playbook that omits a communication plan leaves the investigator improvising updates. The playbook must also name who to escalate to when the documented steps do not reveal a cause. 

 While a playbook diagnoses an issue, the runbook resolves the issue. When a playbook identifies a known root cause, link it to the runbook that fixes it. Build companion runbooks for the causes you find most often to shorten recovery. Start with low-risk incidents that have a small set of likely causes, as they are easier to document well than open-ended, high-severity events. 

 A text document in a shared repository is enough to start. As you build confidence, script the discovery steps and run them in notebooks to gather evidence quickly. Later, pair automated discovery with runbooks to auto-remediate common issues. Automate where an incident recurs, as issues that arise frequently are higher value than one-off problems. 

 On AWS, [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) investigates incidents autonomously and produces root cause analysis and mitigation steps. [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) converts documented discovery steps into automation you run against a workload or trigger from events, so you detect and resolve incidents faster. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a central repository and template:** Store playbooks in your documentation wiki or version control system so investigators can find them under pressure. Use a shared Markdown template so every playbook captures the same metadata, including stakeholders and a communication plan. A playbook template carries more than a runbook template does, because investigation depends on keeping people informed. 

   ```markdown
   # Playbook title
   ## Playbook info
   | Playbook ID | Description | Tools used | Special permissions | Author | Last updated | Escalation contact | Stakeholders | Communication plan |
   |---|---|---|---|---|---|---|---|---|
   | PLAY001 | What incident is this playbook used to investigate? | Tools | Permissions | Your name | 2026-01-01 | Escalation name | Stakeholder names | How updates are shared during the investigation |
   ## Steps
   1. Step one
   2. Step two
   ```

1.  **Select an incident to document first:** Choose a common incident that is low risk and whose root cause is usually one of a few known issues. Starting here builds confidence before you write playbooks for high-risk or poorly understood incidents. 

1.  **Write the discovery steps:** Working outside-in from the symptoms a responder first sees, document what to check and in what order to narrow the cause. Be explicit about which logs, metrics, and components to inspect at each step. Do not assume the reader already knows where to look. 

1.  **Add communication, escalation, and runbook links:** Record who to keep informed and how often, so stakeholder updates happen during the investigation rather than after. Define an escalation path for cases where no root cause emerges. Where a cause has a known fix, link to the companion runbook that resolves it. 

1.  **Validate the playbook with a peer:** Give the draft to a team member and have them investigate a sample incident using only the playbook. Update any step that is unclear or leaves the investigator stuck. 

1.  **Publish and link from alerts:** Publish the playbook to your central store and tell your team and stakeholders. Where an alert corresponds to a playbook, include a direct pointer to the playbook in the alert so responders reach it quickly. 

1.  **Automate as the library matures:** Convert stable discovery steps into scripts, and run them in notebooks or through [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to speed up investigation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS07-BP03 Perform knowledge management](ops07-bp03.md) 

 **Related documents:** 
+  [AWS Systems Manager: Working with runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [Use Automation runbooks to remediate application issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-runbooks.html) 
+  [Support self-service runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-support-runbooks.html) 
+  [Use AWS Systems Manager Automation runbooks to resolve operational tasks](https://aws.amazon.com/blogs/mt/use-aws-systems-manager-automation-runbooks-to-resolve-operational-tasks/) 
+  [Achieving operational excellence using automated playbook and runbook](https://aws.amazon.com/blogs/mt/achieving-operational-excellence-using-automated-playbook-and-runbook/) 

 **Related examples:** 
+  [AWS Customer Playbook Framework](https://github.com/aws-samples/aws-customer-playbook-framework) 
+  [AWS Systems Manager: Automation walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorials.html) 
+  [Build AWS Systems Manager Automation runbooks using AWS CDK](https://aws.amazon.com/blogs/mt/build-aws-systems-manager-automation-runbooks-using-aws-cdk/) 
+  [Rubix - a Python library for building runbooks in Jupyter notebooks](https://github.com/Nurtch/rubix) 
+  [Using Document Builder to create a custom runbook](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-builder.html) 

 **Related services:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 