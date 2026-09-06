

# Amazon VPC peering
<a name="rise-connection-peering"></a>

VPC peering enables network connection between two AWS VPCs using private IPv4 and IPv6 addresses. Instances can communicate over the same network. For more information, see [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) 

Before setting up a VPC peering connection, you need to create a request for SAP’s approval. For a successful VPC peering, the defined IPv4 Classless Inter-Domain Routing (CIDR) block must not overlap. Check with SAP for the CIDR ranges that can be used in RISE with SAP VPC.

VPC peering is one-on-one connection between VPCs, and is not transitive. Traffic cannot transit from one VPC to another via an intermediary VPC. You must setup multiple peering connections to establish direct communication between RISE with SAP VPC and multiple VPCs.

VPC peering works across AWS Regions. All inter-Region traffic is encrypted with no single point of failure or bandwidth bottleneck. Traffic stays on AWS Global Network and never traverses the public internet, reducing threats of common exploits and DDoS attacks.

![VPC peering connections between multiple accounts in multiple Regions.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-peering.jpg)


Data transfer for VPC peering within an Availability Zone is free. Across Availability Zones, AWS charges per GB for data in and data out. Across regions, AWS charges per GB for data out. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/). In your AWS account, use the Availability Zone ID of AWS account managed by SAP to avoid cross-Availability Zone data transfer charges. You can ask for the Availability Zone ID from SAP. For more information, see [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html).


|  | 
| --- |
|  **Pricing example - VPC peering across Availability Zones** ![VPC peering across Availability Zones.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-peering-pricing.png)<br />100GB of data sent from the AWS account – managed by SAP via VPC Peering toward the AWS account – managed by Customer across AZs:<br />100GB \* USD 0.01 per GB = USD 1 (out - billed to AWS account – managed by SAP) and 100GB \* USD 0.01 per GB = USD 1 (IN - billed to AWS account – managed by Customer)<br />Because the cost for data transfer is included in the RISE subscription, the AWS account that you manage will incur only the cost for traffic in, for example, USD 0.01 per GB. This cost example also applies when the sender is the AWS account managed by Customer and the receiver is the AWS account managed by SAP.  | 
|  **Pricing example - VPC peering across Regions**  Cost between AWS Regions vary. For more information, see [Amazon EC2 pricing Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer). ![VPC peering across Regions.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-peering-across-regions-pricing.png)<br />1). 100GB of data sent from the AWS account – managed by SAP via VPC Peering toward the AWS account – managed by Customer across Regions.<br />100GB \* (USD 0.01–USD 0.138 per GB) = USD 1–USD 13.8 (out - billed to AWS account – managed by SAP)<br />Because the cost for data transfer is included in the RISE subscription, the AWS account – managed by Customer will not incur cost for this example.<br />2). 100GB of data sent from the AWS account – managed by Customer via VPC Peering toward the AWS account – managed by SAP across Regions.<br />100GB \* (USD 0.01–USD 0.138 per GB) = USD 1–USD 13.8 (out - billed to AWS account – managed by Customer)<br />As the cost for data transfer is calculated for "data out" the AWS account – managed by Customer will incur the cost for this example. | 