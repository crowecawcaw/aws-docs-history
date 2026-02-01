# DSOPS01-BP01 Establish a compliance function

Organizations operating in the cloud need an effective compliance
function to meet regulatory requirements, protect data, and maintain
stakeholder trust.

**Desired outcome:** A unified,
organization-wide compliance framework that continuously monitors,
enforces, and validates adherence to relevant standards and
regulations.

**Common anti-patterns:**

- Lack of clear compliance policies and procedures.
- Teams prioritize compliance only when there is an impending
  audit.
- Current compliance posture is not fully visible. Extensive
  search and discovery is required to identify compliance gaps.
- Limited involvement of compliance teams in defining security
  policies or during operational readiness review (ORR) of
  workloads.

**Benefits of establishing this best
practice:**

- Streamlined processes and technology enable rapid adaptation to
  new laws, minimizing disruption.
- Clear documentation and centralized systems simplify audits.
- Better decision-making based on objective compliance risk
  awareness. Trained employees and predictive technologies (for
  example, artificial intelligence (AI)) can identify risks early
  and reduce violations.
- Reduced possibility of penalties leading to increased trust from
  customers, partners, and stakeholders.
- Highly visible security posture through consistent application
  of compliance controls and long-term storage of activity logs.
- Reliability in compliance can differentiate your organization in
  regulated industries, giving you improved confidence to expand
  into new territories and industries.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start by developing a compliance-first culture where security and
privacy are embedded into every aspect of the organization's
technology usage. This requires executive sponsorship, clear
governance structures, and a shift from reactive to proactive
compliance management. Balance automation with human oversight,
and use AWS tools while recognizing where third-party solutions
may be necessary.

**Goals of a compliance function:**

- Establish clear ownership, accountability, and decision-making
  processes before implementing technical controls.
- Prioritize controls based on data sensitivity and regulatory
  impact.
- Solution architecture and designs must embed automated
  compliance checking into CI/CD pipelines. Regularly validate
  those checks using automated test cases.
- Make audits self-service. Gather evidence for audits
  continuously. Analyze audit logs and security findings in near
  real-time. Make reports available to auditors on-demand.
- Document and communicate compliance boundaries between your
  teams and your technology service providers.
- Scale compliance by setting organization-wide guardrails while
  empowering teams with the ability to define their own
  controls.

### Implementation steps

Setting up and managing a compliance function that scales across
the organization is a multi-step, multi-year endeavor. The
following guidance outlines a few of the most important steps
you might need to consider.

1. **Establish a compliance governance
   structure:**
   - Form a Cloud Compliance Center of Excellence (Cloud
     Compliance CoE or CCCoE) with executive sponsorship.
     Include experts from legal, operations, cybersecurity,
     data security, business, and technology domains.
     Alternatively, work towards adding compliance
     capabilities into your existing Cloud Center of
     Excellence.
   - Document core compliance processes. Outline your entire
     compliance lifecycle, spanning discovery, baselining,
     development, operationalization, monitoring,
     remediation, and evolution of regulatory requirements
     and associated controls.
   - Define compliance roles (for example, compliance
     officer, security architects or consultants, business
     unit champions, developers, and auditors).
   - Create a responsible, accountable, consulted, informed
     (RACI) matrix for compliance responsibilities across the
     organization. An example RACI matrix (for illustration
     only) is as follows:

   | Activity                    | CCoE | Business Unit Champions | Dev Teams | Security Consultants | Auditors |
   | --------------------------- | ---- | ----------------------- | --------- | -------------------- | -------- |
   | Define compliance standards | A/R  | C                       | I         | C                    | I        |
   | Implement controls          | A    | R                       | R         | C                    | I        |
   | Monitor compliance          | R    | R                       | I         | R                    | I        |
   | Remediate issues            | A    | R                       | R         | C                    | I        |
   | Report compliance status    | R    | C                       | I         | C                    | A        |
   | Conduct audits              | I    | I                       | C         | C                    | R        |

   R = Responsible, A = Accountable, C = Consulted, I =
   Informed
   - Develop compliance policies and standards aligned with
     business objectives. For example, if your business goal
     is to onboard healthcare customers and hold protected
     health information (PHI) data, consider Health Insurance
     Portability and Accountability Act (HIPAA) regulations.
   - Create regionalized standard operating procedures to
     support data subject requests, reporting data breaches
     and more broadly, managing incidents originating from
     non-compliance. For example, here is
     [guidance for data subject requests](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/subject-access-requests/a-guide-to-subject-access/ "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/subject-access-requests/a-guide-to-subject-access/") issued by the UK
     Information Commissioner's Office.
   - Define your audit support process. Consider questions
     such as:
     - What does our certification roadmap look like?
     - How should we resource specific audit processes?
     - How will evidence be captured and preserved?
     - How will re-certification and re-attestation be
       managed?

