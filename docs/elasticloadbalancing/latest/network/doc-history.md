

# Document history for Network Load Balancers
<a name="doc-history"></a>

The following table describes the releases for Network Load Balancers.

| Change | Description | Date | 
| --- |--- |--- |
| [Listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html) | This release adds support for listener rules on Network Load Balancers, enabling custom traffic routing based on source IP address type. You can route IPv4 and IPv6 traffic to separate target groups using a single dual-stack load balancer. | July 10, 2026 | 
| [Weighted target groups](#doc-history) | This release adds support for default action with weighted target groups. | November 19, 2025 | 
| [QUIC and TCP\_QUIC Protocol Support](#doc-history) | This release adds support for QUIC and TCP\_QUIC protocols. | November 13, 2025 | 
| [Secondary IPv4 addresses](#doc-history) | This release adds support to add secondary IPv4 addresses to the load balancer network interfaces. | July 29, 2025 | 
| [Disable Availability Zones](#doc-history) | This releases adds support to disable an Availability Zone for an existing load balancer. | February 13, 2025 | 
| [Capacity Unit reservation](#doc-history) | This release adds support to set a minimum capacity for your load balancer. | November 20, 2024 | 
| [UDP support over IPv6 for dualstack load balancers](#doc-history) | This release enables clients to access UDP-based applications using IPv6. | October 31, 2024 | 
| [RSA 3072-bit and ECDSA 256/384/521-bit certificates](#doc-history) | This release adds support for RSA 3072-bit certificates, and Elliptic Curve Digital Signature Algorithm (ECDSA) 256, 384 and 521-bit certificates via AWS Certificate Manager (ACM). | January 19, 2024 | 
| [FIPS 140-3 TLS termination](#doc-history) | This release adds security policies that use FIPS 140-3 crypotographic modules when terminating TLS connections. | November 20, 2023 | 
| [Zonal DNS affinity](#doc-history) | This release adds support for clients resolving the load balancer DNS to receive an IP address in the same Availability Zone (AZ) they are in. | October 12, 2023 | 
| [Disable unhealthy target connection termination](#doc-history) | This release adds support to maintain active connections to targets that fail health checks. | October 12, 2023 | 
| [Default UDP connection termination](#doc-history) | This release adds support to terminate UDP connections at the end of the deregistration timeout by default. | October 12, 2023 | 
| [Register targets using IPv6](#doc-history) | This release adds support to register instances as targets when addressed by IPv6. | October 2, 2023 | 
| [Security groups for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html) | This release adds support to associate security groups with your Network Load Balancers at creation. | August 10, 2023 | 
| [Target group health](#doc-history) | This release adds support to configure the minimum count or percentage of targets that must be healthy, and what actions the load balancer takes when the threshold is not met. | November 17, 2022 | 
| [Health check configuration](#doc-history) | This release provides improvements to health check configuration. | November 17, 2022 | 
| [Cross-zone load balancing](#doc-history) | This release adds support to configure cross-zone load balancing at the target group level. | November 17, 2022 | 
| [IPv6 target groups](#doc-history) | This release adds support to configure IPv6 target groups for Network Load Balancers. | November 23, 2021 | 
| [IPv6 internal load balancers](#doc-history) | This release adds support to configure IPv6 target groups for Network Load Balancers. | November 23, 2021 | 
| [TLS 1.3](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) | This release adds security policies supporting TLS version 1.3. | October 14, 2021 | 
| [Application Load Balancers as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html) | This release adds support to configure an Application Load Balancer as the target of a Network Load Balancer. | September 27, 2021 | 
| [Client IP preservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#client-ip-preservation) | This release adds support to configure client IP preservation. | February 4, 2021 | 
| [Security policy for FS supporting TLS version 1.2](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) | This release adds a security policy for Forward Secrecy (FS) supporting TLS version 1.2. | November 24, 2020 | 
| [Dual-stack mode](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-ip-address-type.html) | This release adds support for dual-stack mode, which enables clients to connect to the load balancer using both IPv4 addresses and IPv6 addresses. | November 13, 2020 | 
| [Connection termination on deregistration](#doc-history) | This release adds support to close connections to deregistered targets after the end of the deregistration timeout. | November 13, 2020 | 
| [ALPN policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies) | This release adds support for Application-Layer Protocol Negotiation (ALPN) preference lists. | May 27, 2020 | 
| [Sticky sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#sticky-sessions) | This release adds support for sticky sessions based on source IP address and protocol. | February 28, 2020 | 
| [Shared subnets](#doc-history) | This release adds support for specifying subnets that were shared with you by another AWS account. | November 26, 2019 | 
| [Private IP addresses](#doc-history) | This release enables you to provide a private IP address from the IPv4 address range of the subnet you specify when you enable an Availability Zone for an internal load balancer. | November 25, 2019 | 
| [Add subnets](#doc-history) | This release adds support for enabling additional Availability Zones after you create your load balancer. | November 25, 2019 | 
| [Security policies for FS](#doc-history) | This release adds support for three additional predefined forward secrecy security policies. | October 8, 2019 | 
| [SNI support](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html) | This release adds support for Server Name Indication (SNI). | September 12, 2019 | 
| [UDP protocol](#doc-history) | This release adds support for the UDP protocol. | June 24, 2019 | 
| [Available in new region](#doc-history) | This release adds support for Network Load Balancers in the Asia Pacific (Osaka) Region. | June 12, 2019 | 
| [TLS protocol](#doc-history) | This release adds support for the TLS protocol. | January 24, 2019 | 
| [Cross-zone load balancing](#doc-history) | This release adds support for enabling cross-zone load balancing. | February 22, 2018 | 
| [Proxy protocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) | This release adds support for enabling Proxy Protocol. | November 17, 2017 | 
| [IP addresses as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-type) | This release adds support for registering IP addresses as targets. | September 21, 2017 | 
| [New load balancer type](#doc-history) | This release of Elastic Load Balancing introduces Network Load Balancers. | September 7, 2017 | 