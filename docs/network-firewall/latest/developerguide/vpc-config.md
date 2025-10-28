# Configuring your VPC and other components for AWS Network Firewall

This section describes the changes that you must make in your VPC configuration and other components to use
AWS Network Firewall. For information about managing your Amazon Virtual Private Cloud VPC, see the
[Amazon Virtual Private Cloud User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

For examples of architectures that are supported by Network Firewall,
see [Architecture and routing
examples](architectures.md "architectures.md").

###### Unsupported architectures

The following lists architectures and traffic types that Network Firewall doesn't
support:

- VPC peering.
- Inspection of AWS Global Accelerator traffic.
- Inspection of AmazonProvidedDNS traffic for Amazon EC2.

###### Topics

- [VPC subnet configuration for AWS Network Firewall](vpc-config-subnets.md "vpc-config-subnets.md")
- [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md "vpc-config-route-tables.md")
- [Transit gateway attachment configuration for AWS Network Firewall](vpc-config-tgw-multi-az.md "vpc-config-tgw-multi-az.md")
