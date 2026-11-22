

# SEC10-BP02 Develop incident management plans

 An incident management plan gives your team a known way to act when a security event occurs. It defines roles, communication paths, severity levels, and the phases of response, so decisions are made ahead of time. Build a plan that fits your workload and connects to your organization's broader response program. 

 **Desired outcome:** 
+  You have a documented plan that defines roles, responsibilities, and a RACI model for security events. 
+  Your plan defines communication methods, including an out-of-band backup channel, and severity and escalation criteria. 
+  Your workload-specific runbooks connect to your organization's broader incident response program. 
+  You know which AWS response teams and support options are available and how to engage them. 
+  You review and test the plan on a schedule and after organizational or regulatory change. 

 **Common anti-patterns:** 
+  Teams rely on an organization-wide plan with no runbooks specific to their workload. 
+  Plans name no clear owner for decisions, so responders debate authority during an event. 
+  Organizations document a plan but never test it, so gaps surface only during a real incident. 
+  Communication depends on a single channel that may be unavailable when the incident involves it. 
+  Plans ignore the regulatory or data-residency obligations that govern the response. 

 **Benefits of establishing this best practice:** 
+  Responders act quickly because roles, severity, and escalation are defined in advance. 
+  A workload-specific plan closes the gaps that a generic organizational plan leaves open. 
+  Out-of-band communication keeps the response coordinated even when primary systems are affected. 
+  Alignment with regulations reduces legal and compliance exposure during an event. 
+  Regular testing turns the plan into a practiced capability rather than a document. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The plan records who has authority, how severe an event is, who to tell, and what to do in each phase. The cloud carries the same operational roles as on-premises, so use your organization's existing plan as a starting point and extend it with workload-specific detail. 

 Build the plan on the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS secures the cloud, and you secure what you run in it, including the controls you choose and how you respond when they are tested. A defense-in-depth approach shapes the plan around layers of detection and containment. The [AWS Security Incident Response Guide](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.pdf) sets out the concepts for a cloud-centric plan. 

 Ground the plan in an established framework. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) organizes incident response around the six functions of the NIST Cybersecurity Framework 2.0. Govern, Identify, and Protect cover preparation, while Detect, Respond, and Recover cover the response itself. Your regulatory context changes the details. Workloads under FedRAMP, or those holding personally identifiable information, carry notification windows and data-residency constraints. Document these in the plan before an event. 

 When no one owns the decision to escalate or take a system offline, responders lose time debating authority. A RACI model names who is responsible, accountable, consulted, and informed at each phase. Include human resources, legal, executives, and the application owners who understand the workload. Build relationships with those subject matter experts before an incident. 

 If an incident involves your primary messaging system, responders need a backup channel that the unauthorized party does not control. An out-of-band tool such as [AWS Wickr](https://aws.amazon.com/wickr/) keeps coordination secure when your usual systems are suspect. Define severity levels alongside communication paths, because severity drives who you notify and how fast. 

 [Support](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) plans provide access to AWS expertise and tooling. [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) brings AWS incident response engineers into an event on your side of the shared responsibility model. You open a case, or the service opens one from findings it has triaged. Record in your plan [when to contact them](https://docs.aws.amazon.com/security-ir/latest/userguide/when-to-contact-security-ir.html). [AWS Shield](https://aws.amazon.com/shield/) provides managed protection against DDoS without engaging Support. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define roles and a RACI model:** Identify the people and departments who take part in a response, including security, application owners, human resources, legal, and executives. Assign responsible, accountable, consulted, and informed roles for each phase so authority is clear before an event. 

1.  **Adopt a framework-based response structure:** Structure the plan on [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Record the high-level actions for preparation under Govern, Identify, and Protect, and for the response under Detect, Respond, and Recover. 

1.  **Define severity and escalation criteria:** Classify incidents by severity, and tie each level to prioritization and escalation procedures so responders know when and to whom to escalate. 

1.  **Design communication paths with a backup channel:** Document contact information and communication methods, and add an out-of-band channel such as [AWS Wickr](https://aws.amazon.com/wickr/) for use when primary systems are untrusted. 

1.  **Map available AWS response support:** Record how to engage [Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) and how to [open a case with AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/create-an-aws-supported-case.html). Confirm which protections, such as AWS Shield, already cover your workload. Send case notifications to more than one address outside the account. An actor with support permissions can [close a case](https://aws-samples.github.io/threat-technique-catalog-for-aws/Techniques/T1098.A001.html) to hide the activity that opened it. 

1.  **Align with regulatory obligations:** Incorporate the notification windows, data-residency rules, and compliance requirements that govern your workload into the plan. 

1.  **Document, test, and review the plan:** Record the plan as a formal document, test it with all defined roles on a regular cadence, and review it whenever your structure or requirements change. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10-BP01 Identify key personnel and external resources](sec10-bp01.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 
+  [SEC04-BP01 Configure service and application logging](sec04-bp01.md) 

 **Related documents:** 
+  [AWS Security Incident Response Guide (PDF)](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.pdf) 
+  [What is AWS Security Incident Response?](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) 
+  [When to contact AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/when-to-contact-security-ir.html) 
+  [NIST SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) 
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
+  [Getting started with Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Scale Security Operations with AWS Security Incident Response Service (SEC329)](https://www.youtube.com/watch?v=DBKcDH1ba54) 

 **Related services:** 
+  [AWS Security Incident Response](https://aws.amazon.com/security-incident-response/) 
+  [Support](https://aws.amazon.com/premiumsupport/) 
+  [AWS Shield](https://aws.amazon.com/shield/) 