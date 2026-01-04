# LSOPS07-BP01 Maintain a controlled multi-account

environment

Implement standardized account management using templated
environments and automated account provisioning. Establish
organizational guardrails through policies and baseline
configurations. Maintain centralized control over shared services
while providing consistent security across accounts.

**Desired outcome:** Identifiable
resource allocation

**Common anti-patterns:**

- Combining resources into a single account and attempting to
  separate it with complex rules.

**Benefits of establishing this best
practice:** Improved security and auditability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement a structured multi-account strategy that separates
workloads based on their regulatory requirements, security needs,
and operational characteristics. Centralized governance mechanisms
can enforce consistent controls across the accounts while allowing
appropriate flexibility for different workload types. Standardized
account provisioning verifies that new environments are created
with baseline controls already in place, while continuous
monitoring verifies ongoing adherence to organizational standards.

When implementing a controlled multi-account environment, balance
centralized governance with workload-specific requirements.
Establish clear guidelines for account structure and
responsibility boundaries, but allow teams appropriate autonomy
within those guardrails. Implement preventive controls for
critical requirements while using detective controls and
remediation for less critical aspects. This approach maintains
appropriate control while enabling innovation and operational
efficiency.

### Implementation steps

1. Design a multi-account structure aligned with regulatory
   boundaries:

- Implement AWS Organizations for hierarchical account
  management.
- Consider AWS Control Tower for standardized account
  governance.

1. Establish centralized identity and access management:

- Configure AWS IAM Identity Center for centralized user
  management.
- Consider AWS IAM Roles for fine-grained permission controls.

1. Implement standardized account provisioning processes:

- Use AWS Control Tower Account Factory for consistent account
  creation.
- Consider Service Catalog for standardized environment
  provisioning.

1. Deploy preventive guardrails for critical requirements:

- Configure AWS Organizations Service Control Policies (SCPs)
  for preventive controls.
- Consider AWS Control Tower Guardrails for additional
  preventive measures.

1. Establish baseline configurations across accounts:

- Use AWS CloudFormation StackSets for multi-account resource
  deployment.
- Consider AWS Systems Manager for configuration management.

1. Implement centralized monitoring and verification:

- Configure AWS Config Aggregators for multi-account
  visibility.
- Consider AWS Security Hub CSPM for consolidated security and
  monitoring.

## Resources

**Related documents:**

- [Walkthrough:
  Automate Account Provisioning in AWS Control Tower by Service
  Catalog APIs](../../../controltower/latest/userguide/automated-provisioning-walkthrough.md "../../../controltower/latest/userguide/automated-provisioning-walkthrough.md")

**Related examples:**

- [AWS Samples: AWS Control Tower Automate Account Creation](https://github.com/aws-samples/aws-control-tower-automate-account-creation "https://github.com/aws-samples/aws-control-tower-automate-account-creation")
- [Automate
  account customization using Account Factory Customization in
  AWS Control Tower](https://aws.amazon.com/blogs/mt/automate-account-customization-using-account-factory-customization-in-aws-control-tower/ "https://aws.amazon.com/blogs/mt/automate-account-customization-using-account-factory-customization-in-aws-control-tower/")

**Related tools:**

- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [AWS CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Resource
  Access Manager](https://aws.amazon.com/ram/ "https://aws.amazon.com/ram/")
