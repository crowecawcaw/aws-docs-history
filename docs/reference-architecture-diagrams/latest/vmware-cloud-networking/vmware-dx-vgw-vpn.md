# On-Premises Connectivity Using AWS Direct Connect to a Virtual Private Gateway and VPN

Publication date: **March 10, 2022 ([Diagram history](#vmvgw-diagram-history "#vmvgw-diagram-history"))**

This architecture shows on-premises connectivity to VMware Cloud on AWS Software-defined Data Centers (SDDCs) using AWS Direct Connect to a virtual private gateway (VGW) and AWS Site-to-Site VPN for backup connectivity.

## VMware Cloud on AWS networking with Direct Connect to VGW architecture

![Architecture diagram showing on-premises connectivity to VMware Cloud on AWS using AWS Direct Connect private VIF to a virtual private gateway with Site-to-Site VPN backup.](images/vmware-cloud-networking-1.png)

The following numbered items describe the key components in this architecture:

1. A private virtual interface (VIF) establishes connectivity to the VMware Software-defined Data Center (SDDC) A in AWS Region A.
2. An AWS Site-to-Site VPN (over internet) provides backup connectivity to the private VIF to provide resilient connectivity to the VMware SDDC A.
3. A public VIF enables access to all AWS public services and endpoints using public IP addresses.
4. The lack of an [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") connection in Region B creates a design constraint; therefore, a Site-to-Site VPN is established to the VMware SDDC B. This VPN uses the public VIF from the Direct Connect connection in Region A. Site-to-Site VPNs over a public VIF can be used to establish a more consistent network experience compared to internet-based VPNs.
5. A private VIF to the AWS Direct Connect gateway (DXGW) enables the DXGW to establish on-premises communication to [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")s in different Regions by associating the DXGW to the virtual private gateways (VGW).
6. The private VIF to DXGW cannot be used for gateway associations to a VMware SDDC. This feature is not supported on VMware Cloud on AWS.
7. Gateway associations are established between the DXGW and the VGW to enable on-premises communication with Amazon VPCs in multiple Regions.
8. Site-to-Site VPNs are configured as a backup to the DXGW-VGW associations for more resilient connectivity to Amazon VPCs.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                 | Description                                     | Date           |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------- |
| Initial publication                                                                                                    | Reference architecture diagram first published. | March 10, 2022 |
| [Initial publication](vmware-dx-dxgw-tgw.md#vmdxg-diagram-history "vmware-dx-dxgw-tgw.md#vmdxg-diagram-history")       | Reference architecture diagram first published. | March 10, 2022 |
| [Initial publication](vmware-transit-connect.md#vmtc-diagram-history "vmware-transit-connect.md#vmtc-diagram-history") | Reference architecture diagram first published. | March 10, 2022 |
| [Initial publication](vmware-security-vpc.md#vmsec-diagram-history "vmware-security-vpc.md#vmsec-diagram-history")     | Reference architecture diagram first published. | March 10, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
