

# AWS Site-to-Site VPN to an Amazon VPC
<a name="encryption-vpn-to-vpc"></a>

Publication date: **March 5, 2025 ([Diagram history](#tevpc-diagram-history))**

This method achieves traffic encryption by combining the benefits of the end-to-end secure IPSec connection with the low latency and consistent network experience of [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) when reaching resources in your [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

## Site-to-Site VPN over Direct Connect public VIF to a VPC architecture
<a name="tevpc-diagram1"></a>

![Architecture diagram showing traffic encryption using AWS Site-to-Site VPN over an AWS Direct Connect public VIF to reach resources in an Amazon VPC.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/traffic-encryption-direct-connect/images/traffic-encryption-direct-connect-1.png)


**Configuration steps:**

1. Create an AWS Direct Connect connection. For dedicated connections, set up a cross-connect between the AWS device and your device (or partner device) at the location. For hosted connections, you must accept the hosted connection before you can use it.

1. Once the connection is established, create an AWS Direct Connect public virtual interface (VIF) over the existing connection. Configure your customer gateway to bring up the VIF.

1. Once the border gateway protocol (BGP) peer on the VIF is established, AWS advertises its public IP range to the customer gateway device over the public VIF.

1. Create an AWS Site-to-Site VPN to the virtual private gateway associated to the Amazon VPC. AWS provides two VPN endpoints attached to the virtual private gateway, which have public IP addresses that are reachable over the public VIF.

1. Configure your customer gateway with the VPN parameters to bring up the AWS Site-to-Site VPN connection.

**Sample traffic flow:**

1. A client located in the corporate network needs to reach the IP address of an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance in the VPC, so the traffic is routed through the customer gateway.

1. The customer gateway determines that the best route to the VPC is through the AWS Site-to-Site VPN tunnel. The traffic is encrypted based on cryptographic parameters for the IPSec tunnel, with the destination of the encrypted packet being the VPN endpoint public IP address.

1. The customer gateway determines that the best route to the AWS VPN endpoint public IP address is through the Direct Connect public VIF.

1. The AWS VPN endpoint receives the encrypted IPSec traffic and decrypts it. Because the original IP destination address is the Amazon EC2 instance in the VPC, the traffic is routed through the VPC fabric to the Amazon EC2 instance.

1. Return traffic from the Amazon EC2 instance to the client located in the corporate network follows a reverse but identical path.

## Further reading
<a name="tevpc-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="tevpc-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#tevpc-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-vpn-to-tgw.md#tetgw-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-private-ip-vpn.md#tepip-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-macsec.md#temac-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.