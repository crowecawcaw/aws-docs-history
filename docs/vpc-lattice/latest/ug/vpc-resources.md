

# VPC resources in Amazon VPC Lattice
<a name="vpc-resources"></a>

You can share resources and network segments with other teams in your organization or with external independent software vendor (ISV) partners. A resource can be an AWS-native resource such as an Amazon RDS database, a domain name, or an IP address. A network segment can be a list of CIDR ranges in your network. Resources or network segments can be in your VPC or on-premises network. To share resources or network segments, you create a resource gateway in your VPC through which your resource or network segment can be accessed. You create a resource configuration to represent the resource, group of resources, or network segment that you want to share. Then, you use AWS RAM to specify the principals who can access the resource or network segment.

The principals that you share resources or network segments with can access them privately using AWS PrivateLink-based VPC endpoints. They can use a resource endpoint to access an individual resource or pool multiple resources in a VPC Lattice service network, and access the service network from their VPC using a service network endpoint or a service network VPC association. They can access network segments using a tunnel endpoint.

The following sections explain how to create and manage VPC resources in VPC Lattice:

**Topics**
+ [Resource gateways](resource-gateway.md)
+ [Resource configurations](resource-configuration.md)