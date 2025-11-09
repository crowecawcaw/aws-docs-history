# MIDACOST02-BP05 Develop cloud resource policies aligned with manufacturing

operations

Create well-defined policies for cloud resource provisioning, usage, and management that
reflect specific manufacturing processes, compliance requirements, and cost optimization
goals. These policies should consider both IT and OT needs while maintaining operational
efficiency.

**Desired outcome:** Well-defined policies for cloud resource
provisioning, usage, and management that reflect specific manufacturing processes, compliance
requirements, and cost optimization goals.

**Common anti-patterns:**

- Creating generic cloud policies without considering manufacturing-specific needs
- Implementing policies that hinder rapid scaling during production spikes
- Overlooking OT or IT integration in policy development
- Failing to involve key stakeholders (for example, production managers and quality
  control) in policy creation
- Not accounting for different policy needs across various manufacturing stages
  (design, production, and maintenance)
- Implementing strict cost-saving policies that compromise manufacturing system
  reliability

**Benefits of establishing this best practice:**

- Standardized resource management
- Clear governance framework
- Aligned business and IT objectives
- Improved cost control

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Develop and implement comprehensive policies that reflect your organization's specific
manufacturing requirements while improving cost optimization.

### Implementation steps

1. Document organizational requirements:
   - Manufacturing process needs
   - Compliance requirements
   - Cost optimization targets

2. Create policy frameworks for:
   - Resource provisioning
   - Access control
   - Cost allocation
   - Data management

3. Establish review and approval processes.
4. Implement policy enforcement mechanisms.

## Key AWS services

- AWS Organizations
- AWS Control Tower
- Service Catalog
- AWS IAM
- AWS Config
- AWS CloudFormation

## Resources

**Related documents:**

- [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
- [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
- [Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md")
- [AWS Config](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
