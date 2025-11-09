# PERF04-BP07 Optimize network configuration based on

metrics

Use collected and analyzed data to make informed decisions about
optimizing your network configuration.

**Common anti-patterns:**

- You assume that all performance-related issues are
  application-related.
- You only test your network performance from a location close to
  where you have deployed the workload.
- You use default configurations for all network services.
- You overprovision the network resource to provide sufficient
  capacity.

**Benefits of establishing this best
practice:** Collecting necessary metrics of your AWS
network and implementing network monitoring tools allows you to
understand network performance and optimize network configurations.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Monitoring traffic to and from VPCs, subnets, or network
interfaces is crucial to understand how to utilize AWS network
resources and optimize network configurations. By using the
following AWS networking tools, you can further inspect
information about the traffic usage, network access and logs.

### Implementation steps

- Identify the key performance metrics such as latency or packet
  loss to collect. AWS provides several tools that can
  help you to collect these metrics. By using the following
  tools, you can further inspect information about the traffic
  usage, network access, and logs:

| AWS tool                                                                                                                                                                                                                                                                 | Where to use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Amazon VPC IP Address Manager](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md").                                                                                                                                              | Use IPAM to plan, track, and monitor IP addresses for<br>your AWS and on-premises workloads. This is a best<br>practice to optimize IP address usage and allocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [VPC<br>Flow logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")                                                                                                                                                              | Use VPC Flow Logs to capture detailed information about<br>traffic to and from network interfaces in your VPCs.<br>With VPC Flow Logs, you can diagnose overly restrictive<br>or permissive security group rules and determine the<br>direction of the traffic to and from the network<br>interfaces.                                                                                                                                                                                                                                                                                                                                                                                      |
| [AWS Transit Gateway Flow Logs](../../../vpc/latest/tgw/tgw-flow-logs.md "../../../vpc/latest/tgw/tgw-flow-logs.md")                                                                                                                                                     | Use AWS Transit Gateway Flow Logs to capture information<br>about the IP traffic going to and from your transit<br>gateways.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [DNS<br>query logging](../../../Route53/latest/DeveloperGuide/query-logs.md "../../../Route53/latest/DeveloperGuide/query-logs.md")                                                                                                                                      | Log information about public or private DNS queries<br>Route 53 receives. With DNS logs, you can optimize DNS<br>configurations by understanding the domain or subdomain<br>that was requested or Route 53 EDGE locations that<br>responded to DNS queries.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")                                                                                                           | Reachability Analyzer helps you analyze and debug<br>network reachability. Reachability Analyzer is a<br>configuration analysis tool that allows you to perform<br>connectivity testing between a source resource and a<br>destination resource in your VPCs. This tool helps you<br>verify that your network configuration matches your<br>intended connectivity.                                                                                                                                                                                                                                                                                                                         |
| [Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md")                                                                               | Network Access Analyzer helps you understand network<br>access to your resources. You can use Network Access Analyzer to specify your network access requirements and<br>identify potential network paths that do not meet your<br>specified requirements. By optimizing your corresponding<br>network configuration, you can understand and verify the<br>state of your network and demonstrate if your network on<br>AWS meets your compliance requirements.                                                                                                                                                                                                                             |
| [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")                                                                                                                   | Use [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") and turn on the appropriate metrics<br>for network options. Make sure to choose the right<br>network metric for your workload. For example, you can<br>turn on metrics for VPC Network Address Usage, VPC NAT<br>Gateway, AWS Transit Gateway, VPN tunnel, AWS Network Firewall, Elastic Load Balancing, and AWS Direct Connect. Continually monitoring metrics is a good<br>practice to observe and understand your network status<br>and usage, which helps you optimize network<br>configuration based on your observations. |
| [AWS Network Manager](https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/ "https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/") | Using AWS Network Manager, you can monitor the real-time<br>and historical performance of<br>the [AWS Global Network](https://aws.amazon.com/about-aws/global-infrastructure/global_network/ "https://aws.amazon.com/about-aws/global-infrastructure/global_network/") for operational and planning<br>purposes. Network Manager provides aggregate network<br>latency between AWS Regions and Availability Zones and<br>within each Availability Zone, allowing you to better<br>understand how your application performance relates to<br>the performance of the underlying AWS network.                                                                                                 |
| [Amazon CloudWatch RUM](https://aws.amazon.com/blogs/aws/cloudwatch-rum/ "https://aws.amazon.com/blogs/aws/cloudwatch-rum/")                                                                                                                                             | Use Amazon CloudWatch RUM to collect the metrics that<br>give you the insights that help you identify,<br>understand, and improve user experience.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

- Identify top talkers and application traffic patterns using
  VPC and AWS Transit Gateway Flow Logs.
- Assess and optimize your current network architecture
  including VPCs, subnets, and routing. As an example, you can
  evaluate how different VPC peering or AWS Transit Gateway
  can help you improve the networking in your architecture.
- Assess the routing paths in your network to verify that the
  shortest path between destinations is always used. Network Access Analyzer can help you do this.

## Resources

**Related documents:**

- [Public
  DNS query logging](../../../Route53/latest/DeveloperGuide/query-logs.md "../../../Route53/latest/DeveloperGuide/query-logs.md")
- [What
  is IPAM?](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md")
- [What
  is Reachability Analyzer?](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")
- [What
  is Network Access Analyzer?](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md")
- [CloudWatch
  metrics for your VPCs](../../../vpc/latest/userguide/vpc-cloudwatch.md "../../../vpc/latest/userguide/vpc-cloudwatch.md")
- [Optimize
  performance and reduce costs for network analytics with VPC
  Flow Logs in Apache Parquet format](https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/ "https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/")
- [Monitoring
  your global and core networks with Amazon CloudWatch
  metrics](../../../vpc/latest/tgwnm/monitoring-cloudwatch-metrics.md "../../../vpc/latest/tgwnm/monitoring-cloudwatch-metrics.md")
- [Continuously
  monitor network traffic and resources](../../../whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.md "../../../whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.md")

**Related videos:**

- [AWS re:Invent 2023 – A developer's guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY "https://www.youtube.com/watch?v=i77D556lrgY")
- [AWS re:Invent 2023 – Ready for what’s next? Designing networks for growth and flexibility](https://www.youtube.com/watch?v=FkWOhTZSfdA "https://www.youtube.com/watch?v=FkWOhTZSfdA")
- [AWS re:Invent 2023 – Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es "https://www.youtube.com/watch?v=cRdDCkbE4es")
- [AWS re:Invent 2022 – Dive deep on AWS networking infrastructure](https://www.youtube.com/watch?v=HJNR_dX8g8c "https://www.youtube.com/watch?v=HJNR_dX8g8c")
- [AWS re:Invent 2020 – Networking
  best practices and tips with the AWS Well-Architected
  Framework](https://www.youtube.com/watch?v=wOMNpG49BeM "https://www.youtube.com/watch?v=wOMNpG49BeM")
- [AWS re:Invent 2020 – Monitoring
  and troubleshooting network traffic](https://www.youtube.com/watch?v=Ed09ReWRQXc "https://www.youtube.com/watch?v=Ed09ReWRQXc")

**Related examples:**

- [AWS Networking Workshops](https://networking.workshop.aws/ "https://networking.workshop.aws/")
- [AWS Network Monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns "https://github.com/aws-samples/monitor-vpc-network-patterns")
- [Observing and diagnosing your network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US")
- [Finding and addressing network misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/ "https://validating-network-reachability.awssecworkshops.com/")
