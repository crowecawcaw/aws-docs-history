

# HNPERF02-BP03 Choose the right termination endpoint in the cloud
<a name="hnperf02-bp03"></a>

 When establishing cloud connectivity through Points of Presence (PoPs), organizations carefully choose their network termination endpoints. There are options available to connect to directly to one cloud network or through transit cloud constructs for multiple cloud networks. Each option offers different benefits in terms of cost, performance, scalability, and management complexity. 

 **Desired outcome:** 
+  Optimal network connectivity between on-premises environments and cloud resources by selecting the most appropriate termination endpoint.  
+  Maintain flexibility for future network expansion, ensuring consistent performance, and managing costs effectively. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Optimized network performance and reduced latency 
+  Multi-region connectivity through a single connection, reducing complexity and costs.  
+  Cost-effective connectivity based on actual requirements 
+  Simplified network management and operations 
+  Enhanced network security through proper isolation 
+  Flexible architecture that supports business growth 

## Implementation guidance
<a name="implementation-guidance-44"></a>
+  Assess your current and future network requirements, including geographic distribution, bandwidth needs, and application latency requirements. 
+  Use direct connectivity to single cloud network connectivity to avoid additional cloud transit costs, For example, you can use Direct Connect private VIF to connect directly to VPC. 
+  Use cloud transit connectivity to connect to multiple cloud networks. For example, you can use Direct Connect transit VIF to connect to Transit Gateway for VPCs in the same region, or Cloud WAN core network for VPCs in multiple regions. 

## Resources
<a name="resources-35"></a>
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/direct-connect.html) 
+  [Simplify global hybrid connectivity with AWS Cloud WAN and AWS Direct Connect integration](https://aws.amazon.com/blogs/networking-and-content-delivery/simplify-global-hybrid-connectivity-with-aws-cloud-wan-and-aws-direct-connect-integration/) 
+  [Transit gateway attachments to a Direct Connect gateway in AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html) 
+  [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) 