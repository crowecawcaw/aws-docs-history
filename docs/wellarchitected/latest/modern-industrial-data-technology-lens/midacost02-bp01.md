# MIDACOST02-BP01 Track resources over their lifetime

Implement complete visibility and control over resource lifecycle costs from creation to
deletion, with comprehensive tagging aligned to manufacturing processes. This includes
monitoring resource utilization against production metrics, implementing clear ownership and
purpose documentation, and regularly reviewing resource usage patterns. Essential for
understanding total cost of ownership and identifying optimization opportunities.

**Desired outcome:** Complete visibility and control over
resource lifecycle costs from creation to deletion.

**Common anti-patterns:**

- Creating resources without implementing a consistent tagging strategy from day one
- Failing to assign clear ownership of resources during provisioning
- Using generic tags that do not reflect manufacturing-specific contexts (production
  line, cell, product)
- Neglecting to track resource dependencies, leading to orphaned resources after
  decommissioning
- Maintaining resources without clear business justification
- Not implementing automated cleanup procedures for temporary resources
- Tracking only active resources while ignoring deprecated or archived industrial data
- Using the same lifecycle management approach for all data types regardless of their
  criticality or retention requirements
- Failing to consider data compliance requirements when implementing lifecycle policies
- Not accounting for seasonal production variations when evaluating resource
  utilization
- Implementing lifecycle tracking tools without proper team training and documentation
- Allowing multiple teams to create resources without centralized visibility and
  governance

**Benefits of establishing this Best Practice:**

- Improved resource utilization
- Reduced waste from unused resources
- Better understanding of resource ROI
- Enhanced cost allocation accuracy

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Inventory of all manufacturing systems (for example, SCADA, MES, and PLM)
- Mapping of data flows between shop floor and enterprise systems
- Compliance requirements for data retention in your industry

Key decisions needed:

- Resource tagging strategy aligned with production lines and processes
- Lifecycle stages specific to manufacturing data and systems
- Thresholds for resource utilization in different production scenarios

Establish a systematic approach to track resources throughout their entire
lifecycle, from provisioning to decommissioning, with appropriate governance controls for
optimal utilization and cost management in your manufacturing environment.

Consider the following:

- Mapping cloud resources to specific production lines or product types
- Tracking resource usage against production output metrics
- Implementing different lifecycle policies for operational versus analytical data
- Aligning resource reviews with production cycles or shift patterns

Regularly review resource utilization in the context of manufacturing KPIs and adjust
your tracking approach based on changes in production processes or compliance requirements.

### Implementation steps

1. Implement comprehensive tagging strategy aligned with manufacturing processes.
2. Track resource creation, modification, and usage patterns in relation to
   production cycles.
3. Monitor resource dependencies, especially between OT and IT systems.
4. Document resource ownership and purpose, involving both IT and operations teams.
5. Conduct regular reviews of resource utilization metrics against production output.
6. Implement automated reporting on resource lifecycle stages, integrated with
   manufacturing dashboards.

## Key AWS services

- AWS Config
- AWS Systems Manager
- AWS Resource Groups
- AWS Tag Editor
- AWS Cost Explorer
- AWS Application Cost Profiler
- AWS Trusted Advisor

## Resources

**Related documents:**

- [Tagging AWS Resources and Tag Editor](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md")
- [Evaluating Resources with AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")

- [AWS Resource Groups](../../../systems-manager/latest/userguide/systems-manager-resource-groups.md "../../../systems-manager/latest/userguide/systems-manager-resource-groups.md")
