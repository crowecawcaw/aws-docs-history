# DSOPS03-BP01 Plan and prepare for audits

For customers in highly regulated industries, proactive audit
planning assists organizations as they strive to meet their audit
obligations with greater certainty and regularity.

**Desired outcome:** A streamlined,
well-planned, and evidence-based audit process that demonstrates
comprehensive adherence to applicable regulations while minimizing
business disruptions.

**Common anti-patterns:**

- Manual evidence collection when automated solutions are
  available.
- Scrambling to gather documentation days before an audit, leading
  to incomplete or inaccurate evidence.
- Treating audits as solely an IT or security team responsibility
  rather than a cross-functional effort.
- Not auditing vendors and SaaS tools integrated with the
  workload.

**Benefits of establishing this best
practice:**

- Scope of audit exercises is known in advance leading to better
  planning and resource utilization.
- Well-documented audit practices demonstrate due diligence to
  regulators and can reduce scrutiny.
- Audits are conducted in a structured, automated, and repeatable
  manner.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Effective audit preparation in AWS environments requires clear
scoping, establishing automated evidence collection, and
activating operational processes to manage audits end-to-end.

Key steps include:

- Establishing a compliance discovery and analysis methodology
  that assists with narrowing down the scope of an audit
  exercise.
- Creating clear documentation that maps specific regulatory
  requirements to the technical controls and operational
  practices. Many organizations develop and maintain a
  compliance matrix document which serves as a good preliminary
  evidence for auditors.
- Setting up continuous evidence collection mechanisms.
- Provisioning self-serve tools for auditors.
- Developing pre-built reporting templates (mapped to specific
  compliance standards), that can be populated on-demand by
  pulling near real-time data.
- Conducting regular internal assessments, and building a
  feedback loop geared towards addressing gaps found.

### Implementation steps

1. **Conduct readiness
   assessments**:
   - Perform regular internal audits using the same criteria
     as external auditors.
   - If required, schedule third-party pre-assessments before
     formal audits to gain confidence.
   - Run tabletop exercises simulating audit scenarios.
   - Practice evidence retrieval and presentation.

2. **Establish audit governance
   processes**:
   - Create an audit coordination team with representatives
     from key departments.
   - Designate an audit owner to oversee audits. Audit owners
     are typically governance, risk, and compliance (GRC)
     professionals, such as a compliance officer or a General
     Data Protection Regulation (GDPR) data protection
     officer.
   - Develop a communication plan for internal and external
     auditors.
   - Establish a process for managing audit findings and
     remediation.

3. **Prepare audit artifacts**:
   Start building a searchable and readily accessible
   repository of frequently requested audit artifacts. The
   following is a list of some of the items you may need to
   collect:
   - Inventory of software and hardware assets.
   - Security policies, data protection policies and privacy
     policies.
   - Data protection impact assessment (DPIA) reports.
   - Risk registers.
   - Incident management plans.
   - Business continuity plans (bcps). Disaster recovery (dr)
     plans.
   - Documentation related to software development lifecycle
     (SDLC) processes (for example, data handling procedures
     and change management processes).
   - Design documentation (for example, data flow diagrams,
     up-to-date network diagrams, and records of architecture
     decisions).
   - Documents related to previous security incidents. This
     includes root cause analysis (RCA) reports.
   - Contractual agreements entered with your technology
     providers. Agreements entered between AWS and AWS
     Customers can be found in
     [AWS Artifact](../../../artifact/latest/ug/managing-agreements.md "../../../artifact/latest/ug/managing-agreements.md").
   - Attestations and certifications currently held.
   - Audit trails and security-related logs. For example,
     Amazon CloudTrail
     [Data
     and Management Event Logs](../../../awscloudtrail/latest/userguide/cloudtrail-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-events.md"),
     [VPC
     Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"),
     [AWS WAF Logs](../../../waf/latest/developerguide/logging.md "../../../waf/latest/developerguide/logging.md"),
     [Amazon EKS Audit Logs](../../../eks/latest/best-practices/auditing-and-logging.md "../../../eks/latest/best-practices/auditing-and-logging.md"), and
     [Route 53 resolver query logs](../../../Route53/latest/DeveloperGuide/resolver-query-logs.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs.md").
   - Records of training conducted on specific
     compliance-related topics.

4. **Pre-provision audit tools and
   services**:
   - Consider using
     [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md"). Audit Manager provides prebuilt
     frameworks (for example, PCI DSS V3.2.1) that structure
     and automate assessments for a given compliance standard
     or regulation. This potentially shortens your audit
     timelines, reduces inaccuracies, and lowers expenses.
   - Provision read-only auditor roles. The AWS
     [ReadOnlyAccess
     managed policy](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") is an example of one such role. It
     allows auditors access to compliance related services
     such as AWS Audit Manager,
     [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md"), and
     [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

## Resources

**Related best practices:**

- [OPS02-BP02
  Processes and procedures have identified owners](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.md")
- [OPS02-BP03
  Operations activities have identified owners responsible for
  their performance](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_activity_owners.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_activity_owners.md")
- [OPS02-BP04
  Mechanisms exist to manage responsibilities and
  ownership](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_responsibilities_ownership.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_responsibilities_ownership.md")
- [OPS02-BP05
  Mechanisms exist to request additions, changes, and
  exceptions](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_req_add_chg_exception.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_req_add_chg_exception.md")
- [OPS02-BP06
  Responsibilities between teams are predefined or
  negotiated](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_neg_team_agreements.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_neg_team_agreements.md")

**Related documentation:**

- [How
  AWS Audit Manager Simplifies Audit Preparation](https://aws.amazon.com/blogs/aws/aws-audit-manager-simplifies-audit-preparation/ "https://aws.amazon.com/blogs/aws/aws-audit-manager-simplifies-audit-preparation/")
- [Prepare
  for an Audit in AWS Part 1 – AWS Audit Manager, AWS Config,
  and AWS Artifact](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/ "https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/")
- [Prepare
  for an Audit in AWS Part 2 – General Best Practices](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-2-general-best-practices/ "https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-2-general-best-practices/")

**Related services:**

- [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md")
- [AWS Artifact](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md")
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
- [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
