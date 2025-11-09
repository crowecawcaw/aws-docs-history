# Example dual-stack VPC configuration

With a dual-stack configuration, you can use both IPv4 and IPv6 addresses for
communication between resources in your VPC and resources over the internet.

The following diagram represents the architecture of your VPC. Your VPC has a public
subnet and a private subnet. The VPC and subnets have both an IPv4 CIDR block and an
IPv6 CIDR block. There is an EC2 instance in the private subnet that has both an
IPv4 address and an IPv6 address. The instance can send outbound IPv4 traffic to the
internet using a NAT gateway and outbound IPv6 traffic to the internet using an
egress-only internet gateway.

![A VPC with a public subnet, private subnet, NAT gateway, internet gateway, and egress-only internet gateway.](images/vpc-example-dual-stack.png)

###### Route table for public subnet

The following is the route table for the public subnet. The first two entries are the
local routes. The third entry sends all IPv4 traffic to the internet gateway. Note that
the fourth entry is necessary only if you plan to launch EC2 instances with IPv6 addresses
in the public subnet.

| Destination     | Target                |
| --------------- | --------------------- |
| `VPC IPv4 CIDR` | local                 |
| `VPC IPv6 CIDR` | local                 |
| 0.0.0.0/0       | `internet-gateway-id` |
| ::/0            | `internet-gateway-id` |

###### Route table for the private subnet

The following is the route table for the private subnet. The first two entries are
the local routes. The third entry sends all IPv4 traffic to the NAT gateway. The last
entry sends all IPv6 traffic to the egress-only internet gateway.

| Destination     | Target                   |
| --------------- | ------------------------ |
| `VPC IPv4 CIDR` | local                    |
| `VPC IPv6 CIDR` | local                    |
| 0.0.0.0/0       | `nat-gateway-id`         |
| ::/0            | `egress-only-gateway-id` |
