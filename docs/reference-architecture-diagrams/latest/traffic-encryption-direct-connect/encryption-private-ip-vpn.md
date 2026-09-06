

# AWS Site-to-Site VPN Private IP VPN to AWS Transit Gateway
<a name="encryption-private-ip-vpn"></a>

Publication date: **March 5, 2025 ([Diagram history](#tepip-diagram-history))**

AWS Site-to-Site VPN Private IP VPN connections are created over [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) using private IP addresses, enabling enhanced security and network privacy at the same time. Private IP VPNs are deployed on top of transit VIFs and Direct Connect gateways as underlying transport.

For more information about Private IP VPNs, see [Introducing AWS Site-to-Site Private IP VPNs](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-site-to-site-vpn-private-ip-vpns/) on the AWS Blog.

## Private IP VPN over Direct Connect transit VIF to Transit Gateway architecture
<a name="tepip-diagram1"></a>

![Architecture diagram showing traffic encryption using AWS Site-to-Site VPN Private IP VPN over an AWS Direct Connect transit VIF and Direct Connect gateway to reach multiple VPCs through AWS Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/traffic-encryption-direct-connect/images/traffic-encryption-direct-connect-3.png)


**Configuration steps:**

1. Create an AWS Direct Connect connection. For dedicated connections, set up the cross-connect between the AWS device and your device (or partner device) at the location. For hosted connections, you must accept the hosted connection before you can use it.

1. Once the connection is established, create a Direct Connect transit virtual interface (VIF) and Direct Connect gateway. Configure your customer gateway to bring up the VIF.

1. Associate your [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to the Direct Connect gateway, specifying the Transit Gateway CIDR block as the allowed prefix on this attachment. Make sure this CIDR block does not overlap with any [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) CIDR block or on-premises CIDR range.

1. Create the AWS Site-to-Site VPN using the Direct Connect gateway and transit VIF as underlying transport.

1. Bring up the AWS Site-to-Site VPN tunnels and route traffic destined to the Transit Gateway through the AWS Site-to-Site VPN connection.

**Sample traffic flow:**

1. A client located in the corporate network needs to route network traffic to the IP address of an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance in the **spoke VPC A**, and routes the traffic through the customer gateway.

1. The customer gateway determines that the best route to the VPC is through the AWS Site-to-Site VPN connection. The traffic flows through the IPSec tunnels with the selected encryption method, using the transit VIF and Direct Connect gateway as the underlying transport network.

1. The traffic arrives at the Transit Gateway. As per the **Transit Gateway VPN route table**, the traffic is forwarded to the **spoke VPC A**, and then routed to the Amazon EC2 instance.

1. The return traffic from the Amazon EC2 instance to the client located in the corporate network follows a reverse but identical path.

## Further reading
<a name="tepip-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="tepip-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](encryption-vpn-to-vpc.md#tevpc-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-vpn-to-tgw.md#tetgw-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](#tepip-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-macsec.md#temac-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.