# Enable internet access for Amazon MSK

Connect

If your connector for Amazon MSK Connect needs access to the internet, we recommend that you
use the following Amazon Virtual Private Cloud (VPC) settings to enable that access.

- Configure your connector with private subnets.
- Create a public [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") or [NAT
  instance](../../../vpc/latest/userguide/VPC_NAT_Instance.md "../../../vpc/latest/userguide/VPC_NAT_Instance.md") for your VPC in a public subnet. For more information, see the
  [Connect subnets to the internet or other VPCs using NAT devices](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") page in
  the _Amazon Virtual Private Cloud_
  _User Guide_.
- Allow outbound traffic from your private subnets to your NAT gateway or
  instance.
