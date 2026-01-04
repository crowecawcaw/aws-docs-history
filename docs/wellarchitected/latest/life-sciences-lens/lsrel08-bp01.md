# LSREL08-BP01 Incorporate validated redundancy into architecture

design

During the design phase, plan for redundancy across fault-isolated
zones and validate that each component meets regulatory
requirements. Qualification of secondary systems should not be an
afterthought but part of the original architecture plan. Document
design decisions to show how redundancy supports both technical
reliability and regulatory obligations.

**Desired outcome:** Workloads remain
available during component failures, and redundant systems are
equally validated for adherence.

**Common anti-patterns:**

- Treating secondary systems as non-validated backups rather than
  qualified components.
- Adding redundancy late in design, creating gaps.
- Documenting only the primary system in validation records.

**Benefits of establishing this best
practice:** Improves confidence in availability without
compromising regulatory expectations. Provides reproducible
architectural evidence for audits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When planning workload architecture, design for multi-zone
redundancy from the start. Your validation protocols should
explicitly include redundant components, not just primaries. For
each architecture diagram and system description, demonstrate that
redundant paths preserve the same adherence controls, including
data capture and security safeguards. Qualification evidence
should reflect the entire redundant system architecture as
validated.

### Implementation steps

1. Define multi-AZ or multi-Region designs in your architecture
   blueprints and validate them in qualification testing.
2. Document redundancy plans in your system design
   specifications and standard operating procedures.
3. Use AWS services such as Amazon RDS Multi-AZ, Amazon S3
   cross-region replication, or ELB across
   multiple Availability Zones, verifying that validation
   records include both primary and redundant configurations.
