# LSREL04-BP01 Map regulatory requirements to reliability

controls

Create a comprehensive mapping between applicable regulatory
requirements (like GxP, 21 CFR Part 11, and GDPR) and your
reliability controls. Document how each control satisfies specific
regulatory requirements and maintain this mapping as regulations
evolve. For example, if regulations require system availability of
99.9% for critical applications, implement and document the
architecture decisions, monitoring systems, and recovery procedures
that support this requirement.

**Desired outcome:** A clear,
documented traceability matrix between regulatory requirements and
implemented reliability controls that demonstrates adherence and
guides architecture decisions. This mapping serves as evidence
during audits and inspections while verifying that reliability
measures directly address regulatory obligations.

**Common anti-patterns:**

- Implementing reliability controls without considering regulatory
  requirements.
- Failing to document how reliability controls satisfy specific
  regulations.
- Not updating the mapping when regulations or system architecture
  changes.
- Focusing only on technical controls without considering
  procedural and documentation requirements.

**Benefits of establishing this best
practice:**

- Provides clear evidence of regulatory adherence for audits and
  inspections.
- Aligns reliability investments with regulatory priorities.
- Facilitates impact assessment when regulations change.
- Supports risk-based decision making for reliability investments.

## Implementation guidance

Use AWS Config to track configuration changes that might affect
adherence to regulatory requirements.

Consider implementing AWS Audit Manager to continuously audit your
AWS usage to simplify risk assessment and adherence with
regulations.

Implement tagging strategies to identify resources subject to
specific regulatory requirements.

Use AWS Systems Manager documents to standardize and automate
checks.

### Implementation steps

1. Identify the applicable regulatory requirements related to
   system reliability (like FDA, EMA, and ICH).
2. Create a traceability matrix documenting each requirement
   and corresponding control.
3. Use AWS Config to establish configuration rules that enforce
   regulatory requirements.
4. Implement AWS CloudWatch alarms to monitor adherence to
   availability requirements.
5. Document architecture decisions that support regulatory
   requirements using AWS Well-Architected Tool.
6. Establish a review process to update the mapping when
   regulations or systems change.

## Resources

**Related best practices:**

- Implement comprehensive monitoring for regulated systems
- Establish reliability qualification procedures
- Design for fault isolation and  graceful degradation
