

# MACsec Security in AWS Direct Connect
<a name="encryption-macsec"></a>

Publication date: **March 5, 2025 ([Diagram history](#temac-diagram-history))**

This method achieves encryption of traffic using MACsec security (IEEE 802.1AE), delivering native, near line-rate, point-to-point encryption for 10 Gbps and 100 Gbps links.

For more information about MACsec in [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), see [Adding MACsec security to AWS Direct Connect connections](https://aws.amazon.com/blogs/networking-and-content-delivery/adding-macsec-security-to-aws-direct-connect-connections/) on the AWS Blog.

**Note**  
The connection between the customer or partner device at the AWS Direct Connect location and the on-premises customer gateway is only MACsec enabled if the Layer-2 circuit was extended all the way. If the Layer-2 circuit terminates on the customer or partner device at the AWS Direct Connect location, the responsibility for that segment of the circuit lies with the customer or partner.

## MACsec encryption in Direct Connect architecture
<a name="temac-diagram1"></a>

![Architecture diagram showing traffic encryption using MACsec security on an AWS Direct Connect dedicated connection with transit VIF and Transit Gateway to reach multiple VPCs.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/traffic-encryption-direct-connect/images/traffic-encryption-direct-connect-4.png)


**Configuration steps:**

1. To configure MACsec in an AWS Direct Connect dedicated connection, ensure that the device at your end supports MACsec. Additionally, the Direct Connect location must also support MACsec.

1. Create a 10G or 100G AWS Direct Connect dedicated connection, choosing the option for a MACsec-enabled port.

1. Create a Connection Key Name (CKN) and Connectivity Association Key (CAK) pair for the MACsec secret key. Make sure that the key pair is compatible with your device (or partner device).

1. Set up the cross-connect and complete the physical connection to your device (or partner device). Update the device at your end with the CKN/CAK pair.

1. Associate the CKN/CAK pair with the connection through the AWS Management Console, AWS Command Line Interface (CLI), or API.

1. Create a transit VIF to a Direct Connect gateway on the new MACsec-enabled connection, associated with your [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

**Sample traffic flow:**

1. A client located in the corporate network needs to route network traffic to the IP address of an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance in the **spoke VPC A**, and routes the traffic to the customer gateway.

1. The customer gateway determines that the best route to the VPC is through the transit VIF, indicating the traffic should be sent over the Direct Connect connection.

1. As per the **Transit Gateway Direct Connect route table**, the traffic is forwarded to the **spoke VPC A**, and then routed to the Amazon EC2 instance.

1. Return traffic from the Amazon EC2 instance to the client located in the corporate network follows a reverse but identical path.

## Further reading
<a name="temac-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="temac-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](encryption-vpn-to-vpc.md#tevpc-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-vpn-to-tgw.md#tetgw-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](encryption-private-ip-vpn.md#tepip-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 
| [Initial publication](#temac-diagram-history) | Reference architecture diagram first published. | March 5, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.