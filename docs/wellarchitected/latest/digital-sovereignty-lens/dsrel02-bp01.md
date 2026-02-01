# DSREL02-BP01 Implement continuous third-party risk management

(TPRM) processes

In highly regulated industries, a robust third-party risk management
(TPRM) process is essential to mitigate risks associated with vendor
relationships.

A TPRM framework maintains alignment between third-party vendors and
an organization's security standards, regulatory requirements, and
business continuity objectives. This protects against
vulnerabilities, regulatory violations, and operational disruptions
that could lead to penalties, data breaches, or reputational damage.

**Desired outcome:** Third-party
vendor risks are identified, assessed, and mitigated throughout the
vendor engagement lifecycle, maintaining alignment with security
standards and compliance requirements.

**Common anti-patterns:**

- Conducting one-time or as-needed vendor assessments without
  standardized criteria or ongoing monitoring.
- Relying on manual tracking processes and lacking clear
  understanding of data flows and vendor dependencies.
- Using varying security criteria across vendors and failing to
  implement standardized security requirements in contracts.
- Over-relying on vendor self-attestations.
- Allowing unapproved technology usage and lacking proper incident
  response coordination with vendors.
- Failing to adapt evaluations to evolving threats and regulations
  while neglecting continuous compliance monitoring.

**Benefits of establishing this best
practice:**

- Real-time monitoring of vendor risk posture with automated
  alerting and proactive supply chain risk identification.
- Systematic evidence collection and centralized documentation
  demonstrating adherence to industry regulations.
- Streamlined vendor onboarding/offboarding processes while
  maintaining security standards and cost optimization.
- Pre-established communication channels and procedures for
  coordinating security incidents and protecting operations.
- Enhanced confidence from auditors, regulators, and customers
  through demonstrated vendor risk management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement a continuous TPRM lifecycle process integrated with
existing risk management, procurement, and compliance functions,
using AWS services for automation and monitoring.

Key implementation elements:

- Establish centralized TPRM governance with clear roles and
  responsibilities
- Develop standardized vendor assessment questionnaires aligned
  with regulatory requirements
- Create vendor risk scoring models based on data sensitivity
  and service criticality
- Implement automated monitoring and alerting for vendor risk
  changes
- Maintain contractual safeguards and incident response
  alignment
- Maintain continuous compliance checks and detailed audit
  trails

This approach creates a scalable process that maintains consistent
security and regulatory standards across third-party
relationships.

### Implementation steps

1. Establish a governance structure with a TPRM steering
   committee, risk assessment team, compliance officers, and
   business stakeholders.
2. Implement an assessment framework using
   [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/") for vendor questionnaires, risk
   assessment templates, compliance checklists, and evidence
   collection.
3. Configure a vendor management database to track vendor
   profiles, risk scores, compliance status, and contract
   details.
4. Set up automated monitoring using
   [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/"),
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"),
   [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/"), and
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/"). Configure risk alerts, compliance checks, and
   performance monitoring.

## Resources

**Related best practices:**

- [SEC03-BP09
  Share resources securely with a third party](../security-pillar/sec_permissions_share_securely_third_party.md "../security-pillar/sec_permissions_share_securely_third_party.md")
- [MASEC
  2: What security tools (AWS or third-party) do you use?](../mergers-and-acquisitions-lens/masec-2.md "../mergers-and-acquisitions-lens/masec-2.md")

**Related documents:**

- [Plan
  your AWS account governance structure](../../../accounts/latest/reference/plan-acct-structure.md "../../../accounts/latest/reference/plan-acct-structure.md")

**Related videos:**

- [AWS re:Inforce 2024 - Automation in action: Strategies for risk
  mitigation (GRC301)](https://www.youtube.com/watch?v=gbo-Z01NTc8 "https://www.youtube.com/watch?v=gbo-Z01NTc8")

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
