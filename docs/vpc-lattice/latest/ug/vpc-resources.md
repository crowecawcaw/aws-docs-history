# VPC resources in Amazon VPC Lattice

You can share VPC resources with other teams in your organization or with external
independent software vendor (ISV) partners. A VPC resource can be an AWS-native resource such as
an Amazon RDS database, a domain name, or an IP address. The resource can be in your VPC or on-premises
network and does not need to be load-balanced. You use AWS RAM to specify the principals who can
access the resource. You create a resource gateway through which your resource can be accessed.
You also create a resource configuration that represents the resource or a group of resources that
you want to share.

The principals that you share the resource with can access these resources privately using VPC endpoints. They can use a
resource VPC endpoint to access one resource or pool multiple resources in an VPC Lattice
service network, and access the service network using a service-network VPC endpoint.

The following sections explain how to create and manage VPC resources in VPC Lattice:

###### Topics

- [Resource gateways](resource-gateway.md "resource-gateway.md")
- [Resource configurations](resource-configuration.md "resource-configuration.md")
