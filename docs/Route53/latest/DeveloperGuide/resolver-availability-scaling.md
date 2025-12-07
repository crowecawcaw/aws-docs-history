# Route 53 VPC Resolver availability and scaling

Route 53 VPC Resolver, running on the Amazon VPC CIDR + 2 address and fd00:ec2::253, is available by default
in all VPCs, and responds recursively to DNS queries for public records, Amazon VPC-specific
DNS names, and Route 53 private hosted zones. There are two highly available components,
transparent to users, that make up the Route 53 VPC Resolver: the Nitro Resolver service and the
Zonal Resolver fleet. The Nitro Resolver Service is a service that runs in the Nitro
card on Nitro instances and in Dom0 in older generation instances, and consumes packets
addressed to the Route 53 VPC Resolver locally on the host server. For more information, see [The Security Design of the AWS Nitro System](../../../whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.md "../../../whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.md").

The Nitro Resolver service carries a local cache which can help reduce latency by responding
to repeat queries which are made over a short period of time by an instance. When the
Nitro Resolver service receives a query which it does not have a cached answer for, it
forwards the query to the Zonal Resolver fleet, a highly available fleet of resolvers
typically in the same Availability Zone as the instance. When there are failures
handling queries by upstream name servers or other components in the path, the Nitro
Resolver service is frequently able to handle these failures transparently without
impact to the workloads running on the instance. Furthermore, if the Resolver encounters
query timeouts, refused connections, or SERVFAILS from the domain’s name servers, it may
respond with a cached answer beyond the Time-To-Live (TTL) value to improve
availability. Queries between the Nitro Resolver service and Zonal Resolver fleet are
restricted to a tightly controlled network outside of the customer VPC, which is
inaccessible to customers and subject to rigorous security controls. By handling queries
between the Nitro Resolver service and Zonal Resolver fleet outside of the VPC,
customers are prevented from intercepting DNS queries inside of their VPC. Queries
destined to name servers outside of AWS will traverse the public internet, originating
from public IP addresses belonging to the Zonal Resolver fleet. We do not support the
EDNS0-Client Subnet attribute today, which means all queries destined to public DNS name
servers do not include information about the originating customer IP address.

The Nitro Resolver service is part of the Link-Local services on the instance. Link-Local
services include Route 53 VPC Resolver, Amazon Time Service (NTP), Instance Metadata Service (IMDS)
and Windows Licensing Service (for Windows instances). These services scale with each
elastic network interface you create in your VPC, and each network interface allows 1024
packets per second (PPS) destined to Link-Local services. Packets exceeding this limit
are rejected. You can determine if you have exceeded this limit from the
`linklocal_allowance_exceeded` value returned by ethtool. For more
information about the ethtool, see [Monitor
network performance for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/monitoring-network-performance-ena.md "../../../AWSEC2/latest/UserGuide/monitoring-network-performance-ena.md") in the _Amazon EC2 User
Guide_. This metric can also be reported to CloudWatch metrics by the CloudWatch
Agent. Since the Route 53 VPC Resolver is implemented per network interface, it scales and becomes
more reliable as you add more instances in more Availability Zones. There is no per-VPC
aggregate limit on the number of queries, thus the Route 53 VPC Resolver can scale within the
bounds of a VPC, which is inherently based on network address usage (NAU). For more
information, see [Network Address Usage for your
VPC](../../../vpc/latest/userguide/network-address-usage.md "../../../vpc/latest/userguide/network-address-usage.md") in the _Amazon Virtual Private Cloud User Guide_.

The following diagram shows an overview of how Route 53 VPC Resolver resolves DNS queries within
Availability Zones.

![Conceptual graphic that shows how Route 53 VPC Resolver resolves DNS queries within Availability Zones.](images/Resolver-scale-availability2.png)
