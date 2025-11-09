# PERF04-BP01 Understand how networking impacts

performance

Analyze and understand how network-related decisions impact your
workload to provide efficient performance and improved user
experience.

**Common anti-patterns:**

- All traffic flows through your existing data centers.
- You route all traffic through central firewalls instead of using
  cloud-native network security tools.
- You provision AWS Direct Connect connections without understanding
  actual usage requirements.
- You don’t consider workload characteristics and encryption
  overhead when defining your networking solutions.
- You use on-premises concepts and strategies for networking
  solutions in the cloud.

**Benefits of establishing this best
practice:** Understanding how networking impacts workload
performance helps you identify potential bottlenecks, improve user
experience, increase reliability, and lower operational maintenance
as the workload changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The network is responsible for the connectivity between
application components, cloud services, edge networks, and
on-premises data, and therefore it can heavily impact workload
performance. In addition to workload performance, user experience
can be also impacted by network latency, bandwidth, protocols,
location, network congestion, jitter, throughput, and routing
rules.

Have a documented list of networking requirements from the
workload including latency, packet size, routing rules, protocols,
and supporting traffic patterns. Review the available networking
solutions and identify which service meets your workload
networking characteristics. Cloud-based networks can be quickly
rebuilt, so evolving your network architecture over time is
necessary to improve performance efficiency.

### Implementation steps:

- Define and document networking performance requirements,
  including metrics such as network latency, bandwidth,
  protocols, locations, traffic patterns (spikes and
  frequency), throughput, encryption, inspection, and routing
  rules.
- Learn about key AWS networking services like [VPCs](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md"), [AWS Direct Connect](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.md"), [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/"), and [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/").
- Capture the following key networking characteristics:

| Characteristics                         | Tools and metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Foundational networking characteristics | + [VPC<br>Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")<br>+ [AWS Transit Gateway Flow Logs](../../../vpc/latest/tgw/tgw-flow-logs.md "../../../vpc/latest/tgw/tgw-flow-logs.md")<br>+ [AWS Transit Gateway metrics](../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md "../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md")<br>+ [AWS PrivateLink metrics](../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md "../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md")                                                                                                                                                                      |
| Application networking characteristics  | + [Elastic<br>Fabric Adapter](../../../AWSEC2/latest/UserGuide/monitoring-network-performance-ena.md "../../../AWSEC2/latest/UserGuide/monitoring-network-performance-ena.md")<br>+ [AWS App Mesh metrics](../../../app-mesh/latest/userguide/envoy-metrics.md "../../../app-mesh/latest/userguide/envoy-metrics.md")<br>+ [Amazon API Gateway metrics](../../../apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.md "../../../apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.md")                                                                                                                                                                                                                           |
| Edge networking characteristics         | + [Amazon CloudFront metrics](../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md "../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md")<br>+ [Amazon Route 53 metrics](../../../Route53/latest/DeveloperGuide/monitoring-cloudwatch.md "../../../Route53/latest/DeveloperGuide/monitoring-cloudwatch.md")<br>+ [AWS Global Accelerator metrics](../../../global-accelerator/latest/dg/cloudwatch-monitoring.md "../../../global-accelerator/latest/dg/cloudwatch-monitoring.md")                                                                                                                                                                                                                |
| Hybrid networking characteristics       | + [AWS Direct Connect metrics](../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md "../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md")<br>+ [AWS Site-to-Site VPN metrics](../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md "../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md")<br>+ [AWS Client VPN metrics](../../../vpn/latest/clientvpn-admin/monitoring-cloudwatch.md "../../../vpn/latest/clientvpn-admin/monitoring-cloudwatch.md")<br>+ [AWS Cloud WAN metrics](../../../vpc/latest/cloudwan/cloudwan-cloudwatch-metrics.md "../../../vpc/latest/cloudwan/cloudwan-cloudwatch-metrics.md")                                                                                                        |
| Security networking characteristics     | + [AWS Shield, AWS WAF, and AWS Network Firewall metrics](../../../waf/latest/developerguide/monitoring-cloudwatch.md "../../../waf/latest/developerguide/monitoring-cloudwatch.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Tracing characteristics                 | + [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/")<br>+ [VPC<br>Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")<br>+ [Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md")<br>+ [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md")<br>+ [Amazon CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md") |

- Benchmark and test network performance:
  - [Benchmark](https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/ "https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/") network
    throughput, as some factors can affect Amazon EC2 network
    performance when instances are in the same VPC. Measure
    the network bandwidth between Amazon EC2 Linux instances in the
    same VPC.
  - Perform [load
    tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/ "https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/") to experiment with networking solutions and
    options.

## Resources

**Related documents:**

- [Application Load Balancer](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md")
- [EC2
  Enhanced Networking on Linux](../../../AWSEC2/latest/UserGuide/enhanced-networking.md "../../../AWSEC2/latest/UserGuide/enhanced-networking.md")
- [EC2
  Enhanced Networking on Windows](../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md "../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md")
- [EC2
  Placement Groups](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md")
- [Enabling
  Enhanced Networking with the Elastic Network Adapter (ENA) on
  Linux Instances](../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md")
- [Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md")
- [Networking
  Products with AWS](https://aws.amazon.com/products/networking/ "https://aws.amazon.com/products/networking/")
- [Transit Gateway](../../../vpc/latest/tgw.md "../../../vpc/latest/tgw.md")
- [Transitioning
  to latency-based routing in Amazon Route 53](../../../Route53/latest/DeveloperGuide/TutorialTransitionToLBR.md "../../../Route53/latest/DeveloperGuide/TutorialTransitionToLBR.md")
- [VPC
  Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md")

**Related videos:**

- [AWS re:Invent 2023 - AWS networking foundations](https://www.youtube.com/watch?v=8nNurTFy-h4 "https://www.youtube.com/watch?v=8nNurTFy-h4")
- [AWS re:Invent 2023 - What can networking do for your application?](https://www.youtube.com/watch?v=tUh26i8uY9Q "https://www.youtube.com/watch?v=tUh26i8uY9Q")
- [AWS re:Invent 2023 - Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es "https://www.youtube.com/watch?v=cRdDCkbE4es")
- [AWS re:Invent 2023 - A developer’s guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY "https://www.youtube.com/watch?v=i77D556lrgY")
- [AWS re:Invent 2019 - Connectivity
  to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs "https://www.youtube.com/watch?v=eqW6CPb58gs")
- [AWS re:Invent 2019 - Optimizing
  Network Performance for Amazon EC2 Instances](https://www.youtube.com/watch?v=DWiwuYtIgu0 "https://www.youtube.com/watch?v=DWiwuYtIgu0")
- [AWS Summit Online - Improve Global
  Network Performance for Applications](https://youtu.be/vNIALfLTW9M "https://youtu.be/vNIALfLTW9M")
- [AWS re:Invent 2020 - Networking
  best practices and tips with the Well-Architected
  Framework](https://youtu.be/wOMNpG49BeM "https://youtu.be/wOMNpG49BeM")
- [AWS re:Invent 2020 - AWS networking
  best practices in large-scale migrations](https://youtu.be/qCQvwLBjcbs "https://youtu.be/qCQvwLBjcbs")

**Related examples:**

- [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions "https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions")
- [AWS Networking Workshops](https://networking.workshop.aws/ "https://networking.workshop.aws/")
- [Hands-on Network Firewall Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US")
- [Observing and Diagnosing your Network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US")
- [Finding and addressing Network Misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/ "https://validating-network-reachability.awssecworkshops.com/")
