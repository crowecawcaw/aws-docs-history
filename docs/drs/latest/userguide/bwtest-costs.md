

# Costs
<a name="bwtest-costs"></a>

This procedure has two cost line items, and the second is the larger one.
+ The instance-hour is minor for the lifetime of a test, and an in-use public IPv4 address adds a small hourly charge on top of it.
+ Data transfer out dominates. Each measurement run moves real data (a 30-second download phase at 5 Gbps is roughly 18 GB), and data transfer out to the internet is billed per GB beyond the monthly free allowance. Traffic that stays inside the VPC is billed differently and is generally far cheaper, which is one more argument for the private path.

Check current rates for your Region on the [AWS Pricing](https://aws.amazon.com/pricing/) and [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) pages rather than relying on the figures quoted here.