2. **Conduct compliance requirements
   analysis**:
   - Inventory applicable regulations and standards (like
     General Data Protection Regulation (GDPR), HIPAA,
     Payment Card Industry Data Security Standard (PCI-DSS),
     Service Organization Control 2 (SOC 2), and
     International Organization for Standardization 27001
     (ISO 27001)).
   - Build a compliance baseline at an organizational and
     Region level. Allow teams to extend baselines by adding
     requirements unique to their workloads.
   - Map baseline requirements to AWS services and shared
     responsibility boundaries.
   - Identify gaps between current state and regulatory
     requirements.
   - Consider report generation requirements and evidences
     needed to support audit exercises.

3. **Evaluate and integrate compliance
   tooling**:
   - Select services and tools aligned with your compliance
     requirements. For more detail, see
     [Choosing
     AWS security, identity, and governance services](../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md "../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md").
   - Develop prototypes and architecture outlines to gain a
     holistic understanding of how your selected tools work.
     Understand how they integrate with and support your
     compliance workflow.
   - Assess and configure integrations requirements with your
     existing architecture. AWS security and compliance
     services are integrated from the outset. However,
     additional effort may be needed to integrate third-party
     tooling. This includes IT service management (ITSM),
     cloud security posture management (CSPM), security
     information and event management (SIEM), endpoint
     detection and response (EDR), and extended detection and
     response (XDR) tools.
   - Aim to operationalize centralized compliance dashboards.
     Consider adopting a CSPM product (for example,
     [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")), augmented with a product that
     provides data security posture management (DSPM)
     capabilities.

4. **Establish engineering best
   practices**:
   - Build and test automated compliance controls. Write
     [AWS CloudFormation Guard rules](../../../cfn-guard/latest/ug/writing-rules.md "../../../cfn-guard/latest/ug/writing-rules.md") to provision custom
     controls. Use the
     [CloudFormation
     CLI](../../../cfn-guard/latest/ug/writing-rules.md "../../../cfn-guard/latest/ug/writing-rules.md") to validate and unit test your guard rules.
   - Build and test automated remediations.
     [Systems Manager Automation runbooks](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md") provide a large catalog of remediations ready for use.
   - Monitor your compliance status. Many AWS security and
     compliance services provide built-in customizable
     dashboards. For example, AWS Security Hub allows you to
     [create
     custom insights](../../../securityhub/latest/userguide/securityhub-custom-insights.md "../../../securityhub/latest/userguide/securityhub-custom-insights.md") to track issues relevant to your
     workload.
   - Enable tools to automate audits. Consider adopting
     [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md"). It continually audits your AWS
     usage to simplify risk and compliance management. When
     you enable an Audit Manager
     [standard
     framework](../../../audit-manager/latest/userguide/framework-overviews.md "../../../audit-manager/latest/userguide/framework-overviews.md") it automatically collects logs, and
     security findings on your behalf.

5. **Start shortlisting data sources for
   compliance monitoring**: AWS Config can directly
   detect compliance drifts as a result of resource
   misconfigurations (reported as findings). However,
   additional effort is required to detect non-compliance due
   to operational loopholes or code and design flaws. Logs play
   a central role in this process. Candidate sources include
   network flow logs, access logs, service and application
   usage logs, plus security events, and security findings. The
   shortlisted compliance tooling should automatically ingest
   data from multiple data sources and derive insights with
   minimal custom integration code.
6. **Set up service onboarding
   procedures**: Set best practices and enforce
   guardrails to onboard new AWS Services in line with your
   security and compliance best practices. Start with security
   best practices provided with AWS service documentation.
   [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/") contains additional information regarding
   the compliance status of individual AWS services.
   [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") provides more than 700 guardrails in
   the form of preventative, proactive, and detective controls
   to set up consistent and secure cloud environments across
   AWS Regions and accounts.
7. **Set up compliance training
   programs**:
   - Launch training courses to address upskilling needs,
     especially around new tools and techniques.
   - Launch role-based training courses. Consider starting
     with the following topics:
     - Understanding data classification (for example,
       public, internal, confidential).
     - Best practices of handling sensitive data.
     - Understanding regulatory requirements and standards
       (for example, GDPR, HIPAA, PCI-DSS, California
       Consumer Privacy Act (CCPA)).

   - Create mentorship, and advocacy programs to drive
     awareness.

8. **Develop response
   procedures**:
   - Design and develop runbooks for compliance violations
     and security incidents. Consider using
     [AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/what-is-incident-manager.md "../../../incident-manager/latest/userguide/what-is-incident-manager.md") for response
     coordination.
   - Establish evidence preservation and extraction
     procedures to respond to regulatory inquiries. This
     includes data subject requests, data disclosure requests
     from law enforcement agencies, or reporting incidents of
     data breach. Consider building a
     [cyber
     forensics](../../../prescriptive-guidance/latest/security-reference-architecture/cyber-forensics.md "../../../prescriptive-guidance/latest/security-reference-architecture/cyber-forensics.md") capability over time to deal with such
     requirements in a repeatable and predictable manner.

9. **Set objective success
   criteria**: For example,
   - Reduce the total number of resources not meeting
     compliance requirements, or reduce
     _critical_ and
     _high_ issues.
   - Reduce the time between remediation and the first
     detection of a compliance issue.
   - Reduce effort by decreasing the number of days spent
     supporting audits.
   - When you enable Security Hub, it automatically generates
     a dashboard that provides a
     [summary
     of findings by severity](../../../securityhub/latest/userguide/dashboard.md "../../../securityhub/latest/userguide/dashboard.md"). You can drill-down to
     individual findings and extract the data required to
     produce some of the statistics listed above. It also
     possible to build automations to extract this data. For
     example, the
     [Security Hub Compliance Analyzer](https://github.com/awslabs/security-hub-compliance-analyzer "https://github.com/awslabs/security-hub-compliance-analyzer") extracts findings to an
     Amazon S3 Bucket, and then parses out the relevant
     information.

10. **Implement continuous
    improvements**:
    - Monitor health of key compliance metrics.
    - Identify optimization opportunities. Gather feedback and
      implement improvements.
    - Improve control testing procedures.
    - Improve automation runbooks and their coverage.

## Resources

**Related best practices:**

- [[AG.ACG.1]
  Adopt a risk-based compliance framework](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.ACG.2] Implement controlled procedures for introducing new services and features](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.ACG.3]
  Automate deployment of detective controls](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.ACG.4] Strengthen security posture with ubiquitous preventative guardrails](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.ACG.6] Implement auto-remediation for non-compliant findings](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[O.DIP.1]
  Aggregate logs and events across workloads](../devops-guidance/o.dip.md "../devops-guidance/o.dip.md")
- [[O.DIP.2] Centralize logs for enhanced security investigations](../devops-guidance/o.dip.md "../devops-guidance/o.dip.md")
- [OPS01-BP03
  Evaluate governance requirements](../operational-excellence-pillar/ops_priorities_governance_reqs.md "../operational-excellence-pillar/ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")

**Related documents:**

- [Scaling a governance, risk, and compliance program for the cloud, emerging technologies, and innovation](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/ "https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/")
- [Evolving
  GRC to Maximize Your Business Benefits from the Cloud](https://aws.amazon.com/blogs/enterprise-strategy/evolving-grc-to-maximize-your-business-benefits-from-the-cloud/ "https://aws.amazon.com/blogs/enterprise-strategy/evolving-grc-to-maximize-your-business-benefits-from-the-cloud/")
- [Optimizing cloud governance on AWS: Integrating the NIST Cybersecurity Framework, AWS Cloud Adoption Framework, and AWS Well-Architected](https://aws.amazon.com/blogs/security/optimizing-cloud-governance-on-aws-integrating-the-nist-cybersecurity-framework-aws-cloud-adoption-framework-and-aws-well-architected/ "https://aws.amazon.com/blogs/security/optimizing-cloud-governance-on-aws-integrating-the-nist-cybersecurity-framework-aws-cloud-adoption-framework-and-aws-well-architected/")
- [Decision Guide: Choosing AWS security, identity, and governance services](../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md "../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md")
- [Introducing
  AWS Audit Manager Common Controls Library](https://aws.amazon.com/blogs/mt/introducing-aws-audit-manager-common-controls-library/ "https://aws.amazon.com/blogs/mt/introducing-aws-audit-manager-common-controls-library/")
- [AWS Security Incident Response Technical Guide](../../../security-ir/latest/userguide/security-incident-response-guide.md "../../../security-ir/latest/userguide/security-incident-response-guide.md")
- [Training
  programs available through AWS Skill Builder, and AWS Workshops](https://aws.amazon.com/blogs/training-and-certification/safe-and-sound-in-the-cloud-training/ "https://aws.amazon.com/blogs/training-and-certification/safe-and-sound-in-the-cloud-training/").
- [Building
  Security from the Ground up with Secure by Design](https://d1.awsstatic.com/partner-network/AWS-SANS-Secure-by-Design-Whitepaper-2024.pdf "https://d1.awsstatic.com/partner-network/AWS-SANS-Secure-by-Design-Whitepaper-2024.pdf")
