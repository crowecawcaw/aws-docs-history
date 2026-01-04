# LSREL12-BP02 Define recovery time objectives based on

scientific and business impact

Recovery time objectives (RTOs) should be established through
analysis of the scientific and business impact of downtime. For
clinical trial systems, delays may affect patient safety or data
collection. For manufacturing or analytical systems, downtime may
disrupt schedules, supply chains, or data reproducibility. RTOs must
be documented and justified in continuity planning.

**Desired outcome:**

- Recovery time targets reflect business and scientific
  criticality.
- Downtime risks are balanced against cost of recovery
  capabilities.
- RTOs are documented and approved as part of continuity planning.

**Common anti-patterns:**

- Arbitrary RTOs set without input from science or operations
  stakeholders.
- Uniform recovery targets across systems.
- Failure to periodically review RTOs as workloads evolve.

**Benefits of establishing this best
practice:**

- Verifies that critical research and clinical activities resume
  within acceptable windows.
- Avoids over-investment in low-priority systems while
  safeguarding high-value workloads.
- Builds alignment between IT, R&D, QA, and business
  stakeholders.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Conduct impact analyses for each workload, identifying scientific,
regulatory, and operational consequences of downtime. Define
system-specific RTOs based on these findings and align them with
acceptable risk tolerances. Document RTOs in continuity and
disaster recovery plans, and review them regularly to keep them
appropriate as workloads scale.

### Implementation steps

1. Use AWS Well-Architected Resilience Hub to document RTO
   targets for workloads.
2. Configure Amazon RDS Multi-AZ for critical databases to meet
   short RTOs, while less critical workloads can use Amazon Glacier for slower recovery.
3. Run recovery drills using AWS Elastic Disaster Recovery
   (DRS) to validate RTO adherence.
4. Record results in AWS Audit Manager for tracking.
