# LSOPS02-BP01 Establish a central control

framework

Establishing a central control framework and mapping to applicable
frameworks can simplify processes, avoid duplicate effort, and
reduce operational overheads. The IT quality team can define the
required control objectives, while IT process and tooling experts
can determine the best way to implement the controls.

**Desired outcome:**

- Unified control framework that maps to multiple regulatory
  requirements.
- Reduced duplication of efforts across different frameworks.
- Streamlined audit processes with centralized evidence
  collection.

**Common anti-patterns:**

- You implement separate controls for each framework.
- You lack clear mapping between control objectives and regulatory
  requirements.
- You create duplicate controls that are common across frameworks.

**Benefits of establishing this best
practice:**

- Streamlined reporting through consolidated evidence collection.
- Reduced audit preparation time and resource requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a hierarchical structure with clear accountability that
bridges the gap between high-level objectives and specific
technical implementations. This structure should incorporate
risk-based prioritization to focus resources on the most critical
controls while maintaining comprehensive coverage of requirements.

### Implementation steps

1. Inventory the applicable regulatory frameworks and
   requirements:

- Use AWS Audit Manager to catalog regulatory requirements
  across frameworks and collect evidence of auditing.
- Consider AWS Systems Manager Documents for standardized
  documentation.

1. Create a unified control catalog with clear mapping to
   regulatory requirements:

- Implement AWS Systems Manager Parameter Store for
  centralized control definitions.
- Consider Service Catalog for managing approved control
  implementations that can be deployed to multiple workloads.

1. Establish control ownership and responsibilities across
   teams:

- Use AWS Resource Access Manager for sharing control
  resources across teams.
- Consider AWS Organizations for defining organizational
  control responsibilities.

1. Develop standardized templates for control documentation and
   evidence collection:

- Store templates in Amazon S3 with appropriate access
  controls.
- Consider AWS CloudFormation for templating control
  implementation patterns.

1. Implement continuous monitoring of control effectiveness:

- Configure AWS Config Rules to verify control implementation.
- Consider AWS Security Hub CSPM for aggregating control status.

## Resources

**Related guides, videos, and
documentation:**

- [Don't
  Blame Regulators: How Software Excellence Satisfies
  Compliance](https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/ "https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/")

**Related examples:**

- [Conformance
  Pack Sample Templates for AWS Config](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md")
- [Streamline
  compliance management with AWS Config custom rules and
  conformance packs](https://aws.amazon.com/blogs/mt/streamline-compliance-management-with-aws-config-custom-rules-and-conformance-packs/ "https://aws.amazon.com/blogs/mt/streamline-compliance-management-with-aws-config-custom-rules-and-conformance-packs/")

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [AWS Resource
  Access Manager](https://aws.amazon.com/ram/ "https://aws.amazon.com/ram/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
