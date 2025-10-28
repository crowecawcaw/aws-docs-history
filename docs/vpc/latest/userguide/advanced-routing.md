# Advanced routing in your VPC

Configure advanced routing scenarios for your VPC. This section covers both static and dynamic routing approaches for managing traffic flow:

- **Static ingress routing**: Configure static routes to direct
  inbound internet traffic destined for your BYOIP (Bring Your Own IP) address pools
  to specific network interfaces within your VPC.
- **Dynamic routing with VPC Route Server:** Use BGP-based dynamic
  routing to automatically update VPC and internet gateway route tables, providing
  fault tolerance and automatic failover for your workloads.

###### Contents

- [Route internet traffic to a single network interface](igw-ingress-routing.md "igw-ingress-routing.md")
- [Dynamic routing in your VPC using VPC Route Server](dynamic-routing-route-server.md "dynamic-routing-route-server.md")
