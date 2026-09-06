

# AWS Site-to-Site VPN to AWS Transit Gateway (Public VIF)
<a name="encryption-vpn-to-tgw"></a>

Publication date: **March 5, 2025 ([Diagram history](#tetgw-diagram-history))**

This method achieves traffic encryption by combining the benefits of the end-to-end secure IPSec connection with the low latency and consistent network experience of [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) when reaching resources in your [Amazon VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html). This approach is suitable for customers that need to reach multiple VPCs in their AWS environment.

## Site-to-Site VPN over Direct Connect public VIF to Transit Gateway architecture
<a name="tetgw-diagram1"></a>

![Architecture diagram showing traffic encryption using AWS Site-to-Site VPN over a Direct Connect public VIF to reach multiple VPCs through AWS Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/traffic-encryption-direct-connect/images/traffic-encryption-direct-connect-2.png)


**Configuration steps:**

1. Create an AWS Direct Connect connection. For dedicated connections, set up a cross-connect between the AWS device and your device (or partner device) at the location. For hosted connections, you must accept the connection before you can use it.

1. Once the connection is established, create an AWS Direct Connect public virtual interface. Configure your customer gateway to bring up the VIF.

1. Once the BGP peer on the VIF is established, AWS advertises its public IP range to the customer gateway device over the public VIF.

1. Create an AWS Site-to-Site VPN and choose your AWS Transit Gateway instance as the VPN concentrator for the AWS side.

1. Configure the customer gateway with the VPN parameters to bring up the AWS VPN connection and route traffic destined to the Transit Gateway through the AWS VPN connection.

**Sample traffic flow:**

1. A client located in the corporate network needs to route network traffic to the IP address of an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance in the **spoke VPC A**, and routes the traffic through the customer gateway.

1. The customer gateway determines that the best route to the VPC is through the AWS Site-to-Site VPN tunnel. The traffic is encrypted based on cryptographic parameters for the IPSec tunnel, with the destination of the encrypted packet being the AWS VPN endpoint public IP address.

1. The customer gateway determines that the best route to the AWS VPN endpoint public IP address is through the Direct Connect public VIF.

1. The AWS VPN endpoint attached to the Transit Gateway receives the encrypted IPSec traffic and forwards it to the Transit Gateway.

1. The traffic is decrypted, forwarded to the **spoke VPC A**, and routed to the Amazon EC2 instance.

1. Return traffic from the Amazon EC2 instance to the corporate network follows a reverse but identical path.

## Further reading
<a name="tetgw-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="tetgw-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](encryption-vpn-to-vpc.md#tevpc-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](#tetgw-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-private-ip-vpn.md#tepip-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-macsec.md#temac-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.