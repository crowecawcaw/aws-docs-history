# Default VPC components

When we create a default VPC, we do the following to set it up for you:

- Create a VPC with a size `/16` IPv4 CIDR block (`172.31.0.0/16`).
  This provides up to 65,536 private IPv4 addresses.
- Create a size `/20` default subnet in each Availability Zone. This provides up
  to 4,096 addresses per subnet, a few of which are reserved for our use.
- Create an [internet gateway](VPC_Internet_Gateway.md "VPC_Internet_Gateway.md") and connect it to
  your default VPC.
- Add a route to the main route table that points all traffic
  (`0.0.0.0/0`) to the internet gateway.
- Create a default security group and associate it with your default VPC.
- Create a default network access control list (ACL) and associate it with your
  default VPC.
- Associate the default DHCP options set for your AWS account with your default
  VPC.

###### Note

- Amazon creates the above resources on your behalf. IAM policies do not apply to these actions
  because you do not perform these actions. For example, if you have an IAM
  policy that denies the ability to call CreateInternetGateway, and then you
  call CreateDefaultVpc, the internet gateway in the default VPC is still
  created. To prevent Amazon from creating an internet gateway, you would have
  to deny CreateDefaultVpc and CreateInternetGateway.
- To block all traffic to and from the internet gateways in your account, see [Block public access to VPCs and subnets](security-vpc-bpa.md "security-vpc-bpa.md").
  The following figure illustrates the key components that we set up for a default VPC.

![We create a default VPC in each Region, with a default subnet in each Availability Zone.](images/default-vpc.png)
The following table shows the routes in the main route table for the default VPC.

| Destination   | Target                |
| ------------- | --------------------- |
| 172.31.0.0/16 | local                 |
| 0.0.0.0/0     | `internet_gateway_id` |

You can use a default VPC as you would use any other VPC:

- Add additional nondefault subnets.
- Modify the main route table.
- Add additional route tables.
- Associate additional security groups.
- Update the rules of the default security group.
- Add AWS Site-to-Site VPN connections.
- Add more IPv4 CIDR blocks.
- Access VPCs in a remote Region by using a Direct Connect gateway. For
  information about Direct Connect gateway options, see [Direct Connect gateways](../../../directconnect/latest/UserGuide/direct-connect-gateways-intro.md "../../../directconnect/latest/UserGuide/direct-connect-gateways-intro.md") in the _AWS Direct Connect User Guide_.
  You can use a default subnet as you would use any other subnet; add custom route tables and
  set network ACLs. You can also specify a specific default subnet when you launch an EC2
  instance.

You can optionally associate an IPv6 CIDR block with your default VPC.
