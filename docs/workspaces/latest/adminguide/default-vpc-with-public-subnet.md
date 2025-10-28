# Use the Default VPC, Public Subnet,

and Security Group

Your Amazon Web Services account, if it was created after 2013-12-04, has a default VPC in
each AWS Region. The default VPC includes a default public subnet in each
Availability Zone and an internet gateway that is attached to your VPC. The VPC also
includes a default security group. If you are new to WorkSpaces Pools and want to get
started using the service, you can keep the default VPC and security group selected
when you create a WorkSpaces Pool. Then, you can select at least one default
subnet.

###### Note

If your Amazon Web Services account was created before 2013-12-04, you must create a new
VPC or configure an existing one to use with WorkSpaces Pools. We recommend that you
manually configure a VPC with two private subnets for your WorkSpaces Pools and a NAT
gateway in a public subnet. For more information, see [Configure a VPC with Private
Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md"). Alternatively, you can
configure a non-default VPC with a public subnet. For more information, see
[Configure a New or
Existing VPC with a Public Subnet](managing-network-default-internet-access.md "managing-network-default-internet-access.md").

You can enable internet access when you [create the
WorkSpaces Pool directory](create-directory-pools.md "create-directory-pools.md").

Choose the default VPC when you create the directory. The default VPC name uses
the following format: `vpc-``vpc-id``(No_default_value_Name)`.

Then select a default public subnet for **Subnet 1** and,
optionally, another default public subnet for **Subnet 2**. The
default subnet names use the following format:
`subnet-``subnet-id` `|
 (``IPv4 CIDR block``) | Default in`
`availability-zone`.

You can test your internet connectivity by starting your WorkSpaces Pool, and then
connecting to a WorkSpace in the pool and browsing to the internet.
