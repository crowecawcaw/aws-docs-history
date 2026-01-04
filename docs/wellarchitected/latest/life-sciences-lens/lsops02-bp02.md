# LSOPS02-BP02 Implement regulatory

reviews

Incorporate and electronically document formal reviews throughout
the project lifecycle to improve regulatory adherence. This includes
initial framework assessment reviews, design control gates, change
management reviews, pre-submission readiness checks, and periodic
audits to verify ongoing adherence. Document the decisions and
maintain traceability of regulatory requirements implementation
throughout each stage.

**Desired outcome:** A systematic,
documented review process that improves regulatory adherence at
every stage of the project lifecycle, with clear evidence of
requirements verification, issue remediation, and approval decisions
that satisfy regulatory expectations.

**Common anti-patterns:**

- Conducting reviews only at project completion rather than
  throughout the lifecycle.
- Treating reviews as checkboxes rather than substantive
  evaluations.

**Benefits of establishing this best
practice:**

- Early identification and remediation of audit issues.
- Reduced regulatory submission risks.
- Streamlined audit processes.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish a formal review framework with clearly defined stages
aligned to your development lifecycle. Define specific entry and
exit criteria for each review gate, which explicitly addresses
regulatory requirements. Implement electronic documentation
systems that maintain review histories, decisions, and supporting
evidence.

Regulatory reviews should be integrated into your project
lifecycle rather than treated as separate activities. Map key
decision points in your development process where regulatory
reviews provide maximum value. These typically include initial
planning, design completion, pre-implementation,
post-implementation, and pre-submission phases.

Create standardized templates and checklists for each review type
for consistent evaluation. Involve cross-functional teams
including regulatory affairs, quality assurance, technical
experts, and business stakeholders to provide comprehensive
evaluation from multiple perspectives.

### Implementation steps

1. Configure AWS Systems Manager Change Calendar with a
   DEFAULT_CLOSED entry to block changes
   during regulatory review windows.
2. Develop AWS Systems Manager Automation documents to automate
   approved changes based on review procedures and findings.
3. Implement AWS Audit Manager assessments for periodic audit
   verification.

## Resources

**Related examples:**

- [Change
  Management for Life Sciences](https://aws.amazon.com/blogs/mt/change-management-for-life-sciences/ "https://aws.amazon.com/blogs/mt/change-management-for-life-sciences/")
- [Automated
  Evidence Collection for Life Sciences continuous compliance
  solutions using AWS Audit Manager](https://aws.amazon.com/blogs/mt/automated-evidence-collection-for-life-sciences-continuous-compliance-solutions-using-aws-audit-manager/ "https://aws.amazon.com/blogs/mt/automated-evidence-collection-for-life-sciences-continuous-compliance-solutions-using-aws-audit-manager/")

**Related tools:**

- [AWS Systems Manager Documents](../../../systems-manager/latest/userguide/documents.md "../../../systems-manager/latest/userguide/documents.md")
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
