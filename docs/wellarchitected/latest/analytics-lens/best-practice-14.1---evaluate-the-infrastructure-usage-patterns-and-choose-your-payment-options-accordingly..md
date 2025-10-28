# Best practice 14.1 – Evaluate the infrastructure usage patterns and choose your payment options accordingly

On-demand resources provide immense ﬂexibility with
pay-as-you-go payment models across multiple scenarios and
scales. Alternately, Reserved Instances provide significant
cost saving for workloads that have steady resource
utilization and serverless options for unpredictable demand. Perform regular workload resource usage
analysis. Choose the best pricing model to ensure that you
don’t miss cost optimization opportunities and maximize your
discounts.

## Suggestion 14.1.1 – Evaluate available payment options of the infrastructure resources of your choice

Review the pricing page for specific AWS services. Each
service will list the billing metrics, such as runtime or
gigabytes processed, as well as any discount options for
dedicated usage. In addition, many AWS analytics services
offer discounted payment terms, Reserved Instances, or
Savings Plans, in exchange for a specific usage commitment.
Almost all AWS services offer the payment for usage on
demand, meaning you only pay for what you use.

## Suggestion 14.1.2 – For steady, permanent workloads, obtain Reserved Instances or Savings Plans price discounts instead of paying On-Demand Instance pricing

Reserved Instances give you the option to reserve some AWS
resources for a one- or a three-year term. In turn, you
will receive a significant discount compared with the
On-Demand Instance pricing. Workloads that have consistent
long-term usage are good candidates for the Reserved
Instance payment option.

## Suggestion 14.1.3 – Use either on-demand, spot or serverless resources during development and in pre-production environments

Development and pre-production environments frequently change and often do not require 100% availability. Use on-demand instances with start and stop resources, or serverless resources in cases where workload utilization is unpredictable, frequently changes, or is only used for portions of the day. You can use spot instances for fault-tolerant and flexible big data analytics applications. Spot instances are available at up to a 90% discount compared to on-demand prices. Spot instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes.

For more detail, refer to the following:

- [Optimize Cost by Automating the Start or Stop of Resources in Non-Production Environments Spot Instance Best Practices](https://aws.amazon.com/blogs/architecture/optimize-cost-by-automating-the-start-stop-of-resources-in-non-production-environments/ "https://aws.amazon.com/blogs/architecture/optimize-cost-by-automating-the-start-stop-of-resources-in-non-production-environments/")
- [Optimizing Amazon EC2 Spot Instances with Spot Placement Scores](https://aws.amazon.com/blogs/compute/optimizing-amazon-ec2-spot-instances-with-spot-placement-scores/ "https://aws.amazon.com/blogs/compute/optimizing-amazon-ec2-spot-instances-with-spot-placement-scores/")
