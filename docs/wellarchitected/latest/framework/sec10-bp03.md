

# SEC10-BP03 Develop and test security incident response playbooks

 A playbook gives a responder the technical steps to investigate and contain a scenario. A separate management plan defines who responds and how you communicate. 

 **Desired outcome:** 
+  You have playbooks for the incident types you can anticipate, such as denial of service, ransomware, and credential exposure. 
+  You have playbooks for the security findings and alerts your detection tools generate. 
+  Each of your playbooks covers the response phases with concrete technical steps, queries, and expected outcomes. 
+  Your playbooks name the prerequisites, stakeholders, and escalation contacts a responder needs. 
+  You test and update playbooks so they stay accurate as your environment changes. 

 **Common anti-patterns:** 
+  Teams respond to each incident from scratch, repeating investigation work under pressure. 
+  Playbooks exist but are never tested, so responders find broken steps during a real event. 
+  Detection tools generate findings that no playbook tells responders how to handle. 
+  Playbooks omit the prerequisite logs and tools, so a responder cannot follow them. 
+  Playbooks are written once and never updated as the environment and threats change. 

 **Benefits of establishing this best practice:** 
+  Responders act consistently because each scenario has a defined procedure. 
+  Human error drops because steps, queries, and expected outcomes are written down. 
+  Findings from detection tools receive a known, repeatable response. 
+  New responders become effective faster by following tested playbooks. 
+  Testing surfaces broken steps before an incident rather than during one. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A playbook narrows a broad response plan to a single scenario. A generic plan tells you to contain an incident, while a ransomware playbook tells you which systems to isolate, which queries to run, and what successful containment looks like. 

 Build playbooks for both expected incidents and known detection findings. Expected incidents are the scenarios your threat model predicts, such as denial of service, ransomware, and credential exposure. Known findings are the specific outputs of your detection tooling. When [Amazon GuardDuty](https://aws.amazon.com/guardduty/) raises a finding, a playbook keyed to that finding type turns an alert into an action. GuardDuty Extended Threat Detection also produces attack sequence findings that correlate multiple signals into a single critical-severity alert representing a multi-stage attack. Treat these as their own playbooks because they indicate an active, progressing threat. For finding-specific guidance, see [Remediating security issues discovered by GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html). 

 Each playbook states the scenario it addresses and its goal, the prerequisites, and the stakeholders and their contacts. The core is the technical response organized by phase: detect, analyze, contain, eradicate, and recover. Each playbook ends with the expected outcome, so a responder can tell whether it worked. 

 Log sources move, tools change, and account structures evolve, and a playbook that references any of these can become invalid. Test playbooks on the same cadence as the plan and fix the steps that fail. Automate repetitive steps. Use notebook tools such as Jupyter with [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) queries against your CloudTrail logs to capture queries and analysis as reusable, versioned playbooks. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prioritize scenarios to cover:** List the incident types to address, drawing on your threat model for expected incidents and on your detection tools for known findings. Start with the highest-likelihood and highest-impact scenarios. 

1.  **Write the playbook overview and prerequisites:** For each scenario, state the risk it addresses and the goal, then list the logs, detection mechanisms, automated tools, and expected notifications a responder needs. 

1.  **Record communication and escalation details:** Identify the stakeholders involved, their responsibilities, and their contact information, along with the escalation path for the scenario. 

1.  **Document response steps by phase:** Provide the tactical steps, queries, and code for each phase (detect, analyze, contain, eradicate, and recover), so a responder can execute without improvising. 

1.  **Define expected outcomes:** Describe the result of running the queries and code so a responder can confirm the incident is contained and resolved. 

1.  **Test and maintain playbooks:** Exercise each playbook against a simulated scenario, fix steps that fail, and review playbooks on a cadence to keep them current with your environment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 
+  [SEC10-BP01 Identify key personnel and external resources](sec10-bp01.md) 

 **Related documents:** 
+  [Remediating security issues discovered by GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html) 
+  [GuardDuty attack sequence finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html) 

 **Related examples:** 
+  [AWS customer playbook framework](https://github.com/aws-samples/aws-customer-playbook-framework) 
+  [Develop your own Incident Response Playbooks](https://github.com/aws-samples/aws-incident-response-playbooks-workshop) 
+  [Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks) 

 **Related services:** 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 