# Content Domain 2: Network Implementation

###### Tasks

- [Task 2.1: Implement routing and connectivity between on-premises networks and the AWS Cloud](#advanced-networking-specialty-01-domain2-task1 "#advanced-networking-specialty-01-domain2-task1")
- [Task 2.2: Implement routing and connectivity across multiple AWS accounts, Regions, and VPCs to support different connectivity patterns](#advanced-networking-specialty-01-domain2-task2 "#advanced-networking-specialty-01-domain2-task2")
- [Task 2.3: Implement complex hybrid and multi-account DNS architectures](#advanced-networking-specialty-01-domain2-task3 "#advanced-networking-specialty-01-domain2-task3")
- [Task 2.4: Automate and configure network infrastructure](#advanced-networking-specialty-01-domain2-task4 "#advanced-networking-specialty-01-domain2-task4")

## Task 2.1: Implement routing and connectivity between on-premises networks and the AWS Cloud

Knowledge of:

- Routing protocols (for example, static, dynamic)
- VPNs (for example, security, accelerated VPN)
- Layer 1 and types of hardware to use (for example, Letter of Authorization [LOA] documents, colocation facilities, Direct Connect)
- Layer 2 and layer 3 (for example, VLANs, IP addressing, gateways, routing, switching)
- Traffic management and SD-WAN (for example, Transit Gateway Connect)
- DNS (for example, conditional forwarding, hosted zones, resolvers)
- Security appliances (for example, firewalls)
- Load balancing (for example, layer 4 compared with layer 7, reverse proxies, layer 3)
- Infrastructure automation
- AWS Organizations and AWS Resource Access Manager (AWS RAM) (for example, multi-account Transit Gateway, Direct Connect, Amazon VPC, Route 53)
- Test connectivity (for example, Route Analyzer, Reachability Analyzer)
- Networking services of VPCs

Skills in:

- Configuring the physical network requirements for hybrid connectivity solutions
- Configuring static or dynamic routing protocols to work with hybrid connectivity solutions
- Configuring existing on-premises networks to connect with the AWS Cloud
- Configuring existing on-premises name resolution with the AWS Cloud
- Configuring and implementing load balancing solutions
- Configuring network monitoring and logging for AWS services
- Testing and validating connectivity between environments

## Task 2.2: Implement routing and connectivity across multiple AWS accounts, Regions, and VPCs to support different connectivity patterns

Knowledge of:

- Inter-VPC and multi-account connectivity (for example, VPC peering, Transit Gateway, VPN, third-party vendors, SD-WAN, multi-protocol label switching [MPLS])
- Private application connectivity (for example, PrivateLink)
- Methods of expanding AWS networking connectivity (for example, Organizations, AWS RAM)
- Host and service name resolution for applications and clients (for example, DNS)
- Infrastructure automation
- Authentication and authorization (for example, SAML, Active Directory)
- Security (for example, security groups, network ACLs, AWS Network Firewall)
- Test connectivity (for example, Route Analyzer, Reachability Analyzer, tooling)

Skills in:

- Configuring network connectivity architectures by using AWS services in a single-VPC or multi-VPC design (for example, DHCP, routing, security groups)
- Configuring hybrid connectivity with existing third-party vendor solutions
- Configuring a hub-and-spoke network architecture (for example, Transit Gateway, transit VPC)
- Configuring a DNS solution to make hybrid connectivity possible
- Implementing security between network boundaries
- Configuring network monitoring and logging by using AWS solutions

## Task 2.3: Implement complex hybrid and multi-account DNS architectures

Knowledge of:

- When to use private hosted zones and public hosted zones
- Methods to alter traffic management (for example, based on latency, geography, weighting)
- DNS delegation and forwarding (for example, conditional forwarding)
- Different DNS record types (for example, A, AAAA, TXT, pointer records, alias records)
- DNSSEC
- How to share DNS services between accounts (for example, AWS RAM)
- Requirements and implementation options for outbound and inbound endpoints

Skills in:

- Configuring DNS zones and conditional forwarding
- Configuring traffic management by using DNS solutions
- Configuring DNS for hybrid networks
- Configuring appropriate DNS records
- Configuring DNSSEC on Route 53
- Configuring DNS within a centralized or distributed network architecture
- Configuring DNS monitoring and logging on Route 53

## Task 2.4: Automate and configure network infrastructure

Knowledge of:

- Infrastructure as code (IaC) (for example, AWS Cloud Development Kit [AWS CDK], AWS CloudFormation, AWS CLI, AWS SDK, APIs)
- Event-driven network automation
- Common problems of using hardcoded instructions in IaC templates when provisioning cloud networking resources

Skills in:

- Creating and managing repeatable network configurations
- Integrating event-driven networking functions
- Integrating hybrid network automation options with AWS native IaC
- Eliminating risk and achieving efficiency in a cloud networking environment while maintaining the lowest possible cost
- Automating the process of optimizing cloud network resources with IaC
