# Connect your VPC to other networks

You can connect your virtual private cloud (VPC) to other networks, such as other VPCs, the internet, or your on-premises network.

![VPC connectivity options](images/connectivity-overview.png)
You can connect your virtual private cloud (VPC) to other networks, such as other VPCs, the internet, or your on-premises network.

The diagram demonstrates some of these connectivity options. VPC A is connected to the internet through an internet gateway, and the EC2 instance in the private subnet can connect to the internet using a NAT gateway in the public subnet. VPC B is also connected to the internet, but through a direct internet gateway, allowing the EC2 instance in the public subnet to access the internet.

Moreover, VPC A and VPC B are connected to each other through a VPC peering connection and a transit gateway. The transit gateway has a VPN attachment to a data center, and VPC B has an Direct Connect connection to the same data center. This interconnectivity enables organizations to integrate their cloud resources with on-premises infrastructure, creating a hybrid cloud environment.

Connecting VPCs to other networks is an important aspect of building cloud infrastructure within AWS. It offers organizations flexibility and control over their networking configurations, allowing them to design VPC architectures that align with their business requirements and security needs. These connectivity options facilitate efficient data flow between various components of a distributed IT landscape, whether they are within the cloud or on-premises.

AWS provides a range of tools and features to enable these VPC connections, including internet gateways, NAT gateways, VPC peering, transit gateways, and Direct Connect. By leveraging these capabilities, organizations can create secure and integrated cloud environments that seamlessly integrate with their existing IT infrastructure.

You can connect your virtual private cloud (VPC) to other networks. For example,
other VPCs, the internet, or your on-premises network.

For more information, see [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options.md").

###### Contents

- [Enable internet access for a VPC using an internet gateway](VPC_Internet_Gateway.md "VPC_Internet_Gateway.md")
- [Enable outbound IPv6 traffic using an egress-only internet gateway](egress-only-internet-gateway.md "egress-only-internet-gateway.md")
- [Connect to the internet or other networks using NAT devices](vpc-nat.md "vpc-nat.md")
- [Associate Elastic IP addresses with resources in your VPC](vpc-eips.md "vpc-eips.md")
- [Connect your VPC to other VPCs and networks using a transit gateway](extend-tgw.md "extend-tgw.md")
- [Connect your VPC to remote networks using AWS Virtual Private Network](vpn-connections.md "vpn-connections.md")
- [Connect VPCs using VPC peering](vpc-peering.md "vpc-peering.md")
