

# Enable internet access for Amazon MSK Connect
<a name="msk-connect-internet-access"></a>

If your connector for Amazon MSK Connect needs access to the internet, we recommend that you use the following Amazon Virtual Private Cloud (VPC) settings to enable that access.
+ Configure your connector with private subnets.
+ Create a public [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) or [NAT instance](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) for your VPC in a public subnet. For more information, see the [Connect subnets to the internet or other VPCs using NAT devices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) page in the *Amazon Virtual Private Cloud* *User Guide*. 
+ Allow outbound traffic from your private subnets to your NAT gateway or instance.