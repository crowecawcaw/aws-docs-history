

# Highly Resilient On-Premises Connectivity with AWS Transit Gateway and VMware Transit Connect
<a name="vmware-transit-connect"></a>

Publication date: **March 10, 2022 ([Diagram history](#vmtc-diagram-history))**

This architecture shows highly resilient on-premises connectivity to VMware Cloud on AWS using AWS Direct Connect, Direct Connect gateway, AWS Transit Gateway, and VMware Transit Connect (vTGW) for high-bandwidth, low-latency connectivity between SDDCs in an SDDC group.

## Highly resilient connectivity with VMware Transit Connect architecture
<a name="vmtc-diagram1"></a>

![Architecture diagram showing highly resilient on-premises connectivity to VMware Cloud on AWS using Direct Connect, Transit Gateway, and VMware Transit Connect with cross-Region peering.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/vmware-cloud-networking/images/vmware-cloud-networking-3.png)


The following numbered items describe the key components in this architecture:

1. Transit virtual interfaces (VIFs) from two separate [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) instances in different Regions are used to establish resilient and fault-tolerant connectivity to AWS Regions A and B.

1. The DXGW is associated with [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) (TGW) instances in each Region to provide on-premises connectivity.

1. The AWS Transit Gateway is a regional virtual router that is capable of transitive routing between networks connected to VPC, VPN, peering attachments, and DXGW associations.

1. The SDDC group uses a VMware Transit Connect (vTGW) to provide high-bandwidth, low-latency connectivity between SDDCs in an SDDC group, SDDCs and attached VPCs, and SDDCs and on-premises through the DXGW.

1. [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) attachments enable VPCs to establish communication with other VPCs and networks connected to the Transit Gateway. Alternatively, VPC attachments to VMware Transit Connect (vTGW) enable VPCs to establish communication with only SDDC networks connected to the same vTGW.

1. External TGW peering attachments enable communication between the SDDC networks and networks connected to the TGW.

1. The cross-Region VMware Transit Connect peering enables communication only between SDDC networks connected to vTGW A and vTGW B.

1. The cross-Region AWS Transit Gateway peering attachment enables communication between networks connected to TGW A and TGW B.

## Further reading
<a name="vmtc-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="vmtc-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](vmware-dx-vgw-vpn.md#vmvgw-diagram-history) | Reference architecture diagram first published. | March 10, 2022 | 
| [Initial publication](vmware-dx-dxgw-tgw.md#vmdxg-diagram-history) | Reference architecture diagram first published. | March 10, 2022 | 
| [Initial publication](#vmtc-diagram-history) | Reference architecture diagram first published. | March 10, 2022 | 
| [Initial publication](vmware-security-vpc.md#vmsec-diagram-history) | Reference architecture diagram first published. | March 10, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.