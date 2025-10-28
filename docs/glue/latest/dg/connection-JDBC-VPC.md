# Connecting to a JDBC data store in a VPC

Typically, you create resources inside Amazon Virtual Private Cloud (Amazon VPC) so that they cannot be
accessed over the public internet. By default, AWS Glue can't access
resources inside a VPC. To enable AWS Glue to access resources inside your
VPC, you must provide additional VPC-specific configuration information that includes
VPC subnet IDs and security group IDs. AWS Glue uses this information to set up [elastic network
interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") that enable your function to connect securely to other resources
in your private VPC.

When using a VPC endpoint, add it to your route table. For more information, see
[Creating an interface VPC endpoint for AWS Glue](vpc-interface-endpoints.md#vpc-endpoint-create "vpc-interface-endpoints.md#vpc-endpoint-create") and [Prerequisites](connection-S3-VPC.md#connection-S3-VPC-prerequisites "connection-S3-VPC.md#connection-S3-VPC-prerequisites").

When using encryption in Data Catalog, create the KMS interface endpoint and add it to your route table.
For more information, see
[Creating a VPC endpoint for AWS KMS](../../../kms/latest/developerguide/kms-vpc-endpoint.md#vpce-create-endpoint "../../../kms/latest/developerguide/kms-vpc-endpoint.md#vpce-create-endpoint").

## Accessing VPC Data Using elastic network

interfaces

When AWS Glue connects to a JDBC data store in a VPC,
AWS Glue creates an elastic network interface (with the prefix
`Glue_`) in your account to access your VPC data. You can't delete
this network interface as long as it's attached to AWS Glue. As part of
creating the elastic network interface, AWS Glue associates one or more
security groups to it. To enable AWS Glue to create the network
interface, security groups that are associated with the resource must allow inbound
access with a source rule. This rule contains a security group that is associated
with the resource. This gives the elastic network interface access to your data
store with the same security group.

To allow AWS Glue to communicate with its components, specify a
security group with a self-referencing inbound rule for all TCP ports. By creating a
self-referencing rule, you can restrict the source to the same security group in the
VPC and not open it to all networks. The default security group for your VPC might
already have a self-referencing inbound rule for `ALL Traffic`.

You can create rules in the Amazon VPC console. To update rule settings via the
AWS Management Console, navigate to the VPC console ([https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/")), and select the
appropriate security group. Specify the inbound rule for `ALL TCP` to
have as its source the same security group name. For more information about security
group rules, see [Security Groups
for Your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").

Each elastic network interface is assigned a private IP address from the IP
address range in the subnets that you specify. The network interface is not assigned
any public IP addresses. AWS Glue requires internet access (for example,
to access AWS services that don't have VPC endpoints). You can configure a network
address translation (NAT) instance inside your VPC, or you can use the Amazon VPC NAT
gateway. For more information, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the _Amazon VPC User Guide_. You can't
directly use an internet gateway attached to your VPC as a route in your subnet
route table because that requires the network interface to have public IP
addresses.

The VPC network attributes `enableDnsHostnames` and
`enableDnsSupport` must be set to true. For more information, see
[Using DNS with your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").

###### Important

Don't put your data store in a public subnet or in a private subnet that
doesn't have internet access. Instead, attach it only to private subnets that
have internet access through a NAT instance or an Amazon VPC NAT gateway.

## Elastic network interface

properties

To create the elastic network interface, you must supply the following
properties:

**VPC**

The name of the VPC that contains your data store.

**Subnet**

The subnet in the VPC that contains your data store.

**Security groups**

The security groups that are associated with your data store.
AWS Glue associates these security groups with the
elastic network interface that is attached to your VPC subnet. To allow
AWS Glue components to communicate and also prevent
access from other networks, at least one chosen security group must
specify a self-referencing inbound rule for all TCP ports.

For information about managing a VPC with Amazon Redshift, see [Managing Clusters in an Amazon
Virtual Private Cloud (VPC)](../../../redshift/latest/mgmt/managing-clusters-vpc.md "../../../redshift/latest/mgmt/managing-clusters-vpc.md").

For information about managing a VPC with Amazon Relational Database Service (Amazon RDS), see [Working with an
Amazon RDS DB Instance in a VPC](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md").
