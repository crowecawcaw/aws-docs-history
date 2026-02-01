# DSREL03-BP01 Design automated jurisdiction-aware,

fully-observable recovery procedures

Highly regulated industries need automated recovery procedures that
take into account the applicable jurisdiction. These procedures must
comply with data sovereignty laws and industry-specific regulations.
Compliance-aligned recovery automation assists in reducing
inadvertent violations during incidents while maintaining rapid
response capabilities. This approach provides complete audit trails
and enables organizations to reduce potential legal penalties and
business disruption.

**Desired outcome:** Disaster
recovery procedures maintain jurisdictional adherence and data
sovereignty requirements while providing rapid recovery capabilities
and complete audit trails.

**Common anti-patterns:**

- Automatically replicating data across Regions without
  understanding or respecting local data protection laws and
  regulatory requirements.
- Implementing generic or black-box recovery procedures that lack
  transparency and jurisdiction-specific considerations.
- Failing to regularly test recovery procedures in
  compliance-constrained scenarios and lacking automated
  compliance checks.
- Missing comprehensive audit trails and automated notification
  workflows for regulators and compliance teams.
- Not monitoring for regulatory changes and failing to maintain
  dynamic region-specific configurations.

**Benefits of establishing this best
practice:**

- Pre-validated, automated procedures reduce downtime and minimize
  manual compliance verification steps.
- Automated enforcement of jurisdictional requirements and data
  residency rules reduce the chances of potential compliance
  violations during recovery.
- Comprehensive audit trails and transparent recovery procedures
  satisfy regulatory requirements.
- Jurisdiction-aware automation and predefined procedures assists
  with reducing human error and inadvertent violations.
- Improved confidence from regulators and auditors while
  optimizing costs through reduced manual oversight and avoided
  penalties.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design a compliance-first recovery architecture that embeds
regulatory requirements directly into automation logic using AWS
services.

### Implementation Steps

1. Map regulatory requirements to technical controls using
   [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/"),
   [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") Cloud Security Posture Management
   (CSPM),
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") Rules and
   [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") runbooks for automated compliance
   validation and remediation.
2. Implement infrastructure as code templates for
   jurisdiction-aware recovery workflows with appropriate
   regional controls using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/").
3. Use resource tagging and
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") service control policies (SCPs) to
   enforce data sovereignty requirements and block unauthorized
   cross-Region transfers.
4. Deploy comprehensive observability using
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/"),
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), and centralized logging for immutable
   audit trails.
5. Establish policy-driven recovery frameworks that evaluate
   compliance constraints before running recovery actions using
   [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/"),
   [AWS Elastic Disaster Recovery (DRS)](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/"),
   [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/").

This approach facilitates automated, compliance-aligned recovery
processes while maintaining complete visibility for regulatory
reporting.

## Resources

**Related best practices:**

- [OPS01-BP03
  Evaluate governance requirements](../operational-excellence-pillar/ops_priorities_governance_reqs.md "../operational-excellence-pillar/ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [REL13-BP05
  Automate recovery](../reliability-pillar/rel_planning_for_recovery_auto_recovery.md "../reliability-pillar/rel_planning_for_recovery_auto_recovery.md")

**Related videos:**

[AWS re:Inforce 2023 - Best practices for cloud governance at scale
(GRC305)](https://www.youtube.com/watch?v=RBfJFINO3m8 "https://www.youtube.com/watch?v=RBfJFINO3m8")

**Related services:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
