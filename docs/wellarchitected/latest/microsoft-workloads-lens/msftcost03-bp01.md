# MSFTCOST03-BP01 Understand Microsoft SQL Server licensing and

BYOL availability

AWS offers a range of flexible cost optimization choices for
licensing. These licensing options are designed to help you reduce
costs, maintain compliance, and meet your business needs. AWS offers
the license include option, which you can launch Windows EC2
instances with SQL Server installed and licensed on-demand, paying
only for what you use. With the right requirements, you can also
bring your own licenses to AWS, either to Amazon EC2 Dedicated Hosts
or default (shared) tenancy.

**Desired outcome:** Optimize costs
by thoroughly evaluating Microsoft SQL Server licensing options on
AWS, including both the license-included model for on-demand usage
and the Bring Your Own License (BYOL) approach for either Amazon EC2
Dedicated Hosts or default shared tenancy, ensuring that the chosen
licensing strategy aligns with compliance requirements, maximizes
cost savings, and effectively supports business objectives through
AWS's flexible licensing framework.

**Common anti-patterns:**

- Automatically defaulting to license-included instances without
  analyzing BYOL cost benefits, potentially missing out on
  significant savings from existing Microsoft Enterprise
  Agreements or Software Assurance benefits that could be
  leveraged on AWS.
- Failing to properly track and document SQL Server deployments
  across different AWS environments, leading to over-provisioned
  licenses or compliance risks from unintentionally running SQL
  Server workloads on shared tenancy when BYOL requires dedicated
  hosts.
- Choosing licensing models based solely on immediate costs
  without considering long-term implications, such as selecting
  on-demand licensing when workloads are actually stable and
  predictable, resulting in higher total cost of ownership
  compared to BYOL options.

**Benefits of establishing this best
practice:**

- Significant Cost Optimization: By carefully evaluating and
  implementing the most appropriate licensing model (BYOL versus
  license-included), organizations can achieve substantial cost
  savings through efficient license utilization, maximizing
  existing investments in Microsoft agreements, and aligning
  licensing costs with actual usage patterns.
- Enhanced Compliance and Risk Management: Proper licensing
  practices ensure continuous compliance with Microsoft's
  licensing terms and AWS's infrastructure requirements, reducing
  the risk of audit findings, unexpected true-up costs, and
  potential penalties while maintaining clear documentation of
  license deployment and usage.
- Improved Operational Flexibility: Understanding and implementing
  the right licensing strategy enables organizations to scale
  their SQL Server workloads more effectively, choose the most
  cost-effective deployment options (dedicated hosts versus shared
  tenancy), and maintain the agility to adjust licensing
  approaches as business needs evolve.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement effective Microsoft SQL Server licensing on AWS,
start by inventorying existing licenses and analyzing workload
patterns to determine the most cost-effective option between BYOL
and license-included models. Establish clear documentation and
tracking processes using AWS License Manager, and implement
regular reviews to optimize costs while maintaining compliance
with both Microsoft and AWS requirements.

### Implementation steps

1. Conduct a comprehensive inventory of existing SQL Server
   licenses and associated rights (AWS OLA can be useful as
   well).
2. Analyze workload characteristics and usage patterns to
   determine the most cost-effective licensing model (BYOL
   versus license-included).
3. Set up AWS License Manager to track and manage SQL Server
   deployments across your AWS environment.
4. Implement a tagging strategy to accurately monitor and
   allocate SQL Server licensing costs.
5. Establish a regular review process to optimize licensing
   strategy and ensure ongoing compliance with Microsoft and
   AWS requirements.

## Resources

**Related documents:**

- [Understand
  SQL Server licensing](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.md")
- [Amazon Web Services and Microsoft FAQs](https://aws.amazon.com/windows/faq/ "https://aws.amazon.com/windows/faq/")

**Related tools:**

- [What
  is AWS License Manager?](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md")
