# Centralized edge connectivity using transit gateway

AWS Transit Gateway is a service that enables you to connect your VPCs and your on-premises networks to a
single gateway.
Transit gateway (TGW) can be used to consolidate your existing edge connectivity and route it through a
single ingress/egress point. Transit gateway is created in the
networking account of your AMS multi-account environment. For more details about transit gateway, see
[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/").

AWS Direct Connect (DX) gateway is used to connect your DX connection over a transit virtual interface to
the VPCs or VPNs that are attached to your transit gateway.
You associate a Direct Connect gateway with the transit gateway. Then, create a transit virtual interface
for your AWS Direct Connect connection to the Direct Connect gateway. For information
on DX virtual interfaces, see
[AWS Direct Connect Virtual Interfaces](../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md "../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md").

This configuration offers the following benefits. You can:

- Manage a single connection for multiple VPCs or VPNs that are in the same AWS Region.
- Advertise prefixes from on-premises to AWS, and from AWS to on-premises.

###### Note

For information about using a DX with AWS services, see the Resiliency Toolkit section
[Classic](../../../directconnect/latest/UserGuide/getstarted.md "../../../directconnect/latest/UserGuide/getstarted.md"). For more information, see
[Transit Gateway associations](../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md "../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md").

![AWS Transit Gateway network diagram showing connections to VPCs and Direct Connect.](images/malz-cent-edge.png)
To increase the resiliency of your connectivity, we recommend that you
attach at least two transit virtual interfaces from different AWS Direct
Connect locations to the Direct Connect gateway. For more information, see
the [AWS Direct Connect resiliency recommendation](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/").
