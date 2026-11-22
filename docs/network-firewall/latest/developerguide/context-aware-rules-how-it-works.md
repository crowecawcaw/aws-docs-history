

# How context-aware rules work

When traffic travels through an AWS Transit Gateway, the transit gateway tags each packet with the sending resource's context: its VPC, subnet, transit gateway attachment, and Amazon VPC security groups. Traffic carries up to 5 Amazon VPC security groups per network interface, which is the default Amazon VPC quota for security groups per interface. A transit gateway-attached network firewall reads this context and matches it against the context IDs in your rules.

The firewall learns these identities by subscribing to a *context store* in AWS Network Manager. The store maintains a catalog of the AWS resources that can send and receive packets through the associated transit gateway and keeps the firewall in sync as resources are added or removed. To set one up, see [Onboarding your transit gateway to a context store](context-aware-rules-setup.md). When a resource's membership changes, such as when you attach a different Amazon VPC security group to an instance, the firewall evaluates its packets using the new context once the change propagates.

You can reference the following resource types in your rules:


| Resource type | ID format | 
| --- | --- | 
| VPC | vpc-1234567890abcdef0 | 
| Security group | sg-1234567890abcdef0 | 
| Subnet | subnet-0123456789abcdef0 | 
| Transit gateway attachment | tgw-attach-0123456789abcdef0 | 

Destination matching uses a learned identity and carries additional requirements. For details, see [Matching on destination context](context-aware-rules-destination.md).