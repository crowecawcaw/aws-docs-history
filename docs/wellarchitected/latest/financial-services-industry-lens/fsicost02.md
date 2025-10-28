# FSICOST02: Do you apply the Pareto-principle (80/20 rule) to manage, optimize, and

plan your cloud usage and spend?

Investing the right amount of effort in a cost optimization strategy up front allows you to realize the economic benefits of the cloud more readily, by ensuring a consistent adherence to best practices and avoiding unnecessary over provisioning. CFM is paramount not only to effectively manage costs, but also to verify that investments are driving expected business outcomes.

## FSICOST02-BP01 Apply the Pareto-principle 80/20 rule for

your CFM efforts

No matter your organization size, pay specific attention to your capacity
investment while developing CFM-related concepts. Here are some examples of CFM
activities to apply the 80/20 rule to create an optimal input/output solution.

- Cost allocation: Start with default allocation opportunities (per
  AWS account, AWS-generated `createdBy` tag), then follow up by
  tagging all AWS services that support tagging, check overall percentage of cost
  allocation. In case you reach 80% cost allocation, check if equal allocation of the
  unallocated 20% of costs is acceptable for your organization (for example, splitting
  AWS service cost equally between business units or teams). Before spending time
  and budget on a third-party solution (for example, telemetry) ensure that shared
  resources you aim to allocate are substantial (for example, over 20% of monthly
  bill).

- Cost optimization: Incorporate implementation of low-hanging cost optimization
  recommendations (from Cost Explorer or AWS Trusted Advisor) into daily activities of your teams.
  Centralized teams evaluate and book SP and RI quarterly, decentralized teams perform
  instance rightsizing and modernization weekly. CFM practitioners report it is more
  efficient to spend 30 minutes per week rather than one day per month. While
  implementing cost optimization that require technical changes, pay attention to long
  term benefits – one-time adjustments provide reoccurring savings. Evaluate time and
  capacity invested into technical adjustments versus cost saving for at least the
  next 24 months. These types of calculations help prioritize activities with the
  highest impact.
