# Content Domain 3: Network Management and Operation

###### Tasks

- [Task 3.1: Maintain routing and connectivity on AWS and hybrid networks](#advanced-networking-specialty-01-domain3-task1 "#advanced-networking-specialty-01-domain3-task1")
- [Task 3.2: Monitor and analyze network traffic to troubleshoot and optimize connectivity patterns](#advanced-networking-specialty-01-domain3-task2 "#advanced-networking-specialty-01-domain3-task2")
- [Task 3.3: Optimize AWS networks for performance, reliability, and cost-effectiveness](#advanced-networking-specialty-01-domain3-task3 "#advanced-networking-specialty-01-domain3-task3")

## Task 3.1: Maintain routing and connectivity on AWS and hybrid networks

Knowledge of:

- Industry-standard routing protocols that are used in AWS hybrid networks (for example, BGP over Direct Connect)
- Connectivity methods for AWS and hybrid networks (for example, Direct Connect gateway, Transit Gateway, VIFs)
- How limits and quotas affect AWS networking services (for example, bandwidth limits, route limits)
- Available private and public access methods for custom services (for example, PrivateLink, VPC peering)
- Available inter-Regional and intra-Regional communication patterns

Skills in:

- Managing routing protocols for AWS and hybrid connectivity options (for example, over a Direct Connect connection, VPN)
- Maintaining private access to custom services (for example, PrivateLink, VPC peering)
- Using route tables to direct traffic appropriately (for example, automatic propagation, BGP)
- Setting up private access or public access to AWS services (for example, Direct Connect, VPN)
- Optimizing routing over dynamic and static routing protocols (for example, summarizing routes, CIDR overlap)

## Task 3.2: Monitor and analyze network traffic to troubleshoot and optimize connectivity patterns

Knowledge of:

- Network performance metrics and reachability constraints (for example, routing, packet size)
- Appropriate logs and metrics to assess network performance and reachability issues (for example, packet loss)
- Tools to collect and analyze logs and metrics (for example, CloudWatch, VPC Flow Logs, VPC Traffic Mirroring)
- Tools to analyze routing patterns and issues (for example, Reachability Analyzer, Transit Gateway Network Manager)

Skills in:

- Analyzing tool output to assess network performance and troubleshoot connectivity (for example, VPC Flow Logs, Amazon CloudWatch Logs)
- Mapping or understanding network topology (for example, Transit Gateway Network Manager)
- Analyzing packets to identify issues in packet shaping (for example, VPC Traffic Mirroring)
- Troubleshooting connectivity issues that are caused by network misconfiguration (for example, Reachability Analyzer)
- Verifying that a network configuration meets network design requirements (for example, Reachability Analyzer)
- Automating the verification of connectivity intent as a network configuration changes (for example, Reachability Analyzer)
- Troubleshooting packet size mismatches in a VPC to restore network connectivity

## Task 3.3: Optimize AWS networks for performance, reliability, and cost-effectiveness

Knowledge of:

- Situations in which a VPC peer or a transit gateway are appropriate
- Different methods to reduce bandwidth utilization (for example, unicast compared with multicast, CloudFront)
- Cost-effective connectivity options for data transfer between a VPC and on-premises environments
- Different types of network interfaces on AWS
- High-availability features in Route 53 (for example, DNS load balancing using health checks with latency and weighted record sets)
- Availability of options from Route 53 that provide reliability
- Load balancing and traffic distribution patterns
- VPC subnet optimization
- Frame size optimization for bandwidth across different connection types

Skills in:

- Optimizing for network throughput
- Selecting the right network interface for the best performance (for example, elastic network interface, Elastic Network Adapter [ENA], Elastic Fabric Adapter [EFA])
- Choosing between VPC peering, proxy patterns, or a transit gateway connection based on analysis of the network requirements provided
- Implementing a solution on an appropriate network connectivity service (for example, VPC peering, Transit Gateway, VPN connection) to meet network requirements
- Implementing a multicast capability within a VPC and on-premises environments
- Creating Route 53 public hosted zones and private hosted zones and records to optimize application availability (for example, private zonal DNS entry to route traffic to multiple Availability Zones)
- Updating and optimizing subnets for auto scaling configurations to support increased application load
- Updating and optimizing subnets to prevent the depletion of available IP addresses within a VPC (for example, secondary CIDR)
- Configuring jumbo frame support across connection types
- Optimizing network connectivity by using Global Accelerator to improve network performance and application availability
