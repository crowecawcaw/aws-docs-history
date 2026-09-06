

# AWS Network Firewall example architectures with routing
<a name="architectures"></a>

This section provides a high-level view of simple architectures that you can configure with AWS Network Firewall and shows example route table configurations for each. For additional information and examples, see [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/). 

**Note**  
For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*.

**Unsupported architectures**  
The following lists architectures and traffic types that Network Firewall doesn't support:
+ VPC peering.
+ Inspection of AWS Global Accelerator traffic.
+ Inspection of AmazonProvidedDNS traffic for Amazon EC2.

**Topics**
+ [Simple single zone architecture with an internet gateway using AWS Network Firewall](arch-single-zone-igw.md)
+ [Multi zone architecture with an internet gateway using AWS Network Firewall](arch-two-zone-igw.md)
+ [Architecture with an internet gateway and a NAT gateway using AWS Network Firewall](arch-igw-ngw.md)