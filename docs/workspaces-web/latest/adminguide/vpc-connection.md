# Internet connectivity ports for Amazon WorkSpaces Secure Browser

Each WorkSpaces Secure Browser streaming instance has a customer network interface that provides
connectivity to the resources within your VPC, as well as to the internet if private subnets
with NAT gateway are set up.

For internet connectivity, the following ports must be open to all destinations. If you
are using a modified or custom security group, you'll need to add the required rules
manually. For more information, see [Security group
rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules.html "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules.html").

###### Note

This applies to egress traffic.

- TCP 80 (HTTP)
- TCP 443 (HTTPS)
- UDP 8433
