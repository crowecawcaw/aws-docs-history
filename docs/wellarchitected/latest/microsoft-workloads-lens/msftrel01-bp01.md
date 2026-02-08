# MSFTREL01-BP01 Define availability goals for Microsoft

workloads

Identifying your organization's specific availability objectives is
crucial as it guides your focus towards critical factors. This
clarity enables you to establish relevant criteria for assessing and
selecting the most appropriate architectural patterns for your
workload.

**Desired outcome:** Have clearly
defined and documented availability requirements for Microsoft
workloads on AWS that align with business needs, enabling informed
architectural decisions and providing measurable performance targets
that support the organization's operational goals.

**Common anti-patterns:**

- Applying the same availability requirements to each of your
  Microsoft workloads without considering their individual
  business impact or criticality, leading to overprovisioning for
  less critical services or underestimating the needs of
  mission-critical applications.
- Defining initial availability goals but failing to review and
  adjust them as business needs evolve, resulting in outdated
  architectural decisions that no longer align with current
  organizational priorities or growth.

**Benefits of establishing this best
practice:**

- Clear availability requirements avoid over-engineering or
  under-engineering solutions, allocating resources efficiently
  based on actual business needs rather than assumptions and
  leading to better cost control and ROI.
- Well-defined availability goals enable precise architectural
  planning and implementation of appropriate resilience measures,
  resulting in fewer service disruptions and better alignment
  between IT capabilities and business expectations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin with stakeholder workshops to identify and document
availability requirements for each Microsoft workload. Create a
standardized template that captures key metrics (like RTO, RPO,
and SLAs) and business impact levels, then prioritize workloads
based on criticality.

Work with business units to validate these requirements, verifying
that they reflect actual operational needs rather than technical
assumptions.

Document the approved requirements in a central repository,
establish a regular review cycle (for example, quarterly), and use
these specifications to guide architectural decisions in AWS,
including the selection of appropriate Availability Zones, backup
strategies, and failover mechanisms.

### Implementation steps

1. Conduct stakeholder workshops to gather and document
   availability requirements for each Microsoft workload, using
   a standardized template to capture RTO, RPO, and SLA
   targets.
2. Create a prioritized matrix of workloads based on business
   criticality and required availability levels, validated by
   business unit leaders.
3. Establish a central documentation repository for storing and
   managing availability requirements, with clear version
   control and change management processes.
4. Develop architectural blueprints that map the documented
   availability requirements to specific AWS services and
   design patterns.
5. Implement a quarterly review cycle to reassess and update
   availability requirements, continually aligning with
   business needs and AWS best practices.

## Resources

**Related documents:**

- [Understanding
  availability need](../reliability-pillar/understanding-availability-needs.md "../reliability-pillar/understanding-availability-needs.md")
