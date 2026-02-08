# HNSEC02-BP05 Tag networking resources for accountability and

access control

Implementing consistent tagging for networking resources is
essential in hybrid environments to establish clear ownership,
enforce access controls, and ensure proper governance across cloud
and on-premises infrastructure. By applying standardized tags to
networking components, organizations can effectively track resource
ownership, control who can modify critical network configurations,
and enforce the principle of least privilege. These tags enable
granular access policies where permissions can be dynamically
granted based on tag values, creating a strong foundation for
identity and access management while providing the accountability
needed for security audits and compliance requirements.

**Desired outcome:** Enable resource
ownership, cost allocation, and fine-grained access control by
ensuring all networking resources are consistently and accurately
tagged.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Increases accountability and traceability of network resources
- Enables cost allocation and chargeback by business unit or
  environment
- Facilitates automation, compliance, and operational reporting
- Supports fine-grained access control using tag-based policies

## Implementation guidance

- Establish a tagging strategy for all networking resources
- Enforce tagging standards and restrict actions on untagged
  resources. For example, you can achieve this using AWS Organizations Service Control Policies (SCPs) or IAM policies.
- Apply tag-based access control to limit who can modify,
  delete, or create specific networking resources.
- Monitor resource tagging compliance and automate remediation
  where possible using service such as AWS Config rules.

## Resources

- [Tagging
  AWS Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
- [Guidance
  for Tagging on AWS](https://aws.amazon.com/solutions/guidance/tagging-on-aws/ "https://aws.amazon.com/solutions/guidance/tagging-on-aws/")
- [Controlling
  access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")
- [Implement
  AWS resource tagging strategy using AWS Tag Policies and
  Service Control Policies (SCPs)](https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/ "https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/")
- [Implementing
  and enforcing Tagging](../../../whitepapers/latest/tagging-best-practices/implementing-and-enforcing-tagging.md "../../../whitepapers/latest/tagging-best-practices/implementing-and-enforcing-tagging.md")
- [Best
  Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")
