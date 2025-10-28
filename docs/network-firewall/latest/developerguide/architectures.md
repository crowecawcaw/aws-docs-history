# AWS Network Firewall example architectures with routing

This section provides a high-level view of simple architectures that you can configure with
AWS Network Firewall and shows example route table configurations for each. For additional
information and examples, see [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/ "https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/").

###### Note

For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.

###### Unsupported architectures

The following lists architectures and traffic types that Network Firewall doesn't
support:

- VPC peering.
- Inspection of AWS Global Accelerator traffic.
- Inspection of AmazonProvidedDNS traffic for Amazon EC2.

###### Topics

- [Simple single zone architecture with an internet gateway using AWS Network Firewall](arch-single-zone-igw.md "arch-single-zone-igw.md")
- [Multi zone architecture with an internet gateway using AWS Network Firewall](arch-two-zone-igw.md "arch-two-zone-igw.md")
- [Architecture with an internet gateway and a NAT gateway using AWS Network Firewall](arch-igw-ngw.md "arch-igw-ngw.md")
