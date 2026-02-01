# DSREL01-BP07 Create manual backup plans for system

outages

In highly regulated industries, manual contingency plans are
essential for maintaining business continuity and regulatory
compliance when primary systems fail. These plans serve as critical
fallback procedures that enable organizations to continue operations
and protect customer data while addressing technical failures. This
practice assists in avoiding compliance violations, financial
penalties, and reputational damage.

**Desired outcome:** Critical
business operations continue with minimal disruption during system
outages, maintaining service levels and regulatory compliance.

**Common anti-patterns:**

- Assuming automated systems and recovery mechanisms work in every
  scenario without manual backup procedures.
- Maintaining outdated or incomplete procedures that haven't been
  validated through regular drills.
- Creating single points of failure by not clearly defining roles
  or training multiple staff on manual processes.
- Failing to align manual procedures with industry-specific
  compliance requirements and audit obligations.
- Lacking clear escalation paths and failing to prepare necessary
  tools for manual operations.

**Benefits of establishing this best
practice:**

- Maintains operational continuity and minimizes downtime during
  system outages.
- Demonstrates proactive risk management and meets regulatory
  requirements for business continuity.
- Enables immediate action and streamlined decision-making rather
  than waiting for system restoration.
- Maintains service levels and communication during incidents,
  protecting brand reputation.
- Creates a trained workforce capable of running critical
  functions under challenging conditions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Begin by identifying mission-critical systems and mapping
dependencies. Develop clear, role-based procedures for manual
operations, and integrate these plans into broader disaster
recovery strategies. Regularly test and refine processes to
address gaps.

### Implementation steps

1. Identify and document critical systems using
   [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") and
   [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/"), defining priorities for core
   services, business applications, data stores, and
   infrastructure components.
2. Define recovery objectives per system, including RTO, RPO,
   maximum tolerable downtime, and data loss tolerance, using
   [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/") and documenting requirements.
3. Map dependencies using
   [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") and
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/"), documenting service dependencies, data flows,
   network connections, and external services.
4. Develop role-based procedures for operations, security,
   application owners, and support staff, documenting using
   [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") Documents and including validation
   steps.
5. Configure monitoring with
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") for system metrics, service status,
   recovery progress, and compliance checks, setting up alerts
   and creating dashboards.
6. Implement a comprehensive documentation management system
   (DMS), creating operation manuals, quick reference guides,
   troubleshooting guides, and contact lists, with version
   control and scheduled reviews. Services that can support DMS
   include
   [AWS Amazon Kendra](https://aws.amazon.com/kendra/ "https://aws.amazon.com/kendra/"),
   [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") alongside
   [AWS Cloud Storage](https://aws.amazon.com/products/storage/ "https://aws.amazon.com/products/storage/") and
   [AWS Databases](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/").

## Resources

**Related best practices:**

- [OPS10-BP01 Use a process for event, incident, and problem management](../operational-excellence-pillar/ops_event_response_event_incident_problem_process.md "../operational-excellence-pillar/ops_event_response_event_incident_problem_process.md")
- [SEC06-BP03 Reduce manual management and interactive access](../security-pillar/sec_protect_compute_reduce_manual_management.md "../security-pillar/sec_protect_compute_reduce_manual_management.md")
- [REL13-BP01
  Define recovery objectives for downtime and data loss](../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md "../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md")

**Related documents:**

- [AWS Resilience Hub User Guide](../../../resilience-hub/latest/userguide/what-is.md "../../../resilience-hub/latest/userguide/what-is.md")
- [AWS Systems Manager Documents](../../../systems-manager/latest/userguide/sysman-ssm-docs.md "../../../systems-manager/latest/userguide/sysman-ssm-docs.md")
- [Business
  Resilience](https://aws.amazon.com/executive-insights/business-resilience/ "https://aws.amazon.com/executive-insights/business-resilience/")
- [What is
  DMS](https://aws.amazon.com/what-is/dms/ "https://aws.amazon.com/what-is/dms/")

**Related videos:**

- [Backup
  and Disaster Recovery Strategies for Increased Resilience: Leveraging AWS Services for Cost-Effective Business Continuity](https://aws.amazon.com/awstv/watch/173a403d06b/ "https://aws.amazon.com/awstv/watch/173a403d06b/")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
