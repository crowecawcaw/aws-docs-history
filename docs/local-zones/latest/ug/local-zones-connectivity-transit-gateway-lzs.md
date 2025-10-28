# Transit gateway connection between

Local Zones

A transit gateway can be used to connect one Local Zone to another within the same parent Region.
For more information about transit gateways, see [Connect your VPC to other VPCs and networks using a
transit gateway](../../../vpc/latest/userguide/extend-tgw.md "../../../vpc/latest/userguide/extend-tgw.md") in the _Amazon VPC User Guide_.

The following diagram shows the transit gateway connection between two Local Zones in the same
Region.

![An AWS Region with two VPCs. Each VPC contains an Availability Zone and a Local Zone. Each zone has a private subnet. A transit gateway connection facilitates traffic between the two Local Zones.](images/local-zones-same-region.png)
A transit gateway connection between Local Zones is useful when you have workloads in different
Local Zones and also require network connectivity between them.

###### Note

You cannot connect a Local Zone to another Local Zone or Outpost that is within the same VPC.
