# Route table configurations for AWS Network Firewall

To include the Network Firewall firewall in your Amazon Virtual Private Cloud VPC,
you modify the VPC route tables so that the traffic that you want the firewall to filter
passes through the firewall endpoints. Exactly how you do this depends on your
architecture and the traffic that you want to filter. For example, to filter all traffic
between an internet gateway and your customer subnets, you redirect incoming traffic
from the internet gateway and outgoing traffic from the customer subnets through the
firewall endpoint.

For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.

For descriptions of common architectures for AWS Network Firewall, with example route table
configurations, see [AWS Network Firewall example architectures with routing](architectures.md "architectures.md").
