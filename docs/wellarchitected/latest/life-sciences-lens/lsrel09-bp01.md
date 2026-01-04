# LSREL09-BP01 Create and verify rollback

plans

For every release or approved change, maintain a documented rollback
plan that is versioned with the release artifacts. Validate rollback
procedures in non-production environments and include rollback steps
in the change control package and test evidence. Define roles,
approvals, and communications for execution and escalation.

**Desired outcome:** Rollback
processes are predictable, validated, and repeatable so that failed
changes do not compromise operations, regulatory adherence, or data
integrity.

**Common anti-patterns:**

- Relying on undocumented or manual rollback steps.
- Skipping rollback testing due to time constraints.
- Treating rollback as optional rather than mandatory in GxP
  environments.

**Benefits of establishing this best
practice:**

- Reduces risk of prolonged downtime that can invalidate
  experiments or delay clinical timelines.
- Preserves integrity of regulated datasets and audit trails.
- Demonstrates predictable change control to auditors and
  stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Rollback plans should be created alongside release plans and
treated as first-class artifacts in change control. Plans must
include the exact steps to revert application code, configuration,
database schema, and dependent infrastructure changes. Validation
of rollback plans in staging or pre-production environments should
exercise the entire procedure (including approvals and
notifications) so that time-to-rollback and behavioral impacts are
well understood.

Where human steps are required, provide clear runbooks and defined
approvers. Where feasible, automate rollback actions to reduce
human error. Record rollback test evidence, and attach the
evidence to the validation package for auditability.

### Implementation steps

1. Create pipelines and rollback actions in AWS CodePipeline
   and codify deployment artifacts with AWS CloudFormation
   templates so infrastructure changes are reversible.
2. Use AWS CodeDeploy or CloudFormation change-sets with
   pre-defined rollback behavior.
3. Implement standardized rollback runbooks using AWS Systems Manager Automation so operators can run approved, automated
   steps.
4. Store validated rollback artifacts and test evidence in AWS CodeCommit or Amazon S3, and include change-control metadata
   for traceability.

## Resources

**Related best practices:**

- Continuity of workflows and data availability during downtime
- Fault isolation and graceful degradation in workflows
- Automated validation in deployments
