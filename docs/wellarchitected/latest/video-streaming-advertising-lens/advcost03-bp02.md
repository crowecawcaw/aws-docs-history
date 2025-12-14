# ADVCOST03-BP02 When integrating SSPs and DSPs for

programmatic advertising, co-locate the platforms

Keeping SSP and DSP components together can keep transactions fast while minimizing
inter-AZ and inter-Region traffic charges.

## Implementation guidance

When integrating SSPs and DSPs for programmatic advertising, use Network Load
Balancer (NLB) to direct traffic from the SSP to the DSP within the same Availability
Zone. This approach can help optimize costs while providing high performance and
availability.

- **Deploy in the same Availability Zone:** Deploy your SSP
  and DSP components (such as bidding nodes) within the same Availability Zone based on
  expected traffic patterns to minimize cross-AZ data transfer costs and reduce network
  latency.
- **Use Network Load Balancer (NLB):** Use Network Load
  Balancer (NLB) to distribute traffic from the SSP to the DSP instances within the same
  Availability Zone. NLB is cost-effective for TCP traffic and can handle millions of
  requests per second.
- **Configure your NLB:** Set the cross-zone-load-balancing
  attribute to false, or use the appropriate routing policy to prioritize routing within
  the same Availability Zone. This approach routes traffic preferentially to bidder
  nodes within the same Availability Zone, reducing cross-AZ data transfer costs.
- **Monitor and optimize:** Regularly monitor your data
  transfer costs and traffic patterns across Availability Zones. Adjust your resource
  placement and NLB configurations as needed to optimize cost-effectiveness.
- **Use cost optimization tools:** Use AWS Cost Explorer,
  AWS Budgets, and AWS Cost Anomaly Detection to monitor and analyze your costs, set budgets, and
  receive alerts for potential cost anomalies.
- **Automate and scale:** Use AWS CloudFormation or AWS CDK to
  automate the provisioning and management of your SSP and DSP infrastructure, which
  helps you scale efficiently and consistently while maintaining cost optimization.

## Resources

- [Guidance for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/ "https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/")
- [Announcing new AWS Network Load Balancer (NLB) availability and performance
  capabilities](https://aws.amazon.com/about-aws/whats-new/2023/10/aws-nlb-availability-performance-capabilities/ "https://aws.amazon.com/about-aws/whats-new/2023/10/aws-nlb-availability-performance-capabilities/")
