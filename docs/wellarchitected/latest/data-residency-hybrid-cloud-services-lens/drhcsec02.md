# DRHCSEC02-BP01 Separate workloads that have different data residency requirements

As attempting to implement different sets of preventative and
detective controls in the same AWS account is complicated at best,
we highly recommend separating workloads into different accounts
especially when their data residency requirements are different.

**Desired outcome:** An account
structure that allows for separation of workloads with different
data residency requirements into separate accounts, increasing
compliance across the cloud infrastructure.

**Common anti-patterns:**

- Placing multiple workloads with different data residency
  requirements into the same account

**Benefits of establishing this best
practice:** Lowers risk of non-compliance by eliminating
sources of exceptions to preventative and detective control
implementations. Lowers cost of implementation and testing of
controls by minimizing complexity.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AWS accounts provide a security isolation boundary between
workloads or resources that operate at different sensitivity
levels. AWS provides tools to manage your cloud workloads at
scale through a multi-account strategy to leverage this
isolation boundary. For guidance on the concepts, patterns, and
implementation of a multi-account strategy on AWS, see
[Organizing
Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md").

### Implementation steps

1. Identify and group workloads which have the same set of data
   residency requirements
2. **Design an organizational unit
   structure:** A properly designed organizational
   unit structure reduces the management burden required to
   create and maintain service control policies and other
   security controls. Your organizational unit structure should
   be
   [aligned
   with your data residency requirements, business needs, data
   sensitivity, and workload structure](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/ "https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/").
3. **Create a landing zone for your
   multi-account environment:** A landing zone
   provides a consistent security and infrastructure foundation
   from which your organization can quickly develop, launch,
   and deploy workloads. You can use a
   [custom-built
   landing zone or AWS Control Tower](../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md "../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md") to orchestrate your
   environment.

### Resources

- [SEC01-BP01
  Separate workloads using accounts](../security-pillar/sec_securely_operate_multi_accounts.md "../security-pillar/sec_securely_operate_multi_accounts.md")
