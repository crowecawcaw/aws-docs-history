# Provider considerations for

cross-account connections in EventBridge

To create a connection to a private API in another AWS account, the owner of that account must share a VPC Lattice resource configuration for the private API with you.
A resource configuration is a logical object that identifies the API and specifies how and who can access it.
The _provider_ account--that is, the account sharing the VPC Lattice resource configuration for the private API with another account--shares
the VPC Lattice resource configuration using AWS RAM.

If your account is the provider of a VPC Lattice resource configuration, keep the following considerations in mind:

## Resource policy for resource configurations for cross-account

private APIs

By default, creating a AWS RAM resource share includes the necessary share policy,
`AWSRAMPermissionVpcLatticeResourceConfiguration`. If you create
a customer managed permission policy, you must include the necessary
permissions.

The following policy example provides the minimum necessary permissions for EventBridge to
create the resource association necessary for a connection to a private API.

- `vpc-lattice:GetResourceConfiguration` allows EventBridge to retrieve the Amazon VPC Lattice resource
  configuration you specify.
- `vpc-lattice:CreateServiceNetworkResourceAssociation` allows EventBridge to create the
  resource association from the VPC Lattice resource configuration you specify.
- `vpc-lattice:AssociateViaAWSService-EventsAndStates` allows EventBridge to create a resource association to a VPC Lattice service network owned by the service.

```
{
    "Effect": "Allow",
    "Action": [
      "vpc-lattice:CreateServiceNetworkResourceAssociation",
      "vpc-lattice:GetResourceConfiguration",
      "vpc-lattice:AssociateViaAWSService-EventsAndStates"
      ]
}
```

For more information, see [Managing permissions in AWS RAM](../../../ram/latest/userguide/security-ram-permissions.md "../../../ram/latest/userguide/security-ram-permissions.md") in the _AWS Resource Access Manager User Guide_.

## Provider monitoring of connection creation

When another account creates an EventBridge connection using a VPC Lattice resource configuration you have shared,
AWS CloudTrail logs a
`CreateServiceNetworkResourceAssociationBySharee` event. For more information, see [Monitoring connection creation](connection-private.md#connection-private-monitoring-create "connection-private.md#connection-private-monitoring-create").

## Configuring security groups for access to private APIs

With VPC Lattice, you can create and assign security groups to enforce additional
network-level security protections for your target API and resource gateway. In order for EventBridge
and Step Functions to access your private API successfully, the security groups on the
target API and resource gateway must to be configured correctly. If not
configured correctly, the services will return "Connection
Timed Out" errors when attempting to call your API.

For your target API, your security group must be configured to allow all
inbound TCP traffic on port 443 from the security group for your resource
gateway.

For your resource gateway, your security group must be configured to allow the
following:

- All inbound IPv6 TCP traffic across all ports from the ::/0 IPv6 CIDR range.
- All inbound IPv4 TCP traffic across all ports from the 0.0.0.0/0 IPv6 CIDR range.
- All outbound TCP traffic on port 443 to the security group used by your target resource, for
  the IP protocol your target API accepts (IPv4 or IPv6).

For more information, see the following topics in the _Amazon VPC Lattice
User Guide_:

- [Control traffic in VPC Lattice using security groups](../../../vpc-lattice/latest/ug/security-groups.md "../../../vpc-lattice/latest/ug/security-groups.md")
- [Resource gateway in VPC Lattice](../../../vpc-lattice/latest/ug/resource-gateway.md "../../../vpc-lattice/latest/ug/resource-gateway.md")
