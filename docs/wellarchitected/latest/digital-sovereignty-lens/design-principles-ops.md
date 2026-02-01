# Design principles

- **Design to be compliant:** Set
  fulfilling sovereign compliance requirements as a design goal.
  Sovereign compliance in this context refers to national
  cybersecurity standards or frameworks, data privacy
  legislations, and industry regulations with technology
  implications, such as the EU Digital Operational Resilience Act
  (DORA). These requirements may also be technology-specific, such
  as requirements related to the use of cloud infrastructure
  services. Define your compliance metrics and build solutions
  that:
  - Apply automated controls to block noncompliant resources
    from being provisioned.
  - Detect drifts from baseline and forward findings to a single
    pane of glass.
  - Send notifications to stakeholders and downstream
    applications.
  - Run automated remediation to restore adherence. Noncompliant
    resources incur remediation costs and lead to security
    vulnerabilities. These vulnerabilities expose systems to
    intrusions and cyberattacks. The consequences can include
    prolonged outages, reputational damage, and regulatory
    penalties.

- **Maintain a compliance-aligned posture
  with multilayered controls:** Maintain a
  compliance-aligned posture using preventative, proactive, and
  detective controls. Moreover, controls are best implemented and
  maintained using a federated operating model. For example,
  central teams can deploy preventative controls at an
  organizational level, while product teams who are closer to the
  data can set up a mix of proactive and detective controls
  aligned with data protection and data privacy needs of the
  application.
- **Compliance is a shared
  responsibility:** Compliance requires application and
  solution owners across your organization to address their
  responsibilities in detecting and remediating noncompliant
  resources. It demands deep domain, regulatory, and technical
  knowledge, which is best scaled by sharing responsibilities
  through a federated operating model.
- **Make audits less disruptive:**
  Auditors require conclusive evidence demonstrating compliance
  with technical and operational requirements. This includes
  reports, documents, screenshots, code, and configurations. Audit
  activities must maintain business continuity without requiring
  developer intervention. To minimize disruption, implement
  automatic collection and aggregation of audit-related evidence
  and provide auditors with the ability to generate reports
  on-demand.
