# Routing Scenarios with AWS Direct Connect SiteLink

Publication date: **July 25, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

## Traffic Flow Between On-Premises Locations Diagram

With AWS Direct Connect SiteLink, route traffic between AWS Direct Connect locations through the AWS global
network backbone without traversing any AWS Region. Associate your private or transit
virtual interfaces (VIFs) to a common AWS Direct Connect gateway and enable SiteLink in those VIFs.

![Reference architecture diagram showing how to route traffic between AWS Direct Connect locations through the AWS global network backbone without traversing any AWS Region with AWS Direct Connect SiteLink. Associate your private or transit virtual interfaces (VIFs) to a common AWS Direct Connect gateway and enable SiteLink in those VIFs.](images/1-traffic-flow-between-on-premises-locations.png)

1. The customer gateway in corporate data center A advertises its CIDR block (10.0.1.0/24)
   to the **AWS Direct Connect** logical device (not
   shown in the diagram) when configuring the virtual interface.
2. Once the VIF is attached to the **AWS Direct Connect** gateway (DXGW),
   it announces the CIDR block to any resource associated with it (such as
   **Amazon Virtual Private Cloud** (Amazon VPC) or **AWS Transit Gateway**).
   If SiteLink is enabled on this VIF, the CIDR block will also be announced to any other
   VIF that is attached to this **AWS Direct Connect** gateway and has SiteLink enabled.
3. The customer gateway in the corporate data center B configures its VIF and it is associated
   with the **AWS Direct Connect** gateway. It receives the 10.0.1.0/24 block
   with AS PATH 65001 650011 65512. The block 10.0.2.0/24 will also be
   announced to corporate data center A through the gateway with AS PATH 65001 65001 65513.
   Now both locations will be able to route traffic between each other.

1 When connecting two AWS Direct Connect connections to the same AWS device,
you get +1 AS prepended (AWS Direct Connect gateway ASN) when using SiteLink. However, when these connections
are in different sites, you get this ASN twice (+2 AS prepended) – one for each AWS router.

## Traffic Flow Between On-Premises Locations – Backup

You can use AWS Direct Connect SiteLink as a backup path to your private network to
route traffic between on-premises locations through the AWS global network backbone
without traversing any AWS Region.

![Reference architecture diagram showing how to use AWS Direct Connect SiteLink as a backup path to your private network to route traffic between on-premises locations through the AWS global network backbone without traversing any AWS Region.](images/2-traffic-flow-between-on-premises-locations-backup.png)

1. **Preferred** - Customer data centers advertize their respective
   network CIDRs through a private network such as
   MPLS. The customer gateway in corporate data center A receives the CIDR block of corporate data
   center B with the AS PATH 65513.
2. If SiteLink is enabled in both private or transit VIFs, however, the customer gateway in
   corporate data center A also receives the CIDR block of corporate data center B with
   the AS PATH 65001 65001 65513.
3. In the case of an outage of the WAN network, traffic from corporate data center A to
   data center B is routed directly between **AWS Direct Connect** locations
   without traversing any AWS Region.

For more information about how to influence path preference using BGP, refer to
[Creating
active/passive BGP connections over AWS Direct Connect.](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-active-passive-bgp-connections-over-aws-direct-connect/ "https://aws.amazon.com/blogs/networking-and-content-delivery/creating-active-passive-bgp-connections-over-aws-direct-connect/")

## Traffic Flow Between On-Premises Locations – Extension

You can use AWS Direct Connect SiteLink as an extension of your private network to route
traffic between on-premises locations using AWS global network backbone without traversing
any AWS Region. Not all of your datacenters need to have a direct connection.

![Reference architecture diagram showing how to use AWS Direct Connect SiteLink as an extension of your private network to route traffic between on-premises locations using AWS global network backbone without traversing any AWS Region.](images/3-traffic-flow-between-on-premises-locations-extension.png)

1. The customer gateway in corporate data center A receives the CIDR block of corporate data
   center C with the AS PATH 65513 65001 65514 from corporate data center B.
