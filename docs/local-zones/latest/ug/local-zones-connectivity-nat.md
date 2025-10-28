# NAT gateway connection in Local Zones

A NAT gateway is a Network Address Translation (NAT) service. It allows your Amazon VPC resources
in your private subnets to securely access services outside the subnet, including the internet,
while keeping those private resources inaccessible to any unsolicited traffic. For a list of
Local Zones that support NAT gateways, see [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/").

To use NAT gateway to access the internet from your private resources, instantiate your NAT
gateway in the public subnet and then route your internet traffic (`0.0.0.0/0` or
`::/0`) from the private subnet to the NAT gateway. The NAT gateway translates the
private IP address of the traffic coming from your private subnet to the EIP associated with it
so that your private resources can access the internet securely.

The NAT gateway only accepts the response traffic from the destinations that are accessed
and drops any unsolicited inbound connections. This keeps your private resources inaccessible
from the internet.

For more information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_.

The following image shows the traffic flow from a private subnet in a Local Zone to a NAT gateway
in a public subnet in the same Local Zone, then to an internet gateway, and to the internet.

![An AWS Region with a VPC. The VPC contains two Availability Zones and a Local Zone. Each zone has a public subnet and a private subnet. The public subnet in the Local Zone shows a NAT gateway. Traffic flows from the private subnet in the Local Zone to the NAT gateway, then internet gateway, and to the internet.](images/nat-gateway.png)
