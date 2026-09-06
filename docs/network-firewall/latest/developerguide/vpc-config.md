

# Configuring your VPC and other components for AWS Network Firewall
<a name="vpc-config"></a>

This section describes the changes that you must make in your VPC configuration and other components to use AWS Network Firewall. For information about managing your Amazon Virtual Private Cloud VPC, see the [Amazon Virtual Private Cloud User Guide](https://docs.aws.amazon.com/vpc/latest/userguide). 

For examples of architectures that are supported by Network Firewall, see [Architecture and routing examples](architectures.md).

**Unsupported architectures**  
The following lists architectures and traffic types that Network Firewall doesn't support:
+ VPC peering.
+ Inspection of AWS Global Accelerator traffic.
+ Inspection of AmazonProvidedDNS traffic for Amazon EC2.

**Topics**
+ [VPC subnet configuration for AWS Network Firewall](vpc-config-subnets.md)
+ [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md)
+ [Transit gateway attachment configuration for AWS Network Firewall](vpc-config-tgw-multi-az.md)