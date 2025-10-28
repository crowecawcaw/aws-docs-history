# Transit gateway attachment configuration for AWS Network Firewall

This section applies to the use of Network Firewall with a transit gateway in multiple Availability Zones where the firewall endpoints might reside in different Availability Zones than the subnets whose traffic they're filtering.

###### Note

To use this configuration, you must enable appliance mode on the transit gateway VPC attachment for any VPC where Network Firewall endpoints reside.

A Network Firewall endpoint is a stateful network appliance. Enabling appliance mode ensures that the transit gateway continues to use the same Availability Zone for the VPC attachment over the lifetime of a flow of traffic between source and destination.

For information about VPC transit gateways, see the guide
[Amazon Virtual Private Cloud Transit Gateways](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md").

For information about appliance mode and how to enable it in your attachments, see [Availability Zones](../../../vpc/latest/tgw/how-transit-gateways-work.md#tgw-az-overview "../../../vpc/latest/tgw/how-transit-gateways-work.md#tgw-az-overview") and [Example: Appliance in a shared
services VPC](../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md "../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md").
