# DSSEC09-BP01 Integrate compliance requirements into incident

response

Organizations must embed regulatory and compliance requirements into both incident response
planning and running to verify timely incident reporting, evidence preservation, and regulatory
authority notification. This best practice provides guidance on how organizations meet
compliance obligations while containing and remediating incidents. By aligning incident response
capabilities with specific regulatory requirements, organizations demonstrate adherence during
incident investigations and audits.

**Desired outcome:** Organizations respond to security incidents in
accordance with regulatory requirements and procedures. Incidents are contained and remediated
while meeting mandatory reporting obligations, reducing compliance violations.

**Common anti-patterns:**

- Misalignment between incident response plans and regulatory requirements, resulting in
  compliance violations, regulatory fines, and legal liability.
- Incident response plans become outdated due to infrequent reviews, failing to reflect
  changes in organizational structure, regulatory requirements, or technical architecture.
- Failure to run incident response plans during actual incidents, including delayed
  regulatory authority notification and inadequate incident classification.

**Benefits of establishing this best practice:**

- Organizations achieve compliance-ready incident response capabilities, meeting
  regulatory obligations and procedures, and mitigating compliance violations.
- Regular incident response plan validation verifies that incident response capabilities
  remain aligned with evolving regulatory requirements, reducing regulatory risks and fines.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Compliance requirements related to incident reporting include the following:

- **Reporting incidents to National Competent Authorities**:
  Report incidents to a designated authority (such as the Information Commissioner's Office
  ([ICO](https://ico.org.uk/for-the-public/ "https://ico.org.uk/for-the-public/")) or National Cyber Security
  Centre ([NCSC](https://www.ncsc.gov.uk/ "https://www.ncsc.gov.uk/")) or Data Protection Authority
  (DPA) within specific timelines. Consider the following aspects.
  - _Reporting timeframes_: Timeframe within which information must be
    shared with authorities and affected stakeholders.
  - _Impact to stakeholders_: Share information regarding the incident,
    its impact, and steps taken to minimize the impact.
  - _Obligations related to locating root cause(s)_: Conduct and report
    results of a root cause analysis (RCA) within specific timeframes.
  - _Communication protocols_: The contact persons or authorities
    involved in the incident reporting and the method to share the information.

- **Validation of incident handling procedures**: Perform
  periodic reviews (attestation, certification) of your organization's incident handling
  procedures. Validations may include checking for specific capabilities such as digital
  forensics, or usage of specific tools and services.

To meet compliance standards around incident reporting, consider the following.

- **Include regulatory adherence requirements in your incident response
  plan**: This includes:
  - Clear roles and responsibilities for cybersecurity incident management.
  - Cybersecurity incident classification aligned with regulatory and compliance
    standards. The classification determines relevant processes including reporting
    requirements, communication protocols, and information sharing timelines.
  - Internal communication and escalation protocols. Including incident triage,
    internal reporting and case handling procedures.
  - External communication plan. Including authority notification processes,
    regulatory reporting timelines, and information sharing procedures.
  - Cyber resilience capabilities aligned with business continuity (BC) and disaster
    recovery (DR) plans to maintain critical services during cybersecurity incidents.
  - Digital forensics capabilities that meet regulatory reporting needs. These
    capabilities perform thorough assessment, threat neutralization, and evidence
    extraction from compromised systems.

- **Develop and maintain the incident response capabilities
  across**:
  - **People**: Executive sponsors, security analysts, cyber
    incident response team (CIRT), security engineers, legal, Human Resources (HR). Use
    cross-functional teams to assess incident impact and provide response plan inputs.
  - **Process**: Incident response plan, playbook, runbooks,
    DR or BC plan
  - **Technology or tool**: Security information and event
    management (SIEM) tools, security controls, cloud operation tools

- **Regularly review incident response plans**: Update plans to
  reflect organizational changes in people, processes, and technology. Conduct validation
  through tabletop Exercise (TTX), purple or red teaming. Post-incident reviews can also
  provide inputs for incident response plan improvements.

### Implementation steps

1. Identify and clarify applicable compliance standards and requirements. Determine
   which regulatory frameworks apply to your organization (such as GDPR, HIPAA, or
   PCI-DSS). Document the specific incident response capabilities requirements for each
   applicable standard, including notification timelines, reporting procedures, evidence
   preservation requirements, and communication protocols.
2. Develop and validate the incident response plan aligned with compliance
   requirements. Refer to AWS Prescriptive Guidance on [Security recommendations for responding to incidents](../../../prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.md "../../../prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.md"). The document emphasizes
   that successful incident response requires three key foundations - preparation,
   operations, and post-incident activity - and recommends establishing a well-defined
   incident response plan, creating runbooks and playbooks, implementing event-driven
   security automation, documenting support engagement processes, and configuring alerts
   for security events to verify that organizations can effectively detect, respond to, and
   remediate security incidents in the cloud.
3. Implement incident response capabilities. Refer to the [AWS
   Security Incident Response Technical Guide](../../../security-ir/latest/userguide/security-incident-response-guide.md "../../../security-ir/latest/userguide/security-incident-response-guide.md") for an overview of responding to
   incidents within AWS environment. This guide provides step-by-step procedures for the
   three key phases: preparation (establishing incident response plans and automated
   responses), operations (detection, analysis, containment, eradication, and recovery),
   and post-incident activity (lessons learned and process improvements).
4. Validate compliance alignment. Conduct tabletop exercises or simulations to
   validate that your incident response procedures meet the specific requirements of each
   applicable compliance standard.

## Resources

**Related best practices:**

- [SEC10
  How do you anticipate, respond to, and recover from incidents?](../../../latest/security-pillar/preparation.md "../../../latest/security-pillar/preparation.md")
- [SEC01-BP03 Identify and validate control objectives](../security-pillar/sec_securely_operate_control_objectives.md "../security-pillar/sec_securely_operate_control_objectives.md")
- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [SEC01-BP08 Evaluate and implement new security services and features regularly](../security-pillar/sec_securely_operate_implement_services_features.md "../security-pillar/sec_securely_operate_implement_services_features.md")

**Related documents:**

- [AWS Security recommendations for responding to incidents](../../../prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.md "../../../prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.md")
- [AWS Security
  Incident Response Technical Guide](../../../security-ir/latest/userguide/security-incident-response-guide.md "../../../security-ir/latest/userguide/security-incident-response-guide.md")
- [Threat
  Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/ "https://aws-samples.github.io/threat-technique-catalog-for-aws/")

**Related videos:**

- [AWS re:Invent 2025 - AWS
  detection and response innovations that drive security outcomes (SEC323)](https://www.youtube.com/watch?v=MANvue0O8nw "https://www.youtube.com/watch?v=MANvue0O8nw")
- [AWS re:Invent 2025 -
  Accelerating incident response through AIOps (COP334)](https://www.youtube.com/watch?v=Ny4rrINHPe0 "https://www.youtube.com/watch?v=Ny4rrINHPe0")
- [AWS re:Invent 2025 - The
  incident is over: Now what? (COP216)](https://www.youtube.com/watch?v=L5PvkwkpeAM "https://www.youtube.com/watch?v=L5PvkwkpeAM")
