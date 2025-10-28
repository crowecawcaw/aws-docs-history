# Cost optimization

The cost optimization pillar provides guidance to help customers apply
best practices in the design, delivery, and maintenance of their AWS
environments, with the most effective use of services and resources
at a minimal cost. Cost optimization includes the continual process
of refinement and improvement of a system over its entire lifecycle.

Many financial services institutions have low latency requirements
for trading, high performance compute requirements, and constantly
changing security and regulatory requirements. These, coupled with
extrinsic economic drivers, create a demand for robust and dynamic
cost optimization processes across all of the organization's
workloads. Many financial services companies run at enterprise
scale, and thus run hundreds of diverse workloads with large IT and
Security staff.

Compared to small and mid-sized businesses (SMBs), that typically
run an on-premises model where budgets are relatively fixed and
organizations strive to utilize allocated budgets, larger enterprise
workloads running on AWS allow customers the freedom to continuously
evolve and optimize their resources, usage, and processes to stay
efficient. That said, even SMBs can maximize their ROI by migrating
their workloads to the AWS cloud and implementing cost optimization
best practices.

From the initial design of your first proof-of-concept to the
ongoing operation of extensive production workloads, adopting the
cost optimization practices outlined in this whitepaper allows you
to build and operate cost-aware systems that achieve your business
outcomes while minimizing costs, thus allowing your business to
maximize its return on your IT investments.

For most financial services customers, there is a need to understand
cost both at an application-level and at a workload-level to improve
and optimize your costs associated with the workload.

## Design considerations

Similar to the other pillars of the Well-Architected Framework,
there are several trade-offs to consider for cost optimization.
For example, whether you plan to optimize for your
speed-to-market, versus optimizing for cost. In some cases, it's
best to optimize for speed — going to public quickly, shipping new
features, or meeting a deadline — rather than investing in upfront
cost optimization. Because you can optimize over time, you can
gradually migrate your workload to achieve higher cost
optimization once your initial products are launched.

Due to the agility of many enterprise customers' operations,
investing in reserved instances (RIs) and AWS Compute Savings Plans (SPs) and usage of spot instances can provide your team with
direct ways to save on costs, even if you do not utilize them
100%. Nonetheless, capacity planning and usage forecasting is
important for managing your commitment plans.

Design decisions are sometimes directed by haste rather than data,
and the temptation always exists to overcompensate for worst case
scenarios, rather than spend your time benchmarking for a most
cost-optimal deployment. Overcompensation can lead to
over-provisioned and under-optimized deployments. However, you may
find this to be a reasonable approach if you begin your cloud
migration by lifting and shifting resources from your on-premises
environment to the cloud. Once you have stabilized your
cloud-based workloads post-migration, then you can develop a
program to optimize them over time afterwards.

Investing the right amount of effort in a cost optimization
strategy up front allows you to realize the economic benefits of
the cloud more readily, by ensuring a consistent adherence to best
practices and avoiding unnecessary over provisioning. The
following sections provide techniques and best practices for the
initial and ongoing implementation of Cloud Financial Management
and cost optimization for your workloads

Adopting the practices in this pillar helps you
build architectures that can:

- Move your usage and costs in line with demand.
- Use appropriate services and resource types to minimize costs.
- Analyze, attribute, and forecast costs.
- Reduce costs over time.

Cost optimization is a continual process of refinement and
improvement of a system over its entire lifecycle. A
cost-optimized system aims to fully utilize all resources, achieve
an outcome at the lowest possible price point, and meet your
workload's functional and business requirements.

## Design principles

In addition to the
[design
principles](../cost-optimization-pillar/design-principles.md "../cost-optimization-pillar/design-principles.md") described in the cost optimization pillar of the
AWS Well-Architected Framework whitepaper, the Financial Services
Industry Lens identifies the following design principles to
facilitate good design in the cloud for your financial services
workloads.

These design principles can help you to build and operate
cost-aware workloads that achieve business outcomes while
minimizing costs and allowing your organization to maximize your
return on investment:

- **Monitor cost and resource
  utilization:** Financial services workload usage can
  be cyclical and can have usage spikes during specific days
  like month-end or quarter-end, or it can be intra-day during
  specific hours. AWS provides customers with a number of usage
  monitoring services that can scale your operations up and down
  as demand conditions require. Monitor cost at an
  application-level, and a workload-level on a regular basis,
  and optimize usage of resources and cost.
- **Define recovery objectives per
  workload:** FSI customers have workloads with varying
  levels of recovery objectives (RTO and RPO). A cost-conscious
  design approach considers the recovery objectives per workload
  before suggesting an appropriate DR strategy (Backup and
  restore, pilot light, warm standby or active/active).
- **Operational efficiencies:**
  FSI customers may request customization of their workloads to
  achieve certain business outcomes. Using AWS analytics tools,
  you can track, attribute, and charge back your IT costs to
  each responsible FSI business unit and organizational group.
  This encourages accountability among the teams and leads to
  better departmental management of usage costs.
- **Data transfer cost**: In many
  scenarios, the customer workloads can be running in multiple
  Regions. Monitor data transfer and storage egress costs for
  the workload.
- **Adopt cloud financial
  management:** Due to the size of many financial
  services enterprise customers, the benefits of aligning your
  IT organization with a Cloud Financial Management approach
  helps you save on the costs of both infrastructure and
  operations. To enable this capability, invest in knowledge
  building programs, resources, and processes to help become a
  more cost-efficient organization.

## Definitions

There are five focus areas for cost optimization in the cloud as
described in the cost optimization pillar of AWS Well Architected
Framework. These focus areas are applicable to all types of
workloads including financial services. In this section, we have
listed financial services-specific best practices.

- [Practice
  Cloud Financial Management](../cost-optimization-pillar/practice-cloud-financial-management.md "../cost-optimization-pillar/practice-cloud-financial-management.md")
- [Expenditure
  and usage awareness](../cost-optimization-pillar/expenditure-and-usage-awareness.md "../cost-optimization-pillar/expenditure-and-usage-awareness.md")
- [Cost-effective
  resources](../cost-optimization-pillar/cost-effective-resources.md "../cost-optimization-pillar/cost-effective-resources.md")
- [Manage
  demand and supplying resources](../cost-optimization-pillar/manage-demand-and-supply-resources.md "../cost-optimization-pillar/manage-demand-and-supply-resources.md")
- [Optimize
  over time](../cost-optimization-pillar/optimize-over-time.md "../cost-optimization-pillar/optimize-over-time.md")
