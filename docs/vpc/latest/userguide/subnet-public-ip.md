# Modify the IP addressing attributes of your subnet

By default, nondefault subnets have the IPv4 public addressing attribute set to
`false`, and default subnets have this attribute set to `true`. An
exception is a nondefault subnet created by the Amazon EC2 launch instance wizard — the
wizard sets the attribute to `true`. You can modify this attribute using the
Amazon VPC console.

By default, all subnets have the IPv6 addressing attribute set to `false`.
You can modify this attribute using the Amazon VPC console. If you enable the IPv6 addressing
attribute for your subnet, network interfaces created in the subnet receive an IPv6 address
from the range of the subnet. Instances launched into the subnet receive an IPv6 address on
the primary network interface.

Your subnet must have an associated IPv6 CIDR block.

###### Note

If you enable the IPv6 addressing feature for your subnet, your network interface or instance
only receives an IPv6 address if it's created using version `2016-11-15` or
later of the Amazon EC2 API. The Amazon EC2 console uses the latest API version.

###### To modify your subnet's IP addressing behavior

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Select your subnet and choose **Actions**, **Edit subnet settings**.
4. The **Enable auto-assign public IPv4 address** check box, if
   selected, requests a public IPv4 address for all instances launched into the selected
   subnet. Select or clear the check box as required, and then choose
   **Save**.
5. The **Enable auto-assign IPv6 address** check box, if selected,
   requests an IPv6 address for all network interfaces created in the selected subnet.
   Select or clear the check box as required, and then choose
   **Save**.

###### To modify a subnet attribute using the AWS CLI

Use the [modify-subnet-attribute](../../../cli/latest/reference/ec2/modify-subnet-attribute.md "../../../cli/latest/reference/ec2/modify-subnet-attribute.md") command.
