# TELCOCOST02-BP01 Implement dynamic CNF sizing and scaling

strategies based on actual subscriber demands and usage patterns

In traditional on-premises environments, CNF infrastructure is typically sized for peak
capacity expected over the hardware lifetime. To optimize costs in cloud environments,
organizations should implement dynamic sizing strategies that align infrastructure capacity with
actual subscriber demands. This includes utilizing cloud-based auto scaling capabilities,
implementing rightsizing based on usage patterns, and designing CNF architectures that support
horizontal scaling. The approach should balance performance requirements with cost efficiency
while maintaining the ability to handle growth in subscriber demand through elastic
infrastructure scaling.

**Desired outcome:**

- Optimize the cost of your cloud-based network functions (CNFs) by right-sizing
  resources based on actual usage.
- Verify CNF performance meets service-level objectives while minimizing
  over-provisioning.
- Achieve cost savings by dynamically scaling CNF resources up and down in response to
  changing demand.

**Common anti-patterns:**

- Static, one-size-fits-all provisioning of CNF resources without considering variable
  demand.
- Over-provisioning of CNF resources to handle peak capacity, leading to excess costs
  during off-peak periods.
- Lack of visibility into CNF resource utilization and performance, hindering effective
  scaling decisions.

**Benefits of establishing this best practice:**

- Significant cost savings by aligning CNF resources with actual subscriber needs.
- Improved CNF performance and reliability by adapting to changing demand patterns.
- Enhanced operational efficiency through automated scaling and resource management.
- Increased agility in responding to growth or seasonal fluctuations in subscriber base.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implementing dynamic sizing and scaling strategies for your cloud-based Network Functions
(CNFs) is crucial for optimizing costs in a cloud-based telco environment. Unlike traditional
on-premises deployments, the cloud provides the opportunity to right-size your CNF resources
based on actual subscriber demands and usage patterns, rather than provisioning peak capacity.

By using cloud-based auto scaling capabilities, you can dynamically adjust the
resources allocated to your CNFs, verifying performance requirements are met while minimizing
over-provisioning and associated costs. This approach allows you to scale resources up and
down in response to changes in subscriber demand, improving cost-efficiency without
compromising the user experience.

### Implementation steps

- Profile the performance and resource utilization characteristics of your cloud-based network functions (CNFs).
- Use AWS Auto Scaling to automatically scale CNF resources up and down based on
  real-time metrics like CPU, memory, and network utilization.
- Configure Amazon CloudWatch alarms to trigger auto scaling actions when thresholds are
  breached.
- Use Amazon EC2 Auto Scaling groups with a dynamic target tracking scaling policy to maintain
  optimal performance at the lowest cost.
- Analyze historical usage patterns and seasonality to set appropriate scaling
  thresholds and policies.
- Continuously monitor and refine your autoscaling configurations to verify they
  adapt to changing traffic patterns.

## Resources

**Key AWS services:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
