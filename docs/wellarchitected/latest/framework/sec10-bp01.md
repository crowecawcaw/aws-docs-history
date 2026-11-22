

# SEC10-BP01 Identify key personnel and external resources

 Before an incident occurs, identify the internal responders, external partners, and legal contacts who investigate, communicate, and make decisions during a security event. Keep the list current so you can reach the right people quickly when one occurs. 

 **Desired outcome:** 
+  You maintain a current list of key personnel with their roles, responsibilities, and at least two contact methods each. 
+  Your list includes external parties such as software vendors, security partners, cloud providers, and the regulators you must notify. 
+  Your responders have the context and access they need to act as soon as they are engaged. 
+  You review and update the list on a schedule and after any organizational change. 
+  You have an escalation path that engages a backup when a primary contact is unavailable. 

 **Common anti-patterns:** 
+  Teams keep no current list of responders, so an event begins with a search for who to call. 
+  Organizations assume all responders know the people, dependencies, and systems involved in a response. 
+  Teams maintain no repository that describes key infrastructure or application design. 
+  New employees join without onboarding that prepares them to contribute during an event. 
+  Responders have no escalation path when a primary contact does not answer. 

 **Benefits of establishing this best practice:** 
+  Responders engage faster because roles and contacts are known before an event. 
+  Triage time drops because the right people arrive with context and access. 
+  Communication with regulators, customers, and partners follows a known path. 
+  Backups keep the response moving when a primary contact is unavailable. 
+  New team members contribute sooner because onboarding includes response preparation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Consolidate your personnel and resource list in one system and update it as people join, change roles, or leave. Scattered contacts across wikis, chat histories, and personal notes slow down each response. 

 Define the response roles in advance. 
+  An *incident manager* holds overall authority during a response and decides when to escalate. 
+  *Incident responders* investigate and remediate. They are usually the developers and operators who own the affected workload, so the responders change with the type of event. 
+  A *communications lead* handles internal updates and external notifications to customers, regulators, and public agencies. 
+  For distributed teams, name a *subject matter expert* for each mission-critical workload who understands its operation and data classification. 

 Primary contacts are not always reachable. Escalate by role so a response continues when one person is unavailable. Give each contact at least two channels, as a single email address is a single point of failure. Use an on-call rotation to share the load and keep responders familiar with the workload. 

 Independent software vendors, managed service partners, and subcontractors may hold knowledge or access you need to recover. Arrange support relationships with them before an incident, including the appropriate level of [Support](https://aws.amazon.com/premiumsupport/) for prompt access to AWS experts. Some events carry legal obligations. Publicly listed companies and regulated industries must notify agencies within defined windows, so keep contact details for the responsible departments current. 

 A dedicated incident management capability keeps contacts, on-call schedules, and escalation plans in one place and automates paging during an event. [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) holds the team you want AWS to engage during a security event, with each member's title, email address, and notification preferences. Include leadership, legal counsel, managed detection and response partners, and the engineers who own the workload. The service does not schedule on-call rotations or page responders, so pair it with an incident management tool that does. Run this capability from your Security Tooling account so it stays available if a workload account is affected. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up an incident management solution:** Choose a solution that stores contacts, on-call schedules, and escalation plans, and that pages whoever is on call. AWS Marketplace lists [incident management solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=incident+management) that handle on-call rotations, escalation, and automatic paging. Deploy it in your Security Tooling account so it stays available if a workload account is affected. 

1.  **Register your response team with AWS:** Onboard [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) and [configure your incident response team](https://docs.aws.amazon.com/security-ir/latest/userguide/configure-incident-response-team.html). AWS can then engage the right people during a security event. Add the leadership, legal counsel, detection and response partners, and engineers who need to know, then set each member's notification preferences. 

1.  **Record contacts with multiple channels:** Define each responder in your incident management solution with at least two contact channels, such as SMS, phone, and email. This redundancy keeps people reachable when one channel fails. 

1.  **Map roles to a contact directory:** Document each person's role and responsibilities alongside their contacts, covering incident manager, incident responders, communications lead, and subject matter experts. Keep this directory current as people change roles or teams. 

1.  **Engage external partners and legal contacts:** Establish support arrangements with your critical vendors and sign up for the [Support plan](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) that matches your response requirements. Record the agencies and regulators you must notify and the internal owners responsible for those notifications. 

1.  **Define a role-based response and escalation plan:** Build a response plan that engages contacts by role rather than by name, with escalation paths for when a primary contact does not respond. Include contacts responsible for informing external entities even when they are not part of the technical response. 

1.  **Route alerts to responders automatically:** Configure [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules to forward critical findings from [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) or [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms to your incident management solution. The on-call responder is then paged without manual work. Have the same events open an operational work item in [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html), which is where you track the work a response generates. Each item carries a status, an owner, and the data about the affected resources. Responders can see what is still open and what is already done. 

1.  **Onboard and review on a cadence:** Add new responders through an onboarding process that includes incident response simulations, and review the full contact list on a schedule and after each organizational change. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 

 **Related documents:** 
+  [What is AWS Security Incident Response?](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) 
+  [Configure your incident response team](https://docs.aws.amazon.com/security-ir/latest/userguide/configure-incident-response-team.html) 
+  [Managing my incident response team](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-my-incident-response-team.html) 
+  [Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Accelerating incident response with AWS Security Incident Response (TDR421)](https://www.youtube.com/watch?v=EczVWVieRb8) 

 **Related examples:** 
+  [AWS customer playbook framework](https://github.com/aws-samples/aws-customer-playbook-framework) 

 **Related tools:** 
+  [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) 