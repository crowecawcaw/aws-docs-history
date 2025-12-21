# Content Domain 1: Network Design

###### Tasks

- [Task 1.1: Design a solution that incorporates edge network services to optimize user performance and traffic management for global architectures](#advanced-networking-specialty-01-domain1-task1 "#advanced-networking-specialty-01-domain1-task1")
- [Task 1.2: Design DNS solutions that meet public, private, and hybrid requirements](#advanced-networking-specialty-01-domain1-task2 "#advanced-networking-specialty-01-domain1-task2")
- [Task 1.3: Design solutions that integrate load balancing to meet high availability, scalability, and security requirements](#advanced-networking-specialty-01-domain1-task3 "#advanced-networking-specialty-01-domain1-task3")
- [Task 1.4: Define logging and monitoring requirements across AWS and hybrid networks](#advanced-networking-specialty-01-domain1-task4 "#advanced-networking-specialty-01-domain1-task4")
- [Task 1.5: Design a routing strategy and connectivity architecture between on-premises networks and the AWS Cloud](#advanced-networking-specialty-01-domain1-task5 "#advanced-networking-specialty-01-domain1-task5")
- [Task 1.6: Design a routing strategy and connectivity architecture that include multiple AWS accounts, AWS Regions, and VPCs to support different connectivity patterns](#advanced-networking-specialty-01-domain1-task6 "#advanced-networking-specialty-01-domain1-task6")

## Task 1.1: Design a solution that incorporates edge network services to optimize user performance and traffic management for global architectures

Knowledge of:

- Design patterns for the usage of content distribution networks (for example, Amazon CloudFront)
- Design patterns for global traffic management (for example, AWS Global Accelerator)
- Integration patterns for content distribution networks and global traffic management with other services (for example, Elastic Load Balancing [ELB], Amazon API Gateway)

Skills in:

- Evaluating requirements of global inbound and outbound traffic from the internet to design an appropriate content distribution solution

## Task 1.2: Design DNS solutions that meet public, private, and hybrid requirements

Knowledge of:

- DNS protocol (for example, DNS records, TTL, DNSSEC, DNS delegation, zones)
- DNS logging and monitoring
- Amazon Route 53 features (for example, alias records, traffic policies, resolvers, health checks)
- Integration of Route 53 with other AWS networking services (for example, Amazon VPC)
- Integration of Route 53 with hybrid, multi-account, and multi-Region options
- Domain registration

Skills in:

- Using Route 53 public hosted zones
- Using Route 53 private hosted zones
- Using Route 53 Resolver endpoints in hybrid and AWS architectures
- Using Route 53 for global traffic management
- Creating and managing domain registrations

## Task 1.3: Design solutions that integrate load balancing to meet high availability, scalability, and security requirements

Knowledge of:

- How load balancing works at layer 3, layer 4, and layer 7 of the OSI model
- Different types of load balancers and how they meet requirements for network design, high availability, and security
- Connectivity patterns that apply to load balancing based on the use case (for example, internal load balancers, external load balancers)
- Scaling factors for load balancers
- Integrations of load balancers and other AWS services (for example, Global Accelerator, CloudFront, AWS WAF, Route 53, Amazon Elastic Kubernetes Service [Amazon EKS], AWS Certificate Manager [ACM])
- Configuration options for load balancers (for example, proxy protocol, cross-zone load balancing, session affinity [sticky sessions], routing algorithms)
- Configuration options for load balancer target groups (for example, TCP, GENEVE, IP compared with instance)
- AWS Load Balancer Controller for Kubernetes clusters
- Considerations for encryption and authentication with load balancers (for example, TLS termination, TLS passthrough)

Skills in:

- Selecting an appropriate load balancer based on the use case
- Integrating auto scaling with load balancing solutions
- Integrating load balancers with existing application deployments

## Task 1.4: Define logging and monitoring requirements across AWS and hybrid networks

Knowledge of:

- Amazon CloudWatch metrics, agents, logs, alarms, dashboards, and insights in AWS architectures to provide visibility
- AWS Transit Gateway Network Manager in architectures to provide visibility
- VPC Reachability Analyzer in architectures to provide visibility
- Flow logs and traffic mirroring in architectures to provide visibility
- Access logging (for example, load balancers, CloudFront)

Skills in:

- Identifying the logging and monitoring requirements
- Recommending appropriate metrics to provide visibility of the network status
- Capturing baseline network performance

## Task 1.5: Design a routing strategy and connectivity architecture between on-premises networks and the AWS Cloud

Knowledge of:

- Routing fundamentals (for example, dynamic compared with static, BGP)
- Layer 1 and layer 2 concepts for physical interconnects (for example, VLAN, link aggregation group [LAG], optics, jumbo frames)
- Encapsulation and encryption technologies (for example, Generic Routing Encapsulation [GRE], IPsec)
- Resource sharing across AWS accounts
- Overlay networks

Skills in:

- Identifying the requirements for hybrid connectivity
- Designing a redundant hybrid connectivity model with AWS services (for example, AWS Direct Connect, AWS Site-to-Site VPN)
- Designing BGP routing with BGP attributes to influence the traffic flows based on the desired traffic patterns (load sharing, active/passive)
- Designing for integration of a software-defined wide area network (SD-WAN) with AWS (for example, Transit Gateway Connect, overlay networks)

## Task 1.6: Design a routing strategy and connectivity architecture that include multiple AWS accounts, AWS Regions, and VPCs to support different connectivity patterns

Knowledge of:

- Different connectivity patterns and use cases (for example, VPC peering, Transit Gateway, AWS PrivateLink)
- Capabilities and advantages of VPC sharing
- IP subnets and solutions accounting for IP address overlaps

Skills in:

- Connecting multiple VPCs by using the most appropriate services based on requirements (for example, using VPC peering, Transit Gateway, PrivateLink)
- Using VPC sharing in a multi-account setup
- Managing IP overlaps by using different available services and options (for example, NAT, PrivateLink, Transit Gateway routing)
