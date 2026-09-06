

# Architecture with an internet gateway and a NAT gateway using AWS Network Firewall
<a name="arch-igw-ngw"></a>

You can add a network address translation (NAT) gateway to your AWS Network Firewall architecture, for the areas of your VPC where you need NAT capabilities. AWS provides NAT gateways decoupled from your other cloud services, so you can use it in your architecture only where you need it. This can help you reduce load and load costs. For information about NAT gateways, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.

The following figure depicts a VPC configuration for Network Firewall with an internet gateway and a NAT gateway. 

![VPC configuration with an internet gateway and a NAT gateway, showing firewall subnet, NAT gateway subnet, and customer workload subnets.](http://docs.aws.amazon.com/network-firewall/latest/developerguide/images/arch-igw-natgw.png)
