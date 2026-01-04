# LSREL09-BP05 Implement risk-based change control for validated

systems

Establish a structured, risk-based change control process that
categorizes changes according to their potential impact on product
quality, patient safety, and data integrity. Apply proportional
testing and validation depending on the change classification.
High-risk changes to GxP systems should undergo rigorous
verification and dual review, while low-risk changes may be handled
with streamlined procedures. Track, approve, and document changes,
and update validation evidence to confirm the system remains in a
validated state after the change.

**Desired outcome:** Changes are
assessed, approved, tested, and documented based on risk so that
systems remain reliable and validated.

**Common anti-patterns:**

- Treating each change identically.
- Making undocumented infrastructure changes.
- Failing to demonstrate that the validated state was preserved.

**Benefits of establishing this best
practice:** Maintains continuity of validated research
systems, reduces audit findings, and minimizes the chance of
change-related downtime or data issues.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk-based change control should be embedded in governance
processes. Each proposed change should be assessed for potential
impact on regulated workloads. Testing scope and depth must scale
with risk, and approval workflows should reflect that
classification. Documentation should be continuously updated so
there is a clear link between requirements, specifications,
executed tests, and evidence that the validated state was
maintained.

### Implementation steps

1. Use AWS Config to track infrastructure changes and maintain
   a configuration history.
2. Codify infrastructure in AWS CloudFormation with change sets
   for controlled, reversible changes.
3. Store approvals, validation results, and associated
   artifacts in Amazon S3 with Object Lock for immutability.
4. Use AWS Audit Manager to map evidence against regulatory
   controls and demonstrate ongoing validation.
