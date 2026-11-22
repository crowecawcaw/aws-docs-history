

# NAT gateways that Network Firewall creates for a NAT/Proxy firewall

When you create a NAT/Proxy firewall, or add an Availability Zone to it, Network Firewall creates a NAT gateway in the NAT subnet that you specify, with the firewall already attached. The NAT gateway is a resource in your account. To see its details, such as its IP addresses, use the Amazon VPC console or the Amazon EC2 `DescribeNatGateways` API operation.

**Note**  
A NAT gateway that Network Firewall creates for a NAT/Proxy firewall is billed like any other NAT gateway. You pay NAT gateway hourly charges and data processing (bandwidth) charges, in addition to Network Firewall charges. Proxy traffic through the NAT gateway is discounted, and non-proxy (regular) NAT traffic is charged at standard NAT gateway rates. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.

The NAT gateway stays in your account when it's no longer attached to the firewall:
+ When you remove an Availability Zone from the firewall, Network Firewall detaches that Availability Zone's NAT gateway from the firewall. The NAT gateway keeps working as a regular NAT gateway. If you don't need it, delete it in the Amazon VPC console.
+ When you delete the firewall, Network Firewall detaches all of its NAT gateways. By default, the NAT gateways keep working as regular NAT gateways. To delete them along with the firewall, select **Also delete the NAT gateways this firewall created** in the console, or set `DeleteAssociatedNatGateways` to `true` in the `DeleteFirewall` request. With this option, the firewall stays in the `DELETING` state until the NAT gateways are deleted.
+ When you delete a firewall that failed to create, Network Firewall deletes the NAT gateways that it created for that firewall, even if you don't choose to delete them.

If you allocated Elastic IP addresses for the NAT gateways, release them in the Amazon VPC console after the NAT gateways are deleted.

If an Availability Zone fails to set up, delete any NAT gateway that remains in its subnet if you don't need it. Elastic IP addresses aren't released.