2. The customer gateway in data center B receives the CIDR block of corporate data center
   A with AS PATH 65512. Because SiteLink is enabled on the VIFs associated with customer
   gateways in data centers B and C, the customer gateway in data center C can receive the
   CIDR from data center A with AS Path 65001 65001 65513 65512.
3. Traffic between corporate data centers A and C is routed directly between **AWS Direct Connect**
   locations without traversing any AWS Region.

## Full Mesh Connectivity Between On-Premises Locations and AWS

With a common AWS Direct Connect gateway, you can use the AWS backbone as the transit network
to connect between on-premises and AWS resources worldwide. Enable SiteLink on your
VIFs and attach them to a common AWS Direct Connect gateway, connected to your AWS resource
(for example, AWS Transit Gateway or Amazon Virtual Private Cloud).

![Reference architecture diagram showing how to use the AWS backbone as the transit network to connect between on-premises and AWS resources worldwide.](images/4-full-mesh-connectivity.png)

1. If SiteLink is enabled in both transit VIFs, the customer gateway in corporate data
   center A receives the CIDR block of corporate data center B with the AS PATH 65001 65001 65513.
2. Traffic from corporate data center A to data center B is routed directly between
   **AWS Direct Connect** locations without traversing any AWS Region.
3. The customer gateway in corporate data center A receives the CIDR blocks of the
   resources in AWS (Regions 1 and 2) with the AS PATH 65001 from the
   **AWS Direct Connect** gateway.
4. Traffic sent to AWS from corporate data center A arrives at the gateway,
   which routes it to the corresponding **AWS Transit Gateway**
   (in this case the one located in Region 2).
5. **Transit Gateway** in Region 2 routes the traffic to
   the corresponding **Amazon Virtual Private Cloud** (Amazon VPC) according
   to the **Transit Gateway** route table associated with
   the **AWS Direct Connect** gateway association.

## Traffic Segmentation with Several AWS Direct Connect Gateways

You can take advantage of several AWS Direct Connect gateways and multiple VIFs to
segment the traffic between your locations. Common use cases can be segmenting
global and regional networks, or expanding your virtual routing and forwarding
(VRFs). The configuration of multiple VIFs per connection is only possible
with dedicated connections.

![Reference architecture diagram showing how to take advantage of several AWS Direct Connect gateways and multiple VIFs to segment the traffic between your locations.](images/5-traffic-segmentation.png)

1. A private VIF is configured and attached to the regional
   **AWS Direct Connect** gateway with ASN 65002.
   To achieve segmentation with global traffic through the transit
   VIF, a more specific prefix (10.1.0.0/24) is announced. This
   prefix will be used for regional connectivity instead of global
   connectivity.
2. Likewise, a private VIF in corporate data center B is configured
   and attached to the gateway with ASN 65002. If both private VIFs (from
   data centers A and B) have SiteLink enabled, they will be able to
   communicate using the AWS backbone.
3. When corporate data center B needs to communicate with other locations
   globally, it will use the transit VIF attached to the gateway with ASN
4. To not overlap BGP (Border Gateway Protocol) announcements, it
   uses a more specific route (10.2.2.0/24) through the transit VIF.
5. Other SiteLink enabled locations attached to the same gateway
   through the transit VIFs can communicate using the AWS backbone. Global
   connectivity is achieved using ASN 65001, and regional connectivity with
   ASNs 65002 and 65003.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/routing-scenarios-with-aws-direct-connect-sitelink.md "samples/routing-scenarios-with-aws-direct-connect-sitelink.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Introducing AWS Direct Connect SiteLink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/ "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/")

## Contributors

Contributors to this reference architecture diagram include:

- Pablo Sánchez Carmona, Specialist Solutions Architect, Networking, Amazon Web Services
- Ivo Pinto, Senior Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| Minor update        | Update AS PATH prefixes.                        | July 24, 2023 |
| Initial publication | Reference architecture diagram first published. | April 2, 2023 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
