# VPC Setup Recommendations for

WorkSpaces Pools

When you create a WorkSpaces Pools, you specify the VPC and one or more subnets to use.
You can provide additional access control to your VPC by specifying security groups.

The following recommendations can help you configure your VPC more effectively and
securely. In addition, they can help you configure an environment that supports
effective WorkSpaces Pools scaling. With effective WorkSpaces Pools scaling, you can meet
current and anticipated WorkSpaces user demand, while avoiding unnecessary resource usage
and associated costs.

**Overall VPC Configuration**

- Make sure that your VPC configuration can support your WorkSpaces Pools scaling
  needs.

As you develop your plan for WorkSpaces Pools scaling, keep in mind that one
user requires one WorkSpaces. Therefore, the size of your WorkSpaces Pools determines
the number of users who can stream concurrently. For this reason, for each
[instance type](instance-types.md "instance-types.md") that you plan to
use, make sure that the number of WorkSpaces that your VPC can support is greater
than the number of anticipated concurrent users for the same instance
type.

- Make sure that your WorkSpaces Pools account quotas (also referred to as limits)
  are sufficient to support your anticipated demand. To request a quota
  increase, you can use the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For
  information about default WorkSpaces Pools quotas, see [Amazon WorkSpaces quotas](workspaces-limits.md "workspaces-limits.md").
- If you plan to provide your WorkSpaces in WorkSpaces Pools with access to the
  internet, we recommend that you configure a VPC with two private subnets for
  your streaming instances and a NAT gateway in a public subnet.

The NAT gateway lets the WorkSpaces in your private subnets connect to the
internet or other AWS services. However, it prevents the internet from
initiating a connection with those WorkSpaces. In addition, unlike configurations
that use the **Default Internet Access** option for
enabling internet access, the NAT configuration supports more than 100
WorkSpaces. For more information, see [Configure a VPC with Private
Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md").
**Elastic Network Interfaces**

- WorkSpaces Pools creates as many [elastic
  network interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") (network interfaces) as the maximum desired
  capacity of your WorkSpaces Pools. By default, the limit for network interfaces
  per Region is 5000.

When planning capacity for very large deployments, for example, thousands
of WorkSpaces, consider the number of Amazon EC2 instances that are also used in the
same Region.
**Subnets**

- If you are configuring more than one private subnet for your VPC,
  configure each in a different Availability Zone. Doing so increases fault
  tolerance and can help prevent insufficient capacity errors. If you use two
  subnets in the same AZ, you might run out of IP addresses, because
  WorkSpaces Pools will not use the second subnet.
- Make sure that the network resources required for your applications are
  accessible through both of your private subnets.
- Configure each of your private subnets with a subnet mask that allows for
  enough client IP addresses to account for the maximum number of expected
  concurrent users. In addition, allow for additional IP addresses to account
  for anticipated growth. For more information, see [VPC and
  Subnet Sizing for IPv4](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4").
- If you are using a VPC with NAT, configure at least one public subnet with
  a NAT Gateway for internet access, preferably two. Configure the public
  subnets in the same Availability Zones where your private subnets reside.

To enhance fault tolerance and reduce the chance of insufficient capacity
errors for large WorkSpaces Pools deployments, consider extending your VPC
configuration into a third Availability Zone. Include a private subnet,
public subnet, and NAT gateway in this additional Availability Zone.
**Security Groups**

- Use security groups to provide additional access control to your VPC.

Security groups that belong to your VPC let you control the network
traffic between WorkSpaces Pools streaming instances and network resources
required by applications. These resources may include other AWS services
such as Amazon RDS or Amazon FSx, license servers, database servers, file servers, and
application servers.

- Make sure that the security groups provide access to the network resources
  that your applications require.

For
general information about security groups, see [Control traffic to your AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md")
in the _Amazon VPC User Guide_.
