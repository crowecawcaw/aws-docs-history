

# AWS Direct Connect Traffic Flow with AWS Local Zone
<a name="direct-connect-local-zone"></a>

Publication date: **September 29, 2022 ([Diagram history](#diagram-history))**

This architecture shows traffic flows from an on-premises data center to an AWS Local Zone using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) for latency-sensitive applications running in [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

## AWS Direct Connect traffic flow with AWS Local Zone architecture
<a name="diagram1"></a>

![Architecture diagram showing AWS Direct Connect traffic flow to an AWS Local Zone using Direct Connect gateways, VGW, and Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/direct-connect-local-zone/images/direct-connect-local-zone.png)


The following steps describe this architecture:

1. Create AWS Direct Connect gateway (DXGW) "X" and assign a unique autonomous system number (ASN). Attach the Private Virtual Interface (VIF) to DXGW X.

1. Create DXGW "Y" and assign a unique ASN. Attach the Transit VIF to DXGW Y.

1. Create a Virtual Private Gateway (VGW) and attach it to **DXGW X**. Assign a unique ASN to the VGW. Attach the VGW to **VPC A**.

1. Create an [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) (TGW) and attach it to **DXGW Y** using a DXGW attachment. Attach the TGW to **VPC A** using a **VPC A** attachment.

1. Create a parent subnet (**10.0.0.0/24**) with an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance in an Availability Zone (AZ1) and associate it with a route table.

1. Create another subnet (**10.0.1.0/24**) in the AWS Local Zone where the latency-sensitive application runs. Associate this subnet with a separate Local Zone route table.

1. Add the AZ1 parent subnet (**10.0.0.0/24**) in the **DXGW Y** allowed prefixes list. For more information about allowed prefixes, see [Allowed prefixes interactions](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html).

1. AWS Transit Gateway and **DXGW Y** advertise the AZ1 parent subnet (**10.0.0.0/24**) back to on-premises. Traffic destined to the parent subnet follows the TGW path.

1. Traffic destined to the Local Zone subnet (**10.0.1.0/24**) follows the shorter VGW path without hairpinning through the Local Zone parent Region.

1. Avoid routing resources to the Local Zone subnet from on-premises through Transit Gateway because traffic using this path hairpins through the parent Region.

## Further reading
<a name="further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | September 29, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.