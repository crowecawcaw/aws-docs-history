# TELCOOPS02-BP01 Telecommunication resources, operations and

projects have identified owners

Establish clear ownership and accountability frameworks for telecommunications assets,
operations, and projects through formal assignment of responsibilities to specific individuals
or teams. This includes mapping ownership of applications, VNFs, solutions, and infrastructure
components while documenting their business value proposition and justification for ownership
allocation. Clear ownership structures enable efficient decision-making, streamlined problem
resolution, and effective resource management across the telecommunications environment.

**Desired outcome:**

- Clear ownership structure for resources.
- Documented responsibilities and accountabilities.
- Efficient resource allocation.
- Streamlined decision-making process.
- Effective resource management.
- Clear escalation paths.

**Common anti-patterns:**

- Undefined resource ownership.
- Shared responsibilities without clear boundaries.
- Missing accountability frameworks.
- Incomplete resource documentation.
- Unclear decision authority.
- Resource orphaning.
- Ambiguous escalation paths.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Establish a comprehensive resource ownership model that clearly defines responsibilities
for telecommunications assets, operations, and projects. Implement a centralized resource
management system that tracks ownership details, including primary and secondary owners,
escalation paths, and relevant stakeholders. Create detailed RACI (responsible, accountable,
consulted, informed) matrices for each major resource category to verify clear understanding
of roles and decision-making authority. Develop standardized handover procedures and
documentation requirements to maintain continuity during ownership transitions or
organizational changes.

### Implementation steps

- Implement AWS Resource Groups and Tag Editor to define and manage resource ownership tags, and
  integrate with AWS Organizations for hierarchical resource management.
- Use AWS Config to maintain resource inventory and relationships and AWS Systems Manager Resource
  Groups for logical grouping of resources by ownership.
- Deploy Service Catalog for standardized resource provisioning with predefined ownership tags and
  AWS CloudFormation for automated resource creation with ownership metadata.
- Configure AWS Config Rules for ownership monitoring and Amazon CloudWatch for resource utilization
  tracking by owner.
- Use AWS Systems Manager OpsCenter for ownership-related operations management and AWS
  Resource Access Manager for controlled resource sharing.

## Resources

**Key AWS services:**

- [Resource Groups and
  Tagging for AWS](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/ "https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
