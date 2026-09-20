

# DSSEC09-BP01 Integrate compliance requirements into incident response
<a name="dssec09-bp01"></a>

 Organizations embed regulatory and compliance requirements into incident response planning and execution to support timely incident reporting, evidence preservation, and regulatory authority notification. This best practice provides guidance on how organizations meet compliance obligations while containing and remediating incidents. By aligning incident response capabilities with specific regulatory requirements, organizations demonstrate adherence during incident investigations and audits. 

 **Desired outcome:** 
+  Organizations respond to security incidents in accordance with regulatory requirements and procedures. 
+  Incidents are contained and remediated while meeting mandatory reporting obligations, reducing compliance gaps. 

 **Common anti-patterns:** 
+  Misalignment between incident response plans and regulatory requirements, resulting in compliance gaps, regulatory fines, and legal liability. 
+  Incident response plans become outdated because of infrequent reviews, failing to reflect changes in organizational structure, regulatory requirements, or technical architecture. 
+  Failure to run incident response plans during actual incidents, including delayed regulatory authority notification and inadequate incident classification. 

 **Benefits of establishing this best practice:** 
+  Organizations achieve compliance-ready incident response capabilities, meeting regulatory obligations and procedures, and mitigating compliance gaps. 
+  Regular incident response plan validation verifies that incident response capabilities remain aligned with evolving regulatory requirements, reducing regulatory risks and fines. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Compliance requirements related to incident reporting include the following: 
+  **Reporting incidents to National Competent Authorities**: Report incidents to a designated authority (such as the Information Commissioner's Office ([ICO](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/)) or National Cyber Security center ([NCSC](https://report.ncsc.gov.uk/)) or Data Protection Authority (DPA) within specific timelines. Consider the following aspects. 
  +  *Reporting timeframes*: Time frame within which information must be shared with authorities and affected stakeholders. 
  +  *Impact to stakeholders*: Share information regarding the incident, its impact, and steps taken to minimize the impact. 
  +  *Obligations related to locating root causes*: Conduct and report results of a root cause analysis (RCA) within specific timeframes. 
  +  *Communication protocols*: The contact persons or authorities involved in the incident reporting and the method to share the information. 
+  **Validation of incident handling procedures**: Perform periodic reviews (attestation, certification) of your organization's incident handling procedures. Validations may include checking for specific capabilities such as digital forensics, or usage of specific tools and services. 

 To meet compliance standards around incident reporting, consider the following. 
+  **Include regulatory adherence requirements in your incident response plan**: This includes: 
  +  Clear roles and responsibilities for cybersecurity incident management. 
  +  Cybersecurity incident classification aligned with regulatory and compliance standards. The classification determines relevant processes including reporting requirements, communication protocols, and information sharing timelines. 
  +  Internal communication and escalation protocols. Including incident triage, internal reporting and case handling procedures. 
  +  External communication plan. Including authority notification processes, regulatory reporting timelines, and information sharing procedures. 
  +  Cyber resilience capabilities aligned with business continuity (BC) and disaster recovery (DR) plans to maintain critical services during cybersecurity incidents. 
  +  Digital forensics capabilities that meet regulatory reporting needs. These capabilities perform thorough assessment, threat neutralization, and evidence extraction from compromised systems. 
+  **Develop and maintain the incident response capabilities across**: 
  +  **People**: Executive sponsors, security analysts, cyber incident response team (CIRT), security engineers, legal, Human Resources (HR). Use cross-functional teams to assess incident impact and provide response plan inputs. 
  +  **Process**: Incident response plan, playbook, runbooks, DR or BC plan 
  +  **Technology or tool**: Security information and event management (SIEM) tools, security controls, cloud operation tools 
+  **Preserve evidence during incident response**: Incident response might destroy forensic evidence needed later. Preserve forensic evidence before remediation. Create EBS snapshots, capture memory dumps, and export CloudTrail logs before terminating compromised instances. Orchestrate this acquisition with [AWS Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). Implement immutable evidence storage using S3 Object Lock. 
+  **Communicate securely during incident response**: Avoid communicating insecurely during incident response. Use secure communication channels, never discussing incident details in unencrypted email or public chat. Use encrypted communication tools such as AWS Wickr. Implement need-to-know access for incident information. Verify that incident response communications don't cross geographic boundaries not permitted under sovereignty requirements. 
+  **Regularly review incident response plans**: Update plans to reflect organizational changes in people, processes, and technology. Conduct validation through tabletop exercise (TTX), purple or red teaming. Post-incident reviews can also provide inputs for incident response plan improvements. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify and clarify applicable compliance standards and requirements**: Determine which regulatory frameworks apply to your organization (such as GDPR, HIPAA, or PCI-DSS). Document the specific incident response capabilities requirements for each applicable standard, including notification timelines, reporting procedures, evidence preservation requirements, and communication protocols. 

1.  **Develop and validate the incident response plan aligned with compliance requirements**: Refer to AWS Prescriptive Guidance on [Security recommendations for responding to incidents](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.html). The document emphasizes that successful incident response requires three key foundations (preparation, operations, and post-incident activity) and recommends establishing a well-defined incident response plan, creating runbooks and playbooks, implementing event-driven security automation, documenting support engagement processes, and configuring alerts for security events to verify that organizations can effectively detect, respond to, and remediate security incidents in the cloud. 

1.  **Implement incident response capabilities**: Refer to the [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/security-incident-response-guide.html) for an overview of responding to incidents within AWS environment. This guide provides step-by-step procedures for the three key phases: preparation (establishing incident response plans and automated responses), operations (detection, analysis, containment, eradication, and recovery), and post-incident activity (lessons learned and process improvements). 

1.  **Implement incident reporting capabilities**: Establish repeatable procedures for reporting incidents to relevant parties, such as the national Competent Authority applicable in your jurisdiction. Where possible, automate the extraction, normalization, and formatting of the required incident report fields, and consider fully automating the reporting process if appropriate to your compliance requirements. 

1.  **Validate compliance alignment**: Conduct tabletop exercises or simulations to validate that your incident response procedures meet the specific requirements of each applicable compliance standard. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10 How do you anticipate, respond to, and recover from incidents?](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/preparation.html) 
+  [SEC01-BP03 Identify and validate control objectives](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_control_objectives.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 
+  [SEC01-BP08 Evaluate and implement new security services and features regularly](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_implement_services_features.html) 

 **Related documents:** 
+  [AWS Security recommendations for responding to incidents](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.html) 
+  [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/security-incident-response-guide.html) 
+  [Threat Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - AWS detection and response innovations that drive security outcomes (SEC323)](https://www.youtube.com/watch?v=MANvue0O8nw) 
+  [AWS re:Invent 2025 - Accelerating incident response through AIOps (COP334)](https://www.youtube.com/watch?v=Ny4rrINHPe0) 
+  [AWS re:Invent 2025 - The incident is over: Now what? (COP216)](https://www.youtube.com/watch?v=L5PvkwkpeAM) 